# MML Visualizers

Public release companion for the Minimal Math Library visualizer tools.

This repository is the public home for binary releases, file-format documentation, sample data,
checksums, and release validation. The visualizer source code is developed privately; users consume
released archives and the stable `mmlviz` launcher.

## First Prerelease Scope

The first planned prerelease, `v0.1.0-rc.1`, is a Qt-backed binary package exposed through the
toolkit-neutral `mmlviz` launcher. FLTK visualizers and Windows-only WPF extras are deferred from
this initial archive line so the first release can focus on one validated runtime packaging path.

## File Formats

The public v1 visualizer schemas are documented in [docs/file-formats](docs/file-formats). They
cover:

- Real functions
- 2D and 3D parametric curves
- 2D and 3D particle motion
- 2D and 3D scalar fields
- 2D and 3D vector fields
- Parametric surfaces
- Rigid-body motion

Small loadable examples live in [sample-data](sample-data). Each public sample begins with a
`# MML_SCHEMA ...` line and keeps the legacy first non-comment visualizer header so current binary
visualizers can load it.

## Launcher Contract

Released archives expose `mmlviz` as the stable command-line entry point:

```text
mmlviz --version
mmlviz list
mmlviz open <file>
mmlviz <kind> <file>
mmlviz <kind> <file> --smoke-test --exit-after-load
```

Downstream projects such as MML-Packages and SigmaEngine should target `mmlviz` plus the public
schemas instead of invoking individual visualizer executables directly.
