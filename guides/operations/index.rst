.. _operations:

.. _operational_guides_top:

**********************************
Operational Guides
**********************************
The **Operational Guides** page summarizes the following operational guides:

.. hlist::
   :columns: 4

   * :ref:`Access Control <access_control_down>`   
   
   * :ref:`Compression <features_guides_compression_down>`

   * :ref:`Data Clustering <data_clustering_down>`
   
   * :ref:`Foreign Tables <foreign_tables_down>`
   
   * :ref:`Python User-Defined Functions <python_user_defined_functions_down>`

   * :ref:`Saved Queries <saved_queries_down>`
   
   * :ref:`Viewing System Objects as DDL <viewing_system_objects_as_ddl_down>`
   
   * :ref:`Working with External Data <working_with_external_data_down>`
   
   * :ref:`Workload Manager <workload_manager_down>`

.. _access_control_down:

Access Control
--------------
Access control provides authentication and authorization in SQream DB. SQream DB manages authentication and authorization using a role-based access control system (RBAC), like ANSI SQL and other SQL products. SQream DB has a default permissions system which is inspired by Postgres, but with more power. In most cases, this allows an administrator to set things up so that every object gets permissions set automatically.

In SQream DB, users log in from any worker which verifies their roles and permissions from the metadata server. Each statement issues commands as the currently logged in role. Roles are defined at the cluster level, meaning they are valid for all databases in the cluster. To bootstrap SQream DB, a new install will always have one SUPERUSER role, typically named sqream. To create more roles, you should first connect as this role.

For more information, see :ref:`access_control`.

:ref:`Back to top<operational_guides_top>`

.. _features_guides_compression_down:

Compression
----------------------
SQream DB uses compression and encoding techniques to optimize query performance and save on disk space.

For more information, see :ref:`compression`.

:ref:`Back to top<operational_guides_top>`

.. _data_clustering_down:
 
Data Clustering
----------------------
Together with the chunking and Metadata system, SQream DB uses information to execute queries efficiently. SQream DB automatically collects metadata on incoming data. This works well when the data is naturally ordered (e.g. with time-based data). There are situations where you know more about the incoming data than SQream DB. If you help by defining clustering keys, SQream DB can automatically improve query processing. SQream DB’s query optimizer typically selects the most efficient method when executing queries. If no clustering keys are available, it may have to scan tables physically.

For more information, see :ref:`data_clustering`.

:ref:`Back to top<operational_guides_top>`

.. _deleting_data_down:
  
Deleting Data
----------------------
SQream DB supports deleting data, but it’s important to understand how this works and how to maintain deleted data.

For more information, see :ref:`delete`.

:ref:`Back to top<operational_guides_top>`

.. _foreign_tables_down:

Foreign Tables
--------------------------------------------
Foreign tables can be used to run queries directly on data without inserting it into SQream DB first. 
SQream DB supports read only foreign tables, so you can query from foreign tables, but you cannot insert to them, or run deletes or updates on them. Running queries directly on foreign (external) data is most effectively used for things like one off querying. If you will be repeatedly querying data, the performance will usually be better if you insert the data into SQream DB first. Although foreign tables can be used without inserting data into SQream DB, one of their main use cases is to help with the insertion process. An insert select statement on an foreign table can be used to insert data into SQream using the full power of the query engine to perform ETL.

For more information, see :ref:`external_tables`.

:ref:`Back to top<operational_guides_top>`

.. _python_user_defined_functions_down:

Python User-Defined Functions
--------------------------------------------
**User-defined functions (UDFs)** are a feature that extends SQream DB’s built in SQL functionality. SQream DB’s Python UDFs allow developers to create new functionality in SQL by writing the lower-level language implementation in Python.

For more information, see :ref:`python_functions`.

:ref:`Back to top<operational_guides_top>`

.. _saved_queries_down:

Saved Queries
------------------
Saved queries can be used to reuse a query plan for a query to eliminate compilation times for repeated queries. They also provide a way to implement ‘parameterized views’.

For more information, see :ref:`saved_queries`.

:ref:`Back to top<operational_guides_top>`

.. _viewing_system_objects_as_ddl_down:

Viewing System Objects as DDL
------------------
**Comment - Need content.**

For more information, see :ref:`seeing_system_objects_as_ddl`.

:ref:`Back to top<operational_guides_top>`

.. _working_with_external_data_down:

Working with External Data
--------------------------------------------
SQream DB supports external data sources for use with Foreign Tables, COPY FROM, and COPY TO.

For more information, see :ref:`external_data`.

:ref:`Back to top<operational_guides_top>`

.. _workload_manager_down:

Workload Manager
--------------------------------------------
The **Workload Manager** allows SQream DB workers to identify their availability to clients with specific service names. The load balancer uses that information to route statements to specific workers.

For more information, see :ref:`workload_manager`.

:ref:`Back to top<operational_guides_top>`
   
For more information about related guides, see the following pages describing third party tools:  

* :ref:`Client platforms<client_platforms>` - describes how to install and connect a variety of third party tools.

* :ref:`Client drivers<client_drivers>` - describes how to use SQream client drivers and client applications.