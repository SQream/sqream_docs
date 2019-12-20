.. _getting_started:

***************
Getting started
***************

.. TODO: part one of the tutorial is how to connect with clientcmd,
.. and create some tables, insert data and query it
.. part 2: expand on this
.. how to run sqream/check it's running
.. how to add a database and do roles and permissions (to get started)
.. options for inserting data - overview of all of them
.. deleting/managing data overview (including storage reorg)

This tutorial explains the basics of SQream DB SQL.

.. contents:: In this topic:
   :local:

Preparing for this tutorial
===============================

This tutorial assumes you already have a SQream DB cluster running.

.. tip:: **SQream SQL** can be found in the ``bin`` directory of your SQream DB installation, under the name ``ClientCmd``.

Creating your first table
============================

When starting SQream SQL, after entering your password, you are presented with the SQL shell.

.. tip::
   * To exit the shell, type ``\q``  or :kbd:`Ctrl-d`. 
   * A new SQream DB cluster contains a database named `master`. We will start with this database.


.. code-block:: psql

   $ ClientCmd --port=5000 --username=rhendricks -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

To create a table, we will use the :ref:`create_table` syntax, with a table name and some column specifications.

For example,

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );

.. tip:: Statements and queries are standard SQL, followed by a semicolon (``;``).

If the table already exists and you want to drop the current table and create a new one, you can add ``OR REPLACE`` after the ``CREATE`` keyword.

.. code-block:: postgres

   CREATE OR REPLACE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );


You can ask SQream DB to list the full, verbose ``CREATE TABLE`` statement for any table, by using the :ref:`get_ddl` function, with the table name.

.. code-block:: psql

   master=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
   "id" int not null,
   "name" varchar(20),
   "weight" int
   );

.. note:
   * SQream DB identifier names such as table names and column names are not case sensitive. SQream DB lowercases all identifiers bu default. If you want to maintain case, enclose the identifiers with double-quotes.
   * SQream DB places all tables in the `public` schema, unless another schema is created and specified as part of the table name.

If you are done with this table, you can use :ref:`drop_table` to remove the table and all of its data.

.. code-block:: psql

   master=> DROP TABLE cool_animals;
   
   executed

Listing tables
=================

To see the tables in the current database, we will query the catalog

.. code-block:: psql

   master=> SELECT table_name FROM sqream_catalog.tables;
   cool_animals
   
   1 rows


Inserting rows
=================

Inserting rows into a table can be performed with the :ref:`insert` statement.
The statement includes the table name, an optional list of column names, and column values listed in the same order as the column names:

.. code-block:: psql

   master=> INSERT INTO cool_animals VALUES (1, 'Dog', 7);
   
   executed

To change the order of values, specify the column order:

.. code-block:: psql

   master=> INSERT INTO cool_animals(weight, id, name) VALUES (3, 2, 'Possum');
   
   executed

To insert multiple rows, use sets of parentheses:

.. code-block:: psql

   master=> INSERT INTO cool_animals VALUES
         (3, 'Cat', 5),
         (4, 'Elephant', 6500),
         (5, 'Rhinoceros', 2100);
   
   executed

When you leave out columns that have a :ref:`default value<default_values>` (including default ``NULL`` value) the default value is used.

.. code-block:: psql

   master=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed

.. code-block:: psql

   master=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed
   master=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

.. note:: Null row values are represented as ``\N``

Queries
=========

For querying, use the :ref:`select` keyword, followed by a list of columns and values to be returned, and the table to get the data from.

.. code-block:: psql

   master=> SELECT id, name, weight FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

To get all columns without specifying them, use the star operator ``*``:

.. code-block:: psql

   master=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

To get the number of values in a table without getting the full result set, use :ref:`COUNT(*)<count>`:

.. code-block:: psql

   master=> SELECT COUNT(*) FROM cool_animals;
   6
   
   1 row


Filter results by adding a :ref:`WHERE<where>` clause and specifying the filter condition:

.. code-block:: psql

   master=> SELECT id, name, weight FROM cool_animals WHERE weight > 1000;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   
   2 rows

Sort the results by adding an :ref:`ORDER BY<order_by>` clause, and specifying ascending (``ASC``) or descending (``DESC``) order:

.. code-block:: psql

   master=> SELECT * FROM cool_animals ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3
   6,\N,\N

   6 rows

Filter null rows by adding a filter :ref:`IS NOT NULL<is_null>`:

.. code-block:: psql

   master=> SELECT * FROM cool_animals WHERE weight IS NOT NULL ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3

   5 rows

Delete rows
=============

To delete rows in a table selectively, use the :ref:`DELETE<delete>` command, with a table name and a `WHERE` clause to specify which rows are to be deleted:

.. code-block:: psql

   master=> DELETE FROM cool_animals WHERE weight is null;
   
   executed
   master=> SELECT  * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100

   5 rows

To delete all rows in a table, use the :ref:`TRUNCATE<truncate>` command followed by the table name:

.. code-block:: psql

   master=> TRUNCATE TABLE cool_animals;
   
   executed

.. rubric:: What's next?

* Explore all of SQream DB's :ref:`SQL Syntax <sql_syntax>`
* See the full :ref:`SQream SQL CLI reference <sqream_sql_cli_reference>`
* Connect a :ref:`third party tool to SQream DB <third_party_tools>` and start analyzing data
