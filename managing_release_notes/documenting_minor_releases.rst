.. _documenting_minor_releases:

***********************
How Do I Document Minor Releases?
***********************
This page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
==========
Documenting minor releases is a little more compiclated than documenting major releases. Because several releases are completed during the year, we give users access to all of them, as in the `2021.2 release notes <https://docs.sqream.com/en/latest/releases/2021.2_index.html>`_.

Displaying Your Minor Release Pages
===============================
This page describes how to display your minor release pages when publishing minor releases.

**To display your minor release pages:**

1. In GitHub, access the most current branch.
  
   For example, access the v2022.1.2 branch.

2. In the main folder, open the **index.rst** file.

    ::

3. Set the ``toctree`` syntax as in the following example:

   .. code-block::

      .. toctree::
         :maxdepth: 1
         :glob:

         2022.1.2
         2022.1.1
         2022.1

.. tip:: Each of the above is the **page anchor** of each respective page. The page anchor is used for calling and referencing other pages. Only include the pages that you want to display in your menu.

4. In the **release_notes** folder, open the **index.rst** file.

    ::

5. As in Step 3, set the ``toctree`` syntax as in the following example:

   .. code-block::

      .. toctree::
         :maxdepth: 1
         :glob:

         2022.1.2
         2022.1.1
         2022.1

   The syntax in steps 3 and 5 instructs GitHub to display the **2022.1.2**, **2022.1.1**, and **2022.1** pages.

   .. note:: Only include the page anchor of the files that you want to display on the menu.

6. When you are ready to publish the branch, set it to **Public**.

   For more information about setting a branch to **Public**, see :ref:`setting_a_branch_to_public`.

Setting Your Absolute Links
===============================
While the best practice for making links is to use the ``:ref:`` syntax, the one notable exception is the links on each minor release notes page. Because we **do not show** any minor branches on the fly-out menu, users have no way to access them. However, because the minor branches are public users must be able to access them.

Therefore, every link on each respective release notes page must be an **absolute link** pointing to its respective branch. For example, all links on the 2022.1.2 branch must be absolute links to that branch. Clicking one of these absolute links takes the user to that specific branch, where all of its features are documented. Once in that branch, all ``:ref:`` links point to only to pages within that specific branch.

The following is an absolute link to the **Query Healer** page on the 2022.1.2 branch:

.. code-block::

   https://docs.sqream.com/en/v2022.1.2/feature_guides/query_healer.html

.. tip:: The file being called by the ``toctree`` syntax must be located in the folder containing the **index** file calling it. Even if the page's anchor exists in the TOC tree, the page will not appear on the front-end if the file is not in the same folder as the **index** file. To the converse, if the file exists, but its anchor is not in the TOC tree, users will be able to search for it using the search bar, but will not see it anywhere on the menu.