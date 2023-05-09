.. _flexible_data_clustering_overview:

***********************
Overeview
***********************
**Flexible data clustering** refers to sorting table data along naturally occuring dimensions, such as name, date, or location. Data clustering optimizes table structure to significantly improve query performance, especially on very large tables. A well-clustered table increases the effectivity of the metadata collected by focusing on a specific and limited range of rows, called **chunks**.

The following are some scenarios ideal for data clustering:

* Queries containg a ``WHERE`` predicate written as ``column COMPARISON value``, such as ``date_column > '2019-01-01'`` or ``id = 107`` when the columns referenced are clustering keys.

  In such a case SQream reads the portion of data that contain values matching these predicates only.

* Two clustered tables joined by their respective clustering keys.

  In such a case SQream uses metadata to more easily identify matching chunks.