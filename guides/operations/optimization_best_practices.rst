.. _sql_best_practices:

**********************************
Optimization and Best Practices
**********************************

This topic explains some best practices of working with SQream.

See also our :ref:`monitoring_query_performance` guide for more information.

.. contents:: In this topic:
   :local:

.. _table_design_best_practices:

Table Design
==============
This section describes best practices and guidelines for designing tables.

Using Date and Datetime Types for Columns
-----------------------------------------

When creating tables with dates or timestamps, using the purpose-built ``DATE`` and ``DATETIME`` types over integer types or ``VARCHAR`` will bring performance and storage footprint improvements, and in many cases huge performance improvements (as well as data integrity benefits). SQream stores dates and datetimes very efficiently and can strongly optimize queries using these specific types.

Shortening VARCHAR Length
--------------------------------------

With the ``VARCHAR`` type, the length has a direct effect on query performance.

If the size of your column is predictable, by defining an appropriate column length (no longer than the maximum actual value) you will get the following benefits:

* Data loading issues can be identified more quickly

* SQream can reserve less memory for decompression operations

* Third-party tools that expect a data size are less likely to over-allocate memory

Avoiding Flattening or Denormalizing Data
-----------------------------------

SQream executes JOIN operations very effectively. It is almost always better to JOIN tables at query-time rather than flatten/denormalize your tables.

This will also reduce storage size and reduce row-lengths.

We highly suggest using ``INT`` or ``BIGINT`` as join keys, rather than a text/string type.

Converting Foreign Tables to Native Tables
-------------------------------------------

SQream's native storage is heavily optimized for analytic workloads. It is always faster for querying than other formats, even columnar ones such as Parquet. It also enables the use of additional metadata to help speed up queries, in some cases by many orders of magnitude.

You can improve the performance of all operations by converting :ref:`foreign tables<external_tables>` into native tables by using the :ref:`create_table_as` syntax.

For example,

.. code-block:: postgres

   CREATE TABLE native_table AS SELECT * FROM external_table

The one situation when this wouldn't be as useful is when data will be only queried once.

Leverating Column Data Information
-------------------------------------------------------------

Knowing the data types and their ranges can help design a better table.

Identifying Relevance of Setting NULL or NOT NULL Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, if a value cannot be omitted (or ``NULL``), you must specify a ``NOT NULL`` constraint on the columns.

In addition to saving data storage, specifying ``NOT NULL`` informs the query compiler that a column cannot have a ``NULL`` value, which can improve query performance.

Shortening VARCHAR Length
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Although long strings do not affect storage, they require a lot of memory while queries are being run. If a column's string length is less than 50 characters, specify ``VARCHAR(50)`` rather than an arbitrarily large number.


Sorting Data
==============
Sorting data is an important factor in minimizing storage size and improving query performance for the following reasons:

* Minimizing storage saves on physical resources and increases performance by reducing overall disk I/O. Prioritize the sorting of low-cardinality columns. This reduces the number of chunks and extents that SQream reads during query execution.

* Where possible, sort columns with the lowest cardinality first. Avoid sorting ``VARCHAR`` and ``TEXT`` columns with lengths exceeding 50 characters.

* For longer-running queries that run on a regular basis, performance can be improved by sorting data based on the ``WHERE`` and ``GROUP BY`` parameters. Data can be sorted during insert by using :ref:`external_tables` or by using :ref:`create_table_as`.

.. _query_best_practices:

Best Practices for Writing SQL Queries
=====================

This section describes best practices for writing SQL queries.


Reducing Data Sets Before Joining Tables
-----------------------------------------

Reducing the input to a ``JOIN`` clause can increase performance.
Some queries benefit from retreiving a reduced dataset as a subquery prior to a join, as shown in the following example:

.. code-block:: postgres

   SELECT store_name, SUM(amount)
   FROM store_dim AS dim INNER JOIN store_fact AS fact ON dim.store_id=fact.store_id
   WHERE p_date BETWEEN '2018-07-01' AND '2018-07-31'
   GROUP BY 1;

This can be rewritten as follows:

.. code-block:: postgres

   SELECT store_name, sum_amount
   FROM store_dim AS dim INNER JOIN
      (SELECT SUM(amount) AS sum_amount, store_id
      FROM store_fact
      WHERE p_date BETWEEN '2018-07-01' AND '2018-07-31'
      group by 2) AS fact
   ON dim.store_id=fact.store_id; 

Using an ANSI JOIN
----------------------------

SQream prefers the ANSI JOIN syntax.
In some cases ANSI JOINs performs better than the non-ANSI variety, as shown in the following example:

.. code-block:: postgres
   :caption: ANSI JOIN will perform better

   SELECT p.name, s.name, c.name
   FROM  "Products" AS p
   JOIN  "Sales" AS s
     ON  p.product_id = s.sale_id
   JOIN  "Customers" as c
     ON  s.c_id = c.id AND c.id = 20301125;

SQream supports the following non-ANSI JOIN, but does not recommend using it:

.. code-block:: postgres
   :caption: Non-ANSI JOIN may not perform well

   SELECT p.name, s.name, c.name
   FROM "Products" AS p, "Sales" AS s, "Customers" as c
   WHERE p.product_id = s.sale_id
     AND s.c_id = c.id
     AND c.id = 20301125;



.. _high_selectivity:

Using a High Selectivity Hint
--------------------------------

**Selectivity** is the ratio of cardinality to the number of records of a chunk. Selectivity is defined as ``:math:`\frac{\text{Distinct values}}{\text{Total number of records in a chunk}}```.

SQream employees a hint function called ``HIGH_SELECTIVITY``, which is a function that can be used for wrapping a condition. The hint signals to SQream that the result of the condition is very sparse and to rechunk the results into fewer, fuller chunks.

SQream recommends using the high selectivity hint when you expect a predicate to filter out most values, such as when data is dispersed over many chunks, indicating that the data has not been optimally clustered.

The following example shows data that is not clustered optimally:

.. code-block:: postgres

   SELECT store_name, SUM(amount) FROM store_dim 
   WHERE HIGH_SELECTIVITY(p_date = '2018-07-01')
   GROUP BY 1;

This hint tells the query compiler that the ``WHERE`` condition is expected to filter out more than 60% of values. While it does not affect query results, using it correctly can improve query performance.

.. tip:: The ``HIGH_SELECTIVITY()`` hint function can only be used as part of the ``WHERE`` clause and cannot be used in equijoin conditions, cases, or in the select list.

For more information about identifying scenarios for the high selectivity hint, see the :ref:`Monitoring Query Performance Guide<high_selectivity_data_opt>`.

For more information about optimal data clustering, see :ref:`not well-clustered<data_clustering>`).

Casting Smaller Types to Avoid Aggregate Overflow
------------------------------------------------------

When using an ``INT`` or smaller type, the ``SUM`` and ``COUNT`` operations return a value of the same type. 
To avoid overflow on large results, cast the column up to a larger type, as shown in the following example:

.. code-block:: postgres

   SELECT store_name, SUM(amount :: BIGINT) FROM store_dim 
   GROUP BY 1;


Preferring ``COUNT(*)`` and ``COUNT`` on Non-Nullable Columns
------------------------------------------------------------

SQream optimizes ``COUNT(*)`` queries very strongly. This also applies to ``COUNT(column_name)`` on non-nullable columns. Using ``COUNT(column_name)`` on a nullable column operate quickly, but much slower than the previous variations.


Returning Only Required Columns
-------------------------------

Returning only the columns you need to client programs can improve overall query performance.
This also reduces the overall result set, which can improve performance in third-party tools.

SQream is able to optimize out unneeded columns very strongly due to its columnar storage.

Using Saved Queries to Reduce Recurring Compilation Duration
-------------------------------------------------------

:ref:`saved_queries` are compiled when they are created. The query plan is saved in SQream's metadata for later re-use.

Because the query plan is saved, they can be used to reduce compilation overhead, especially with very complex queries, such as queries with lots of values in an :ref:`IN` predicate.

When executed, the saved query plan is recalled and executed on the up-to-date data stored on disk.

See how to use saved queries in the :ref:`saved queries guide<saved_queries>`.

Pre-Filtering to Reduce JOIN Complexity
--------------------------------------------------------
The following is the correct syntax for pre-filtering to reduce JOIN complexity by filtering and reducing table sizes before joining them:

.. code-block:: postgres

   SELECT store_name,
          SUM(amount)
   FROM dimention dim
     JOIN fact ON dim.store_id = fact.store_id
   WHERE p_date BETWEEN '2019-07-01' AND '2019-07-31'
   GROUP BY store_name;

The example above can be rewritten as follows:

.. code-block:: postgres

   SELECT store_name,
          sum_amount
   FROM dimention AS dim
     INNER JOIN (SELECT SUM(amount) AS sum_amount,
                        store_id
                 FROM fact
                 WHERE p_date BETWEEN '2019-07-01' AND '2019-07-31'
                 GROUP BY store_id) AS fact ON dim.store_id = fact.store_id;
				 
For more information about reducing JOIN complexity, see :ref:`JOIN<joins>`.


.. _data_loading_considerations:

Data Loading Considerations
=================================

Enabling and Using Natural Data Sorting
----------------------------------------

Tabular data is often naturally ordered along a dimension, such as a timestamp or area. This natural order is a major factor for query performance during later stages, as data that is naturally sorted can be more easily compressed and analyzed with SQream's metadata collection.

For example, when data is sorted by timestamp, filtering on this timestamp is more effective than filtering on an unordered column. Natural ordering can also be used for effective **DELETE** operations.

For more information about Delete operations, see :ref:`delete operations`.


Further Reading and Monitoring Query Performance
=======================================================
For more information about built-in monitoring utilities, see the :ref:`monitoring_query_performance` guide. The Monitoring Query Performance Guide also gives concerete examples for improving query performance.