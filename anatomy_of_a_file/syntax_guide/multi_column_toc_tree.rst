.. _multi_column_toc_tree:

***********************
Creating a Multi-Column TOC Tree
***********************
The following is the syntax for multi-column TOC trees:

.. code-block:: console

  .. toctree::
     :columns: 2
     :maxdepth: 2

     moduleA.rst
     moduleB.rst

You can use this if you have very long lists that you want to display in more than one column, as in `Built-In Scalar Functions <https://docs.sqream.com/en/latest/reference/sql/sql_functions/scalar_functions/index.html>`_.