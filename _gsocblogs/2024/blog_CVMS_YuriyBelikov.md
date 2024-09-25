---
project: HSF CernVM-FS
title: CernVM-FS - Integration of FUSE-T libary for macOS laptop clients. Levaraging modern overlay FS features in cvmfs_server
author: Yuriy Belikov
date: 25.09.2024
year: 2024
layout: blog_post
logo:
intro: |
    Worked on integration of modern overlay FS feature in CVMFS server part and replacement of macFUSE kernel extension with FUSE-T user-space library on for macOS laptop clients.
    At this point a backbone for metadata-only copying and zero-copy directory renames is implemented for Linux server part and still goes through a refinement and adjustment 
    due to various differences in overlay FS behaviour discovered on the course of the project. FUSE-T support for macOS clients is primarily done apart several issues that we
    find critical for CVMFS client stability. I helped with creation of GitHub Actions CI pipeline for macOS clients, prepared a table of issues with FUSE-T that were encountered  
    during this project. Currently, I am continuing my work on adding an ability for users to switch back to macFUSE kext.
---

<h3> Project: CernVM-FS - Integration of FUSE-T libary for macOS laptop clients. Levaraging modern overlay FS features in cvmfs_server </h3>
<h3> Mentor: Valentin Volkl</h3>

**Related repositories:** [CVMFS fork](https://github.com/YBelikov/cvmfs), [CVMFS origin](https://github.com/cvmfs/cvmfs)

**Check out my work here:** [FUSE-T](https://github.com/cvmfs/cvmfs/pull/3587), [Overlay FS](https://github.com/cvmfs/cvmfs/pull/3547)
# Getting into the Process
When the accepted projects were announced, I already started my participation in CVMFS project under Ukrainian Remote Student Internship and was already working 
on integrating capabilities provided by metadata only copying for edited files and zero-copy renames in overlay FS at the core of cvmfs_server utility.
However, we outlined replacing macFUSE kernel extension with FUSE-T user-space library as the main goal for GSoC. The motivation behind this is a potential
simplification of macOS client installation process:
- Currently, installing third-party kernel extensions require double reboot
- Manual degrading of macOS security protection mechanisms

On top of that, FUSE-T creats a potential foundation for making a brew package for CVMFS client as well allows creation GitHub Actions macOS CI. 
Moreover I proposed continuation of my work with overlay FS updates during the period of my participation in GSoC what was also welcomed.
Since I had already been in touch with Valentin as with my internship supervisor and other members of CVMFS team there were no need in Community Bonding Period.
Thus, I started working on these tasks.

# Goals and objectives for FUSE-T project
- Determine key components of FUSE-T installation: headers, libraries, any helper binaries
- Update CMake build files accordingly (later we decided to keep backward compatibility with macFUSE kext)
- Update bash scripts that perform various commands on behalf of macOS client accordingly
- Update parts that test the presence of macOS fuse-related libraries
- Change integration tests if necessary to comply with FUSE-T

# Motivation behind cmvfs_server modification 
On **cvmfs_server publish**  command, the utility traverses scratch area and stores information about the contents of repository in file catalogs and the content itself in a compressed manner.
Since compression, hashing and updating file catalogs is performed for full copies of the modified files modern overlay FS features have a potential to improve performance of cvmfs_server transactions via avoiding the unnecessary data copying to scratch area.

However, integrating zero-copy directory renames appeared not as trivial as was firstly expected:
As initial logic of cvmfs transactions relies on the fact that scratch area contains full copies of file system objects zero-copy rename leads to wiping out old directory with all its contents
Subdirectories removal creates a different footprint in the upper-layer directory: a whiteout appears instead of the removed subdirectory which is not the case for a usual setup

# Goals and objectives for overlay FS project
- Enable metacopy and redirect_dir features for CVMFS repositories mounting
- Update scratch area traversal routine accordingly
- Implement catalog entries renaming (avoid remove + add sequence)
- Implement metadata-only update for catalog entries
- Expand integration tests with new cases that cover various renaming scenarios
- Cover new functionality under a separate option that would make it possible to enable/disable this feature

# What was done for overlay FS project:
- Upgrades for scratch area traversal: made it 3-steps currently for proper separation of whiteouts left after a removal and after renaming.
- Upgrades for catalog manager: added object that manage new SQL queries.
- Changes in FS synchronization mechanism to properly handle nested whiteouts.
- New integration test that deal with directories renamings and various related cases: partial modification of a nested content, removal of nested files and directories.
- Tracking the files created with metadata-only xattr.
- Overlay FS documentation got [a tiny patch](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/commit/Documentation/filesystems/overlayfs.rst?id=930b7c32ea2b514fb2c37aa3d4b946d954ee7fa2) clarifying metacopy section.

# What was done for FUSE-T project
- CMake update to overcome issues with dyld failing to find dynamic libraries.
- Updated CMake build files for FUSE-T usage.
- Updated FUSE-T installation check.
- GitHub Actions pipeline with updated macOS CI support (introduced small fixes for GitHub Actions setup created by Valentin). 
- Achieved integration tests passing on a reduced tests set.

# Questions left for overlay FS (and yet to be resolved)
- Benchmarking: since the changes required to make replace one-step scratch area traversal with the three-step (could it be reduced to two-step?).
- How to separate new files from updated files in renamed directories (in principle such entries are absent in readonly layer).
- Is it possible to update only file content hash instead of the whole entry in a catalog DB table?
- Nested catalogs support.

# Encountered issues with FUSE-T (yet to be resolved)
- FUSE-T invokes listxattr before calling getxattr:
- If your filesystem doesn’t expect this you are in trouble: in our case magic attributes doesn’t work properly.
- Hidden extended attributes are not supported; not a big issue since they are utilized by cvmfs_server (which is not supported on macOS)
- Mounting takes a time frame (usually a few seconds) long enough to fail immediate subsequent commands (such as calling **ls \<repo\>** right after mount)
- Sometimes we get directory “loops” inside directories where usually regular files are stored: nested directory refers a parent directory

# Conclusions
That was quite an interesting journey that led to conducting two talks: one during [CERN-SFT group meeting](https://indico.cern.ch/event/1402909/) where I presented my preliminary benchmarks
made for overlay FS redirect_dir and metacopy options on a toy setup; the other one was during [CERN-VM FS Workshop 2024](https://indico.cern.ch/event/1347727/timetable/) where I presented the detailed 
outcomes of my GSoC project in more detailed way.
I am grateful for this opportunity to collaborate on this project and contribute in such a huge organisation as CERN. I want to thank my supervisor
Valentin Volkl for his guidance and support all the way through this period. 
There is still work to do: FUSE-T integration appeared not as easy as we were expecting as it brings some peculiar issues
on repositories reloads and IPC management that are yet to be resolved.
As well overlay FS part contained various not-so-trivial parts such as nested whiteouts and partial content updates for directories.
I hope I will help with resolution of the remaining issues and my work will be good foundation for the future release of CVMFS.
