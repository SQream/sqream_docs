.. _create_database:

*****************
CREATE DATABASE
*****************
The ``CREATE DATABASE`` command creates a new database in SQream.

Overview
---------
The **CREATE DATABASE** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Syntax
==========
The following is the correct syntax for the CREATE DATABASE command:

.. code-block:: postgres

   create_database_statement ::=

       CREATE DATABASE database_name ;

   database_name ::= identifier

Parameters
============
The following table shows the CREATE DATABASE parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The name of the database name. The database name must be unique, and follows :ref:`Identifier rules <identifiers>`
     
Example
===========
The following example shows how to use CREATE DATABASE:

.. code-block:: postgres

   CREATE DATABASE raviga;

.. code-block:: postgres

   CREATE DATABASE my_db;

If the database already exists, an error will be displayed:

.. code-block:: psql
  
  master=> CREATE DATABASE MY_DB;
  Database 'my_db' already exists

.. note:: SQream :ref:`identifiers <identifiers>` are always converted to lowercase, so ``my_db`` is the same as ``MY_DB``, unless explicitly quoted as ``"MY_DB"``.

Permissions
=============
Only roles with superuser permissions can create a new database.