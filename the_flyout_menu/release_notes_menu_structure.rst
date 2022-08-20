.. _release_notes_menu_structure:

***********************
Major vs. Minor Branches
***********************
The release notes menu structure depends on whether a version has any minor versions or not. If a version doesn't have any minor versions, such as the `2020.2 Release Notes <https://docs.sqream.com/en/latest/releases/2020.2.html>`_ version, the Release Notes section must directly to its release notes page.

However, versions with minor versions, such as 2021.2, all related minor versions must be nested in it, such as the `Release Notes 2021.2 <https://docs.sqream.com/en/latest/releases/2021.2_index.html>`_ page.

The following is the actual ``toctree`` syntax from the Release Notes index page:

.. code-block:: console

   .. toctree::
      :maxdepth: 2
      :glob:
      :hidden:

      2022.1_index
      2021.2_index
      2021.1_index
      2020.3_index
      2020.2
      2020.1

Notice that the 2020.2 menu item is simply the 2020.2 release notes page, while the 2021.2 menu item (2021.2_index) is a separate page with its own ``toctree`` referring to all other versions released in 2021.2.

For example, the following is the ``toctree`` syntax located on the **2021.2_index** file:

.. code-block:: console

   .. toctree::
      :maxdepth: 1
      :glob:

      2021.2.1.24
      2021.2.1
      2021.2

.. note:: The ``_index`` suffix *must be* appended to the branch name to display menu items as **nested sub-menu items**.