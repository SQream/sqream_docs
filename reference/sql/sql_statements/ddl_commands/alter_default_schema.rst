.. _alter_default_schema:

**********************
ALTER DEFAULT SCHEMA
**********************

``ALTER DEFAULT SCHEMA`` can be used to change a role's default schema.

The default schema in SQream DB is ``public``.

Permissions
=============

No special permissions are required

Syntax
==========

.. code-block:: postgres

   alter_default_schema_statement ::=
       ALTER DEFAULT SCHEMA FOR role_name TO schema_name
       ;

   role_name ::= identifier
   
   schema_name ::= identifier 



Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role the change will apply to.
   * - ``schema_name``
     - The new default schema name.

Examples
===========

Altering the default schema for a role
-----------------------------------------

.. code-block:: postgres

   SELECT * FROM users; -- Refers to public.users
   
   ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
   SELECT * FROM users; -- Now refers to staging.users, rather than public.users
