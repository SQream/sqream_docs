.. _what_are_branches_used_for:

***********************
What are Branches Used For?
***********************
This page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
======================
Branches have the following main uses: 

* Advancing from one release to the next. 

   ::

* Storing content relevant to a particular project scope.

   ::

* Moving large amounts of content from one area of the menu to another.

   ::

* Making identical modifications across all branches.

Main Use of Branches
======================
Because in many cases pages and features are *release-driven*, the best practice is to create branches belonging to each release, and not to every specific project (unless needed for some reason, such as the **replace_varchar_with_text** branch).

.. image:: /_static/images/advancing_rn.png
    :align: right

Using branches is ideal for creating **release notes**, each of which is based on, and adds to (and/or modifies) information from the previous release. For example, when you create v2022.2 of the release notes, you should base it on v2022.1 and begin modifying it.

The best way to think about it as follows:

* **v2022.1** + *x* changes = **v2022.2**

     ::

* **v2022.2** + *x* changes =  **v2022.3**, and so on.

Each release notes branch is identical to the one before it, but includes some new information not included in the original, as shown to the right.

Other Ways to Use Branches
======================
You can also create branches for projects that contain a high number of pages to **help you keep track of the content** related to that scope. Creating a branch for this purpose simply allows you to store your content in a branch dedicated to that folder. You don't actually publish such a branch, and instead transfer the relevant content from it to a live branch with every release. Some examples of this type of branch are **reference_guides** and **configuration_guides**.

.. tip:: You **can** publish this type of branch to bring its contents to the front-end if you want. However, because changes made on one branch often (but not always) require changes made in other areas of the documentation, it's recommended to manually copy and paste all required modified files into a local folder, and to copy them into all required live branch pages. In other words, in some cases, the interrelated nature of our documentation set makes having pure branches only nominally effective. For example, if you commit changes made on the **configuration_guides** branch, all related feature modifications, which are not made on that branch, will not be published. 

A less common, but correct way, to use branches is **as a "container"** for moving a large amount of content from one area of the menu to another. For example, if you need to completely restructure your topic menu, you can use branches as containers with built-in indexes and folder structures. This allows you to create the new structure once correctly, and then to apply it on every branch.

.. warning:: Because GitHub may not recognize complex menu changes made using branch merges, you may need to make them manually.

Another correct use of a branch is to **make one specific set of changes across all branches**. One example of this type of branch is **replace_varchar_with_text**. ``VARCHAR`` is a data type that we replaced with another called ``TEXT``. This required all instances of ``VARCHAR`` to be replaced with ``TEXT`` on all branches according to a specific set of rules. Because the changes were identical on all branches and did not affect any other areas of the documentation, I created this branch based on the provided rules and applied the changes to every other branch. The alternative to this method would have been to manually change all of the same instances of every branch, which would have been increased the probability of human error, not to mention being daunting and tedious.