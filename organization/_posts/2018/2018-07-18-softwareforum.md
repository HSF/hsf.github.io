---
title: "HSF Software Forum on Vectorisation Tools, 18 July, 2018"
layout: default
---

# {{page.title}}

[Meeting Agenda and Slides](https://indico.cern.ch/event/736105/) 

Introduction
============
-   Next meetings being planned, 
    [check Indico for the status](https://indico.cern.ch/category/10392/). Please 
    send any suggestions for presentations or discussion topics.

VecCore
=======
-   Why does CPU go down between 2027-2030 in the CMS plot? 
    - It's a guess that 10%
      optimisation can be found every year, based on previous experience
      in CMS.
-   Quadratic benchmark shows that icc does vectorise very well, but
    noted that this is only for simple cases - it still doesn't work
    for complex cases or branchy code (otherwise we'd just buy icc!).
    More recent versions of gcc and clang do better than the versions
    in the plots.
-   User code needs to choose the backend. Can do this as a typedef, so
    that one can easily switch. Is this adaptable to large code bases
    that may have different sweet spots? 
    - Yes, it can be made fairly
      independent of the 'core' code.
-   C++ standard evolution? It's discussed, but not clear when it will come. Can
    add the standard as another backend when it's available. Some
    algorithms may work more efficiently with short vectors. Alignment
    is a problem - has had very poor support in C++, but much improved
    in C++17 (compiler directive available).
-   ISPC compiler considered R&D project by Intel - it's now an open
    source project, but future not clear.
    
SOAContainer
============
-   Will the loop vectorise properly on slides 17, 18? A. Yes - the
    compilers will vectorise that.
-   Intel's Arrow Street? No experience with that.
-   Marco C - way to use it has improved a lot.
    -   Can the results be serialised by ROOT? Not tried yet. Would need
        to perhaps manipulate the data to serialise (costs a bit).
-   Frank - looks a lot like xAOD and its features.
-   Guilhereme - could this be a view of the data that's in ROOT, as a
    split tree.
    -   Problem is that in memory representation is row-wise again.
    -   Only really take advantage of columns in analysis (usually).
-   Is there another way to do it than macros?
    -   It can be done without the marcos, but requires a lot of boiler
        plate, which is rather worse.

