.. _creating_your_first_table:

****************************
Creating Your First Table
****************************

Creating a Table

The ``CREATE TABLE`` syntax is used to create your first table. This table includes a table name and column specifications, as shown in the following example:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name TEXT,
      weight INT
   );

For more information on creating a table, see :ref:`create_table`.


Replacing a Table
-----------------

You can drop an existing table and create a new one by adding the ``OR REPLACE`` parameter after the ``CREATE`` keyword, as shown in the following example:

.. code-block:: postgres

   CREATE OR REPLACE TABLE cool_animals (
      id INT NOT NULL,
      name TEXT,
      weight INT
   );


Listing a CREATE TABLE Statement
--------------------------------

You can list the full, verbose ``CREATE TABLE`` statement for a table by using the **GET DDL** function with the table name as shown in the following example:

.. code-block:: psql

   test=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
   "id" int not null,
   "name" text,
   "weight" int
   );

.. note:: 

   * SQream DB identifier names such as table names and column names are not case sensitive. SQream DB lowercases all identifiers bu default. If you want to maintain case, enclose the identifiers with double-quotes.
   * SQream DB places all tables in the `public` schema, unless another schema is created and specified as part of the table name.
   
For information on listing a ``CREATE TABLE`` statement, see :ref:`get_ddl`.

Dropping a Table
----------------

When you have finished working with your table, you can drop the table to remove it table and its content, as shown in the following example:

.. code-block:: psql

   test=> DROP TABLE cool_animals;
   
   executed
   
For more information on dropping tables, see :ref:`drop_table`.