# Installing MML Visualizers

MML Visualizers is distributed as binary release archives. The source code for the visualizer apps is private; this repository contains the public release metadata, documentation, and sample files.

## Download

1. Open the latest release for this repository.
2. Download the archive for your platform:
   - `MML-Visualizers-<version>-windows-x64-msvc143.zip`
   - `MML-Visualizers-<version>-linux-x64-glibc.tar.gz`
   - `MML-Visualizers-<version>-macos-arm64.tar.gz`
  - Optional FLTK 2D companion archives:
    - `MML-Visualizers-FLTK-<version>-windows-x64-msvc143.zip`
    - `MML-Visualizers-FLTK-<version>-linux-x64-glibc.tar.gz`
    - `MML-Visualizers-FLTK-<version>-macos-arm64.tar.gz`
  - Optional Windows WPF companion archive:
    - `MML-Visualizers-WPF-<version>-windows-x64-msvc143.zip`
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

FLTK archives use the same layout under an `MML-Visualizers-FLTK-<version>-<platform>/`
directory and include the `real-function`, `curve2d`, `particle2d`, and `vector2d` launcher kinds.
WPF archives use the same layout under an `MML-Visualizers-WPF-<version>-windows-x64-msvc143/`
directory, include the full native Windows app catalog including `world` scenes, and require the
.NET 8 Desktop Runtime on Windows.

## License

Read `licenses/MML-Visualizers-LICENSE.md` in the extracted archive before using the tools. MML
Visualizers are free for personal, educational, and non-commercial academic use. Commercial use
requires a separate paid commercial license.

The license applies to the visualizer applications and release binaries. Your `.mml` and
`.mmlworld` files are your data; the public schemas, generated data files, and small samples are
intended to remain freely usable unless a specific file says otherwise.

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
Individual apps may be Qt-backed, FLTK-backed, or WPF-backed depending on the archive family, but
the public contract is the launcher plus schema IDs.

For CMake consumers, see [CMake integration](cmake-integration.md).
