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

.. code-block:: sql

	DROP DATABASE database_name

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

Dropping a database and all of its objects:

.. code-block:: sql

	DROP DATABASE raviga;