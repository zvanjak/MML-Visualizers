# Installing MML Visualizers

MML Visualizers is distributed as binary release archives. The source code for the visualizer apps is private; this repository contains the public release metadata, documentation, and sample files.

## Download

1. Open the latest release for this repository.
2. Download the archive for your platform:
   - `MML-Visualizers-<version>-windows-x64-msvc143.zip`
   - `MML-Visualizers-<version>-linux-x64-glibc.tar.gz`
   - `MML-Visualizers-<version>-macos-arm64.tar.gz`
3. Download `SHA256SUMS` from the same release.

## Verify

Windows PowerShell:

```powershell
Get-FileHash .\MML-Visualizers-<version>-windows-x64-msvc143.zip -Algorithm SHA256
Get-Content .\SHA256SUMS
```

Linux/macOS:

```bash
sha256sum -c SHA256SUMS
```

On macOS, use `shasum -a 256` if `sha256sum` is unavailable.

## Extract

Extract the archive anywhere writable. Each archive expands to one top-level directory:

```text
MML-Visualizers-<version>-<platform>/
  bin/
  cmake/
  share/mml-visualizers/
  licenses/
```

## Run

Use the toolkit-neutral launcher:

```bash
./bin/mmlviz --version
./bin/mmlviz list
./bin/mmlviz curve3d share/mml-visualizers/sample-data/ParametricCurve3D/helix.mml
```

For automated checks:

```bash
./bin/mmlviz curve3d share/mml-visualizers/sample-data/ParametricCurve3D/helix.mml --smoke-test --exit-after-load
```

Windows PowerShell example:

```powershell
.\bin\mmlviz.exe --version
.\bin\mmlviz.exe list
.\bin\mmlviz.exe curve3d .\share\mml-visualizers\sample-data\ParametricCurve3D\helix.mml
```

## Downstream Integration

Prefer `mmlviz` and the documented schemas over individual implementation executable names.
Individual apps may be Qt-backed in the first prerelease, but the public contract is the launcher
plus schema IDs.

For CMake consumers, see [CMake integration](cmake-integration.md).
