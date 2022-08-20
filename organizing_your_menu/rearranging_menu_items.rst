.. _rearranging_menu_items:

***********************
How Do I Rearrange Menu Items?
***********************
In its simplest form, you rearrange your menu items by doing one or more of the following in your respective ``toctree``:

* Changing the order of file anchors within a menu.

   ::

* Moving a file anchor from a menu to another menu.

   ::

* Moving a file anchor from a menu to a nested menu.

   ::

* Moving a file anchor from one nested menu to another nested menu.

The following is an example of changing the order of file anchors within a menu with a particular arrangement:

.. code-block:: console

   .. toctree::
      :maxdepth: 1
      :titlesonly:

      automatic foreign table DDL resolution
      key_evaluation
      data_encryption
      compression
      python_functions
      workload_manager
      transactions
      concurrency_and_locks
      concurrency_and_scaling_in_sqream

The following shows the new menu order:

.. code-block:: console

   .. toctree::
      :maxdepth: 1
      :titlesonly:

      python_functions
      workload_manager
      transactions
      concurrency_and_locks
      concurrency_and_scaling_in_sqream
      automatic foreign table DDL resolution
      key_evaluation
      data_encryption
      compression

Just as you can change the anchor order as shown above, you can move anchors between menus and/or nested menus.

.. note:: Moving anchors between menus requires you to move the corresponding page files into the folder corresponding to the menu. If you do not move both the anchor **and** the file, the page will not appear in the menu.