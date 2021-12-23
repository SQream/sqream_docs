.. _cluster_by:

**********************
CLUSTER BY
**********************

``CLUSTER BY`` can be used to change clustering keys in a table.

For more information, see the following:

* :ref:`data_clustering`
* :ref:`drop_clustering_key`
* :ref:`create_table`



Syntax
==========
The following is the correct syntax for the CLUSTER BY command:

.. code-block:: postgres

   alter_table_rename_table_statement ::=
       ALTER TABLE [schema_name.]table_name CLUSTER BY column_name [, ...]
       ;

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
   * - ``table_name``
     - The table name to apply the change to.
   * - ``column_name [, ... ]``
     - Comma separated list of columns to create clustering keys for


Usage Notes
=================
The following usage notes apply to the CLUSTER BY command:

* Removing clustering keys does not affect existing data.
* To force data to re-cluster, the table has to be recreated (i.e. with :ref:`create_table_as`).


Example
===========
The following example shows how to recluster a table:


.. code-block:: postgres

   ALTER TABLE public.users CLUSTER BY start_date;

Permissions
=============
The role must have the ``DDL`` permission at the database or table level.