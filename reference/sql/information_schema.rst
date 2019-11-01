.. _information_schema:

*************************************
Information Schema (SQream catalog)
*************************************

SQream DB contains a virtual schema called ``sqream_catalog`` that contains information about your database's objects - tables, columns, views, permissions, and more.

Because the catalog is a virtual schema, it is available from any database.

Some additional catalog tables are used primarily for internal introspection, which could change across SQream DB versions.


.. contents:: In this topic:
   :local:

Types of data exposed by ``sqream_catalog``
==============================================

.. list-table:: Database objects
   :widths: auto
   :header-rows: 1
   
   * - Object
     - Table
   * - Columns
     - ``columns``, ``external_table_columns``
   * - Databases
     - ``databases``
   * - Permissions
     - ``table_permissions``, ``database_permissions``, ``schema_permissions``, ``permission_types``, ``udf_permissions``
   * - Roles
     - ``roles``, ``roles_memeberships``
   * - Sequences
     - ``identity_key``
   * - Tables
     - ``tables``, ``external_tables``
   * - Views
     - ``views``
   * - UDFs
     - ``user_defined_functions``

The catalog contains a few more tables which contain storage details for internal use

.. list-table:: Storage objects
   :widths: auto
   :header-rows: 1
   
   * - Object
     - Table
   * - Extents
     - ``extents``
   * - Chunks
     - ``chunks``
   * - Delete predicates
     - ``delete_predicates``

Tables in the catalog
========================

columns
--------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the table
   * - ``schema_name``
     - Name of the schema containing the table
   * - ``table_id``
     - Database-unique ID of the table
   * - ``table_name``
     - Name of the table
   * - ``column_id``
     - Ordinal of the column in the table (begins at 0)
   * - ``column_name``
     - Name of the column
   * - ``type_name``
     - :ref:`Data type <data_types>` of the column
   * - ``column_size``
     - The maximum length in bytes.
   * - ``has_default``
     - ``NULL`` if the column has no default value. ``1`` if the default is a fixed value, or ``2`` if the default is a :ref:`SEQUENCE <sequence>`
   * - ``default_value``
     - Default value for the column, or the 
   * - ``compression_strategy``
     - User-overridden compression strategy
   * - ``created``
     - Timestamp when the column was created
   * - ``altered``
     - Timestamp when the column was last altered
