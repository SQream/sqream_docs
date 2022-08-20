.. _create_view:

*****************
CREATE VIEW
*****************

``CREATE VIEW`` creates a new view in an existing database. A view is a virtual table.

.. tip:: 
   * Use views to simplify complex queries or present only partial data to specific roles.
   * If an underlying table has changed (new columns, changed names, etc.) - a view may be invalidated. To recompile the view, see :ref:`SELECT RECOMPILE_VIEW(\<view name>)<recompile_view>`


Permissions
=============

The role must have the ``CREATE`` permission at the database level, as well as ``SELECT`` permissions for any tables referenced by the view.

Syntax
==========

.. code-block:: postgres

   create_view_statement ::=
       CREATE VIEW [schema_name].view_name [ column_list ]
       AS
       query
       ;

   schema_name ::= identifier  

   view_name ::= identifier  

   column_list ::= ( { column_name [, ...] } )

   column_name ::= identifier
   

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema in which to create the view.
   * - ``view_name``
     - The name of the view to create, which must be unique inside the schema.
   * - ``column_list``
     - An optional comma separated list of column names for the view. If specified, these column names will override the column names in the response of the query in the ``AS query`` statement.
   * - ``AS query``
     - The select query to execute when the view is referenced.

.. * - ``OR REPLACE``
..   - Create a new view, and overwrite any existing views by the same name. Does not return an error if the view already exists.

Examples
===========

A simple view
-----------------

.. code-block:: postgres

   CREATE VIEW only_agressive_animals AS
     SELECT * FROM cool_animals WHERE is_agressive=true;
    
   SELECT * FROM only_agressive_animals;

Overriding default column names
---------------------------------

.. code-block:: postgres

   CREATE VIEW only_relaxed_animals (animal_id, animal_name, should_i_worry) AS
     SELECT id, name, is_agressive FROM cool_animals WHERE is_agressive=false;
