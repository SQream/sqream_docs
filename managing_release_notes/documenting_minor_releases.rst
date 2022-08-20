.. _documenting_minor_releases:

***********************
How Do I Document Minor Releases?
***********************
Because many releases are completed on a yearly basis, we give users access to all of them, as in the `2021.2 release notes <https://docs.sqream.com/en/latest/releases/2021.2_index.html>`_.

You do this by nesting all releases under the **2021.2_index** file using a TOC tree, as follows:

.. code-block::

   .. toctree::
      :maxdepth: 1
      :glob:

      2021.2.1.24
      2021.2.1
      2021.2

Here's where it gets a little complex, so take a seat.

As described earlier, it's better (and correct) to use the **ref** syntax to create links to other pages. However, this rule does not apply to links on minor release notes pages.

For example, when you're viewing the **2021.2** branch on the front end, the menu shows a link to each of the nested minor branches. However, clicking **Release Notes 2021.2.1.24** *does not* take you to the 2021.2.1.24 branch, but rather to the page referring to that release notes file *in the branch that you're already on* (2022.2). This is the correct behavior.

Here's where it gets a little tricky. Notice that the `Release Notes 2021.2.1.24 <https://docs.sqream.com/en/v2022.1/releases/2021.2.1.24.html>`_ page describes the **Query Healer** feature. Because this feature was introduced in version 2021.2.1.24, it is documented on only the 2021.2.1.24 branch and all later branches. This feature *does not exist* on all versions (and therefore branches) before 2021.2.1.24. Therefore, the link to the Query Healer documentation is actually a link to the Query Healer page located *on the 2021.2.1.24 branch*.

If you click the Query Healer link on this page, you'll notice that you're taken to the 2021.2.1.24 branch, away from the branch that you were previously on. However, the entire branch is identical except for the Query Healer (and related configuration flags). This is the reason for basing a new release branch on the previous version. If you were to search for the Query Healer on the 2021.2 (or earlier) branch, you would not find it. The **query_healer** page does not exist in the folders belonging to all branches preceding 2021.2.1.24.

When it's time to advance to the new release, you simply add the new release's anchor (for example, 2021.2.1.25) to the TOC tree file, as follows:

.. code-block::

   .. toctree::
      :maxdepth: 1
      :glob:

      2021.2.1.25
      2021.2.1.24
      2021.2.1
      2021.2

.. tip:: Make sure that you've added the actual 2021.2.1.25 file to the 2021.2 folder. Even if the anchor exists in the TOC tree, the page will not appear on the front-end if the file does not exist. To the converse, if the file exists, but its anchor is not in the TOC tree, users will be able to search for it using the search bar, but will not see it anywhere on the menu.

This content of this page is related to the :ref:`release_notes_menu_structure` page.