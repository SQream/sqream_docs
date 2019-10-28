.. _sqream_sql:

***************************
Quick guide to SQream SQL
***************************

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

.. tip:: * To exit the shell, type ``\q``  or :kbd:`Ctrl-d`. 
   * A new SQream DB cluster contains a database named `master`. We will start with this database.

.. code-block:: psql

   $ ClientCmd --port=5000 --username=rhendricks -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

To create a table, we will use the :ref:`CREATE TABLE <create_table>` syntax, with a table name and some :ref:`column specifications <column_specs>`.

For example,

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20) NOT NULL,
      weight INT NOT NULL
   );

.. tip:: Statements and queries are standard SQL, followed by a semicolon (``;``).

If the table already exists and you want to drop the current table and create a new one, you can add ``OR REPLACE`` after the ``CREATE`` keyword.

.. code-block:: postgres

   CREATE OR REPLACE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20) NOT NULL,
      weight INT NOT NULL
   );


You can ask SQream DB to list the full, verbose ``CREATE TABLE`` statement for any table, by using the :ref:`GET_DDL <get_ddl>` function, with the table name.

.. code-block:: psql

   master=> SELECT GET_DDL('cool_animals');
   
