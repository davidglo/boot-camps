Version Control

----

**Original material by Katy Huff, Anthony Scopatz, and Sri Hari Krishna
Narayanan**

## github.com?

GitHub is a site where many people store their open (and closed) source
code repositories. It provides tools for browsing, collaborating on and
documenting code. Your home institution may have a repository hosting
system of it's own. To find out, ask your system administrator.  GitHub,
much like other forge hosting services (
[launchpad](https://launchpad.net), [bitbucket](https://bitbucket.org),
[googlecode](http://code.google.com), [sourceforge](http://sourceforge.net)
etc.) provides :

-   landing page support 
-   wiki support
-   network graphs and time histories of commits
-   code browser with syntax highlighting
-   issue (ticket) tracking
-   user downloads
-   varying permissions for various groups of users
-   commit triggered mailing lists
-   other service hooks (twitter, etc.)

## github login 

Setting up github requires a github user name and password.  Please take a
moment to [create a free github account](https://github.com/signup/free) (if you
want to start paying, you can add that to your account some other day).

## git remote : Steps for Forking a Repository

A key step to interacting with an online repository that you have forked
is adding the original as a remote repository. By adding the remote
repository, you inform git of a new option for fetching updates and
pushing commits.

The **git remote** command allows you to add, name, rename, list, and
delete repositories such as the original one **upstream** from your
fork, others that may be **parallel** to your fork, and so on.

### Exercise : Fork Our GitHub Repository

In step 1, you will make a copy "fork" of our test repository TESTREPO on github.  This gives you a copy of this repository that you control.

In step 2, you will make a copy of **your** fork of the repository on your hard drive.

In step 3, you will let git know that in addition to your local copy and your fork on github, there is another github repository (called "upstream") that you might want to get updates from.

Step 1 : Go to our
[repository](https://github.com/USERNAME/TESTREPO)
from your browser, and click on the Fork button. Choose to fork it to your
username rather than any organizations.

Step 2 : Clone it. From your terminal :

    $ git clone https://github.com/YOU/TESTREPO.git
    $ cd TESTREPO
Note: YOU is a placeholder for YOUR github username.  If git asks you for a password here, it probably means there isn't any repository a the url that you provided.

Step 3 : 

    $ git remote add upstream https://github.com/USERNAME/boot-camps.git
    $ git remote -v
    origin  https://github.com/YOU/TESTREPO.git (fetch)
    origin  https://github.com/YOU/TESTREPO.git (push)
    upstream        https://github.com/USERNAME/boot-camps.git (fetch)
    upstream        https://github.com/USERNAME/boot-camps.git (push)
    $

All repositories that are clones begin with a remote called origin.
### What's going on here?
The **git remote add** merely defines a nickname and a location that git will be able to communicate with for making copies of your repository.  "origin" and "upstream" are nicknames for your fork of TESTREPO and the "original" TESTREPO, respectively.

## git fetch : Fetching the contents of a remote

Now that you have alerted your repository to the presence of others, it
is able to pull in updates from those repositories. In this case, if you
want your master branch to track updates in the original TESTREPO
repository, you simply **git fetch** that repository into the master
branch of your current repository.

The fetch command alone merely pulls down information recent changes
from the original master (upstream) repository. By itself, the fetch
command does not change your local working copy. To update your local
working copy to include recent changes in the original (upstream)
repository, it is necessary to also merge.

## git merge : Merging the contents of a remote

To incorporate upstream changes from the original master repository (in
this case USERNAME/TESTREPO) into your local working copy, you
must both fetch and merge. The process of merging may result in
conflicts, so pay attention. This is where version control is both at
its most powerful and its most complicated.

### Exercise : Fetch and Merge the Contents of Our GitHub Repository

Step 1 : Fetch the recent remote repository history

    $ git fetch upstream

Step 2 : Make certain you are in the master branch and merge the
upstream master branch into your master branch

    $ git checkout master
    $ git merge upstream/master

Step 3 : Check out what happened by browsing the directory.

## git pull : Pull = Fetch + Merge

The command **git pull** is the same as executing **git fetch** followed
by **git merge**. Though it is not recommened for cases in which there
are many branches to consider, the pull command is shorter and simpler
than fetching and merging as it automates the branch matching.
Specificially, to perform the same task as we did in the previous
exercise, the pull command would be :

    $ git pull upstream
    Already up-to-date.

When there have been remote changes, the pull will apply those changes
to your local branch, unless there are conflicts with your local
changes.

## git push : Sending Your Commits to Remote Repositories

The **git push** command pushes commits in a local working copy to a
remote repository. The syntax is git push [remote] [local branch].
Before pushing, a developer should always pull (or fetch + merge), so
that there is an opportunity to resolve conflicts before pushing to the
remote.

### Exercise : Push a change to github
We'll talk about conflicts later, but first, let's make a small change
that won't have any conflicts and send our changes to
your fork, the "origin."

1. Create a file in the `messages` directory whose filename is your github
id.  (This is to ensure no conflicts just yet!)  Add a line of text, perhaps a
description of how you use / how you expect to use programming in your
work.

2.  commit your change with `git add <USERNAME>` and `git commit -m "commit message"`

3.  Update your fork ("origin") with your new changes:
    $ git push origin master

This will update your github fork with any changes you've committed.
Once you do this, you can see your changes on the github web interface
to your repository, along with the time you made the change and
your commit message.

If you have permission to push to the upstream repository, sending
commits to that remote is exactly analagous.

    $ git push upstream master

In the case of the upstream push, new developer accounts will not allow
this push to succeed. You're welcome to try it though.

There is now a hierarchy of git repositories.  There was the upstream
repository that you can't write to, there is your fork of that repository
that you have updated, and there is the local copy on your hard drive.

## github pull requests 

One protocol for updating repositories that we use at software carpentry
is the "pull request."   This is a bundle of updates to the repository
that can be accepted and merged into the upstream repository or rejected
and not merged.  If you would like to share your changes with the
upstream repository, click the green "compare and review" button, and
github will show you a summary of your commits.  If you then
click on "Click to create a pull request for this comparison," your
request will be sent to the upstream repository for acceptance or
rejection.

## git merge : Conflicts

This is the trickiest part of version control, so let's take it very
carefully.

Conflicts happen when git tries to combine changes from two different
branches (local and remote, development and master) but finds that 
changes in the two branches interfere with each other and can't be
automatically merged.

Branches are a tool that git uses to facilitate managing changes.  
They allow us to switch between states of the repository and refer to
states that we desire to merge.  

You'll often want to start a new branch for development, make your changes there,
and then merge these changes into your main branch. It's a good convention
to think of your master branch as
the "production branch," typically by keeping that branch clean of your
local edits until they are ready for release. Developers typically use the
master branch of their local fork to track other developers' changes in the
remote repository until their own local development branch changes are
ready for production.

Note, your fork contains a file called Readme.md.  This is a
standard documentation file that appears rendered on the landing page
for the repository in github. To see the rendered version, visit your
fork on github, (https://github.com/YOU/TESTREPO/README.md).  We
can edit this file on two different (local) branches and cause a merge
conflict, and if we try to update with remote changes that conflict with
our local changes we will also trigger a merge conflict.


### Exercise : Experience a Conflict

Step 1 : Make a new branch, edit the readme file in that branch, and
commit your changes.  Let's change the greeting "Vanakkam" to some other
greeting.

    $ git branch development
    $ git checkout development
    Switched to branch 'development'
    $ kate Readme.md &
    <edit the readme file and exit kate>
    $ git commit -am "Changed the welcome message to ... "

Step 2 : Mirror the remote upstream repository in your master branch 
by pulling down my changes

    $ git checkout master
    Switched to branch 'master'
    $ git fetch upstream
    $ git merge upstream/master
    Updating 43844ea..3b36a87
    Fast-forward
     README.rst |   2 +-
     1 files changed, 1 insertions(+), 1 deletions(-)

Step 3 : You want to push it to the internet eventually, so you pull
updates from the upstream repository, but will experience a conflict.

    $ git merge development
    Auto-merging Readme.md
    CONFLICT (content): Merge conflict in Readme.md
    Automatic merge failed; fix conflicts and then commit the result.

## git resolve : Resolving Conflicts

Now what?

Git has paused the merge. You can see this with the **git status**
command.

    # On branch master
    # Unmerged paths:
    #   (use "git add/rm <file>..." as appropriate to mark resolution)
    #
    #       unmerged:      Readme.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

The only thing that has changed is the Readme.md file. Opening it,
you'll see something like this at the beginning of the file.

    =====================
    <<<<<<< HEAD
    Vanakkam
    =======
    Willkommen
    >>>>>>> development
    =====================

The intent is for you to edit the file, knowing now that I wanted the
Welcome to say Vanakkam. If you want it to say Willkommen, you should
delete the other lines. However, if you want to be inclusive, you may
want to change it to read Vanakkam and Willkommen. Decisions such as this
one must be made by a human, and why conflict resolution is not handled
more automatically by the version control system.

    Vanakkam and Willkommen

This results in a status To alert git that you have made appropriate
alterations,

    $ git add Readme.md
    $ git commit
    Merge branch 'development'

    Conflicts:
      Readme.md
    #
    # It looks like you may be committing a MERGE.
    # If this is not correct, please remove the file
    # .git/MERGE_HEAD
    # and try again.
    #
    $ git push origin master
    Counting objects: 10, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 762 bytes, done.
    Total 6 (delta 2), reused 0 (delta 0)
    To git@github.com:username/TESTREPO.git

## synchronizing 
Now that lots of us created files and put in pull requests,
we begin to suspect that the upstream repository might have
new content and we are out of date. Try
    $ git pull upstream master
to fetch, merge, and commit the changes from upstream repository--
including other people's changes that have been added to upstream.
In this way we can all get updates of what the rest of us are 
working on.

But now our forks -- on github -- are out of date.  We can push
to update those
    $ git push origin master
And all is synchronized.

## gitolite

[Gitolite](https://github.com/sitaramc/gitolite) is a way for you to host
your own multi-user git repositories. I'm not going to go into details
here, but all you need is a machine with some drive space and network
access. You can install [minimal
ubuntu](https://help.ubuntu.com/community/Installation/MinimalCD), then
sudo apt-get install gitolite will pull in everything you need. At that
point, your collaborators will only need to send you their public ssh keys
for you to configure pull and push access to the repos.
