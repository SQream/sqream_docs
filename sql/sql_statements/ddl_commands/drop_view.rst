.. _drop_view:

**********************
DROP VIEW
**********************

``DROP VIEW`` can be used to remove a view.

Because a view is logical, this does not affect any data in any of the referenced tables.

Permissions
=============

The role must have the ``DDL`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   drop_view_statement ::=
       DROP VIEW [ IF EXISTS ] [schema_name.]view_name
       ;

   view_name ::= identifier
   
   schema_name ::= identifier



Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``IF EXISTS``
     - Drop the view if it exists. Does not error if the view does not exist.
   * - ``schema_name``
     - The name of the schema from which to drop the view.
   * - ``view_name``
     - The name of the view to drop.

Examples
===========

Dropping a table
---------------------------------------------

.. code-block:: postgres

   DROP VIEW angry_animals;


Dropping a view (always succeeds)
-------------------------------------

.. code-block:: psql

   farm=> DROP VIEW angry_animals;
   executed
   
   farm=> DROP VIEW angry_animals;
   View 'public.angry_animals' not found
   
   -- This will succeed, even though the view does not exist
   farm=> DROP VIEW IF EXISTS angry_animals;
   executed
   
