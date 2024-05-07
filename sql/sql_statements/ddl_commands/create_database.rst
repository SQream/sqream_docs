:orphan:

.. _create_database:

*****************
CREATE DATABASE
*****************

``CREATE DATABASE`` creates a new database in BLUE

Permissions
=============

Only a superuser can create a new database

Syntax
==========

.. code-block:: postgres

   create_database_statement ::=

       CREATE DATABASE database_name ;

   database_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The name of the database name. The database name must be unique, and follows :ref:`Identifier rules <keywords_and_identifiers>`
     
Examples
===========

.. code-block:: postgres

   CREATE DATABASE raviga;

.. code-block:: postgres

   CREATE DATABASE my_db;

If the database already exists, an error will appear:

.. code-block:: psql
  
  master=> CREATE DATABASE MY_DB;
  Database 'my_db' already exists

.. note:: BLUE :ref:`identifiers <keywords_and_identifiers>` are always converted to lowercase, so ``my_db`` is the same as ``MY_DB``, unless explicitly quoted as ``"MY_DB"``.