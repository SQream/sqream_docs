.. _overview:

***********************
Overview
***********************
**Data clustering** refers to sorting table data along naturally occuring dimensions, such as name, date, or location. Data clustering optimizes table structure to significantly improve query performance, especially on very large tables.

A well-clustered table increases the effectivity of the metadata collected by focusing on a specific and limited range of rows, called **chunks**. Chunks, sometimes referred to as **partitions**, are a contiguous number of rows in a specific column.

The following figure shows a table rows grouped as chunks:

.. figure:: /_static/images/chunking2.png
   :scale: 100 %
   
The following figure shows the rows from the table above converted into chunks:
   
.. figure:: /_static/images/chunking_metadata2.png
   :scale: 100 %

The following are some scenarios ideal for data clustering:

* Queries containg a ``WHERE`` predicate written as ``column COMPARISON value``, such as ``date_column > '2019-01-01'`` or ``id = 107`` when the columns referenced are clustering keys.
  In such a case SQream reads the portion of data that contain values matching these predicates only.

* Two clustered tables joined by their respective clustering keys.

  In such a case SQream uses metadata to more easily identify matching chunks.