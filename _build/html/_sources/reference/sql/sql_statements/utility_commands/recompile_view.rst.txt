.. _recompile_view:

*****************
RECOMPILE_VIEW
*****************

``RECOMPILE_VIEW(<view name>)`` is a function that can recreate a view that has been invalidated due to a schema change.

Permissions
=============
The role must have the ``DDL`` permission at the database level, as well as ``SELECT`` permissions for any tables referenced by the view.

Syntax
==========

.. code-block:: postgres

   recompile_view_statement ::=
       SELECT RECOMPILE_VIEW('[schema_name].view_name')
       ;

   schema_name ::= identifier  

   view_name ::= identifier  


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema the view is in.
   * - ``view_name``
     - The name of the view.

Examples
===========

Recreating a view that has been invalidated
---------------------------------------------

.. code-block:: psql

   farm=> SELECT * FROM agressive_animals;
   View 'public.agressive_animals' is invalid since it references a table that has been dropped/altered. The probable candidates are: [ "public.cool_animals" ]

   farm=> SELECT recompile_view('only_agressive_animals');
   executed
