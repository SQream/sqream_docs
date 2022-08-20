.. _toc_tree:

***********************
Creating a TOC Tree
***********************
The ``toctree`` syntax is used in **index** files for nesting pages under a topic menu.

The following is the syntax for a ``toctree``:

.. code-block:: console

   .. toctree::
      :maxdepth: 1
      :caption: Getting Started
      :glob:

      overview/index
      doc_set/index
      main_tasks/index
      platforms/index

The ``:maxdepth::`` sets the maximum amount of heading levels to show, and ``:caption:`` lets you set a caption. Both are optional. Note that the menu item **will not be displayed on your menu** if you do not append it with ``/index``.

.. note:: For a nested folder (a folder containing sub-pages) to appear in your menu, you **must** append it with ``/index``. For a regular page to appear in your menu, you must **not** append it with ``/index``.
