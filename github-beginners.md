---
title: GitHub for Beginners
author: Michel Jouvin
layout: default
---

This pages is a GitHub and Git survival kit for people not familiar with these tools! This is not a documentation or tutorial about these tools. Many excellent ones are already available, including:

* [GitHub Bootcamp](https://help.github.com/categories/bootcamp/), in particular [fork a repository](https://help.github.com/articles/fork-a-repo)
* [Git for the Novice](http://swcarpentry.github.io/git-novice/) from [Software Carpentry](http://software-carpentry.org/)
* [Git Book](https://git-scm.com/book/en/v2): the definitive Git reference! Certainly not for beginners!


## GitHUb Workflow

At a first glance, GitHub (and Git) may look complex with their "workflows". But they are not so much in fact. What makes these tools great is that hey allow a clear separation between your personal work and what you decide to show or export. Your personal work, unlike with tools like SVN, can be versionned and you can work on different things in parallel (branches) very easily.

In the HSF web site context, what is shared is what is in the project repository called, [hep-sf.github.io](https://github.com/HEP-SF/hep-sf.github.io). Your personal environment is made of 2 parts:

* One personal repository on GitHub, called a *fork*. It is typically created using the GitHub web interface, click on the `Fork` button when you are in the project repository. Despite this is a Git repository, you cannot access it directly from you local computer with Git commands (for example, you cannot `git commit` changes made on your local computer to it).
* One (or several) clone of your personal repository on GitHub. This is where you'll make/develop your changes, using the full versionning capabilities of Git. And until you publish (`git push`) your changes to your personal repository (fork) on GitHub, they are not visible by anybody else. Once in your personal repository, it is potentially visible but you control when you want to submit these changes to the project repository creating a `pull request`: at this point people can review/comment your changes and people with the appropriate permissions can `merge` your changes in the project repository.

With this *GitHub workflow*, the only repository you need to have write access to on GitHub is your personal repository. This ensures that nothing wrong can happen to the project repository because you are not a Git/GitHub expert.

For simple things, there is an alternative to creating a clone on your local computer: you can use the GitHub editor in the web interface. When you save your changes, this commits your changes and you are asked for *commit message*. Note that this is really limited to situations where your contribution is limited to only one file as you cannot edit several files and commit them togheter this way. Apart from the management of the Git clone, there workflow for pushing your changes to the project repository remains the same, using *pull request*.

Sections below give more details on the main steps involved. Examples are based on the HSF web site [repository](https://github.com/HEP-SF/hep-sf.github.io). Note that there is a help available for each Git command that can be displayed with:

```bash
git help
git help command
```


## GitHub Account Creation and Configuration

To contribute, you definitely need to have a GitHub account: connect to [gitHub](http://github.com) and follow the instructions.

Once you have an account, if you want to use the full workflow with a clone of the GitHub repository on your local computer, it is recommended to configure your SSK keys that will be used for the authentication: follow the GitHub [documentation(https://help.github.com/articles/generating-ssh-keys/). Using SSH keys is not a requirement but is recommended: the alternative if you want to contribute is to use `https` but in this case any interaction with GiHb through the `git` command will require that you enter your password...


## Creating your Personal Environment

As explained in the introduction, this involves 2 steps:

* Creating your personal fork: with your browser, open the HSF web site [repository](https://github.com/HEP-SF/hep-sf.github.io) and click on the `Fork` button at the top-right of page.
* Creating your local clone of your personal fork (assuming your name is `dupont`: 

  ```bash
  # The local Git repository will be in a directory hep-sf.github.io in your current directory.
  # The exact URL to use is on the right side of web page, when you display your personal fork.
  git clone git@github.com:dupont/hep-sf.github.io.git
  # Move in your repository
  cd hep-sf.github.io
  ```

* Connect your local clone to the project repository: as it will be explained in other sectinos, there are several occasions where you will want to import changes that happened in the project repository into your local clone that you use to develop your contributions. In Git, this involves creating a *remote* and is done with:

  ```bash
  # Later to refer to the project repository, we'll use the remote called upstream
  git remote add upstream git@github.com:HEP-SF/hep-sf.github.io.git
  ```

Note that adding a remote adds no information to the repository itself.


## Making your Changes

This step is about making your changes in your local clone: nothing will be visible on GitHub at this stage. There are many variations of the steps involved here: below are the main/recommanded ones.

* Get the last updates from the project repository and add them to your local clone. **This doesn't make any change** to your local developments (branches):

  ```bash
  git fetch upstream
  ```

* Create a branch for your new contribution. Unlike tools like SVN, branches are cheap, don't use space and you can have hundred of thems without impact on performances (existing branches can be displayed with `git branch`). Here we'll start a new branch based on the last state of the main project branch called `master`):

  ```bash
  # New branch will be called mydev1
  git checkout -b mydev1 upstream/master
  ```

* Make your changes: create new files, modify new ones with your preferred editor.

* Commit your changes. Git is quite powerful to select what you are the changes you want to make part of a commit: this allows to commit separately several set of changes made at the same time. For this reason, there is a command `git add` than can be used before the commit itself (`git commit`). Here we describe the simplest form that you can use if you want all your changes to be part of a single commit (the proposed commands given here are working with Git v1 and v2). When you enter the commit, you'll be asked for a message: it is important to say in a few words the reason for the change.

  ```bash
  # Add all your changes to the next commit
  git add .
  # -m option can be used to set the commit message rather than being asked for
  git commit
  ```

Note that you can do the cycle edit/commit as many times as you want, until you are satisfied, before pushing your changes.

## Publishing your Changes

Publishing changes involves 2 steps (again!):

* Pushing your changes to your personal fork on GitHub. This is done on your local machine with the following Git command. Note that the command is executed twice: the first time to check that what will be done is correct, the second to actually do it: this is by no means mandatory but is a best practice, in particular when you are not familiar with Git.

  ```bash
  # In this command origin is the Git remote pointing to your fork
  # and HEAD is a symbolic name for the current branch.
  # After the first push of your branch to GitHub, you can use 'git push' without options
  git push --set-upstream origin HEAD -n
  # Check what will be done by the command and reexecute without -n to actually do it
  git push --set-upstream origin HEAD
  
  ```

* Ask for your changes to be integrated into the project. This is done by creating a pull request, using the web interface: if you open either your personal fork or the project repository after you have pushed something to a branch of your personal fork that is not yet published in an open pull request, GitHub will display a line proposing to create a pull request. Just click the button, check the title of the pull request and add a description.

After the pull request has been created, all the persons interested in the project repository changes will be notified by email. Everybody can subscribe the repository [notifications](https://help.github.com/articles/about-notifications/). At this point, your contribution is open for review: people can comment, suggest changes... At some point, when there is an agreement that the contribution is in good shape, somebody with the appropriate permission will *merge* it in the poject repository (this is a one-click operation).

Note that as soon as a pull request is open, every change that you make to the personal branch that you published (whic is the source of the pull request) is published immediately (until the pull request is closed/merged). You cannot create several pull requests with the same source branch.
 
When the pull request is merged, you can decide to delete your personal branch that was used to make your contribution but there is no real need to do it... It's a matter of personal taste!
