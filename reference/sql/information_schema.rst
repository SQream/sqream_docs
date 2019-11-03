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

     
     
table_permissions
------------------

``table_permissions`` identifies all permissions granted to tables. 

.. There is one row for each combination of grantor, grantee, and column (defined by table_catalog, table_schema, table_name, and column_name).

database_permissions
----------------------

``database_permissions`` identifies all permissions granted to databases. 


schema_permissions
--------------------

permission_types
------------------

udf_permissions
------------------

roles
------

roles_memberships
-------------------

identity_key
--------------

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



.. _external_tables_table:

external_tables
----------------

views
-------

user_defined_functions
-------------------------

Additional tables 
======================

extents
----------

chunks
-------

delete_predicates
-------------------