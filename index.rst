.. _index:


.. role:: blue
   :class: blue-text

.. raw:: html

   <style>
   .blue-text {
       color: blue !important;
   }
   </style>

SQream :blue:`Blue` Documentation
=================================


SQream Blue is a cloud-native fully-managed data lakehouse built for fast, reliable, and cost-effective data processing utilizing a patented GPU-acceleration engine. The platform enables easy data preparation and transformation from and to the data lake, for faster analytics and AI/ML.

**Capabilities**

Architecture
    SQream Blue utilizes direct access to data in open-standard formats, eliminating the need for data ingestion or movement. Data remains in the customer's low-cost cloud storage throughout the preparation cycle, ensuring privacy, ownership, and a single source of truth, while eliminating data duplication. 
Parallelism
    SQream Blue uses the GPU to achieve parallel data processing. By breaking large tasks into smaller processes, SQream Blue distributes operations across multiple GPU cores, allowing administrators to :ref:`balance parallelism and concurrency<performance_and_concurrency_preferences>` according to their business needs.
Connectivity
    SQream Blue easily integrates with common open-source workflow management and orchestration tools, such as Apache Airflow, Dgaster, and Prefect. It also supports industry-standard JDBC and  Python :ref:`connectors<connecting_to_blue>`, and provides a REST API for cluster management. 


**Optimizations**

Optimized for Apache Parquet
    SQream Blue's processing engine utilizes Parquet's column-oriented structure and metadata to avoid unnecessary data reads, resulting in optimized processing times. 
GPU Optimization Engine
    SQream Blue's performance relies on a patented GPU acceleration technology that synchronizes all available resources (CPU, GPU, RAM) and utilizes the GPU's processing power for even the most complex analytical tasks. 


.. toctree::
   :caption: Getting Started
   :glob: 
   :maxdepth: 2
   :titlesonly:
   :hidden:

   getting_started/index
   getting_started/performing_basic_blue_operations
   managing_your_resources/index 

.. toctree::
   :caption: Guides
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   access_control/index
   access_tokens/index
   cloud_storage_platforms/index
   foreign_tables/index
   blue_console/index
   saved_queries/index
   statistics/index
   connecting_to_blue/index

.. toctree::
   :caption: Reference 
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   sql/index
   data_type_guides/index
   file_types/index
   syntax_notation/index

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

