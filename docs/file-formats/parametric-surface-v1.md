# Parametric Surface v1

Schema ID: `mml.parametric_surface.v1`

Use for sampled parametric surfaces.

```text
# MML_SCHEMA mml.parametric_surface.v1
# columns: u w x y z
PARAMETRIC_SURFACE_CARTESIAN
<title>
u1: <min-u>
u2: <max-u>
NumPointsU: <nu>
w1: <min-w>
w2: <max-w>
NumPointsW: <nw>
<u> <w> <x> <y> <z>
...
```

The second parameter is named `w` to match the existing visualizer files.

Sample: `sample-data/ParametricSurface/patch.mml`.
