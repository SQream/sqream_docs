.. _create_table_as:

*****************
CREATE TABLE AS
*****************
 
The ``CREATE TABLE AS`` commands creates a new table from the result of a select query.


Syntax
==========
The following is the correct syntax for creating a table from the result of a select query:


..     CREATE [ OR REPLACE ] TABLE [schema_name].table_name (
..         { column_def [, ...] }
..     ) AS query

.. code-block:: postgres

   create_table_statement ::=
       CREATE [ OR REPLACE ] TABLE [schema_name].table_name AS query
       ;

   schema_name ::= identifier  

   table_name ::= identifier  


.. _ctas_params:

Parameters
============
The following parameters can be used when creating a table from the result of a select query:

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

Permissions
=============
The role must have the ``CREATE`` permission at the schema level, as well as ``SELECT`` permissions for any tables referenced by the statement.


Examples
===========
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

.. warning:: The ``SELECT`` statement decrypts information by default. When executing ``CREATE TABLE AS SELECT``, encrypted information will appear as clear text in the newly created table.

Creating a Copy of a Foreign Table or View
---------------------------------------------------------------------------

.. code-block:: postgres
   
   CREATE TABLE users AS SELECT * FROM users_source;
   
For more information, see :ref:`CREATE FOREIGN TABLE <create_foreign_table>`.

Filtering
------------

.. code-block:: postgres
   
   CREATE TABLE users_uk AS SELECT * FROM users WHERE country = 'United Kingdom';

Adding Columns
-----------------------

.. code-block:: postgres
   
   CREATE TABLE users_uk_new AS SELECT GETDATE() as "Date",*,false as is_new FROM users_uk;

Creating a Table From Values
-----------------------------------------

.. code-block:: postgres
   
   CREATE TABLE new_users 
     AS VALUES(GETDATE(),'Richard','Foxworthy','1984-03-03',True)
