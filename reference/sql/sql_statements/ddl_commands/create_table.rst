.. _create_table:

*****************
CREATE TABLE
*****************

The ``CREATE TABLE`` statement is used to create a new table in an existing database.

.. tip:: 
   * To create a table based on the result of a select query, see :ref:`CREATE TABLE AS <create_table_as>`.
   * To create a table based on files like Parquet and ORC, see :ref:`CREATE FOREIGN TABLE <create_foreign_table>`



Syntax
==========
The following is the correct syntax for creating a table:

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] TABLE [schema_name.]table_name (
           { column_def [, ...] }
       )
       [ CLUSTER BY { column_name [, ...] } ]
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

   column_name ::= identifier
   
   column_constraint ::=
       { NOT NULL | NULL }
   
   default ::=
       DEFAULT default_value
       | IDENTITY [ ( start_with [ , increment_by ] ) ]

Parameters
============
The following parameters can be used when creating a table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Creates a new tables and overwrites any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name.
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``CLUSTER BY column_name1 ...``
     - 
         A commma separated list of clustering column keys.
         
         See :ref:`flexible_data_clustering` for more information.
   * - ``LIKE``
     - Duplicates the column structure of an existing table.
	 
	 
.. _default_values:

Default Value Constraints
===============

The ``DEFAULT`` value constraint specifies a value to use if one is not defined in an :ref:`insert` or :ref:`copy_from` statement. 

The value may either be a literal, **GETDATE()**, or Null, which is evaluated at the time the row is created.

.. note:: The ``DEFAULT`` constraint only applies if the column does not have a value specified in the :ref:`insert` or :ref:`copy_from` statement. You can still insert a ``NULL`` into an nullable column by explicitly inserting ``NULL``. For example, ``INSERT INTO cool_animals VALUES (1, 'Gnu', NULL)``.

Syntax
---------
The following is the correct syntax for using the **DEFAULT** value constraints:


.. code-block:: postgres

   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

   column_constraint ::=
       { NOT NULL | NULL }

   default ::=
       DEFAULT default_value
       | IDENTITY [ ( start_with [ , increment_by ] ) ]
   
   check_specification ::= 
      CHECK( 'CS compression_spec' )
   
   compression_spec ::=
       { "default" | "p4d" | "dict" | "rle" | "sequence" | "flat" }


.. _identity:

Identity
-----------------------
The ``Identity`` (or sequence) columns can be used for generating key values. Some databases call this ``AUTOINCREMENT``.

The **identity** property on a column guarantees that each new row inserted is generated based on the current seed & increment.

.. warning:: 
   The identity property on a column does not guarantee uniqueness. The identity value can be bypassed by specifying it in an :ref:`insert` command.
   
The following table describes the identity parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``start_with``
     - A value that is used for the very first row loaded into the table.
   * - ``increment_by``
     - Incremental value that is added to the identity value of the previous row that was loaded.

Examples
===========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Creating a Standard Table
-----------------
The following is an example of the syntax used to create a standard table:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name text(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL
   );

Creating a Table with Default Value Constraints for Some Columns
---------------------------------------------------
The following is an example of the syntax used to create a table with default value constraints for some columns:


.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name text(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL DEFAULT false NOT NULL
   );

.. note:: The nullable/non-nullable constraint appears at the end, after the default option

Creating a Table with an Identity Column
---------------------------------------------------
The following is an example of the syntax used to create a table with an identity (auto-increment) column:


.. code-block:: postgres

   CREATE TABLE users (
      id BIGINT IDENTITY(0,1) NOT NULL , -- Start with 0, increment by 1
      name TEXT(30) NOT NULL,
      country TEXT(30) DEFAULT 'Unknown' NOT NULL
   );

.. note:: 
   * Identity columns are supported on ``BIGINT`` columns.
   
   * Identity does not enforce the uniqueness of values. The identity value can be bypassed by specifying it in an :ref:`insert` command.

Creating a Table from a SELECT Query
-----------------------------------------
The following is an example of the syntax used to create a table from a SELECT query:

.. code-block:: postgres
   
   CREATE TABLE users_uk AS SELECT * FROM users WHERE country = 'United Kingdom';
   
For more information on creating a new table from the results of a SELECT query, see :ref:`CREATE TABLE AS <create_table_as>`.

Creating a Table with a Clustering Key
----------------------------------------------
When data in a table is stored in a sorted order, the sorted columns are considered clustered. Good clustering can have a significant positive impact on performance.

In the following example, we expect the ``start_date`` column to be naturally clustered, as new users sign up and get a newer start date.

When the clustering key is set, if the incoming data isn’t naturally clustered, it will be clustered by SQream DB during insert or bulk load.

The following is an example of the syntax used to create a table with a clustering key:

.. code-block:: postgres

   CREATE TABLE users (
      name TEXT(30) NOT NULL,
      start_date datetime not null,
      country TEXT(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY start_date;
   
For more information on data clustering, see :ref:`data_clustering`.
   
Duplicating the Column Structure of an Existing Table
-----------------

Syntax
************
The following is the correct syntax for duplicating the column structure of an existing table:

.. code-block:: postgres

   CREATE [OR REPLACE] TABLE table_name
   {
     (column_name column_type [{NULL | NOT NULL}] [,...])
     | LIKE source_table_name
   }
   [CLUSTER BY ...]
   ;

Examples
**************
This section includes the following examples of duplicating the column structure of an existing table using the ``LIKE`` clause:

.. contents:: 
   :local:
   :depth: 3

Creating a Table Using an Explicit Column List
~~~~~~~~~~~~
The following is an example of creating a table using an explict column list:

.. code-block:: postgres

   CREATE TABLE t1(x int default 0 not null, y text(10) null);
   
Creating a Second Table Based on the Structure of Another Table
~~~~~~~~~~~~
Either of the following examples can be used to create a second table based on the structure of another table.

**Example 1**

.. code-block:: postgres

   CREATE TABLE t2 LIKE t1;

**Example 2**

.. code-block:: postgres

   CREATE TABLE t2(x int default 0 not null, y text(10) null);
   
The generated output of both of the statements above is identical.
   
Creating a Table based on Foreign Tables and Views
~~~~~~~~~~~~
The following is example of creating a table based on foreign tables and views:


.. code-block:: postgres

   CREATE VIEW v as SELECT x+1,y,y || 'abc' from t1;
   CREATE TABLE t3 LIKE v;

When duplicating the column structure of an existing table, the target table of the ``LIKE`` clause can be a regular or an external table, or a view.

The following table describes the properties that must be copied from the target table:

+-----------------------------+------------------+---------------------------------+---------------------------------+
| **Property**                | **Native Table** | **External Table**              | **View**                        |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Column names                | Must be copied   | Must be copied                  | Must be copied                  |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Column types                | Must be copied   | Must be copied                  | Must be copied                  |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| ``NULL``/``NOT NULL``       | Must be copied   | Must be copied                  | Must be copied                  |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| ``text`` length constraints | Must be copied   | Must be copied                  | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Compression specification   | Must be copied   | Does not exist in source object | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Default/identity            | Must be copied   | Does not exist in source object | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+

Permissions
=============
The role must have the ``CREATE`` permission at the schema level.