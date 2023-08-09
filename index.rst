.. _index:

.. role:: red
   :class: red-text

.. raw:: html

   <style>
   .red-text {
       color: red !important;
   }
   </style>

:red:`BLUE` Documentation
=========================


BLUE is a cloud-based platform designed for enterprises utilizing data lake architectures, aiming to simplify data integration workflows and enable cloud migration. It incorporates patented GPU optimization, parallelism, and Apache Parquet support for efficient data processing. The platform seamlessly integrates with popular open-source workflow tools and employs a robust security architecture to enhance data integrity.

A notable capability of BLUE lies in handling data integration tasks, from 2TB to petabyte scales. This makes it well-suited for swift and effective processing of large data volumes. Additionally, BLUE embraces both datalake house and query engine technologies, empowering businesses to gain comprehensive data insights and real-time analysis, thus expediting decision-making.

Whether your enterprise is already cloud-based or planning to migrate, BLUE optimizes data workflows, capitalizing on the benefits of cloud-based data storage and processing.

--------------------------

Main Features and Capabilities
------------------------------

.. glossary::

  GPU Optimization Engine
      BLUE's performance relies on a patented GPU acceleration technology that synchronizes all available resources (CPU, GPU, RAM) and utilizes the GPU's processing power for even the most complex analytical tasks.
   
  GPU Optimization Engine
      BLUE's performance relies on a patented GPU acceleration technology that synchronizes all available resources (CPU, GPU, RAM) and utilizes the GPU's processing power for even the most complex analytical tasks. 
   
  Parallelism
      BLUE uses the GPU to achieve parallel data processing. By breaking large tasks into smaller processes, BLUE distributes operations across multiple GPU cores, allowing administrators to balance parallelism and concurrency according to their business needs.
   
  Optimized for Apache Parquet
      BLUE's processing engine utilizes Parquet's column-oriented structure and metadata to avoid unnecessary data reads, resulting in optimized processing times. 
   
  Connectivity 
      BLUE easily integrates with common open-source workflow management and orchestration tools, such as Apache Airflow, Dgaster, and Prefect. It also supports industry-standard ODBC, JDBC, and  Python connectors, and provides a REST API for cluster management.  
   
  Architecture 
      BLUE does not require data ingestion or movement and relies on direct access to data in open-standard formats. Throughout the data preparation cycle, all data remains in the customer's low-cost cloud storage, ensuring privacy and ownership while preserving a single source of truth and eliminating the need for data duplication. 





.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   getting_started/index
   configuration_guides/index
   operational_guides/index
   feature_guides/index
   data_type_guides/index
   file_types/index
   reference/index
   releases/index
   troubleshooting/index
   glossary

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
