.. _insert:

**********************
INSERT
**********************

``INSERT`` inserts one or more rows into a table.

.. tip:: 
   * To bulk load data into existing tables, the :ref:`COPY FROM<copy_from>` command performs better than ``INSERT``.
   * To load Parquet or ORC files, see :ref:`CREATE EXTERNAL TABLE<create_external_table>`

Permissions
=============

The role must have the ``INSERT`` permission to the destination table.

Syntax
==========

.. code-block:: postgres

   insert_statement ::=

    INSERT INTO [schema_name.]table_name
        [ ( column_name [, ... ] ) ]
    query ;
    

   schema_name ::= identifier
   
   table_name ::= identifier

   column_name ::= identifier


Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``[schema_name.]table_name``
     - Table to insert data into
   * - ``( column_name [, ...] )``
     - A comma separated list of column names that specifies the destination columns of the insert.
   * - ``query``
     - A :ref:`SELECT<select>` or :ref:`VALUES<values>` statement. Each value must match the data type of its destination column. The values must also match the order of the table or columns if specified with ` (column_name, ...)`.



Examples
===========

Inserting a single row
------------------------------

.. code-block:: postgres
   
   INSERT INTO cool_animals VALUES (5, 'fox', 15);

Inserting into rows with default values
------------------------------------------

The ``id`` column is an :ref:`IDENTITY<identity>` column, and has a default, so it can be omitted.

.. code-block:: postgres
   
   INSERT INTO cool_animals(name, weight) VALUES ('fox', 15);

Changing column order
------------------------------

.. code-block:: postgres
   
   INSERT INTO cool_animals(name, weight, id) VALUES ('possum', 7, 6);

Inserting multiple rows
----------------------------

.. code-block:: postgres
   
   INSERT INTO cool_animals(name, weight) VALUES ('koala', 20), ('lemur', 6), ('kiwi', 3);

Import data from other tables
--------------------------------

``INSERT`` can be used to insert data obtained from queries on other tables, including :ref:`external tables<create_external_table>`.

For example,

.. code-block:: psql
   
   farm=> SELECT name, weight FROM all_animals
   .      WHERE region = 'Australia';
   
   name     | weight
   ---------+-------
   Kangaroo | 120
   Koala    | 20
   Wombat   | 60
   Platypus | 5
   Wallaby  | 35
   Echidna  | 8
   Dingo    | 25

.. code-block:: postgres
   
   INSERT INTO cool_animals(name,weight) 
     SELECT name, weight FROM all_animals
     WHERE region = 'Australia';

Inserting data with positional placeholders
---------------------------------------------

When preparing an ``INSERT`` statement for loading data over the network (for example, from a :ref:`Python<pysqream>` or :ref:`Java<java_jdbc>` application, use positional placeholders.

Example using Python:

.. code-block:: python

   data = [["Kangaroo", 120], ["Koala", 20], ["Platypus", 5]]
   data_len = len(data)

   insert_stmt = 'INSERT INTO cool_animals (name, weight) VALUES (?, ?)'
   con.executemany(insert_stmt, data)
   
.. note:: The ``executemany`` method is used only for parametrized statements like ``INSERT``. Running multiple ``SELECT`` queries or other statements this way is not supported.


