:orphan:

.. _use_schema:

**********
USE SCHEMA
**********

The ``USE SCHEMA`` command lets you shift between schemes within an existing session. If the ``schema`` argument is ``null``, ``USE SCHEMA`` uses the current schema and switches to the defined schema.

Syntax
======

.. code-block:: postgres

   USE SCHEMA <schema_name>
   
You can **combine** USE commands as shown in the following examples:

.. code-block:: postgres
   
   USE DATABASE <db_name> SCHEMA <schema_name>
  
.. code-block:: postgres
 
   USE SCHEMA <schema_name> DATABASE <db_name>
  
The compiler executes both of the above commands in the same order regardless of how you write them, switching the database first and the schema second.

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema.
     
Examples
========

.. code-block:: postgres

   USE SCHEMA customers;
   
.. code-block:: postgres
   
   USE DATABASE master SCHEMA customers;

Permissions
===========

The ``USE SCHEMA`` command requires **Comment** permission. 