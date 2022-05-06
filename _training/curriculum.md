---
title: HSF Software Training Center
layout: plain
---

## Idea

Training in software and computing are essential ingredients for the success of any HEP experiment. As most experiments have similar basic prerequisites (Unix shell, Python, C++, …) we want to join our efforts and create one introductory software training curriculum that serves HEP newcomers the software skills needed as they enter the field, and in parallel, instill best practices for writing software.

The curriculum is comprised of a set of standardized *modules*, so that students can focus on what is most relevant to them.

## The modules

### Basics

{% include list_of_selected_training_modules.html ids="unix,git,python,ssh,ml" %}

### Software Development and Deployment

{% include list_of_selected_training_modules.html ids="git,cicd,cicdgithub,docker,testingpython" %}

### C++ corner

{% include list_of_selected_training_modules.html ids="hepcpp,moderncpp,cmake"%}

### Machine learning and other analysis tools

{% include list_of_selected_training_modules.html ids="ml,gpuml" %}

### HEP specific tools

{% include list_of_selected_training_modules.html ids="uproot,scikithep" %}

### Miscellaneous

{% include list_of_selected_training_modules.html ids="simpleanalysis" %}

### Planned or in early development

{% include list_of_selected_training_modules.html ids="root,advancedgit,grid,parallel,alpaka,yadagereana,doc,generators,matplotlib" %}

## Further reads

* Show all modules in a table (mostly for administrative purposes): [click here]({{site.baseurl}}/training/curriculum_table.html)
* I want to **contribute** or **teach**:
Contributions of any kind are very welcome! There are various ways you can get involved:

    * Join our **meetings** to give feedback and discuss with us (details at our [main page]({{ site.baseurl }}/workinggroups/training.html))
    * **Bugs reports or feature requests**: Directly open an issue on github or (even better) submit a pull request to fix things.
    * Want to **contribute your own module**? We compiled a small list of recommendations [here]({{ site.baseurl }}/training/module-guidelines.html). Of course we always encourage you to talk to us early for a better coordination. There is also more technical information for [creating a new module]({{ site.baseurl }}/training/howto-new-module.html) or using the [HSF style]({{ site.baseurl }}/training/howto-update-module-style.html).
    * Want to **help out at a workshop?** [More information on the different roles in our training events]({{ site.baseurl }}/training/educators.html)
    * Want to **organize your own workshop**? [ We got you covered.]({{ site.baseurl }}/training/howto-event.html)
