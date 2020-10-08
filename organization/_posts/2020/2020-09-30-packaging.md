---
title: "HSF Software Tools and Packaging Working Group Meeting #30, 30th September 2020"
layout: meetings
---
# HSF Software Tools and Packaging Working Group Meeting #3, 30th September 2020

*This notebook is used to record the minutes of the HSF Software Tools and Packaging meetings. These are archived after each meeting onto the [HSF Website](https://hepsoftwarefoundation.org).*

*If you find you cannot edit these notes please login with your GitHub account!*

Present/Contributors: Ben Morgan, Serhan Mete, Andre Sailer, Attila Krasznahorkay, Charles Leggett, Frank Winklmeier, Graeme Stewart, Henry Schreiner, Jim Pivarski, Matti Kortelainen, Tao Lin, Chris Green, Brett, Liz Sexton-Kennedy, James Amundson

Apologies: 

## Introduction (Ben)
- As always, ideas or requests for presentations/topical meetings welcome! Just contact Ben, Serhan and Martin.
    - Likely have updates/tutorials on some packaging tools in next month or two (will discuss offline/through mailing list)
- Please note upcoming [HSF/WLCG Virtual Workshop, 19-24 November](https://indico.cern.ch/event/941278/)
    - Especially [call for abstracts](https://indico.cern.ch/event/941278/abstracts/) on any software/development R&D


## An Introduction to Modern CMake (Henry)
- One main take-home: links on the front page to blog and training links
- Talk is interactive, so can follow along, or revisit using the link on the agenda
- Based on CMake 3.18
- Example on Rake
    - Knows what to run, but less ...
- CMake = Build system generator
    - But can use it to trigger build/install
- Core concepts
    - minimal script
    - separation of build/source dirs
- Wide range of buildsystems for C/C++
    - cmake, scons, meson, bazel 
    - Other languages have their own (e.g. Rust)
- CMake has become a standard tool
    - Wide IDE support (either in CMake, or via IDEs themselves)
    - Libraries provide support for integration
- Custom buildsystems going away
    - e.g Qt6, Boost
    - Google dual support Bazel, CMake
- Growing support/improvements in things like Thrust/TBB/PyBind11
    - Attila: Isn't TBB still using plain Make? Henry: main thing is that TBB installs a "TBBConfig.cmake" file that allows easy use of TBB in CMake projects.
- "Modern" CMake roughly from 2014 with CMake 3.0
    - "Target" based
    - CMake 3.12 "more modern cmake", unified target behaviour
- CMake backward compatibility with policies
    - The `cmake_minimum_required` command
    - CMake 3.12 introduced version ranges for this
    - Do/Don't recommendation
    - Chris: Also minimum version determined by needs for commands (e.g. subcommands in list)
    - Henry: yes, key thing is the "Do" on testing with lowest version you want to support
    - Example of a bad policy in CMake 3.9:
        - breaks IPO
    - Thus the recommendation on don't setting the min version low without a range
    - Attila: big problem is updating min version through a project's file
    - Henry: one recommendation here (though CMake didn't do this themselves) is not to set minimum required on anything other than `CMakeLists.txt`.
- Minimum versions by OS (e.g. "out-the-box" on CentOS etc), vs CMake features (what it can do)
- Installing CMake now very easy across all platforms (inc. GitLab/Hub CI)
    - See the installing page on the website
- Modern cmake has better CLI, so can run underlying configure/build/test/install directly through the `cmake` command
- Key CMake convention: property initialization
    - A property `MY_PROPERTY` initialized by `CMAKE_MY_PROPERTY`
- Key tips for packaging:
    - Use targets
    - Don't write a "FindMyPackage", write "MyPackageConfig"
    - Don't hardcode system/compiler/flags in targets
- Downloading dependencies
    - classic: ExternalProject (build time)
    - new: FetchContent, (configure time)
        - Like submodules, much easier integration, direct use of targets provided by subproject.
- Can also integrate with Conan/Conan.io
    - requires conan (but can bootstrap it in your cmake script)
- Imported targets
    - A target that comes from outside the project
    - Cmake 3.11 now makes these much easier to define much like all other targets
- CUDA a first class language from 3.8/9, more development since then, including
    - C++ standards
    - .cu files automatically handled with nvcc
- Attila: should things like CMAKE_CXX/CUDA_STANDARD be cached (so can override)?
    - Henry: yes, and also consider using compile features
- Chris: Is it possible to have a subproject that uses a language that the top level project doesn't?
    - Henry: it should be, but would need to check
    - Chris: have had this fail up to 3.14
    - To be checked!
- Major updates to CUDA support in 3.17/18
    - architectures, clang, shared cudart, FindCUDAToolkit
- Extra tools and integrations
    - IPO/PIC
    - ccache
    - clang-tidy, clang tooling
    - Work well with GitHub Actions (and ci)
- Also a cmake-format tool now
    - Just like black/clang-format for CMake
    - Builtin GitHub Action support
- Use try_compile/try_run/WriteCompilerDetectionHeader to check/addpt to different compilers
- Python and CMake
    - New "FindPython" module is recommended over separate Interp/Libs modules
    - Best since 3.15, PyPy needs 3.18
    - Attila: Quite slow in ATLAS due to number of calls
    - Henry: due to behaviour of FindPython in supporting multiple versions, so trying to refind Python each call. Is a variable that can be set to disable that. Looks like this is new in 3.18. Can vendor this in projects if you can't require 3.18.
- Python/CMake: See Scikit-build and CMake wheels
    - Not as reliable as setuptools for non-standard Python setups
    - See [https://github.com/scikit-hep/boost-histogram](https://github.com/scikit-hep/boost-histogram) for an example
- Contributions to the HSF training and CLI repo welcome!
- Chris: Is there any support for symbol visibility?
    - Henry: there are target properties to set the default visibility
    - Attila: there is a module for this? Yes, [GenerateExportHeader](https://cmake.org/cmake/help/latest/module/GenerateExportHeader.html)!
- Liz: With modern CMake, has the overlap between build/package managers increased?
    - Henry: still a role for downloading binaries with a package manager, though there's good integration with Conan
    - Attila: still think there's a role for a higher level tools, e.g. for hardware level optimization
    - Patrick: there is good communication between spack and cmake to make them work well together
    - Chris: Upgrades to CETmodules are integrating the modern features, with spack.
    - Graeme: EP-SFT at CERN working on turn key stack using spack
## AOB
