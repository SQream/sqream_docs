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
   getting_started/connecting_to_blue
      

.. toctree::
   :caption: Guides
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   cloud_storage_platforms/index
   data_type_guides/index
   file_types/index
   configuration_guides/index
   operational_guides/access_tokens


.. toctree::
   :caption: Reference 
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   reference/index

.. toctree::
   :caption: System Operation
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   operational_guides/index
   feature_guides/index

.. toctree::
   :caption: Releases
   :glob:
   :maxdepth: 2
   :titlesonly:
   :hidden:

   releases/index
   troubleshooting/index

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
