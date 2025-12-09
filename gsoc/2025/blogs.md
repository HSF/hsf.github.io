---
title: HSF student pages for GSoC 2025
layout: plain
year: 2025
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

## Full list of projects in 2025

- Abhishikth Mallampalli - [Highly Granular Quantization for CICADA](https://github.com/abhi-mal/google-summer-of-code-2025-cicada) - Lino Gerlach, Jennifer Ngadiuba  
- Andrei Girjoaba - [Integrating Support for Google XLS in hls4ml](https://github.com/fastmachinelearning/hls4ml/pull/1343) - Vladimir L, Dimitrios Danopoulos  
- Carter Capetz - [Physics-Constrained Autoencoders: Intelligent Compression in High Energy Physics](https://github.com/ccapetz/baler/tree/early-work) - James Smith  
- JohnKala - [Background Enrichment augmented Anomaly Detection (BEAD)– Contrastive VAE & Transformer Architecture](https://gist.github.com/JohnKala/9e41c2cfc213920abd80db494f624faf) - Pratik Jawahar, Sukanya Sinha  
- Kriti Mahajan - [RNTuple in JSROOT](https://drive.google.com/file/d/1d3hSGvQk0-77gMFqEoX0CCCdswliuL3L/view?usp=sharing) - Sergey Linev, Giacomo Parolini  
- MytsV - [Rucio WebUI Revamp](https://github.com/rucio/webui) - Martin B, Mayank Sharma  
- Osama Tahir - [Intelligent Log Analysis for the HSF Conditions Database](https://github.com/BNLNPPS/intelligent-logging-pipeline) - Michel Villanueva, Ruslan Mashinistov  
- Prasanna Kasar - [TMVA SOFIE - Enhancing Keras Parser and JAX/FLAX Integration](https://gist.github.com/PrasannaKasar/3cf1ccc7109a9bf5d784b973233ed05a) - Lorenzo Moneta, Sanjiban Sengupta  
- S. Akash - [TMVA SOFIE - GPU Support for Machine Learning Inference](https://gist.github.com/Akasxh/037013605f9823ac5eeb1c577177eafd) - Lorenzo Moneta, Sanjiban Sengupta  
- Tarun Nandi - [Data Representation Optimisation for Generative Model-based Fast Calorimeter Shower Simulation](https://github.com/Tarun-Nandi/Data-Representation-Optimisation-Algorithms-CERN--GSoC-) - Piyush Raikwar, Peter McKeown  
- Yolanne Lee - [Neural (De)compression for High Energy Physics](https://github.com/yolannel/ATLAS_decompression) - Maciej Szymański, Peter Van Gemmeren
- Jason Wu - [Evaluating CVMFS for Machine Learning Model Distribution](https://github.com/jasonwu224/cvmfs-model-file-benchmark) - Lorenzo Moneta, Valentin Volkl  
- Petro Zarytski - [Improve automatic differentiation of object-oriented paradigms using Clad](https://gist.github.com/PetroZarytskyi/b640ef2ba030255189450f2f26fcd3f8) - Vassil Vassilev, David Lange  
- Karan Singh - [Benchmarking Sustainability of Classical & Quantum Algorithms for particle trajectory reconstruction](https://github.com/KaranSinghDev/E-QUEST) - MiriamLucioMartinez, Arantza Oyanguren  
- Kossi Glokpor - [Implementing a deprecation system for Ganga](https://github.com/ganga-devs/ganga/pull/2422) - Alexander Richards, Ulrik  
- Madlani Shivam - [Extending support on custom kernels with virtme-ng](https://github.com/cvmfs/cvmfs/pull/3986) - Valentin Volkl, Georgios Christodoulis  
- Salvador de la Torre Gonzalez - [CARTopiaX: an Agent-Based Simulation of CAR T-Cell Therapy built on BioDynaMo](https://gist.github.com/salva24/c22145c877561dca80cfd42d2b0d08c8) - Vassil Vassilev, Lukas Breitwieser  
- Abhinav Kumar - [Implementing Debugging Support for xeus-cpp](https://gist.github.com/kr-2003/fa5a74d074d68883524cafab14672b55) - Vassil Vassilev, Vipul Cariappa  
- Abdelrhman Elrawy - [Support usage of Thrust API in Clad](https://gist.github.com/a-elrawy/91706938192dbf45b4afcff5ef83a66b) - Vassil Vassilev, Alexander Penev  
- Aditi Milind Joshi - [Implement and improve an efficient, layered tape with prefetching capabilities](https://gist.github.com/aditimjoshi/6eba0e696637094be570b35a01f16836) - Vassil Vassilev, David Lange  
- Aditya Pandey - [Using ROOT in the field of genome sequencing](https://gist.github.com/AdityaPandeyCN/894eb69e2e3790f43fbcd1c16ffa4f14) - Vassil Vassilev, Martin Vassilev  
- Jiayang Li - [Enable automatic differentiation of OpenMP programs with Clad](https://gist.github.com/Errant404/3976629ac5eb56ad1fa11576536b61a3) - Vassil Vassilev, Martin Vassilev  
- Maksym Andriichuk - [Implement activity analysis for reverse-mode differentiation of (CUDA) GPU kernels](https://gist.github.com/ovdiiuv/4cf58ac514a6d5d5d852a4529baed736) - Vassil Vassilev, David Lange  
- Rohan Timmaraju - [Enhancing LLM Training Efficiency with Clad for Automatic Differentiation in C++](https://compiler-research.org/blogs/gsoc25_rohan_final_blog/) - Vassil Vassilev, David Lange  
- Sakshi Kumar - [GreenML@CERN – A Comprehensive Framework for Energy-Efficient Scientific Machine Learning](https://github.com/sakshikumar19/Google-Summer-of-Code-2025) - Caterina Doglioni
