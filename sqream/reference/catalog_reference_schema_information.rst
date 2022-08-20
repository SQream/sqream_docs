.. _catalog_reference_schema_information:

*************************************
What Information Does the Schema Contain?
*************************************
The schema includes tables designated and relevant for both external and internal use:

.. contents:: 
   :local:
   :depth: 1
   
External Tables
-----------------
The following table shows the data objects contained in the ``sqream_catalog`` schema designated for external use:

.. list-table:: Database Objects
   :widths: 20 180
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
   :widths: 20 180
   :header-rows: 1
   
   * - Database Object
     - Table
   * - Extents
     - Shows ``extents``.
   * - Chunk columns
     - Shows ``chunks_columns``.
   * - Chunks
     - Shows ``chunks``.
   * - Delete predicates
     - Shows ``delete_predicates``. For more information, see :ref:`Deleting Data<delete_guide>`.