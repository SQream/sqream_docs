.. _truncate:

**********************
TRUNCATE_IF_EXISTS
**********************

``TRUNCATE_IF_EXISTS`` removes all rows from a table. It does not generate an error if the table does not exist.

It is functionally identical to running a ``DELETE`` statement without a ``WHERE`` clause.

Permissions
=============

The role must have the ``DELETE`` permission at the table level.

Syntax
==========

.. code-block:: postgres

   truncate_table_statement ::=
       TRUNCATE [ TABLE ] [schema_name.]table_name 
           [ RESTART IDENTITY | CONTINUE IDENTITY ]
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
   * - ``RESTART IDENTITY``
     - Automatically restart sequences owned by columns of the truncated table.
   * - ``CONTINUE IDENTITY``
     - Do not change the values of sequences. This is the default.

Examples
===========

Truncating an existing table
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
   
   farm=> SELECT TRUNCATE_IF_EXISTS('public', 'cool_animals'); 
   Status:  0 result rows
   
   farm=> SELECT * FROM cool_animals;
   
   0 rows
   

Truncating a non-existing table
---------------------------------------------
.. code-block:: psql

   farm=> SELECT * FROM cool_animals2;
   
   Status:  Ended with errorError preparing statement: At row 1, col 15: table not found public.cool_animals2
   
   farm=> SELECT TRUNCATE_IF_EXISTS('public', 'cool_animals2');
   
   Status:  0 result rows