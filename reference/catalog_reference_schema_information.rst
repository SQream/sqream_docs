.. _catalog_reference_schema_information:

*****************************************
What Information Does the Schema Contain?
*****************************************

The schema contains data management tables with information about structure and management of database elements, including tables, schemas, queries, and permissions, and physical storage and organization of data tables of extents, chunk columns, chunks, and delete predicates.
   
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
   * - :ref:`Permissions<permissions>`
     - ``table_permissions``, ``database_permissions``, ``schema_permissions``, ``permission_types``, ``udf_permissions``, ``sqream_catalog.table_default_permissions``
   * - :ref:`Queries<queries>`
     - ``saved_queries``
   * - :ref:`Roles<roles>`
     - ``roles``, ``roles_memeberships``
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
   * - Extents
     - Shows ``extents``
   * - Chunk columns
     - Shows ``chunks_columns``
   * - Chunks
     - Shows ``chunks``
   * - Delete predicates
     - Shows ``delete_predicates``. For more information, see :ref:`Deleting Data<delete_guide>`