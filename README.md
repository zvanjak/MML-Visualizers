<div align="center">

# 📊 MML Visualizers

### **Interactive visual tools for Minimal Math Library data**

*Functions • curves • surfaces • fields • particles • rigid bodies • world scenes*

[![Validate release](https://github.com/zvanjak/MML-Visualizers/actions/workflows/validate-release.yml/badge.svg)](https://github.com/zvanjak/MML-Visualizers/actions/workflows/validate-release.yml)
[![Latest release](https://img.shields.io/github/v/release/zvanjak/MML-Visualizers?label=release)](https://github.com/zvanjak/MML-Visualizers/releases)
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20macOS-blue)](#gallery)
[![License](https://img.shields.io/badge/license-free%20personal%2Feducation%20%7C%20commercial%20paid-blue.svg)](LICENSE.md)

**Turn MML `.mml` and `.mmlworld` data files into interactive plots, surfaces, animations, and scenes.**

[Releases](https://github.com/zvanjak/MML-Visualizers/releases) • [Gallery](#gallery) • [Install](docs/install.md) • [File formats](docs/file-formats) • [Sample data](sample-data)

</div>

---

Public release companion for the Minimal Math Library visualizer tools.

This repository is the public home for binary releases, file-format documentation, sample data,
checksums, and release validation. The visualizer source code is developed privately; users consume
released archives and the stable `mmlviz` launcher.

MML Visualizers are free for personal, educational, and non-commercial academic use. Commercial
use requires a separate paid commercial license; see [LICENSE.md](LICENSE.md) and
[Licenses and notices](licenses/README.md).

## Quick Start

1. Download the archive for your platform from [Releases](https://github.com/zvanjak/MML-Visualizers/releases).
2. Verify it with `SHA256SUMS`.
3. Extract it and run the toolkit-neutral launcher:

```text
mmlviz --version
mmlviz list
mmlviz open sample-data/ScalarFunction2D/saddle.mml
```

You can also launch a specific visualizer kind:

```text
mmlviz scalar2d sample-data/ScalarFunction2D/saddle.mml
mmlviz curve3d sample-data/ParametricCurve3D/helix.mml
mmlviz rigid-body sample-data/RigidBodyMovement/spinning-box.mml
```

---

## Gallery

### Windows — WPF Visualizers

<table>
<tr>
<td align="center" width="25%">

**Real Functions**

![WPF Real](docs/images/readme/visualization_suite/win/wpf_real_func_multi_damped_oscillations.png)

</td>
<td align="center" width="25%">

**Real Functions (Lorentz)**

![WPF Lorentz](docs/images/readme/visualization_suite/win/wpf_real_func_multi_Lorentz.png)

</td>
<td align="center" width="25%">

**Scalar Function 2D**

![WPF Scalar 2D](docs/images/readme/visualization_suite/win/wpf_scalar_func_2d.png)

</td>
<td align="center" width="25%">

**Scalar Function 3D**

![WPF Scalar 3D](docs/images/readme/visualization_suite/win/wpf_scalar_func_3d.png)

</td>
</tr>
<tr>
<td align="center">

**Parametric Curve 2D**

![WPF Curve 2D](docs/images/readme/visualization_suite/win/wpf_param_curve_2d_butterfly.png)

</td>
<td align="center">

**Parametric Curve 3D**

![WPF Curve 3D](docs/images/readme/visualization_suite/win/wpf_param_curve_3d.png)

</td>
<td align="center">

**Parametric Surface**

![WPF Surface](docs/images/readme/visualization_suite/win/wpf_param_surface.png)

</td>
<td align="center">

**Vector Field 3D**

![WPF VecField](docs/images/readme/visualization_suite/win/wpf_vector_field_3d.png)

</td>
</tr>
<tr>
<td align="center">

**Particle Visualizer 2D**

![WPF Particle 2D](docs/images/readme/visualization_suite/win/wpf_particle_vis_2d.png)

</td>
<td align="center">

**Particle Visualizer 3D**

![WPF Particle 3D](docs/images/readme/visualization_suite/win/wpf_particle_vis_3d.png)

</td>
<td align="center">

**Rigid Body Simulation**

![WPF Rigid](docs/images/readme/visualization_suite/win/wpf_rigid_body.png)

</td>
<td align="center">

</td>
</tr>
</table>

### Windows — Qt Visualizers

<table>
<tr>
<td align="center" width="25%">

**Real Functions**

![Qt Real](docs/images/readme/visualization_suite/win/win_qt_real_func_multi.png)

</td>
<td align="center" width="25%">

**Scalar Function 2D**

![Qt Scalar 2D](docs/images/readme/visualization_suite/win/win_qt_scalar_func_2d.png)

</td>
<td align="center" width="25%">

**Scalar Function 3D**

![Qt Scalar 3D](docs/images/readme/visualization_suite/win/win_qt_scalar_func_3d.png)

</td>
<td align="center" width="25%">

**Parametric Surface**

![Qt Surface](docs/images/readme/visualization_suite/win/win_qt_param_surface.png)

</td>
</tr>
<tr>
<td align="center">

**Parametric Curve 2D**

![Qt Curve 2D](docs/images/readme/visualization_suite/win/win_qt_param_curve_2d.png)

</td>
<td align="center">

**Parametric Curve 3D**

![Qt Curve 3D](docs/images/readme/visualization_suite/win/win_qt_param_curve_3d.png)

</td>
<td align="center">

**Vector Field 3D**

![Qt VecField](docs/images/readme/visualization_suite/win/win_qt_vector_field_3d.png)

</td>
<td align="center">

**Rigid Body Simulation**

![Qt Rigid](docs/images/readme/visualization_suite/win/win_qt_rigid_body.png)

</td>
</tr>
<tr>
<td align="center">

**Particle Visualizer 2D**

![Qt Particle 2D](docs/images/readme/visualization_suite/win/win_qt_particle_vis_2d.png)

</td>
<td align="center">

**Particle Visualizer 3D**

![Qt Particle 3D](docs/images/readme/visualization_suite/win/win_qt_particle_vis_3d.png)

</td>
<td align="center">

</td>
<td align="center">

</td>
</tr>
</table>

### Linux — Qt Visualizers

<table>
<tr>
<td align="center" width="25%">

**Real Functions**

![Linux Real](docs/images/readme/visualization_suite/linux/linux_qt_real_func_multri.png)

</td>
<td align="center" width="25%">

**Scalar Function 2D**

![Linux Scalar 2D](docs/images/readme/visualization_suite/linux/linux_qt_scalar_func_2d.png)

</td>
<td align="center" width="25%">

**Scalar Function 3D**

![Linux Scalar 3D](docs/images/readme/visualization_suite/linux/linux_qt_scalar_func_3d.png)

</td>
<td align="center" width="25%">

**Parametric Surface**

![Linux Surface](docs/images/readme/visualization_suite/linux/linux_qt_param_surface.png)

</td>
</tr>
<tr>
<td align="center">

**Parametric Curve 2D**

![Linux Curve 2D](docs/images/readme/visualization_suite/linux/linux_qt_param_curve_2d.png)

</td>
<td align="center">

**Parametric Curve 3D**

![Linux Curve 3D](docs/images/readme/visualization_suite/linux/linux_qt_param_curve_3d.png)

</td>
<td align="center">

**Vector Field 3D**

![Linux VecField](docs/images/readme/visualization_suite/linux/linux_qt_vector_field_3d.png)

</td>
<td align="center">

**Rigid Body Simulation**

![Linux Rigid](docs/images/readme/visualization_suite/linux/linux_qt_rigid_body_vis.png)

</td>
</tr>
<tr>
<td align="center">

**Particle Visualizer 2D**

![Linux Particle 2D](docs/images/readme/visualization_suite/linux/linux_qt_particle_vis_2d.png)

</td>
<td align="center">

**Particle Visualizer 3D**

![Linux Particle 3D](docs/images/readme/visualization_suite/linux/linux_qt_particle_vis_3d.png)

</td>
<td align="center">

**Scalar 2D (Dark Theme)**

![Linux Scalar Dark](docs/images/readme/visualization_suite/linux/linux_qt_scalar_func_2d_dark.png)

</td>
<td align="center">

**Parametric Surface (Dark)**

![Linux Surface Dark](docs/images/readme/visualization_suite/linux/linux_qt_param_surface_dark.png)

</td>
</tr>
</table>

### macOS — Qt Visualizers

<table>
<tr>
<td align="center" width="25%">

**Real Functions**

![Mac Real](docs/images/readme/visualization_suite/mac/mac_qt_real_func_multi.png)

</td>
<td align="center" width="25%">

**Real Functions (Lorentz)**

![Mac Lorentz](docs/images/readme/visualization_suite/mac/mac_qt_real_func_multi_Lorentz_system.png)

</td>
<td align="center" width="25%">

**Scalar Function 2D**

![Mac Scalar 2D](docs/images/readme/visualization_suite/mac/mac_qt_scalar_func_2d_monkey_saddle.png)

</td>
<td align="center" width="25%">

**Scalar Function 3D**

![Mac Scalar 3D](docs/images/readme/visualization_suite/mac/mac_qt_scalar_function_3d_gyroid.png)

</td>
</tr>
<tr>
<td align="center">

**Parametric Curve 2D**

![Mac Curve 2D](docs/images/readme/visualization_suite/mac/mac_qt_param_curve_2de_butterfly.png)

</td>
<td align="center">

**Parametric Curve 3D**

![Mac Curve 3D](docs/images/readme/visualization_suite/mac/mac_qt_param_curve_3d_trefoil.png)

</td>
<td align="center">

**Parametric Surface**

![Mac Surface](docs/images/readme/visualization_suite/mac/mac_qt_param_surface_klein.png)

</td>
<td align="center">

**Vector Field 3D**

![Mac VecField](docs/images/readme/visualization_suite/mac/mac_qt_vector_field_3d_gravity.png)

</td>
</tr>
<tr>
<td align="center">

**Particle Visualizer 2D**

![Mac Particle 2D](docs/images/readme/visualization_suite/mac/mac_qt_particle_visualizer_2d.png)

</td>
<td align="center">

**Particle Visualizer 3D**

![Mac Particle 3D](docs/images/readme/visualization_suite/mac/mac_qt_partice_visualizer_3d.png)

</td>
<td align="center">

**Scalar Function 2D (Ripple)**

![Mac Ripple](docs/images/readme/visualization_suite/mac/mac_qt_scalar_func_2d_ripple.png)

</td>
<td align="center">

**Rigid Body Simulation**

![Mac Rigid](docs/images/readme/visualization_suite/mac/mac_qt_rigid_body.png)

</td>
</tr>
</table>

## Release Families

The primary `MML-Visualizers` archives are Qt-backed packages exposed through the toolkit-neutral
`mmlviz` launcher and cover the cross-platform public app catalog. `MML-Visualizers-FLTK` archives are a
lighter FLTK-backed companion family for the four 2D visualizers implemented in FLTK:
real functions, 2D parametric curves, 2D particle motion, and 2D vector fields.
`MML-Visualizers-WPF` archives are Windows-only, framework-dependent WPF packages covering the
full native Windows visualizer family, including world-scene `.mmlworld` files.

## Documentation

- [Install and run released archives](docs/install.md)
- [CMake integration](docs/cmake-integration.md)
- [App catalog](docs/app-catalog.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Release notes template](docs/release-notes-template.md)
- [Licenses and notices](licenses/README.md)
- [File formats](docs/file-formats)
- [Sample data](sample-data)

## Release Health

The public validation workflow downloads a published release archive, verifies `SHA256SUMS`,
extracts the package, checks manifests and required license/notice files, runs `mmlviz --version`
and `mmlviz list`, then smoke-loads one public sample for every visualizer kind in that release
family. Qt archives validate the cross-platform catalog, WPF archives also validate the Windows-only
world-scene visualizer, and FLTK archives validate the four FLTK-supported 2D visualizers. The
workflow can be run manually for a release tag and also runs when a release is published.

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
- World scenes (`.mmlworld`, WPF release family)

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
