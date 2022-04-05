.. _optimization_best_practices:

**********************************
Optimization and Best Practices
**********************************

This topic explains some best practices of working with SQream DB.

See also our :ref:`monitoring_query_performance` guide for more information.

.. contents:: In this topic:
   :local:

.. _table_design_best_practices:

Table design
==============
This section describes best practices and guidelines for designing tables.

Use date and datetime types for columns
-----------------------------------------

When creating tables with dates or timestamps, using the purpose-built ``DATE`` and ``DATETIME`` types over integer types or ``VARCHAR`` will bring performance and storage footprint improvements, and in many cases huge performance improvements (as well as data integrity benefits). SQream DB stores dates and datetimes very efficiently and can strongly optimize queries using these specific types.

Reduce varchar length to a minimum
--------------------------------------

With the ``VARCHAR`` type, the length has a direct effect on query performance.

If the size of your column is predictable, by defining an appropriate column length (no longer than the maximum actual value) you will get the following benefits:

* Data loading issues can be identified more quickly

* SQream DB can reserve less memory for decompression operations

* Third-party tools that expect a data size are less likely to over-allocate memory

Don't flatten or denormalize data
-----------------------------------

SQream DB executes JOIN operations very effectively. It is almost always better to JOIN tables at query-time rather than flatten/denormalize your tables.

This will also reduce storage size and reduce row-lengths.

We highly suggest using ``INT`` or ``BIGINT`` as join keys, rather than a text/string type.

Convert foreign tables to native tables
-------------------------------------------

SQream DB's native storage is heavily optimized for analytic workloads. It is always faster for querying than other formats, even columnar ones such as Parquet. It also enables the use of additional metadata to help speed up queries, in some cases by many orders of magnitude.

You can improve the performance of all operations by converting :ref:`foreign tables<external_tables>` into native tables by using the :ref:`create_table_as` syntax.

For example,

.. code-block:: postgres

   CREATE TABLE native_table AS SELECT * FROM external_table

The one situation when this wouldn't be as useful is when data will be only queried once.

Use information about the column data to your advantage
-------------------------------------------------------------

Knowing the data types and their ranges can help design a better table.

Set ``NULL`` or ``NOT NULL`` when relevant
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, if a value can't be missing (or ``NULL``), specify a ``NOT NULL`` constraint on the columns.

Not only does specifying ``NOT NULL`` save on data storage, it lets the query compiler know that a column cannot have a ``NULL`` value, which can improve query performance.

Keep VARCHAR lengths to a minimum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While it won't make a big difference in storage, large strings allocate a lot of memory at query time.

If a column's string length never exceeds 50 characters, specify ``VARCHAR(50)`` rather than an arbitrarily large number.


Sorting 
==============

Data sorting is an important factor in minimizing storage size and improving query performance.

* Minimizing storage saves on physical resources and increases performance by reducing overall disk I/O. Prioritize the sorting of low-cardinality columns. This reduces the number of chunks and extents that SQream DB reads during query execution.

* Where possible, sort columns with the lowest cardinality first. Avoid sorting ``VARCHAR`` and ``TEXT/NVARCHAR`` columns with lengths exceeding 50 characters.

* For longer-running queries that run on a regular basis, performance can be improved by sorting data based on the ``WHERE`` and ``GROUP BY`` parameters. Data can be sorted during insert by using :ref:`external_tables` or by using :ref:`create_table_as`.

.. _query_best_practices:

Query best practices
=====================

This section describes best practices for writing SQL queries.


Reduce data sets before joining tables
-----------------------------------------

Reducing the input to a ``JOIN`` clause can increase performance.
Some queries benefit from retreiving a reduced dataset as a subquery prior to a join.

For example,

.. code-block:: postgres

   SELECT store_name, SUM(amount)
   FROM store_dim AS dim INNER JOIN store_fact AS fact ON dim.store_id=fact.store_id
   WHERE p_date BETWEEN '2018-07-01' AND '2018-07-31'
   GROUP BY 1;

Can be rewritten as

.. code-block:: postgres

   SELECT store_name, sum_amount
   FROM store_dim AS dim INNER JOIN
      (SELECT SUM(amount) AS sum_amount, store_id
      FROM store_fact
      WHERE p_date BETWEEN '2018-07-01' AND '2018-07-31'
      group by 2) AS fact
   ON dim.store_id=fact.store_id; 

Prefer the ANSI JOIN
----------------------------

SQream DB prefers the ANSI JOIN syntax.
In some cases, the ANSI JOIN performs better than the non-ANSI variety.

For example, this ANSI JOIN example will perform better:

.. code-block:: postgres
   :caption: ANSI JOIN will perform better

   SELECT p.name, s.name, c.name
   FROM  "Products" AS p
   JOIN  "Sales" AS s
     ON  p.product_id = s.sale_id
   JOIN  "Customers" as c
     ON  s.c_id = c.id AND c.id = 20301125;

This non-ANSI JOIN is supported, but not recommended:

.. code-block:: postgres
   :caption: Non-ANSI JOIN may not perform well

   SELECT p.name, s.name, c.name
   FROM "Products" AS p, "Sales" AS s, "Customers" as c
   WHERE p.product_id = s.sale_id
     AND s.c_id = c.id
     AND c.id = 20301125;



.. _high_selectivity:

Use the high selectivity hint
--------------------------------

Selectivity is the ratio of cardinality to the number of records of a chunk. We define selectivity as :math:`\frac{\text{Distinct values}}{\text{Total number of records in a chunk}}`

SQream DB has a hint function called ``HIGH_SELECTIVITY``, which is a function you can wrap a condition in.

The hint signals to SQream DB that the result of the condition will be very sparse, and that it should attempt to rechunk
the results into fewer, fuller chunks.

Use the high selectivity hint when you expect a predicate to filter out most values. For example, when the data is dispersed over lots of chunks (meaning that the data is :ref:`not well-clustered<data_clustering>`).

For example,

.. code-block:: postgres

   SELECT store_name, SUM(amount) FROM store_dim 
   WHERE HIGH_SELECTIVITY(p_date = '2018-07-01')
   GROUP BY 1;

This hint tells the query compiler that the ``WHERE`` condition is expected to filter out more than 60% of values. It never affects the query results, but when used correctly can improve query performance.

.. tip:: The ``HIGH_SELECTIVITY()`` hint function can only be used as part of the ``WHERE`` clause. It can't be used in equijoin conditions, cases, or in the select list.

Read more about identifying the scenarios for the high selectivity hint in our :ref:`Monitoring query performance guide<high_selectivity_data_opt>`.

Cast smaller types to avoid overflow in aggregates
------------------------------------------------------

When using an ``INT`` or smaller type, the ``SUM`` and ``COUNT`` operations return a value of the same type. 
To avoid overflow on large results, cast the column up to a larger type.

For example

.. code-block:: postgres

   SELECT store_name, SUM(amount :: BIGINT) FROM store_dim 
   GROUP BY 1;


Prefer ``COUNT(*)`` and ``COUNT`` on non-nullable columns
------------------------------------------------------------

SQream DB optimizes ``COUNT(*)`` queries very strongly. This also applies to ``COUNT(column_name)`` on non-nullable columns. Using ``COUNT(column_name)`` on a nullable column will operate quickly, but much slower than the previous variations.


Return only required columns
-------------------------------

Returning only the columns you need to client programs can improve overall query performance.
This also reduces the overall result set, which can improve performance in third-party tools.

SQream is able to optimize out unneeded columns very strongly due to its columnar storage.

Use saved queries to reduce recurring compilation time
-------------------------------------------------------

:ref:`saved_queries` are compiled when they are created. The query plan is saved in SQream DB's metadata for later re-use.

Because the query plan is saved, they can be used to reduce compilation overhead, especially with very complex queries, such as queries with lots of values in an :ref:`IN` predicate.

When executed, the saved query plan is recalled and executed on the up-to-date data stored on disk.

See how to use saved queries in the :ref:`saved queries guide<saved_queries>`.

Pre-filter to reduce :ref:`JOIN<joins>` complexity
--------------------------------------------------------

Filter and reduce table sizes prior to joining on them

.. code-block:: postgres

   SELECT store_name,
          SUM(amount)
   FROM dimention dim
     JOIN fact ON dim.store_id = fact.store_id
   WHERE p_date BETWEEN '2019-07-01' AND '2019-07-31'
   GROUP BY store_name;

Can be rewritten as:

.. code-block:: postgres

   SELECT store_name,
          sum_amount
   FROM dimention AS dim
     INNER JOIN (SELECT SUM(amount) AS sum_amount,
                        store_id
                 FROM fact
                 WHERE p_date BETWEEN '2019-07-01' AND '2019-07-31'
                 GROUP BY store_id) AS fact ON dim.store_id = fact.store_id;


.. _data_loading_considerations:

Data loading considerations
=================================

Allow and use natural sorting on data
----------------------------------------

Very often, tabular data is already naturally ordered along a dimension such as a timestamp or area.

This natural order is a major factor for query performance later on, as data that is naturally sorted can be more easily compressed and analyzed with SQream DB's metadata collection.

For example, when data is sorted by timestamp, filtering on this timestamp is more effective than filtering on an unordered column.

Natural ordering can also be used for effective :ref:`delete` operations.


Further reading and monitoring query performance
=======================================================

Read our :ref:`monitoring_query_performance` guide to learn how to use the built in monitoring utilities. 
The guide also gives concerete examples for improving query performance.
