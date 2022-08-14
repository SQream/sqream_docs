.. _catalog_reference_catalog_tables:

*************************************
Catalog Tables
*************************************
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
The ``column`` data object is used with standard tables and is described in the following table:

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
     - Reserved for internal use.
   * - ``default_process_chunk_size``
     - Reserved for internal use.
   * - ``rechunk_size``
     - Reserved for internal use.
   * - ``storage_subchunk_size``
     - Reserved for internal use.
   * - ``compression_chunk_size_threshold``
     - Reserved for internal use.

.. _permissions:

Permissions
----------------
The ``permissions`` data object is used for displaying permissions information, such as roles (also known as **grantees**), and is described in the following tables:

.. contents:: 
   :local:
   :depth: 1
   
Permission Types
***********
The ``permission_types`` object identifies the permission names existing in the database.

The following table describes the ``permission_types`` data object:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``permission_type_id``
     - Shows the permission type's ID.
   * - ``name``
     - Shows the name of the permission type.
   
Default Permissions
***********
The commands included in the **Default Permissions** section describe how to check the following default permissions:

.. contents:: 
   :local:
   :depth: 1

Default Table Permissions
~~~~~~~~~~~~~~~~
The ``sqream_catalog.table_default_permissions`` command shows the columns described below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the database that the default permission rule applies to.
   * - ``schema_id``
     - Shows the schema that the rule applies to, or ``NULL`` if the ``ALTER`` statement does not specify a schema.
   * - ``modifier_role_id``
     - Shows the role to apply the rule to.
   * - ``getter_role_id``
     - Shows the role that the permission is granted to.
   * - ``permission_type``
     - Shows the type of permission granted.
	 
Default Schema Permissions
~~~~~~~~~~~~~~~~
The ``sqream_catalog.schema_default_permissions`` command shows the columns described below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the database that the default permission rule applies to.
   * - ``modifier_role_id``
     - Shows the role to apply the rule to.
   * - ``getter_role_id``
     - Shows the role that the permission is granted to.
   * - ``permission_type``
     - Shows the type of permission granted.
	 
For an example of using the ``sqream_catalog.table_default_permissions`` command, see `Granting Default Table Permissions <https://docs.sqream.com/en/v2021.2/reference/sql/sql_statements/access_control_commands/alter_default_permissions.html#granting-default-table-permissions>`_.

Table Permissions
***********
The ``table_permissions`` data object identifies all permissions granted to tables. Each role-permission combination displays one row.

The following table describes the ``table_permissions`` data object: 

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the table.
   * - ``table_id``
     - Shows the ID of the table the permission applies to.
   * - ``role_id``
     - Shows the ID of the role granted permissions.
   * - ``permission_type``
     - Identifies the permission type.
	 
Database Permissions
***********
The ``database_permissions`` data object identifies all permissions granted to databases. Each role-permission combination displays one row.

The following table describes the ``database_permissions`` data object: 

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database the permission applies to
   * - ``role_id``
     - Shows the ID of the role granted permissions.
   * - ``permission_type``
     - Identifies the permission type.
	 
Schema Permissions
***********
The ``schema_permissions`` data object identifies all permissions granted to schemas. Each role-permission combination displays one row.

The following table describes the ``schema_permissions`` data object: 

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the schema.
   * - ``schema_id``
     - Shows the ID of the schema the permission applies to.
   * - ``role_id``
     - Shows the ID of the role granted permissions.
   * - ``permission_type``
     - Identifies the permission type.

.. _queries:

Queries
----------------
The ``savedqueries`` data object identifies the saved_queries in the database, as shown in the following table:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``name``
     - Shows the saved query name.
   * - ``num_parameters``
     - Shows the number of parameters to be replaced at run-time.

For more information, see :ref:`saved_queries<saved_queries>`.

.. _roles:
	 
Roles
----------------
The ``roles`` data object is used for displaying role information, and is described in the following tables:

.. contents:: 
   :local:
   :depth: 1   

Roles
***********
The ``roles`` data object identifies the roles in the database, as shown in the following table:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``role_id``
     - Shows the role's database-unique ID.
   * - ``name``
     - Shows the role's name.
   * - ``superuser``
     - Identifies whether the role is a superuser (``1`` - superuser, ``0`` - regular user).
   * - ``login``
     - Identifies whether the role can be used to log in to SQream (``1`` - yes, ``0`` - no).
   * - ``has_password``
     - Identifies whether the role has a password (``1`` - yes, ``0`` - no).
   * - ``can_create_function``
     - Identifies whether role can create UDFs (``1`` - yes, ``0`` - no).
     
Role Memberships
***********
The ``roles_memberships`` data object identifies the role memberships in the database, as shown below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``role_id``
     - Shows the role ID.
   * - ``member_role_id``
     - Shows the ID of the parent role that this role inherits from.
   * - ``inherit``
     - Identifies whether permissions are inherited (``1`` - yes, ``0`` - no).	 

.. _schemas:

Schemas
----------------
The ``schemas`` data object identifies all the database's schemas, as shown below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``schema_id``
     - Shows the schema's unique ID.
   * - ``schema_name``
     - Shows the schema's name.
   * - ``schema_owner``
     - Shows the name of the role that owns the schema.
   * - ``rechunker_ignore``
     - Reserved for internal use.

.. _sequences:

Sequences
----------------
The ``sequences`` data object is used for displaying identity key information.

.. _tables:

Tables
----------------
The ``tables`` data object is used for displaying table information, and is described in the following tables:

.. contents:: 
   :local:
   :depth: 1   

Tables
***********
The ``tables`` data object identifies proper (**Comment** - *What does "proper" mean?*) SQream tables in the database, as shown in the following table:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the table.
   * - ``table_id``
     - Shows the table's database-unique ID.
   * - ``schema_name``
     - Shows the name of the schema containing the table.
   * - ``table_name``
     - Shows the name of the table.
   * - ``row_count_valid``
     - Identifies whether the ``row_count`` can be used.
   * - ``row_count``
     - Shows the number of rows in the table.
   * - ``rechunker_ignore``
     - Relevant for internal use.
	 
Foreign Tables
***********
The ``external_tables`` data object identifies foreign tables in the database, as shown below:

.. list-table::
   :widths: 20 200
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the table.
   * - ``table_id``
     - Shows the table's database-unique ID.
   * - ``schema_name``
     - Shows the name of the schema containing the table.
   * - ``table_name``
     - Shows the name of the table.
   * - ``format``
     - Identifies the foreign data wrapper used. ``0`` for ``csv_fdw``, ``1`` for ``parquet_fdw``, ``2`` for ``orc_fdw``.         
   * - ``created``
     - Identifies the clause used to create the table.

.. _views:

Views
----------------
The ``views`` data object is used for displaying views in the database, as shown below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``view_id``
     - Shows the view's database-unique ID.
   * - ``view_schema``
     - Shows the name of the schema containing the view.
   * - ``view_name``
     - Shows the name of the view.
   * - ``view_data``
     - Reserved for internal use.
   * - ``view_query_text``
     - Identifies the ``AS`` clause used to create the view.

.. _udfs:

User Defined Functions
----------------
The ``udf`` data object is used for displaying UDFs in the database, as shown below:

.. list-table::
   :widths: 20 180
   :header-rows: 1
   
   * - Column
     - Description
   * - ``database_name``
     - Shows the name of the database containing the view.
   * - ``function_id``
     - Shows the UDF's database-unique ID.
   * - ``function_name``
     - Shows the name of the UDF.