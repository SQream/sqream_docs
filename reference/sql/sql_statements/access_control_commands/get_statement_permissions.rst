.. _get_statement_permissions:

****************************
GET_STATEMENT_PERMISSIONS
****************************

``GET_STATEMENT_PERMISSIONS`` analyzes an SQL statement and returns a list of permissions required to execute it.

Use this function to understand the permissions required, before :ref:`granting<grant>` them to a specific role.

Learn more about the permission system in the :ref:`access control guide<access_control>`.

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

The following table describes the supported permissions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Permission
     - Object
     - Description
   * - ``LOGIN``
     - Cluster
     - Login permissions (with a password) allows a role to be a user and login to a database
   * - ``PASSWORD``
     - Cluster
     - Sets the password for a user role
   * - ``CREATE FUNCTION``
     - Database
     - Allows a user to :ref:`create a Python UDF<create_function>`
   * - ``SUPERUSER``
     - Cluster, Database, Schema
     - The most privileged role, with full control over a cluster, database, or schema
   * - ``CONNECT``
     - Database
     - Allows a user to connect and use a database
   * - ``CREATE``
     - Database, Schema
     - For a role to create and manage objects, it needs the ``CREATE`` and ``USAGE`` permissions at the respective level
   * - ``USAGE``
     - Schema
     - For a role to see tables in a schema, it needs the ``USAGE`` permissions
   * - ``SELECT``
     - Table
     - Allows a user to run :ref:`select` queries on table contents
   * - ``INSERT``
     - Table
     - Allows a user to run :ref:`copy_from` and :ref:`insert` statements to load data into a table
   * - ``UPDATE``
     - Table
     - Allows a user to modify the value of certain columns in existing rows without creating a table
   * - ``DELETE``
     - Table
     - Allows a user to run :ref:`delete`, :ref:`truncate` statements to delete data from a table
   * - ``DDL``
     - Database, Schema, Table, Function
     - Allows a user to :ref:`alter tables<alter_table>`, rename columns and tables, etc.
   * - ``EXECUTE``
     - Function
     - Allows a user to execute UDFs
   * - ``ALL``
     - Cluster, Database, Schema, Table, Function
     - All of the above permissions at the respective level


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
