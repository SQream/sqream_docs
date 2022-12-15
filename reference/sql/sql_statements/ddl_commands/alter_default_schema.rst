.. _alter_default_schema:

**********************
ALTER DEFAULT SCHEMA
**********************

The ``ALTER DEFAULT SCHEMA`` command can be used to change a role's default schema. The default schema in SQream is ``public``.

For more information, see :ref:`create_schema` and :ref:`drop_schema`. 



Syntax
==========
The following is the correct syntax for altering a default schema:

.. code-block:: postgres

   alter_default_schema_statement ::=
       ALTER DEFAULT SCHEMA FOR role_name TO schema_name
       ;

   role_name ::= identifier
   
   schema_name ::= identifier 



Parameters
============
The following parameters can be used when altering a default schema:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role the change will apply to.
   * - ``schema_name``
     - The new default schema name.
	 
Permissions
=============
To alter user default schema, the current role must have a ``superuser`` permission.

Examples
===========
This section includes an example of **altering the default schema for a role**:

.. code-block:: postgres

   SELECT * FROM users; -- Refers to public.users
   
   ALTER DEFAULT SCHEMA FOR bgilfoyle TO staging;
   
   SELECT * FROM users; -- Now refers to staging.users, rather than public.users
