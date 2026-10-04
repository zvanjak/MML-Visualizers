# Parametric Curve 2D v1

Schema ID: `mml.parametric_curve_2d.v1`

Use for sampled planar parametric curves.

```text
# MML_SCHEMA mml.parametric_curve_2d.v1
# columns: t x y
PARAMETRIC_CURVE_CARTESIAN_2D
<title>
t1: <min-t>
t2: <max-t>
NumPoints: <n>
<t0> <x0> <y0>
...
```

Legacy polar files may use `PARAMETRIC_CURVE_POLAR_2D`; public Cartesian samples should use `PARAMETRIC_CURVE_CARTESIAN_2D`.

Sample: `sample-data/ParametricCurve2D/unit-circle.mml`.
