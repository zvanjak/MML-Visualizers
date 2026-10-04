#!/usr/bin/env python3
"""Validate a published MML Visualizers binary archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path

ALL_SAMPLE_CASES = [
    ("real-function", "RealFunction/parabola.mml"),
    ("curve2d", "ParametricCurve2D/unit-circle.mml"),
    ("curve3d", "ParametricCurve3D/helix.mml"),
    ("surface", "ParametricSurface/patch.mml"),
    ("particle2d", "ParticleVisualizer2D/two-particles.mml"),
    ("particle3d", "ParticleVisualizer3D/two-particles.mml"),
    ("scalar2d", "ScalarFunction2D/saddle.mml"),
    ("scalar3d", "ScalarFunction3D/gaussian-blob.mml"),
    ("vector2d", "VectorField2D/rotation.mml"),
    ("vector3d", "VectorField3D/radial.mml"),
    ("rigid-body", "RigidBodyMovement/spinning-box.mml"),
]

FLTK_SAMPLE_CASES = [
    ("real-function", "RealFunction/parabola.mml"),
    ("curve2d", "ParametricCurve2D/unit-circle.mml"),
    ("particle2d", "ParticleVisualizer2D/two-particles.mml"),
    ("vector2d", "VectorField2D/rotation.mml"),
]

WPF_SAMPLE_CASES = [*ALL_SAMPLE_CASES, ("world", "WorldScene/basis-arrows.mmlworld")]

SAMPLE_CASE_SETS = {
    "all": ALL_SAMPLE_CASES,
    "fltk": FLTK_SAMPLE_CASES,
    "wpf": WPF_SAMPLE_CASES,
}

LOADER_ERROR_MARKERS = [
    "Cannot open",
    "Expected",
    "Unsupported",
    "No data",
    "Failed to open",
    "Invalid file format",
    "Missing ",
    "Error:",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path, help="Release archive to validate")
    parser.add_argument("--sha256sums", required=True, type=Path, help="SHA256SUMS file from the release")
    parser.add_argument("--expected-version", required=True, help="Expected artifactVersion, usually the release tag without v")
    parser.add_argument("--expected-platform", required=True, help="Expected release-manifest platformId")
    parser.add_argument("--sample-set", choices=sorted(SAMPLE_CASE_SETS), default="all", help="Sample smoke matrix to run")
    parser.add_argument("--work-dir", default=Path(".release-validation"), type=Path, help="Temporary extraction directory")
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_checksum(archive: Path, sha256sums: Path) -> None:
    actual = sha256(archive)
    archive_name = archive.name
    matches = []
    for raw_line in sha256sums.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2 and Path(parts[-1]).name == archive_name:
            matches.append(parts[0].lower())
    if not matches:
        raise RuntimeError(f"{sha256sums} does not contain an entry for {archive_name}")
    if actual.lower() not in matches:
        raise RuntimeError(f"SHA-256 mismatch for {archive_name}: got {actual}, expected one of {matches}")


def extract_archive(archive: Path, work_dir: Path) -> Path:
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    if archive.suffix.lower() == ".zip":
        with zipfile.ZipFile(archive) as handle:
            handle.extractall(work_dir)
    elif archive.name.endswith(".tar.gz") or archive.name.endswith(".tgz"):
        with tarfile.open(archive, "r:gz") as handle:
            handle.extractall(work_dir)
    else:
        raise RuntimeError(f"Unsupported archive type: {archive}")

    roots = [path for path in work_dir.iterdir() if path.is_dir()]
    if len(roots) != 1:
        raise RuntimeError(f"Expected one extracted root directory in {work_dir}, found {len(roots)}")
    return roots[0]


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise RuntimeError(f"Missing JSON file: {path}")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def verify_license_files(release_root: Path, manifest: dict) -> None:
    license_directory = manifest.get("licenseDirectory")
    if license_directory != "licenses":
        raise RuntimeError(f"release-manifest licenseDirectory is {license_directory!r}, expected 'licenses'")

    license_root = release_root / license_directory
    for name in ("MML-Visualizers-LICENSE.md", "third-party-notices.md"):
        path = license_root / name
        if not path.is_file():
            raise RuntimeError(f"Missing release license/notice file: {path}")


def executable_path(release_root: Path) -> Path:
    name = "mmlviz.exe" if os.name == "nt" else "mmlviz"
    path = release_root / "bin" / name
    if not path.is_file():
        raise RuntimeError(f"Missing launcher: {path}")
    return path


def run_command(command: list[str], *, cwd: Path | None = None) -> str:
    completed = subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = completed.stdout or ""
    sys.stdout.write(output)
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {completed.returncode}: {' '.join(command)}")
    return output


def run_mmlviz(mmlviz: Path, args: list[str]) -> str:
    command = [str(mmlviz), *args]
    if sys.platform.startswith("linux") and shutil.which("xvfb-run"):
        command = ["xvfb-run", "-a", *command]
    return run_command(command)


def assert_no_loader_errors(output: str) -> None:
    hits = [marker for marker in LOADER_ERROR_MARKERS if marker in output]
    if hits:
        raise RuntimeError(f"Smoke-test output contains loader error markers: {', '.join(hits)}")


def validate(args: argparse.Namespace) -> None:
    archive = args.archive.resolve()
    sha256sums = args.sha256sums.resolve()
    verify_checksum(archive, sha256sums)

    release_root = extract_archive(archive, args.work_dir.resolve())
    manifest = load_json(release_root / "share" / "mml-visualizers" / "release-manifest.json")
    app_manifest = load_json(release_root / "share" / "mml-visualizers" / "app-manifest.json")

    if manifest.get("artifactVersion") != args.expected_version:
        raise RuntimeError(f"artifactVersion mismatch: {manifest.get('artifactVersion')!r} != {args.expected_version!r}")
    if manifest.get("platformId") != args.expected_platform:
        raise RuntimeError(f"platformId mismatch: {manifest.get('platformId')!r} != {args.expected_platform!r}")
    verify_license_files(release_root, manifest)
    if app_manifest.get("launcher", {}).get("id") != "mmlviz":
        raise RuntimeError("app-manifest launcher id is not 'mmlviz'")

    mmlviz = executable_path(release_root)
    run_mmlviz(mmlviz, ["--version"])
    run_mmlviz(mmlviz, ["list"])

    sample_root = release_root / "share" / "mml-visualizers" / "sample-data"
    smoke_output = []
    for kind, relative_sample in SAMPLE_CASE_SETS[args.sample_set]:
        sample = sample_root / Path(relative_sample)
        if not sample.is_file():
            raise RuntimeError(f"Missing sample for {kind}: {sample}")
        smoke_output.append(run_mmlviz(mmlviz, [kind, str(sample), "--smoke-test", "--exit-after-load"]))
    assert_no_loader_errors("\n".join(smoke_output))

    print(f"Validated {archive.name} for {args.expected_platform}")


def main() -> int:
    try:
        validate(parse_args())
        return 0
    except Exception as exc:  # noqa: BLE001 - command-line tool should report any validation failure.
        print(f"release validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
