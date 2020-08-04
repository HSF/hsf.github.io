---
title: Updating a carpentry-style module with the HSF style
layout: plain
---

If...

* you have built a carpentry style lesson by following the software carpentry tutorial
* you want to make it an HSF training module that is part of our [curriculum](hepsoftwarefoundation.org/training/curriculum)
* you have already talked to us about it

**OR**

* you are maintaining an HSF module
* you want to update the style

then this section is for you. If you want to update a new module from scratch, see [here](howto-new-module).

**If you're not entirely confident with git, perhaps it's best to have one of our friendly experts look at this!**

We have forked the [carpentries style repository](https://github.com/carpentries/styles/) and [added some style adjustments](https://github.com/hsf-training/hsf-styles). What you can do to get them is to add our repository as the remote and pull from it. 

This might however create some merge conflicts, for example if the original version of style repository that you used to kick off your lesson repository with is outdated (or ours is). Again, we're here to help if you feel lost.

1. **IMPORTANT!** Make sure you do not have any uncommited changes in your repsitory. This makes sure we can't destroy any of your work.

2. Add our repository as a remote (called ``template``):

   ```sh
   git remote add template https://github.com/hsf-training/hsf-styles.git
   ```

3. Configure the remote to not pull tags:

   ```sh
   git config --local remote.template.tagOpt --no-tags
   ```

4. Pull!

   ```sh
   git pull template gh-pages
   ```

5. Merge conflicts? Sorry to hear that. There's a couple of options:
    1. Feeling lost? Abort by doing ``git reset --hard`` (note that all non-commited changes will be lost!)
    2. Resolving the merge conflicts and commit! That would be awesome. If resolve by overwriting a file with with the version from the styles repository, ``git checkout template/gh-pages -- path/to/your/file`` is your friend

6. No merge conflicts? Congratulations, you're almost done!

7. Edit the file ``_config.yml``. Change the first setting to ``carpentry: "hsf"``. This will activate all remaining changes.
