:orphan:

.. _create_table:

************
CREATE TABLE
************

The ``CREATE TABLE`` statement is used to create a new table in an existing database.

.. tip:: 
   * To create a table based on the result of a select query, see :ref:`CREATE TABLE AS <create_table_as>`.
   * To create a table based on files like Parquet and ORC, see :ref:`CREATE FOREIGN TABLE <create_foreign_table>`   

Syntax
======

.. code-block:: postgres

   CREATE [ OR REPLACE ] TABLE [ "<schema_name>". ]"<table_name>"
    {
     ( <column_def> [, ...] [ { NULL | NOT NULL } ]
      | LIKE "<source_table_name>" [ INCLUDE PERMISSIONS ] )
    } 
    |  [ CLUSTER BY "<column_name>" [, ...] ]

      -- column_def: 
      { "<column_name>" <type_name> [ DEFAULT ] [ <column_constraint> ] }
        
         -- column_constraint:
         { NOT NULL | NULL }

         -- DEFAULT:
         DEFAULT <default_value>
         | IDENTITY [ ( <start_with> [ , increment_by ] ) ] [ check_specification ]
         | check_specification [ IDENTITY [ ( start_with [ , increment_by ] ) ] 

            -- start_with: A value that is used for the very first row loaded into the table.
            -- increment_by: Incremental value that is added to the identity value of the previous row that was loaded.

            -- check_specification:
            CHECK( 'CS compression_spec' )
               
            -- compression_spec:
            { "default" | "p4d" | "dict" | "rle" | "sequence" | "flat" }

Parameters
==========

The following parameters can be used when creating a table:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``OR REPLACE``
     - Creates a new table and overwrites any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check table contents or structure, only the table name.
   * - ``schema_name``
     - The name of the schema in which to create the table.
   * - ``table_name``
     - The name of the table to create, which must be unique inside the schema.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``CLUSTER BY column_name1 ...``
     - 
         A comma separated list of clustering column keys.
         
         See :ref:`cluster_by` for more information.
   * - ``LIKE``
     - Duplicates the column structure of an existing table. The newly created table is granted default ``CREATE TABLE`` permissions: ``SELECT``, ``INSERT``, ``DELETE``, ``DDL``, and ``UPDATE``
   * - ``INCLUDE PERMISSIONS``
     - In addition to the default CREATE TABLE permissions (``SELECT``, ``INSERT``, ``DELETE``, ``DDL``, and ``UPDATE``), the newly created table is granted the source table existing permissions

.. _identity:

Usage Notes
===========

.. glossary::

   ``CREATE TABLE... LIKE``

      When using ``CREATE TABLE... LIKE``, the permissions from the source table are inherited by the newly created table. To add extra permissions to the new table, you can utilize the ``INCLUDE PERMISSIONS`` clause.

   ``DEFAULT``

      The ``DEFAULT`` value constraint specifies a default value to use if none is provided in an :ref:`insert` or :ref:`copy_from` statement. This value can be a literal or ``NULL``. It's worth noting that even for nullable columns, you can still explicitly insert a ``NULL`` value using the ``NULL`` keyword, as demonstrated in the example:

      .. code-block:: postgres

         INSERT INTO
           cool_animals
         VALUES
           (1, 'Gnu', NULL); 

   Identity
      Identity (or sequence) columns in a database table serve as a mechanism for generating unique key values automatically. The identity property ensures that each new row inserted into the table is assigned a value based on the current seed and increment specified for the column.

      .. warning:: 
         The identity property on a column does not guarantee uniqueness. The identity value can be bypassed by specifying it in an :ref:`insert` command.
   
Examples
========

Creating a Standard Table
--------------------------

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name text NOT NULL,
      weight FLOAT,
      is_agressive BOOL
   );

Creating a Table with Default Value Constraints for Some Columns
----------------------------------------------------------------

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name TEXT NOT NULL,
      weight FLOAT,
      is_agressive BOOL DEFAULT false NOT NULL
   );

   -- The nullable/non-nullable constraint appears at the end, after the default option.

Creating a Table with an Identity Column
----------------------------------------

Identity does not enforce the uniqueness of values. The identity value can be bypassed by specifying it in an :ref:`insert` command.

.. code-block:: postgres

   CREATE TABLE users (
      id BIGINT IDENTITY(0,1) NOT NULL , -- Start with 0, increment by 1
      name TEXT NOT NULL,
      country TEXT DEFAULT 'Unknown' NOT NULL
   );

Creating a Table from a ``SELECT`` Query
----------------------------------------

.. code-block:: postgres
   
	CREATE TABLE
	  users_uk AS
	SELECT
	  *
	FROM
	  users
	WHERE
	  country = 'United Kingdom';

For more information on creating a new table from the results of a ``SELECT`` query, see :ref:`CREATE TABLE AS <create_table_as>`.

Creating a Table with a Clustering Key
--------------------------------------

When data within a table is organized in a sorted manner, the columns responsible for this sorting are termed as clustered. Effective clustering can greatly enhance performance. For instance, in the scenario provided, the ``start_date`` column is anticipated to naturally cluster due to the continuous influx of new users and their corresponding start dates. However, in cases where the clustering of incoming data isn't inherent, BLUE will automatically cluster it during insertion or bulk loading processes once the clustering key is set.

.. code-block:: postgres

   CREATE TABLE users (
      name TEXT NOT NULL,
      start_date DATETIME not null,
      country TEXT DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY start_date;
   
For more information on data clustering, see :ref:`cluster_by`.
   
Duplicating the Column Structure of an Existing Table
-----------------------------------------------------

Syntax
^^^^^^

.. code-block:: postgres

   CREATE [OR REPLACE] TABLE "<table_name>"
   {
     ( "<column_name>"" <column_type> [{NULL | NOT NULL}] [,...])
     | LIKE "<source_table_name>" [INCLUDE PERMISSIONS]
   }
   [CLUSTER BY ...]

Examples
^^^^^^^^

This section includes examples of duplicating the column structure of an existing table using the ``LIKE`` clause:

Creating a Table Using an Explicit Column List
""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: postgres

   CREATE TABLE t1 (
      x INT DEFAULT 0 NOT NULL,
      y TEXT NULL
   );
   
Creating a Second Table Based on the Structure of Another Table
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Either of the following examples can be used to create a second table based on the structure of another table.

**Example 1**

.. code-block:: postgres

   CREATE TABLE t2 
   LIKE t1
   ;

**Example 2**

.. code-block:: postgres

   CREATE TABLE t2 (
      x INT DEFAULT 0 NOT NULL,
      y TEXT NULL
   );
   
The generated output of both of the statements above is identical.
   
Creating a Table based on Foreign Tables and Views
""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: postgres

   CREATE VIEW v
   AS
     SELECT x + 1,
            y,
            y
            || 'abc'
     FROM   t1;
   
   
   CREATE TABLE t3 LIKE v;

When duplicating the column structure of an existing table, the target table of the ``LIKE`` clause can be either a native, a regular or an external table, or a view.

The following table describes which properties are copied from the target table to the newly created table:

+-----------------------------+------------------+---------------------------------+---------------------------------+
| **Property**                | **Native Table** | **External Table**              | **View**                        |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Column names                | Copied           | Copied                          | Copied                          |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Column types                | Copied           | Copied                          | Copied                          |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| ``NULL``/``NOT NULL``       | Copied           | Copied                          | Copied                          |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| ``text`` length constraints | Copied           | Copied                          | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Compression specification   | Copied           | Does not exist in source object | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+
| Default/identity            | Copied           | Does not exist in source object | Does not exist in source object |
+-----------------------------+------------------+---------------------------------+---------------------------------+

Permissions
===========

``CREATE TABLE`` requires ``CREATE`` permission at the schema level.