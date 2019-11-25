.. _truncate:

**********************
TRUNCATE
**********************

``TRUNCATE`` removes all rows from a table.

It is functionally identical to running a ``DELETE`` statement without a ``WHERE`` clause.

Privileges
=============

The role must have the ``DELETE`` permission at the table level.

Synopsis
==========

.. code-block:: postgres

   truncate_table_statement ::=
       TRUNCATE [ TABLE ] [schema_name.]table_name
       ;

   table_name ::= identifier
   
   schema_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema for the table.
   * - ``table_name``
     - The name of the table to truncate.

Examples
===========

Truncating a table
---------------------------------------------

.. code-block:: psql

   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
   farm=> TRUNCATE TABLE cool_animals;
   executed
   
   farm=> SELECT * FROM cool_animals;
   
   0 rows