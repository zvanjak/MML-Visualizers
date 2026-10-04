# Real Function v1

Schema ID: `mml.real_function.v1`

Use for one or more scalar time/abscissa series. Current visualizers support the legacy headers `REAL_FUNCTION` and `MULTI_REAL_FUNCTION`; public producers should prefer `REAL_FUNCTION` for one series and `MULTI_REAL_FUNCTION` for multiple series.

## Single-Series Layout

```text
# MML_SCHEMA mml.real_function.v1
# columns: x y
REAL_FUNCTION
<title>
x1: <min-x>
x2: <max-x>
NumPoints: <n>
<x0> <y0>
...
```

## Multi-Series Layout

```text
# MML_SCHEMA mml.real_function.v1
# columns: x y1 y2 ...
MULTI_REAL_FUNCTION
<title>
<num-series>
<label-1>
<label-2>
...
x1: <min-x>
x2: <max-x>
NumPoints: <n>
<x0> <y1> <y2> ...
...
```

Sample: `sample-data/RealFunction/parabola.mml`.
