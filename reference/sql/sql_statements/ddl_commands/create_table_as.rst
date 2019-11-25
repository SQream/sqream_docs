.. _create_table_as:

*****************
CREATE TABLE AS
*****************

``CREATE TABLE AS`` creates a new table from the result of a select query.

Privileges
=============
The role must have the ``CREATE`` permission at the schema level, as well as ``SELECT`` privileges for any tables referenced by the statement.

Synopsis
==========

..     CREATE [ OR REPLACE ] TABLE [schema_name].table_name (
..         { column_def [, ...] }
..     ) AS query

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] TABLE [schema_name].table_name AS query
       ;

   schema_name ::= identifier  

   table_name ::= identifier  

..   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

..   column_name ::= identifier
   
..   column_constraint ::=
..       { NOT NULL | NULL }
   
..   default ::=
   
..       DEFAULT default_value
..       | IDENTITY [ ( start_with [ , increment_by ] ) ]


Parameters
============

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
   * - ``query``
     - A select query that returns data

..    * - ``column_def``
..     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.

Examples
===========

Create a copy of an :ref:`external table <create_external_table>` or view
---------------------------------------------------------------------------

.. code-block:: postgres
   
   CREATE TABLE users AS SELECT * FROM users_source;

Filtering
------------

.. code-block:: postgres
   
   CREATE TABLE users_uk AS SELECT * FROM users WHERE country = 'United Kingdom';

Adding columns
-----------------------

.. code-block:: postgres
   
   CREATE TABLE users_uk_new AS SELECT GETDATE() as "Date",*,false as is_new FROM users_uk;

Creating a table from values
-----------------------------------------

.. code-block:: postgres
   
   CREATE TABLE new_users 
     AS VALUES(GETDATE(),'Richard','Foxworthy','1984-03-03',True)
