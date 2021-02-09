---
title: CVMFS preload capability
layout: default
project: CernVM-FS
year: 2021
organization:
 - CERN
---


## Description
[CernVM-FS (CVMFS)][cvmfs] is a service for fast and reliable software distribution on a global scale. It is capable of delivering the scientific software used by the High Energy Physics (HEP) community to thousands of client nodes worldwide. Data is organized in repositories that are mounted as a POSIX read-only file system by the clients. Files and metadata are downloaded on-demand by means of HTTP requests and take advantage of several layers of caches.

As of today, distribution and caching are based on a per-file granularity. In some cases, however, it is known upfront that all files of a certain set are required if any of the files is accessed. This is the case, for instance, of well-known Python libraries (e.g., Tensorflow) that upon start always load a certain set of inter-dependent python files. The ability to load all required files together would improve performance in case of cold caches.

The goal of this project is to introduce the concept of _bundles_ in CVMFS to provide a preload capability:
  1. A bundle is a special object with the binary format of an object pack that is used to concatenate multiple objects in a single blob. Bundles are created by the CVMFS server at the time of publication (i.e., when new content is added to the repository) and are then stored and distributed to clients.
  2. Special hidden files `.cvmfsbundles` list of files that belong to a bundle. The list must contain only regular files and every file can only belong to one bundle at most. The list of files belonging to a bundle is maintained by the repository administrators.
  3. The directory structure of a repository is represented in the form of _catalogs_, a database table storing the metadata of files. The table should include an additional column that specifies a bundle identifier (`bundle_id`) so that when a file is fetched also the corresponding bundle can be identified and downloaded.
  4. When the client has a cache miss for a file that is part of a bundle, it can check the catalog for files part of that bundle. It can then decide whether to download the individual files or the entire bundle based on the cache contents.


## Task ideas and expected results
1. Develop server-side support for _bundles_ as object packs to encapsulate several regular files into a single blob
2. Develop server-side support for `.cvmfsbundles` files to describe the list of regular files part of the same bundle
3. Extend _catalogs_ by adding a column to the database table reporting bundle identifiers
4. Implement client capability to preload and cache additional content based on bundles


## Evaluation Task
Interested students, please contact the mentors for an evaluation task.


## Requirements
 * C++
 * sqlite


## Mentors
 * **Jakob Blomer [jblomer@cern.ch](mailto:jblomer@cern.ch)** CERN
 * Enrico Bocchi [enrico.bocchi@cern.ch](mailto:enrico.bocchi@cern.ch) CERN


## Links
 * [CernVM-FS][cvmfs]
 * [CVMFS Github][cvmfs-repo]


[cvmfs]: https://cernvm.cern.ch/fs/
[cvmfs-repo]: https://github.com/cvmfs/cvmfs
