# MML Visualizer File Formats

MML Visualizer files are plain text so numerical tools can generate them without linking to visualizer code. Public v1 files use a schema comment followed by the legacy visualizer header that current apps already understand:

```text
# MML_SCHEMA mml.parametric_curve_3d.v1
# name: Example
# columns: t x y z
PARAMETRIC_CURVE_CARTESIAN_3D
Example
...
```

Rules shared by all v1 schemas:

- Lines beginning with `#` are comments and may carry metadata.
- The `# MML_SCHEMA <schema-id>` line identifies the public stable schema.
- The first non-comment line is the legacy visualizer header used by current binaries.
- Numeric values use decimal text with `.` as the decimal separator.
- Data rows are whitespace separated unless the schema explicitly documents comma-separated rows.
- Producers may add extra comment metadata, but should not add extra non-comment records unless the schema allows it.

## Schemas

| Schema ID | Document | Sample |
| --- | --- | --- |
| `mml.real_function.v1` | [real-function-v1.md](real-function-v1.md) | `sample-data/RealFunction/parabola.mml` |
| `mml.parametric_curve_2d.v1` | [parametric-curve-2d-v1.md](parametric-curve-2d-v1.md) | `sample-data/ParametricCurve2D/unit-circle.mml` |
| `mml.parametric_curve_3d.v1` | [parametric-curve-3d-v1.md](parametric-curve-3d-v1.md) | `sample-data/ParametricCurve3D/helix.mml` |
| `mml.particle_2d.v1` | [particle-2d-v1.md](particle-2d-v1.md) | `sample-data/ParticleVisualizer2D/two-particles.mml` |
| `mml.particle_3d.v1` | [particle-3d-v1.md](particle-3d-v1.md) | `sample-data/ParticleVisualizer3D/two-particles.mml` |
| `mml.scalar_function_2d.v1` | [scalar-function-2d-v1.md](scalar-function-2d-v1.md) | `sample-data/ScalarFunction2D/saddle.mml` |
| `mml.scalar_function_3d.v1` | [scalar-function-3d-v1.md](scalar-function-3d-v1.md) | `sample-data/ScalarFunction3D/gaussian-blob.mml` |
| `mml.vector_field_2d.v1` | [vector-field-2d-v1.md](vector-field-2d-v1.md) | `sample-data/VectorField2D/rotation.mml` |
| `mml.vector_field_3d.v1` | [vector-field-3d-v1.md](vector-field-3d-v1.md) | `sample-data/VectorField3D/radial.mml` |
| `mml.parametric_surface.v1` | [parametric-surface-v1.md](parametric-surface-v1.md) | `sample-data/ParametricSurface/patch.mml` |
| `mml.rigid_body_motion.v1` | [rigid-body-motion-v1.md](rigid-body-motion-v1.md) | `sample-data/RigidBodyMovement/spinning-box.mml` |
