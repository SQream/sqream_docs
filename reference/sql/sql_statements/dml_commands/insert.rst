.. _insert:

******
INSERT
******

The ``INSERT`` command is used to insert one or more rows into a table in a database. However, for bulk loading large amounts of data into existing tables, the :ref:`COPY FROM<copy_from>` command typically offers better performance compared to using multiple INSERT statements.

Syntax
======

.. code-block:: postgres

   INSERT INTO [ "<schema_name>". ]"<table_name>"
   [ ( "<column_name>" [, ... ] ) ]
   VALUES ( <value> [, ...] )
   | <query>

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_name``
     - A comma separated list of column names that specifies the destination columns of the insert.
   * - ``query``
     - A :ref:`SELECT<select>` or :ref:`VALUES<values>` statement is used for providing data to be inserted into a table. Each value in the statement must correspond to the data type of its destination column in the table. Additionally, the order of the values must match the order of the columns specified in the table or within parentheses if column names are explicitly provided.

Examples
========

Inserting a Single Row
----------------------

.. code-block:: postgres
   
   INSERT INTO
     cool_animals
   VALUES
     (5, 'fox', 15);

Inserting Into Rows with Default Values
---------------------------------------

The ``id`` column is designated as an :ref:`IDENTITY <identity>` column and is configured with a default value, thus it can be excluded from explicit value assignment during insertion.

.. code-block:: postgres
   
   INSERT INTO
     cool_animals(name, weight)
   VALUES
     ('fox', 15);

Changing Column Order
---------------------

.. code-block:: postgres
   
   INSERT INTO
     cool_animals(name, weight, id)
   VALUES
     ('possum', 7, 6);

Inserting Multiple Rows
-----------------------

.. code-block:: postgres
   
   INSERT INTO
     cool_animals(name, weight)
   VALUES
     ('koala', 20),
     ('lemur', 6),
     ('kiwi', 3);

Import data from other tables
-----------------------------

The ``SELECT`` statement decrypts information by default. When executing ``INSERT INTO TABLE AS SELECT``, encrypted information will appear as clear text in the newly created table.

The ``INSERT`` statement can be used to insert data obtained from queries performed on other tables, including :ref:`foreign tables<create_foreign_table>`.

For example,

.. code-block:: postgres
   
   SELECT
     name,
     weight
   FROM
     all_animals
   WHERE
     region = 'Australia';
   
Output:

.. code-block:: none

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
   
   INSERT INTO
     cool_animals(name, weight)
   SELECT
     name,
     weight
   FROM
     all_animals
   WHERE
     region = 'Australia';

Inserting Data with Positional Placeholders
-------------------------------------------

When preparing an ``INSERT`` statement for loading data over the network (for example, from a :ref:`Python<pysqream>` or :ref:`Java<java_jdbc>` application, use positional placeholders.

.. note:: The ``executemany`` method is used only for parametrized statements like ``INSERT``. Running multiple ``SELECT`` queries or other statements this way is not supported.

Example using Python:

.. code-block:: python

   data = [["Kangaroo", 120], ["Koala", 20], ["Platypus", 5]]
   data_len = len(data)

   insert_stmt = 'INSERT INTO cool_animals (name, weight) VALUES (?, ?)'
   con.executemany(insert_stmt, data)
   

Permissions
=============

The role must have the ``INSERT`` permission to the destination table.

