# Parametric Curve 3D v1

Schema ID: `mml.parametric_curve_3d.v1`

Use for sampled spatial parametric curves and trajectories.

```text
# MML_SCHEMA mml.parametric_curve_3d.v1
# columns: t x y z
PARAMETRIC_CURVE_CARTESIAN_3D
<title>
t1: <min-t>
t2: <max-t>
NumPoints: <n>
<t0> <x0> <y0> <z0>
...
```

Legacy spherical and cylindrical files may use `PARAMETRIC_CURVE_SPHERICAL_3D` or `PARAMETRIC_CURVE_CYLINDRICAL_3D`. Public Cartesian samples should use `PARAMETRIC_CURVE_CARTESIAN_3D`.

Sample: `sample-data/ParametricCurve3D/helix.mml`.
