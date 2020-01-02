.. _drop_database:

**********************
DROP DATABASE
**********************

``DROP DATABASE`` can be used to remove a database and all of its objects.

Permissions
=============

The role must have the ``DDL`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   drop_database_statement ::=
       DROP DATABASE database_name
       ;

   database_name ::= identifier



Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``database_name``
     - The name of the database to drop. This can not be the current database in use.

Examples
===========

Dropping a database and all of its objects
---------------------------------------------

.. code-block:: psql

   master=> DROP DATABASE raviga;
   executed


Dropping the current database
--------------------------------

The current database in use can't be dropped. Switch to another database first.

.. code-block:: psql

   raviga=> DROP DATABASE raviga;
   Current open database 'raviga' cannot be dropped.
   
   raviga=> \c master
   master=> DROP DATABASE raviga;
   executed