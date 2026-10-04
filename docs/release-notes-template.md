# MML Visualizers <version> Release Notes

## Downloads

| Platform | Archive | SHA-256 |
| --- | --- | --- |
| Windows x64 | `MML-Visualizers-<version>-windows-x64-msvc143.zip` | See `SHA256SUMS` |
| Linux x64 | `MML-Visualizers-<version>-linux-x64-glibc.tar.gz` | See `SHA256SUMS` |
| macOS arm64 | `MML-Visualizers-<version>-macos-arm64.tar.gz` | See `SHA256SUMS` |

## Scope

- Qt-backed visualizer binaries exposed through `mmlviz`.
- Public v1 file schemas and sample data.
- FLTK and WPF visualizers are deferred from this prerelease.

## Validation

- `mmlviz --version`
- `mmlviz list`
- One smoke-load sample per supported visualizer kind with `--smoke-test --exit-after-load`
- Archive checksum verification
- Manifest/platform/version checks

## Compatibility

- MML Core: `>=2.0.0`
- MML Packages: `>=0.1.0-rc.5`

## Known Limitations

- Smoke tests validate launch and file loading, not full interactive rendering behavior.
- Linux headless CI may require `xvfb-run`.
- macOS prerelease artifacts may require local trust handling if unsigned.

## Changes

- Add release highlights here.

## Checksums

Paste or attach `SHA256SUMS` from the release gate.
