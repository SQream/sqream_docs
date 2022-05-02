.. _cluster_by:

**********************
CLUSTER BY
**********************
The ``CLUSTER BY`` command is used for changing clustering keys in a table.

For more information, see the following:

* :ref:`flexible_data_clustering`

   ::

* :ref:`drop_clustering_key`

   ::
   
* :ref:`create_table`

Syntax
==========
The following is the correct syntax for the CLUSTER BY command:

.. code-block:: postgres

   alter_table_rename_table_statement ::=
       ALTER TABLE [schema_name.]table_name CLUSTER BY column_name [, ...]
       ;
	   
   create_table_statement ::=
       CREATE [ OR REPLACE ] TABLE [schema_name.]table_name (
           { column_def [, ...] }
       )
       [ CLUSTER BY { column_name [, ...] } ]
       ;
	   
   column_def :: = { column_name type_name [ default ] [ column_constraint ] }

   table_name ::= identifier
   
   column_name ::= identifier


Parameters
============
The following table shows the CLUSTER BY parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified.
   * - ``OR REPLACE``
     - Creates a new tables and overwrites any existing table by the same name. Does not return an error if the table already exists. ``CREATE OR REPLACE`` does not check the table contents or structure, only the table name.
   * - ``column_def``
     - A comma separated list of column definitions. A minimal column definition includes a name identifier and a datatype. Other column constraints and default values can be added optionally.
   * - ``table_name``
     - The table name to apply the change to.
   * - ``column_name [, ... ]``
     - Comma separated list of columns to create clustering keys for.

Usage Notes
=================
Removing clustering keys does not affect existing data.

To force data to re-cluster, the table has to be recreated (i.e. with :ref:`create_table`).


Example
===========
Reclustering a Table
-----------------------------------------
The following example shows how to recluster a table:

.. code-block:: postgres

   ALTER TABLE public.users CLUSTER BY start_date;

Permissions
=============
The role must have the ``DDL`` permission at the database or table level.