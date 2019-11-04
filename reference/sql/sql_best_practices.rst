.. _sql_best_practices:

***************************
SQL best practices
***************************

This topic explains the best practices for optimizing SQL performance with SQream DB.

Table design
==============
This section describes best practices and guidelines for designing tables.

Use date and datetime types for columns
----------------------------------------

When creating tables with dates or timestamps, we recommend the purpose-built ``date`` and ``datetime`` data types over standard integers or a ``VARCHAR``. SQream DB stores dates more efficiently and can optimize queries on specific timeframes.

Reduce varchars to a minimum
------------------------------

While SQream DB compresses all data types, with data types like VARCHAR the length declaration has a direct effect on query performance.

If the size of your column is predictable, we recommend you define an appropriate column length:

* Data loading issues can be identified more quickly

* SQream DB can reserve less memory for decompression operations

* Third-party tools that expect a data size are less likely to over-allocate memory

Normalize data when possible
-------------------------------

SQream DB optimizes the JOIN operation. Unlike some databases, it is better to JOIN the dimensions at query-time rather than flatten the table.

This also reduces storage and can help with referential integrity.


Convert an external table to a proper table
---------------------------------------------

SQream DB's storage is optimized for large analytic workloads. Some tools that generate source data such as Parquet files may not be optimized for your workloads.

Consider converting external tables to a proper table, using the ``CREATE TABLE AS`` syntax.

For example,

.. code-block:: postgres

   CREATE TABLE proper_table AS SELECT * FROM external_table

Query optimizations
=====================

This section describes best practices and guidelines for writing SQL queries.


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

  
Use high selectivity hints
----------------------------

Use the high selectivity hint when you expect a query to filter out most values.

For example,

.. code-block:: postgres

   SELECT store_name, SUM(amount) FROM store_dim 
   WHERE HIGH_SELECTIVITY(p_date = '2018-07-01')
   GROUP BY 1;


Up-cast smaller datatypes to avoid overflow
----------------------------------------------

When using an ``int`` or smaller datatype, the ``SUM`` and ``COUNT`` operations return will return a value of the same type. To avoid overflow on large results, cast the column up to a larger type.

For example

.. code-block:: postgres

   SELECT store_name, SUM(amount :: BIGINT) FROM store_dim 
   GROUP BY 1;


Prefer ``COUNT(*)``
-------------------

SQream DB optimizes ``COUNT(*)`` queries. Prefer this syntax to ``COUNT(column_name)``.


Query only required columns
------------------------------

Like other columnar databases, SQream DB reads data on a column-by-column basis. If not all columns are required, removing them from the SELECT clause can improve overall query performance.