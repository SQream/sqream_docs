.. _get_statement_permissions:

****************************
GET_STATEMENT_PERMISSIONS
****************************

``GET_STATEMENT_PERMISSIONS`` analyzes an SQL statement and returns a list of permissions required to execute it.

Use this function to understand the permissions required, before :ref:`granting<grant>` them to a specific role.

See also :ref:`grant`, :ref:`create_role`.

Permissions
=============

No special permissions are required to run ``GET_STATEMENT_PERMISSIONS``.

Syntax
==========

.. code-block:: postgres

   get_statement_permissions_statement ::=
       SELECT GET_STATEMENT_PERMISSIONS(query_stmt)
       ;
   

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``query_stmt``
     - The statement to analyze


Returns
=========

This utility returns details of the required permissions to run the statement.

If the statement requires no special permissions, the utility returns an empty result set.

.. list-table:: Result columns
   :widths: auto
   :header-rows: 1
   
   * - ``permission_type``
     - The permission type required
   * - ``object_type``
     - The object on which the permission is required
   * - ``object_name``
     - The object name

.. include:: grant.rst
   :start-line: 123
   :end-line: 174

Examples
===========

Getting permission details for a simple statement
----------------------------------------------------

.. code-block:: psql
   
   t=> SELECT GET_STATEMENT_PERMISSIONS('SELECT * from nba');
   permission_type | object_type | object_name
   ----------------+-------------+-------------------
   SELECT          | table       | master.public.nba
   USAGE           | schema      | master.public

Getting permission details for a DDL statement
----------------------------------------------------

.. tip:: Use dollar quoting (``$$``) to avoid escaping a statement

.. code-block:: psql
   
   t=> SELECT GET_STATEMENT_PERMISSIONS($$ALTER TABLE nba RENAME COLUMN "Weight" TO "Mass"$$);
   permission_type | object_type | object_name
   ----------------+-------------+-------------------
   DDL             | table       | master.public.nba
   USAGE           | schema      | master.public
