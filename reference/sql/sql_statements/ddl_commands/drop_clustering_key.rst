.. _drop_clustering_key:

*******************
DROP CLUSTERING KEY
*******************
 
``DROP CLUSTERING KEY`` drops all clustering keys in a table.

Read our :ref:`cluster_by` guide for more information.

See also :ref:`create_table`

Syntax
======

.. code-block:: postgres

	ALTER TABLE [schema_name.]table_name DROP CLUSTERING KEY

	table_name ::= identifier

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified
   * - ``table_name``
     - The table name to apply the change to

Usage notes
===========

* Removing clustering keys does not affect existing data

* To force data to re-cluster, the table has to be recreated (i.e. with :ref:`create_table_as`)

Examples
========

Dropping Clustering Keys in a Table
-----------------------------------

.. code-block:: postgres

	ALTER TABLE 
	  public.users DROP CLUSTERING KEY

Permissions
===========

The role must have the ``DDL`` permission at the database or table level.
