:orphan:

.. _create_table_as:

***************
CREATE TABLE AS
***************
 
The ``CREATE TABLE AS`` commands creates a new table from the result of a ``SELECT`` query.

Syntax
======

.. code-block:: postgres

   CREATE [ OR REPLACE ] TABLE [ "<schema_name>". ] "<table_name>" AS < query >;

.. _ctas_params:

Parameters
==========

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
     - A ``SELECT`` query that returns data

Examples
========

The ``SELECT`` statement decrypts information by default. When executing ``CREATE TABLE AS SELECT``, encrypted information will appear as clear text in the newly created table.

Creating a Copy of a Foreign Table or View
------------------------------------------

.. code-block:: postgres
   
   CREATE TABLE
     users AS
   SELECT
     *
   FROM
     users_source;
   
For more information, see :ref:`CREATE FOREIGN TABLE <create_foreign_table>`.

Filtering
---------

.. code-block:: postgres
   
   CREATE TABLE
     users_uk AS
   SELECT
     *
   FROM
     users
   WHERE
     country = 'United Kingdom';

Adding Columns
--------------

.. code-block:: postgres
   
   CREATE TABLE
     users_uk_new AS
   SELECT
     GETDATE() AS "Date",
     *,
     false AS is_new
   FROM
     users_uk;

Creating a Table From Values
----------------------------

.. code-block:: postgres
   
   CREATE TABLE
     new_users AS
   VALUES
   (
       GETDATE(),
       'Richard',
       'Foxworthy',
       '1984-03-03',
       True
     );

Permissions
===========

The role must have the ``CREATE`` permission at the schema level, as well as ``SELECT`` permissions for any tables referenced by the statement.