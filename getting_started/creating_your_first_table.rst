.. _creating_your_first_table:

****************************
Creating Your First Table
****************************
The **Creating Your First Table** section describes the following:

* :ref:`Creating a table<creating_a_table>`
* :ref:`Replacing a table<replacing_a_table>`
* :ref:`Listing a CREATE TABLE statement<listing_a_create_table_statement>`
* :ref:`Dropping a table<dropping_a_table>`


.. _creating_a_table:

**Creating a Table**

The ``CREATE TABLE`` syntax is used to create your first table. This table includes a table name and column specifications, as shown in the following example:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );

For more information on creating a table, see :ref:`create_table`.

.. _replacing_a_table:

**Replacing a Table**

You can drop an existing table and create a new one by adding the ``OR REPLACE`` parameter after the ``CREATE`` keyword, as shown in the following example:

.. code-block:: postgres

   CREATE OR REPLACE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );

.. TODO: cool_animals? I think we need to decide if the customer for this documenation is 12 years old, or an IT professional.
.. _listing_a_create_table_statement:

**Listing a CREATE TABLE Statement**

You can list the full, verbose ``CREATE TABLE`` statement for a table by using the **GET DDL** function with the table name as shown in the following example:

.. code-block:: psql

   test=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
   "id" int not null,
   "name" varchar(20),
   "weight" int
   );

.. note:: 

   * SQream DB identifier names such as table names and column names are not case sensitive. SQream DB lowercases all identifiers bu default. If you want to maintain case, enclose the identifiers with double-quotes.
   * SQream DB places all tables in the `public` schema, unless another schema is created and specified as part of the table name.

For information on listing a ``CREATE TABLE`` statement, see :ref:`get_ddl`.

.. _dropping_a_table:

**Dropping a Table**

When you have finished working with your table, you can drop the table to remove it table and its content, as shown in the following example:

.. code-block:: psql

   test=> DROP TABLE cool_animals;

   executed
   
For more information on dropping tables, see :ref:`drop_table`.
