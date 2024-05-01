.. _index:


.. role:: blue
   :class: blue-text

.. raw:: html

   <style>
   .blue-text {
       color: blue !important;
   }
   </style>

:blue:`BLUE` Documentation
==========================


BLUE is a cloud-based platform designed for enterprises utilizing data lake architectures, aiming to simplify data integration workflows and enable cloud migration.

A notable capability of BLUE lies in handling data integration tasks, from 2TB to petabyte scales. This makes it well-suited for swift and effective processing of large data volumes. BLUE embraces both data lakehouse and query engine technologies, empowering businesses to gain comprehensive data insights and real-time analysis.

**Capabilities**

.. grid:: 3

  .. grid-item-card:: Architecture

      BLUE utilizes direct access to data in open-standard formats, eliminating the need for data ingestion or movement. Data remains in the customer's low-cost cloud storage throughout the preparation cycle, ensuring privacy, ownership, and a single source of truth, while eliminating data duplication. 

  .. grid-item-card:: Parallelism

      BLUE uses the GPU to achieve parallel data processing. By breaking large tasks into smaller processes, BLUE distributes operations across multiple GPU cores, allowing administrators to balance parallelism and concurrency according to their business needs.

  .. grid-item-card:: Connectivity

      BLUE easily integrates with common open-source workflow management and orchestration tools, such as Apache Airflow, Dgaster, and Prefect. It also supports industry-standard ODBC, JDBC, and  Python connectors, and provides a REST API for cluster management. 

**Optamizations**

.. grid:: 2

  .. grid-item-card:: Optimized for Apache Parquet

      BLUE's processing engine utilizes Parquet's column-oriented structure and metadata to avoid unnecessary data reads, resulting in optimized processing times. 

  .. grid-item-card:: GPU Optimization Engine

      BLUE's performance relies on a patented GPU acceleration technology that synchronizes all available resources (CPU, GPU, RAM) and utilizes the GPU's processing power for even the most complex analytical tasks. 


.. toctree::
   :caption: Getting Started
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   getting_started/index
   getting_started/blue_tour
   getting_started/architecture
   getting_started/performing_basic_blue_operations

.. toctree::
   :caption: Guides
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   access_control/index
   access_tokens/index
   cloud_storage_platforms/index
   blue_console/index
   saved_queries/index
   connecting_to_blue/index

.. toctree::
   :caption: Reference 
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   data_type_guides/index
   sql/index
   file_types/index
   syntax_notation/index
   foreign_tables/index


.. toctree::
   :caption: System Operations
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:
   
   audit_log_operation/index
   delete_guide/index
   
.. toctree::
   :caption: Performance Tuning
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:
   
   optimization_best_practices/index
   optimization_best_practices/monitoring_query_performance
   optimization_best_practices/concurrency_and_locks
   optimization_best_practices/concurrency_and_scaling_in_sqream
   

.. toctree::
   :caption: Releases
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   releases/index
   
.. toctree::
   :caption: Troubleshooting
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:
   
   troubleshooting/index

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
