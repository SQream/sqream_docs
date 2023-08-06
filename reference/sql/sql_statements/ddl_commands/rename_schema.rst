.. _rename_schema:

*************
RENAME SCHEMA
*************
 
``RENAME SCHEMA`` can be used to rename a schema. 

.. warning:: Renaming a schema can void existing views that use this schema. See more about :ref:`recompiling views <recompile_view>`.

Permissions
===========

The role must have the ``DDL`` permission at the database or table level.

Syntax
======

.. code-block:: postgres

   alter_schema_rename_schema_statement ::=
       ALTER SCHEMA [database_name.]current_name RENAME TO new_name
       ;

   current_name ::= identifier
   
   database_name ::= identifier
   
   new_name ::= identifier

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The database name for the schema. Defaults to ``master`` if not specified.
   * - ``current_name``
     - The schema name to apply the change to.
   * - ``new_name``
     - The new schema name.
     
Examples
========


.. code-block:: postgres

   ALTER SCHEMA master.staging RENAME TO staging_new;


