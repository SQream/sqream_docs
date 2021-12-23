.. _create_table:

*****************
CREATE TABLE
*****************
The ``CREATE TABLE`` command creates a new table in an existing database.

.. tip:: 
   * To create a table based on the result of a select query, see :ref:`CREATE TABLE AS <create_table_as>`.
   * To create a table based on files like Parquet and ORC, see :ref:`CREATE FOREIGN TABLE <create_foreign_table>`

Overview
---------
The **CREATE TABLE** page describes the following:

.. contents:: 
   :local:
   :depth: 1

CREATE_TABLE Syntax
==========
The following is the corrext syntax for CREATE_TABLE:

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
The following table shows the CREATE_TABLE parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Create a new table, and overwrite any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name.
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``CLUSTER BY column_name1 ...``
     - 
         A commma separated list of clustering column keys.
         
         See :ref:`data_clustering` for more information.

.. _default_values:

Default Values
===============
This section describes the CREATE_TABLE default values.
The ``DEFAULT`` value constraint specifies a value to use if a value isn't defined in an :ref:`insert` or :ref:`copy_from` statement. The value may be either a literal or `GETDATE()`, which is s evaluated at the time the row is created.

.. note:: The ``DEFAULT`` constraint only applies if the column does not have a value specified in the :ref:`insert` or :ref:`copy_from` statement. You can still insert a ``NULL`` into an nullable column by explicitly inserting ``NULL``. For example, ``INSERT INTO cool_animals VALUES (1, 'Gnu', NULL)``.

CREATE_DEFAULT_VALUES Syntax
~~~~~~~~~~~~~
The following is the correct syntax for DEFAULT_VALUES:

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

Generating Key Values with Identity Columns
~~~~~~~~~~~~~
You can use **identity columns** for generating key values. Some databases call this ``AUTOINCREMENT``.

The identity property on a column guarantees that each new row inserted is generated based on the current seed and increment.

.. warning:: 
   The identity property on a column does not guarantee uniqueness. The identity value can be bypassed by specifying it in an :ref:`insert` command.

Parameters
============
The following table shows the CREATE_TABLE parameters:

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
   
Creating a Simple Table
-----------------
The following example shows how to create a simple table:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name varchar(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL
   );

Creating a Table with Default Values for Some Columns
---------------------------------------------------
The following example shows how to create a table with default values for some columns:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name varchar(30) NOT NULL,
      weight FLOAT,
      is_agressive BOOL DEFAULT false NOT NULL
   );

.. note:: The nullable/non-nullable constraint appears at the end, after the default option

Creting a Table with an Identity (Autoincrement) Column
---------------------------------------------------
The following table shows how to create a table with an identity (autoincrement) column:

.. code-block:: postgres

   CREATE TABLE users (
      id BIGINT IDENTITY(0,1) NOT NULL , -- Start with 0, increment by 1
      name VARCHAR(30) NOT NULL,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   );

.. note:: 
   * Identity columns are supported on ``BIGINT`` columns.
   
   * Identity does not enforce the uniqueness of values. The identity value can be bypassed by specifying it in an :ref:`insert` command.

Creating a Table from a SELECT Query
-----------------------------------------
The following example shows how to create a table from a SELECT query:

.. code-block:: postgres
   
   CREATE TABLE users_uk AS SELECT * FROM users WHERE country = 'United Kingdom';
   
You can use a :ref:`CREATE TABLE AS <create_table_as>` statement to create a new table from the results of a SELECT query.

Creating a Table with a Clustering Key
----------------------------------------------
When data in a table is stored in a sorted order, the sorted columns are considered clustered. Good clustering can have a significant positive impact on performance.

In the following example, we expect the ``start_date`` column to be naturally clustered, as new users sign up and get a newer start date.

When the clustering key is set, if the incoming data isn’t naturally clustered, it will be clustered by SQream DB during insert or bulk load.

The following example shows how to create a table with a clustering key:

.. code-block:: postgres

   CREATE TABLE users (
      name VARCHAR(30) NOT NULL,
      start_date datetime not null,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY start_date;

For more information, see :ref:`data_clustering`.

Permissions
=============
The role must have the ``CREATE`` permission at the schema level.