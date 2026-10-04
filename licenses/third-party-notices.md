# Third-Party Notices

This file is the notice entry point for MML Visualizers release archives. The first-party MML
Visualizers license is installed beside it as `MML-Visualizers-LICENSE.md`.

MML Visualizers release archives can be produced in three families:

- `MML-Visualizers`: Qt 6 / OpenGL visualizers.
- `MML-Visualizers-FLTK`: FLTK visualizers.
- `MML-Visualizers-WPF`: Windows-only WPF visualizers targeting .NET 8.

Every release artifact must keep this file and the component notice files in the `licenses/`
directory. The exact files redistributed by a platform artifact are controlled by the release
manifest, app manifest, CMake install rules, and deployment tool output. Re-run the release gate for
the artifact being published and verify that its shipped binaries match this notice inventory.

## Component Notice Files

The release notice set is:

- `MML-Visualizers-LICENSE.md` - first-party MML Visualizers license.
- `Qt-LICENSE.md` - Qt runtime libraries, plugins, and deployment tools.
- `FLTK-LICENSE.md` - FLTK runtime libraries or statically linked FLTK code.
- `DotNet-WPF-NOTICES.md` - WPF/.NET runtime requirements and redistribution notes.
- `OpenGL-NOTICES.md` - OpenGL/GLU and platform graphics dependencies.
- `Compiler-Runtime-NOTICES.md` - MSVC, libstdc++, libc++, and other compiler runtime notes.
- `ICU-LICENSE.md` - ICU libraries when bundled with Qt releases, especially Linux archives.

Do not publish a binary release until the exact redistributed dependency set has been reviewed for
the specific platform artifact.
