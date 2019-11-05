.. _sql_best_practices:

***************************
SQream DB best practices
***************************

This topic explains some best practices of working with SQream DB.

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

This will also reduce storage size.


Convert external tables to native tables
-------------------------------------------

SQream DB's native storage is heavily optimized for analytic workloads. It is always faster for querying than other formats, even columnar ones such as Parquet. It also enables the use of additional metadata to help speed up queries, in some cases by many orders of magnitude.

You can improve the performance of all operations by converting external tables into native tables, e.g. by using the ``CREATE TABLE AS`` syntax.

For example,

.. code-block:: postgres

   CREATE TABLE native_table AS SELECT * FROM external_table


One situation when this wouldn't be as useful is when you are only likely to query the data one time.

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

  
Use the high selectivity hint
--------------------------------

Use the high selectivity hint when you expect a predicate to filter out most values.

For example,

.. code-block:: postgres

   SELECT store_name, SUM(amount) FROM store_dim 
   WHERE HIGH_SELECTIVITY(p_date = '2018-07-01')
   GROUP BY 1;


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
