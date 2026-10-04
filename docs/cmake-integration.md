# CMake Integration

Installed MML Visualizers archives include a CMake package config in `cmake/` so downstream projects can discover the released tools without the private source tree.

Point `CMAKE_PREFIX_PATH` at the extracted release root, then call `find_package`:

```cmake
find_package(MMLVisualizers CONFIG REQUIRED)

add_custom_target(open_curve3d_sample
    COMMAND MMLVisualizers::mmlviz
            curve3d
            "${MMLVisualizers_SAMPLE_DATA_DIR}/ParametricCurve3D/helix.mml"
    VERBATIM
)
```

The package defines these path variables:

```cmake
MMLVisualizers_VERSION
MMLVisualizers_SHARE_DIR
MMLVisualizers_SAMPLE_DATA_DIR
MMLVisualizers_FILE_FORMATS_DIR
```

The stable launcher target is:

```cmake
MMLVisualizers::mmlviz
```

Archives that include the corresponding applications also expose individual executable targets:

```cmake
MMLVisualizers::RealFunction
MMLVisualizers::ParametricCurve2D
MMLVisualizers::ParametricCurve3D
MMLVisualizers::Particle2D
MMLVisualizers::Particle3D
MMLVisualizers::ScalarFunction2D
MMLVisualizers::ScalarFunction3D
MMLVisualizers::VectorField2D
MMLVisualizers::VectorField3D
MMLVisualizers::ParametricSurface
MMLVisualizers::RigidBodyMovement
```

Prefer `MMLVisualizers::mmlviz` for automation and cross-version compatibility. Use individual targets only when a downstream project intentionally needs to launch a specific implementation executable.
