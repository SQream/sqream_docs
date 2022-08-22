.. _documenting_major_releases:

***********************
How Do I Document Major Releases?
***********************
Publishing major releases is simpler than publising minor ones, and this page describes how to display your major release page when publishing a major release.

**To display your major release page:**

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

.. tip:: **2022.1.2** is the **page anchor** of the 2022.1.2 release notes page. The page anchor is used for calling and referencing other pages.

4. In the **release_notes** folder, open the **index.rst** file.

    ::

5. As in steps 2 and 3, set the ``toctree`` syntax as in the following example:

   .. code-block::

      .. toctree::
         :maxdepth: 1
         :glob:

         2022.1.2

    The syntax in steps 3 and 5 instructs GitHub to display the **2022.1.2** page.

6. When you are ready to publish the branch, set it to **Public**.

   For more information about setting a branch to **Public**, see :ref:`setting_a_branch_to_public`.