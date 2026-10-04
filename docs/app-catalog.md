# App Catalog

All apps are launched through `mmlviz`. The `implementation` value is informational; downstream projects should use the stable kind and schema IDs.

| Kind | Display name | Primary schema | Archive families |
| --- | --- | --- | --- |
| `real-function` | MML Real Function Visualizer | `mml.real_function.v1` | Qt, FLTK, WPF |
| `curve2d` | MML Parametric Curve 2D Visualizer | `mml.parametric_curve_2d.v1` | Qt, FLTK, WPF |
| `curve3d` | MML Parametric Curve 3D Visualizer | `mml.parametric_curve_3d.v1` | Qt, WPF |
| `particle2d` | MML Particle 2D Visualizer | `mml.particle_2d.v1` | Qt, FLTK, WPF |
| `particle3d` | MML Particle 3D Visualizer | `mml.particle_3d.v1` | Qt, WPF |
| `scalar2d` | MML Scalar Function 2D Visualizer | `mml.scalar_function_2d.v1` | Qt, WPF |
| `scalar3d` | MML Scalar Function 3D Visualizer | `mml.scalar_function_3d.v1` | Qt, WPF |
| `vector2d` | MML Vector Field 2D Visualizer | `mml.vector_field_2d.v1` | Qt, FLTK, WPF |
| `vector3d` | MML Vector Field 3D Visualizer | `mml.vector_field_3d.v1` | Qt, WPF |
| `surface` | MML Parametric Surface Visualizer | `mml.parametric_surface.v1` | Qt, WPF |
| `rigid-body` | MML Rigid Body Motion Visualizer | `mml.rigid_body_motion.v1` | Qt, WPF |
| `world` | MML World Scene Visualizer | `mml.world_scene.v1` | WPF |

## Commands

List available apps in an extracted release:

```bash
mmlviz list
```

Open by kind:

```bash
mmlviz curve3d path/to/file.mml
```

Open by schema/header detection:

```bash
mmlviz open path/to/file.mml
```

Run release smoke mode:

```bash
mmlviz curve3d path/to/file.mml --smoke-test --exit-after-load
```
