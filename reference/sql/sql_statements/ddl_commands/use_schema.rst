.. _use_schema:

*****************
USE SCHEMA
*****************
The ``USE SCHEMA`` command lets you switch your schema. If the ``db_name`` argument is ``null``, ``USE SCHEMA`` uses the current database and switches to the defined schema.

**Comment** - *Please confirm/correct the description above.*

Syntax
==========
The following is the correct syntax for switching schemas:

.. code-block:: postgres

   USE SCHEMA <schema_name>
   
You can **combine** USE commands as shown in the following examples:

.. code-block:: postgres
   
   USE DATABASE <db_name> SCHEMA <schema_name>
  
.. code-block:: postgres
 
   USE SCHEMA <schema_name> DATABASE <db_name>
  
The compiler executes both of the above commands in the same order regardless of how you write them, switching the database first and the schema second.

Parameters
============
The following parameter can be used when switching databases with the **USE SCHEMA** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema.
     
Examples
===========
The following are examples of the **USE SCHEMA** command:

.. code-block:: postgres

   USE SCHEMA <customers>
   
.. code-block:: postgres
   
   USE DATABASE <master> SCHEMA <customers>

Permissions
=============
**Comment** - *What are the permissions?*