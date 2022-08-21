.. _what_are_branches_used_for:

***********************
What are Branches Used For?
***********************
Because in many cases pages and features are *release-driven*, the best practice is to create branches belonging to each release, and not to every specific project (unless needed for some reason, such as replace_varchar_with_text, described earlier).

Branches have the following main uses: 

* Advancing from one release to the next. 

   ::

* Storing content relevant to a particular project scope.

   ::

* Moving large amounts of content from one area of the menu to another.

   ::

* Making identical modifications across all branches.

.. image:: /_static/images/advancing_rn.png
    :align: right

Using branches is ideal for creating **release notes**, each of which is based on, and adds to (and/or modifies) information from the previous release. For example, when you create v2022.2 of the release notes, you should base it on v2022.1 and begin modifying it.The best way to think about it as follows: v2022.2 is v2022.1 + *x* changes, v2022.3 is v2022.2 with *x* changes, and so on. Each release notes branch is identical to the one before it, but includes some new information not included in the original. Some examples of release notes branches are **2022.1**, **2022.2**, and **2022.3**, as shown to the right.

You can also create branches for projects that contain a high number of pages to **help you keep track of the content** related to that scope. Creating a branch for this purpose simply allows you to store your content in a branch dedicated to that folder. You don't actually publish such a branch, and instead transfer the relevant content from it to a live branch with every release. Some examples of this type of branch are **reference_guides** and **configuration_guides**.

A less common, but correct way, to use branches is **as a "package"** for moving a large amount of content from one area of the menu to another. For example, if you need to completely restructure your topic menu, you can use branches as containers with built-in indexes and folder structures. This allows you to create the new structure once correctly, and then to apply it on every branch. How to move large amounts of content will be described later, once you are more familiar with branch scope, described in the next section. Some examples of this type of branch are 

Another correct use of a branch is to **make one specific set of changes across all branches**. One example of this type of branch is **replace_varchar_with_text**. ``VARCHAR`` is a data type that we replaced with another called ``TEXT``. This required all instances of ``VARCHAR`` to be replaced with ``TEXT`` on all branches according to a specific set of rules. Because the changes were identical on all branches and did not affect any other areas of the documentation, I created this branch based on the provided rules and applied the changes to every other branch. The alternative to this method would have been to manually change all of the same instances of every branch, which would have been increased the probability of human error, not to mention daunting and tedious.