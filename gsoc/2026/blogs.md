---
title: HSF participant pages for GSoC 2026
layout: plain
year: 2026
---

{% assign sorted_blogs = site.gsocblogs | sort: 'title' %}
{% for blog in sorted_blogs %}
{%- if blog.year == page.year %}
{% assign blog_intro = blog.intro | strip_newlines | markdownify %}
<div class="blog-header" style="text-align: left">
  <div class="row">
    <div class="col-sm-2">
      <img src="/images/{{ blog.logo }}" alt="{{ blog.project }}" width="80px">
    </div>
    <div class="col-sm-7" style="text-align: left;">
      <h2>{{ blog.title }}</h2>
    </div> 
    <div class="col-sm-3" style="text-align: center;">
      {% if blog.avatar %}
      <img src="{{ blog.avatar }}" alt="{{ blog.author }}" width="100px">
      {% else %}
        {% if blog.photo %}
        <img src="/images/{{ blog.photo }}" alt="{{ blog.author }}" width="100px">
        {% endif %}
      {% endif %}
      <p style="font-weight: bold; text-align: center; font-style: oblique;"> {{ blog.author }}</p> 
    </div>
  </div>
</div>
{{blog_intro}}

[ <span style="color:blue">Read more ...</span> ]( {{ blog.url }} )
<hr>
{%- endif -%}
{% endfor %}

## Full list of projects in 2026

- Aashirvad - [Publication of OmniFold Weights A Standardized Format for ML Based Unfolding Results](https://github.com/aashirvad08/omnifold-publication.git) - Tanvi Wamorkar  
- Abdelrhman Elrawy - [Enabling Differentiable Rendering via AD of Parallel C++ STL Primitives in Clad](https://gist.github.com/a-elrawy/55c73be41f3ffee4634db23dba0c3468) - Vassil Vassilev, Alexander Penev  
- Ahmed Idani - [Fine grained storage for the DUNE experiment](https://gist.github.com/Ahmed-Idani/2a9d3bdc4b03b0e3d0cf4da4e82c258f) - Wanwei Wu  
- Akshat Rai - [EKO Oxidation: Maturing the Rust Core of EKO](https://hepsoftwarefoundation.org/gsoc/blogs/2026/blog_NNPDF_AkshatRai.html) - Juan M. Cruz-Martinez, Felix Hekhorn  
- Antonio Battaglia - [Automatic answering and evaluation of support tickets](https://antubattle.github.io/gsoc26/) - Hasan Ozturk  
- Arnav Dham - [Apache Arrow Interface for PODIO](https://hepsoftwarefoundation.org/gsoc/blogs/2026/blog_Final_Apache_Arrow_interface_for_PODIO_ArnavDham.html) - Wouter Deconinck, Dmitry Kalinkin  
- AtikSantellan - [Characterizing I/O Performance for ML Data Loaders at Scale using Darshan](https://gist.github.com/iCebka/4ea6b5927a773c7bad6e66bd46276af2) - Rui Wang  
- Bibhor Puhan - [AI-Accelerated Signal Reconstruction for the ATLAS Tile Calorimeter at the HL-LHC](https://hepsoftwarefoundation.org/gsoc/blogs/2026/blog_ATLAS_BibhorPuhan.html) - Luca Fiorini  
- Douglas Lindsay - [Automated Software Performance Monitoring for the ATLAS experiment](https://hepsoftwarefoundation.org/gsoc/blogs/2026/blog_automated_software_performance_monitoring_DouglasLindsay.html) - Maciej Szymański  
- fogsong - [Clad as a First-Class Gradient Engine in LibTorch](https://compiler-research.org/blogs/gsoc26_kacent_introduction_blog/) - Vassil Vassilev, David Lange, Aaron Jomy  
- Harsh Chauhan - [ML Inference on heterogeneous architectures using SOFIE](https://gist.github.com/harz05/fa2d6148c4cc0d851a881aa076c98ce8) - Lorenzo Moneta, Sanjiban Sengupta  
- Harshit Nagpal - [Parallel Processing Improvements in Julia Jet Reconstruction](https://harshitnagpal29.github.io/gsoc-2026-jetreco/) - Graeme Stewart, Mateusz Fila  
- Jas Mehta - [S3 Backend for RNTuple](https://gist.github.com/JasMehta08/2b684e7f21fcdf5ebd8a79c8b27f0ac4) - Giacomo Parolini  
- Kerem Sahin - [Implement CppInterOp API exposing memory ownership and thread safety](https://gist.github.com/keremsahn/57c72ed73010e09af84db262c788a85d) - Vassil Vassilev, Vipul Cariappa, Aaron Jomy  
- L Venkata Subramanyam - [Debugging CVMFS Processes in D-State](https://physic69.github.io/blog/) - Valentin Volkl, Madlani Shivam, Georgios Christodoulis  
- Salvador de la Torre Gonzalez - [CARTopiaX: Extending a Next-Generation Platform for Computational Cancer Biology](https://gist.github.com/salva24/afe3e615b03e8bf0b5d81329157592c3) - Vassil Vassilev, Lukas Breitwieser, Luciana Luque  
- Sarthak Negi - [AI-Assisted PostgreSQL Optimization Using EXPLAIN Plans](https://gist.github.com/sarthaksarthak9/85d8211688221545a56645b385629072) - Ruslan Mashinistov  
- Sebastian Paucar - [Debuggable Installations for Spack Packages](https://github.com/HSF/hsf.github.io/pull/1962) - Wouter Deconinck  
- Siyu (Rain) Chen - [Data Representation Optimization for ML-based calorimeter simulation](https://github.com/fast-sim/showerRepresentationStudies) - Anna Zaborowska, Peter McKeown  
- Soumyadip Niyogi - [Integration of Combine with FCCAnalyses](https://github.com/captainvogon/gsoc2026) - Juraj Smieško, Jan Eysermans  
- utk4r-sh - [Enabling Sustainable ARM Support for the Belle II Software](https://salsa.debian.org/-/snippets/866) - Giacomo De Pietro  
- Vaishnavi Mishra - [Generative-AI Assisted Testing of Complex Stacks of Spack Packages](https://github.com/VaishnaviOnPC/spack-ai-test) - Wouter Deconinck  
- Vedant Goyal - [Consolidate and advance the GPU infrastructure in Clad](https://gist.github.com/Vedant2005goyal/57f79f52409fb1ba3d66c0cd362fd3ec) - Vassil Vassilev, David Lange, Aaron Jomy  
- Vishwajeet Singh - [Constellation: Web Interface for Controlling and Monitoring Experimental Setups](https://gitlab.desy.de/constellation/webcontrol) - Stephan Lachnit, Simon Spannagel  
- Worakan Lasudee - [Transformer based Reconstruction for LHCb PicoCal Calorimeter](https://github.com/Lworakan/GSoC2026-picocal-spacetime-transformer.git) - Felipe Souza de Almeida  

