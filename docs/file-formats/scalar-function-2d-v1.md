# Scalar Function 2D v1

Schema ID: `mml.scalar_function_2d.v1`

Use for sampled scalar fields on a 2D grid.

```text
# MML_SCHEMA mml.scalar_function_2d.v1
# columns: x y value
SCALAR_FUNCTION_CARTESIAN_2D
<title>
x1: <min-x>
x2: <max-x>
NumPointsX: <nx>
y1: <min-y>
y2: <max-y>
NumPointsY: <ny>
<x> <y> <value>
...
```

Rows may be ordered in any consistent grid traversal; current generators usually write x-major rows.

Sample: `sample-data/ScalarFunction2D/saddle.mml`.
