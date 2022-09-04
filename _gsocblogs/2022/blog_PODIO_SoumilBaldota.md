---

project: HSF
title: Interfacing PODIO with Julia
author: Soumil Baldota
date: 4.09.2022 
year: 2022 
layout: blog_post
logo: podio-logo.png
intro: Final progress report

---
**About Me**

I am Soumil Baldota in my sophomore year in college with a few years of development experience in C++ and Python. For me Julia was a new language but I got acclimated quickly and have had a good time contributing to HSF organization. I am thankful to my mentors and the organization.

---

**Community Bonding**

In the community bonding period, with the help of Thomas and Benedikt, I setup my development environment along with local install of podio. To get familiar with podio and the contributing workflow. I worked on some minor issues.

---

**Issues raised:**
- [clang-tidy](https://github.com/AIDASoft/podio/issues/297)
- [pylint](https://github.com/AIDASoft/podio/issues/298)

---

**Pull Requests:**
- [Replace obj_needs_destructor by more general concept](https://github.com/AIDASoft/podio/pull/291)
- [Review generator python code](https://github.com/AIDASoft/podio/pull/293)
- [running pre-commit locally](https://github.com/AIDASoft/podio/pull/296)
- [Julia preprocessing](https://github.com/AIDASoft/podio/pull/311)
- [adding namespaces](https://github.com/AIDASoft/podio/pull/325)
- [add documentation](https://github.com/AIDASoft/podio/pull/329)

---

  
**Coding Period**

Following the Community Bonding Period I began to work on a prototype for the Interface which described how the generated code would look like. The prototype was created for classes with one to one relations, one to many relations and vector members. Then I made unittests for the prototype and added them to github actions for continuous integration. 
The prototype can be found at the below link
[Prototype](https://github.com/soumilbaldota/PODIO_Julia_Interface_Prototype.git)

After the prototype was created. I added an attribute to store the Julia type of a data member described in C++ to the MemberVariable Class and a function to [get the Julia type](https://github.com/AIDASoft/podio/pull/310/files#diff-c129698a9b29360c0e27c5e4f710981b4f99524ad44c039202d750bcf349c834) in [generator_utils.py](https://github.com/AIDASoft/podio/blob/julia/python/generator_utils.py), this was a necessary step to feed the jinja2 templates with the appropriate Julia type for code generation.
After Julia type was added I made some [unittests](https://github.com/AIDASoft/podio/pull/310/files#diff-61702c3a214182795b1d726c5dc1679a64a10274b7929e4ad4ceaf8dc87c203d) for the same and added them to [test_MemberParser.py](https://github.com/AIDASoft/podio/blob/julia/python/test_MemberParser.py).

Following the addition of the attributes necessary for building the includes required to feed new templates that will generate Julia code. There is actual preprocessing required for building these includes required by our [Constructor](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/Constructor.jl.jinja2) and the [MutableStruct](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/MutableStruct.jl.jinja2) templates(covered further in the blog). This preprocessing is done by the [**preprocess_for_julia**](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/podio_class_generator.py#L295-L320) function. This functions fills our includes dictionary passed to the templates.

Mutually Recursive Type Declarations in Julia required the use of Parametric types which required the list of parameters required by each Constructor. This data is processed by the [**get_julia_params**](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/podio_class_generator.py#L286-L293)

Wrapping the modules generated in parent namespaces required the collection of children in each namespace this is handled by the function [**get_namespace_dict**](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/podio_class_generator.py#L107-L115). 

**Templates**
- [MutableStuct.jl.jinja2 template](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/MutableStruct.jl.jinja2) is used for generation of Structs which use the includes_jl and params_jl dictionaries created while preprocessing. 

- [Constructor.jl.jinja2 template](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/Constructor.jl.jinja2) is used for creating corresponding Constructors which initialize the structs with default values and bring the datatypes into their own namespace/module.

- [JuliaCollection.jl.jinja2 template](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/JuliaCollection.jl.jinja2) is used for creating Collection of the given Datatype.

- [ParentModule.jl.jinja2 template](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/python/templates/ParentModule.jl.jinja2) is used to create a parent namespace.

**Testing**

[**unittests**](https://github.com/AIDASoft/podio/blob/59fe1e740ca0a7dbff1180c1425047ed1ab3e027/tests/unittest.jl) were added to test the functionality of the following in the generated code:
- Namespaces
- Collections
- Cyclic Dependency
- Vector Members
- Relations

This was added to CI of the repo by Thomas.
