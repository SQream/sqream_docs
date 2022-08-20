.. _using_the_page_updater_branch:

***********************
Using the Page Updater Branch
***********************
Before a release is published, and the branch is still private, you can make any changes you need on it and check how they look on the front end. This is done by generating a build file, described in the next section.

However, once you've published a branch and it is live, you probably do not want to modify its content without first checking it on the build file. The reason for this is that small syntactical errors have unpredicted effects, such as removing tables that you've made or messing up your formatting. Therefore, the **page_updater** branch is a general branch used for viewing pages after publishing a branch. 