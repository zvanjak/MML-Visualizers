# Troubleshooting

## `mmlviz` Is Not Found

Run it from the extracted archive's `bin` directory or add that directory to `PATH`.

Windows:

```powershell
.\bin\mmlviz.exe --version
```

Linux/macOS:

```bash
./bin/mmlviz --version
```

## A File Opens With The Wrong Visualizer

Each public file should start with a schema line such as:

```text
# MML_SCHEMA mml.parametric_curve_3d.v1
```

If no schema line exists, `mmlviz` falls back to the first non-comment legacy header. Check the format docs in `docs/file-formats/` and compare against a sample in `sample-data/`.

## Smoke Test Exits Nonzero

Run the same command without filtering output and check for loader messages:

```bash
mmlviz curve3d sample-data/ParametricCurve3D/helix.mml --smoke-test --exit-after-load
```

Common causes:

- The sample path is relative to a different working directory.
- The file has a schema ID that does not match the selected kind.
- The archive was copied without its runtime libraries or plugins.
- On Linux, a GUI display or `xvfb-run` may be required in headless CI.

## Windows Runtime Or Plugin Errors

Use the released archive as extracted. Do not copy only `mmlviz.exe`; Qt runtime DLLs and plugins must remain next to the staged binaries.

## Linux Headless CI

Use `xvfb-run` when running smoke tests on a machine without a display:

```bash
xvfb-run -a ./bin/mmlviz curve3d share/mml-visualizers/sample-data/ParametricCurve3D/helix.mml --smoke-test --exit-after-load
```

## macOS Gatekeeper

Unsigned prerelease archives may require normal local trust handling before first launch. Prefer running `mmlviz --version` and a smoke test before opening large data files interactively.

## Reporting Problems

Include:

- Platform and archive name.
- Output of `mmlviz --version`.
- The exact command that failed.
- The first lines of the input file, including `# MML_SCHEMA` if present.
