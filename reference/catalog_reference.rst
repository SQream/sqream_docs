.. _catalog_reference:

*************************************
Catalog Reference Guide
*************************************
The **Catalog Reference Guide** describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
====================
The SQream database uses a schema called ``sqream_catalog`` that contains information about your database's objects, such tables, columns, views, and permissions. Some additional catalog tables are used primarily for internal analysis and which may be different across SQream versions.

What Information Does the Schema Contain?
==============================================
The schema includes tables designated and relevant for both external and internal use:

.. contents:: 
   :local:
   :depth: 1
   
External Tables
-----------------
The following table shows the data objects contained in the ``sqream_catalog`` schema designated for external use:

.. list-table:: Database Objects
   :widths: 20 110
   :header-rows: 1
   
   * - Database Object
     - Table
   * - :ref:`Clustering Keys<clustering_keys>`
     - ``clustering_keys``
   * - :ref:`Columns<columns>`
     - ``columns``, ``external_table_columns``
   * - :ref:`Databases<databases>`
     - ``databases``
   * - :ref:`Permissions<permissions>`
     - ``table_permissions``, ``database_permissions``, ``schema_permissions``, ``permission_types``, ``udf_permissions``, ``sqream_catalog.table_default_permissions``
   * - :ref:`Queries<queries>`
     - ``saved_queries``
   * - :ref:`Roles<roles>`
     - ``roles``, ``roles_memeberships``
   * - :ref:`Schemas<schemas>`
     - ``schemas``
   * - :ref:`Sequences<sequences>`
     - ``identity_key``
   * - :ref:`Tables<tables>`
     - ``tables``, ``external_tables``
   * - :ref:`Views<views>`
     - ``views``
   * - :ref:`User Defined Functions<udfs>`
     - ``user_defined_functions``

Internal Tables
-----------------
The following table shows the data objects contained in the ``sqream_catalog`` schema designated for internal use:

.. list-table:: Storage Objects
   :widths: 100 750
   :header-rows: 1
   
   * - Database Object
     - Table
   * - Extents
     - Shows ``extents``.
   * - Chunks
     - Shows ``chunks``.
   * - Delete predicates
     - Shows ``delete_predicates``. For more information, see :ref:`Deleting Data<delete_guide>`.

Catalog Tables
========================
The ``sqream_catalog`` includes the following tables:

.. contents:: 
   :local:
   :depth: 1
   
.. _clustering_keys:
   
Clustering Keys
----------------
The ``clustering_keys`` data object is used for explicit clustering keys for tables. If you define more than one clustering key, each key is listed in a separate row, and is described in the following table:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the table.
   * - ``table_id``
     - Shows the ID of the table containing the column.
   * - ``schema_name``
     - Shows the name of the schema containing the table.
   * - ``table_name``
     - Shows the name of the table containing the column.
   * - ``clustering_key``
     - Shows the name of the column used as a clustering key for this table.

.. _columns:

Columns
----------------
The **Columns** database object shows the following tables:

.. contents:: 
   :local:
   :depth: 1
   
Columns
***********
The ``column`` database object is used with standard tables and is described in the following table:

.. list-table::
   :widths: 20 150
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the table.
   * - ``schema_name``
     - Shows the name of the schema containing the table.
   * - ``table_id``
     - Shows the ID of the table containing the column.
   * - ``table_name``
     - Shows the name of the table containing the column.
   * - ``column_id``
     - Shows the ordinal number of the column in the table (begins at **0**).
   * - ``column_name``
     - Shows the column's name.
   * - ``type_name``
     - Shows the column's data type. For more information see :ref:`Supported Data Types <supported_data_types>`.
   * - ``column_size``
     - Shows the maximum length in bytes.
   * - ``has_default``
     - Shows ``NULL`` if the column has no default value, ``1`` if the default is a fixed value, or ``2`` if the default is an identity. For more information, see :ref:`identity`.
   * - ``default_value``
     - Shows the column's default value. For more information, see :ref:`Default Value Constraints<default_values>`.
   * - ``compression_strategy``
     - Shows the compression strategy that a user has overridden.
   * - ``created``
     - Shows the timestamp displaying when the column was created.
   * - ``altered``
     - Shows the timestamp displaying when the column was last altered.
	 
External Table Columns
***********
The ``external_table_columns`` is used for viewing data from foreign tables.

For more information on foreign tables, see :ref:`CREATE FOREIGN TABLE<create_foreign_table>`.

.. _databases:

Databases
----------------
The ``databases`` data object is used for displaying database information, and is described in the following table:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_Id``
     - Shows the database's unique ID.
   * - ``database_name``
     - Shows the database's name.
   * - ``default_disk_chunk_size``
     - Relevant for internal use.
   * - ``default_process_chunk_size``
     - Relevant for internal use.
   * - ``rechunk_size``
     - Relevant for internal use.
   * - ``storage_subchunk_size``
     - Relevant for internal use.
   * - ``compression_chunk_size_threshold``
     - Relevant for internal use.

.. _permissions:

Permissions
----------------
The ``permissions`` data object is used for displaying permissions information, and is described in the following tables:

.. contents:: 
   :local:
   :depth: 1   

Table Permissions
***********
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
	 
database_permissions
***********
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
	 
schema_permissions
***********

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
	 
permission_types
***********
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
	 

udf_permissions
***********

.. _queries:

Queries
----------------
``savedqueries`` identifies the :ref:`saved_queries<saved_queries>` in the database.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Description
   * - ``name``
     - Saved query name
   * - ``num_parameters``
     - Number of parameters to be replaced at run-time	 

.. _roles:
	 
Roles
----------------
roles
***********

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
***********

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
	 

.. _schemas:

Schemas
----------------
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

.. _sequences:

Sequences
----------------
identity_key
***********

.. _tables:

Tables
----------------
Tables
***********
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
	 
Foreign Tables
***********
``external_tables`` identifies foreign tables in the database.

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
     - 
         Identifies the foreign data wrapper used.
      
         ``0`` for csv_fdw, ``1`` for parquet_fdw, ``2`` for orc_fdw.
         
   * - ``created``
     - Identifies the clause used to create the table

.. _views:

Views
----------------
Views
***********
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

.. _udfs:

User Defined Functions
----------------

user_defined_functions
***********
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











  














  





  







Additional tables 
======================

There are additional tables in the catalog that can be used for performance monitoring and inspection.

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
     - ID for the extent
   * - ``size``
     - Extent size in megabytes
   * - ``path``
     - Full path to the extent on the file system

chunk_columns
-------------------

``chunk_columns`` lists chunk information by column.

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
   * - ``chunk_id``
     - ID for the chunk
   * - ``extent_id``
     - ID for the extent
   * - ``compressed_size``
     - Actual chunk size in bytes
   * - ``uncompressed_size``
     - Uncompressed chunk size in bytes
   * - ``compression_type``
     - Actual compression scheme for this chunk
   * - ``long_min``
     - Minimum numeric value in this chunk (if exists)
   * - ``long_max``
     - Maximum numeric value in this chunk (if exists)
   * - ``string_min``
     - Minimum text value in this chunk (if exists)
   * - ``string_max``
     - Maximum text value in this chunk (if exists)
   * - ``offset_in_file``
     - Internal use

.. note:: This is an internal table designed for low-level performance troubleshooting.

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

.. code-block:: psql

   master=> SELECT * FROM sqream_catalog.tables;
   database_name | table_id | schema_name | table_name     | row_count_valid | row_count | rechunker_ignore
   --------------+----------+-------------+----------------+-----------------+-----------+-----------------
   master        |        1 | public      | nba            | true            |       457 |                0
   master        |       12 | public      | cool_dates     | true            |         5 |                0
   master        |       13 | public      | cool_numbers   | true            |         9 |                0
   master        |       27 | public      | jabberwocky    | true            |         8 |                0

List all schemas in the database
------------------------------------

.. code-block:: psql
   
   master=> SELECT * FROM sqream_catalog.schemas;
   schema_id | schema_name   | schema_owner | rechunker_ignore
   ----------+---------------+--------------+-----------------
           0 | public        | sqream       | false           
           1 | secret_schema | mjordan      | false           


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


List :ref:`saved_queries`
-----------------------------

.. code-block:: postgres

   SELECT * FROM sqream_catalog.savedqueries;
