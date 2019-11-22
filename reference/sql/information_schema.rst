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
   * - Schemas
     - ``schemas``
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

Column objects for standard tables

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
     - ID of the table containing the column
   * - ``table_name``
     - Name of the table containing the column
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


.. _external_tables_table:

external_tables
----------------

``external_tables`` identifies external tables in the database.

For ``TABLES`` see :ref:`tables <tables_table>`

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the table
   * - ``table_id``
     - Database-unique ID for the table
   * - ``schema_name``
     - Name of the schema containing the table
   * - ``table_name``
     - Name of the table
   * - ``format``
     - Identifies the source format. ``0`` for CSV, ``1`` for Parquet
   * - ``created``
     - Identifies the clause used to create the table

external_table_columns
------------------------

Column objects for external tables

databases
-----------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_Id``
     - Unique ID of the database
   * - ``database_name``
     - Name of the database
   * - ``default_disk_chunk_size``
     - Internal use
   * - ``default_process_chunk_size``
     - Internal use
   * - ``rechunk_size``
     - Internal use
   * - ``storage_subchunk_size``
     - Internal use
   * - ``compression_chunk_size_threshold``
     - Internal use

database_permissions
----------------------

``database_permissions`` identifies all permissions granted to databases. 

There is one row for each combination of role (grantee) and permission granted to a database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database the permission applies to
   * - ``role_id``
     - ID of the role granted permissions (grantee)
   * - ``permission_type``
     - Identifies the permission type
  

identity_key
--------------


permission_types
------------------

``permission_types`` Identifies the permission names that exist in the database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``permission_type_id``
     - ID of the permission type
   * - ``name``
     - Name of the permission type

roles
------

``roles`` identifies the roles in the database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``role_id``
     - Database-unique ID of the role
   * - ``name``
     - Name of the role
   * - ``superuser``
     - Identifies if this role is a superuser. ``1`` for superuser or ``0`` otherwise.
   * - ``login``
     - Identifies if this role can be used to log in to SQream DB. ``1`` for yes or ``0`` otherwise.
   * - ``has_password``
     - Identifies if this role has a password. ``1`` for yes or ``0`` otherwise.
   * - ``can_create_function``
     - Identifies if this role can create UDFs. ``1`` for yes, ``0`` otherwise.
     
roles_memberships
-------------------

``roles_memberships`` identifies the role memberships in the database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``role_id``
     - Role ID
   * - ``member_role_id``
     - ID of the parent role from which this role will inherit
   * - ``inherit``
     - Identifies if permissions are inherited. ``1`` for yes or ``0`` otherwise.


schemas
----------

``schemas`` identifies all the database's schemas.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``schema_id``
     - Unique ID of the schema
   * - ``schema_name``
     - Name of the schema
   * - ``schema_owner``
     - Name of the role who owns this schema
   * - ``rechunker_ignore``
     - Internal use


schema_permissions
--------------------

``schema_permissions`` identifies all permissions granted to schemas. 

There is one row for each combination of role (grantee) and permission granted to a schema.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the schema
   * - ``schema_id``
     - ID of the schema the permission applies to
   * - ``role_id``
     - ID of the role granted permissions (grantee)
   * - ``permission_type``
     - Identifies the permission type
  

.. _tables_table:

tables
----------

``tables`` identifies proper SQream tables in the database.

For ``EXTERNAL TABLES`` see :ref:`external_tables <external_tables_table>`

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the table
   * - ``table_id``
     - Database-unique ID for the table
   * - ``schema_name``
     - Name of the schema containing the table
   * - ``table_name``
     - Name of the table
   * - ``row_count_valid``
     - Identifies if the ``row_count`` can be used
   * - ``row_count``
     - Number of rows in the table
   * - ``rechunker_ignore``
     - Internal use


table_permissions
------------------

``table_permissions`` identifies all permissions granted to tables. 

There is one row for each combination of role (grantee) and permission granted to a table.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the table
   * - ``table_id``
     - ID of the table the permission applies to
   * - ``role_id``
     - ID of the role granted permissions (grantee)
   * - ``permission_type``
     - Identifies the permission type
  

udf_permissions
------------------

user_defined_functions
-------------------------

``user_defined_functions`` identifies UDFs in the database. 

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the database containing the view
   * - ``function_id``
     - Database-unique ID for the UDF
   * - ``function_name``
     - Name of the UDF

views
-------

``views`` identifies views in the database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``view_id``
     - Database-unique ID for the view
   * - ``view_schema``
     - Name of the schema containing the view
   * - ``view_name``
     - Name of the view
   * - ``view_data``
     - Internal use
   * - ``view_query_text``
     - Identifies the ``AS`` clause used to create the view


Additional tables 
======================

There are additional tables in the information schema that can be used for performance monitoring and inspection.

The definition for these tables is provided below could change across SQream DB versions.

extents
----------

``extents`` identifies storage extents.

Each storage extents can contain several chunks.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the extent
   * - ``table_id``
     - ID of the table containing the extent
   * - ``column_id``
     - ID of the column containing the extent
   * - ``extent_id``
     - ``???``-wide ID for the extent
   * - ``size``
     - Extent size in megabytes
   * - ``path``
     - Full path to the extent on the file system


chunks
-------

``chunks`` identifies storage chunks.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the chunk
   * - ``table_id``
     - ID of the table containing the chunk
   * - ``column_id``
     - ID of the column containing the chunk
   * - ``rows_num``
     - Amount of rows contained in the chunk
   * - ``deletion_status``
     - When data is deleted from the table, it is first deleted logically. This value identifies how much data is deleted from the chunk. ``0`` for no data, ``1`` for some data, ``2`` to specify the entire chunk is deleted.

delete_predicates
-------------------

``delete_predicates`` identifies the existing delete predicates that have not been cleaned up.

Each :ref:`DELETE <delete>` command may result in several entries in this table.

.. note:: This is an internal table designed for low-level performance troubleshooting.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Name of the databse containing the predicate
   * - ``table_id``
     - ID of the table containing the predicate
   * - ``max_chunk_id``
     - Internal use. Placeholder marker for the highest ``chunk_id`` logged during the DELETE operation.
   * - ``delete_predicate``
     - Identifies the DELETE predicate


Examples
===========

List all tables in the database
----------------------------------

.. code-block:: postgres

   SELECT * FROM sqream_catalog.tables;


.. todo: plug in result from this

List columns and their types for a specific table
---------------------------------------------------

.. code-block:: postgres

   SELECT column_name, type_name 
   FROM sqream_catalog.columns
   WHERE table_name='cool_animals';

List delete predicates
------------------------


.. code-block:: postgres

   SELECT  t.table_name, d.*  FROM 
   sqream_catalog.delete_predicates AS d  
   INNER JOIN sqream_catalog.tables AS t  
   ON d.table_id=t.table_id;
