---
title: CernVM's fruitful Summer -  GSoC 2011
layout: plain
year: 2011
---
{:refdef: style="text-align: center;"}
![gsoc-logo-2011](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images_archive/original_images/GSOC_2011_300x200px_URL.png)
{: refdef}

This was the first year [CERN](http://public.web.cern.ch/public/)
participated in *[Google Summer of Code](http://code.google.com/soc/)*,
and it turned out to be an amazing experience for us! We were given four
students to mentor, all of whom proved to be very skilled developers.
The students quickly familiarized themselves with our code base and
managed to make valuable contributions within the three month time frame
of *Google Summer of Code*. Our students were very open and willing to
learn and spent a considerable amount of their time researching tools,
libraries, and the latest technological developments. As a result, all
four students were able to solve their problems and come up with
interesting ideas for future development. The code and the documentation
they produced is available
[here](http://code.google.com/p/google-summer-of-code-2011-cernvm/downloads/list).
The specific problems (projects) that we suggested to our students
spanned several domains, ranging from consistent replication of
terabytes of data across several remote sites to automated testing of
virtual machine releases.

**Josip Lisec** was working on the development of the monitoring system
for the [CernVM](http://cernvm.cern.ch/portal/) Co-Pilot framework,
which is mainly used as a distributed computing platform within the
LHC\@home 2.0 volunteer computing project. The [LHC\@home
2.0](http://lhcathome2.cern.ch/) project currently has more than 9,000
registered users who contribute their spare CPU cycles for the
simulation of the particle collision events in CERN\'s [Large Hadron
Collider](http://press.web.cern.ch/public/en/LHC/LHC-en.html) (LHC).
After some research, Josip decided to integrate existing tools with the
Co-Pilot as opposed to trying to reinvent the wheel by rewriting
everything from scratch. This resulted in a nicely engineered monitoring
framework, parts of which were put into production while the *Google
Summer of Code* was still going on (Josip\'s developments have now been
fully integrated after completion of the program). Since this was
Josip\'s first encounter with Perl, he has been seen adding support for
\'[my](http://perldoc.perl.org/functions/my.html)\' keyword to every
other major programming language since the *Google Summer of Code*
concluded.\
\
The goal of **Yin Qiu**\'s project was to devise a mechanism for a
consistent replication of changes made to the central repository of
[CernVM File System](http://cernvm.cern.ch/portal/startcvmfs)
(CernVM-FS) to a globally distributed set of mirror servers. CernVM-FS
is used to host and distribute the application software of CERN LHC
experiments to hundreds of Grid sites, as well as the laptops and
workstations of users worldwide. As such, it is currently one of the
central components of the distributed computing infrastructures on which
CERN [ATLAS](http://www.atlas.ch/) and
[LHCb](http://user.web.cern.ch/public/en/LHC/LHCb-en.html) experiments
rely. Yin\'s approach was to organize CernVM-FS mirrors into a
Paxos-managed replication network and to enforce state machine version
transitions on them. Following the suggestion of Jakob, his mentor, Yin
implemented a messaging framework which is used to orchestrate the
replication process and facilitates the implementation of new features.
He also managed to implement a couple of Python plugins which ensure the
consistency of data across replicas. The project is currently in the
state of a working prototype.\
\
**Jesse Williamson** took up the challenge of designing a new library
for CernVM-FS to consolidate support for various cryptographic hashing
algorithms. The first task was to survey the implementation of CernVM-FS
and establish a list of requirements. Next, quite a bit of effort was
spent on designing the library specifically so that it would be easy to
use, comparatively simple to extend, and robust enough to support
extensions like a streaming interface and compression. Since CernVM-FS
is heavily used in production, it has been very important to make sure
that the new developments do not break anything. Jesse has developed a
set of unit tests which ensure that all the existing features and
properties were maintained.\
\
The design of new C++ libraries was certainly an improvement, but it
also became clear late in the cycle that a further abstraction to fully
separate digests and hash functions will be necessary to avoid memory
fragmentation issues and ensure stronger const-correctness\
\
**Jonathan Gillet** worked on implementing a solution for automating the
testing of CernVM virtual machine images on multiple hypervisors and
operating systems. The solution, which is a ready to use testing
infrastructure for CernVM, was developed in collaboration with other
open source projects such as [AMD
Tapper](http://developer.amd.com/zones/opensource/AMDTapper/Pages/default.aspx)
(used for the reports and web interface), [libvirt](http://libvirt.org/)
(interaction with hypervisors), and
[Homebrew](http://mxcl.github.com/homebrew/) (OS X support).  The main
goals of the project were accomplished with support for all major
hypervisors running on Linux and OS X platforms. The framework automates
the task of downloading and configuring the CernVM images on the fly,
and executing a series of thorough tests which check various features of
CernVM images before release. Documentation was also an important goal
of the project; in total there are now over two hundred pages of
documentation which cover everything from setting up the testing
infrastructure and virtual machines to a complete API reference.\
\
We certainly enjoyed *Google Summer of Code* 2011, and we sincerely
congratulate all of our students and mentors for successfully completing
the program!\
\
*By Artem Harutyunyan, Senior Fellow, CernVM Project (CERN) and Google
Summer of Code Mentor*\
[(original article on Google Open Source
Blog)](http://google-opensource.blogspot.fr/2011/12/cernvms-fruitful-summer.html)
