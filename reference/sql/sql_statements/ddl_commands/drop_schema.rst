.. _drop_schema:

**********************
DROP SCHEMA
**********************
 
``DROP SCHEMA`` can be used to remove a schema.

The schema has to be empty before removal. 

SQream DB does not support dropping a schema with objects.

See also: :ref:`create_schema`, :ref:`alter_default_schema`.

Permissions
=============

The role must have the ``DDL`` permission at the database level.

Syntax
==========

.. code-block:: postgres

   drop_schema_statement ::=
       DROP SCHEMA schema_name
       ;

   schema_name ::= identifier  


Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema to drop

Examples
===========

Dropping a schema
---------------------------------------------

.. code-block:: postgres

   DROP SCHEMA test;

Dropping a schema if it's not empty
----------------------------------------------

If a schema contains several tables, SQream DB will alert you that these tables need to be dropped first.

This prevents accidental dropping of full schemas.

.. code-block:: psql
   
   t=> DROP SCHEMA test;
   Schema 'test' contains the following objects:
   Tables - 'test.foo' , 'test.bar'
   Please drop its content and then try again.
   
To drop the schema, drop the schema's tables first, and then drop the schema:

.. code-block:: psql
   
   t=> DROP TABLE test.foo;
   executed
   t=> DROP TABLE test.bar;
   executed
   t=> DROP SCHEMA test;
   executed