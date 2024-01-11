.. _catalog_reference:

***********************
Catalog Reference
***********************

The SQreamDB database uses a schema called ``sqream_catalog`` that contains information about database objects such as tables, columns, views, and permissions. Some additional catalog tables are used primarily for internal analysis and may differ across SQreamDB versions.


What Information Does the Schema Contain?
==========================================

The schema contains data management tables with information about structure and management of database elements, including tables, schemas, queries, and permissions, and physical storage and organization of data tables of extents, chunk columns, chunks, and delete predicates.
   
How to Get Table Information?
=============================

To get the information stored on a table, use this syntax, as in this example of working with the ``parameters`` table:

.. code-block:: sql

	SELECT * FROM sqream_catalog.parameters;
	
To get the table ddl, use this syntax, as in this example of working with the ``parameters`` table:

.. code-block:: sql

	SELECT get_ddl('sqream_catalog.parameters'); 
   
Database Management Tables
---------------------------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Database Object
     - Table
   * - :ref:`Clustering Keys<clustering_keys>`
     - ``clustering_keys``
   * - :ref:`Columns<columns>`
     - ``columns``, ``external_table_columns``
   * - :ref:`Databases<databases>`
     - ``databases``
   * - :ref:`Parameters<parameters>`
     - ``parameters``
   * - :ref:`Permissions<permissions>`
     - ``table_permissions``, ``database_permissions``, ``schema_permissions``, ``permission_types``, ``udf_permissions``, ``sqream_catalog.table_default_permissions``
   * - :ref:`Queries<queries>`
     - ``savedqueries``
   * - :ref:`Roles<roles>`
     - ``roles``, ``role_memberships``
   * - :ref:`Schemas<schemas>`
     - ``schemas``
   * - :ref:`Tables<tables>`
     - ``tables``, ``external_tables``
   * - :ref:`Views<views>`
     - ``views``
   * - :ref:`User Defined Functions<udfs>`
     - ``user_defined_functions``

Data Storage and Organization Tables
---------------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Database Object
     - Table
   * - :ref:`Extents<extents>`
     - Shows ``extents``
   * - :ref:`Chunk columns<chunk_columns>`
     - Shows ``chunks_columns``
   * - :ref:`Chunks<chunks>`
     - Shows ``chunks``
   * - :ref:`Delete predicates<delete_predicates>`
     - Shows ``delete_predicates``. For more information, see :ref:`Deleting Data<delete_guide>`

.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:


   catalog_reference_catalog_tables
   catalog_reference_additonal_tables
   catalog_reference_examples