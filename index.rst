.. _index:

.. raw:: html

	<font color="red">BLUE</font>
=================================


\\tl;dr
^^^^^^

Blue is a cloud-based platform designed for businesses using data lake architectures. It makes it easy to set up new workflows for complex data integration and move your data integration to the cloud. With a patented GPU optimization engine, parallelism, and optimization for Apache Parquet, Blue helps you process data quickly and efficiently. Plus, it connects seamlessly with your favorite open-source workflow tools and offers a unique architecture that keeps your data secure and eliminates duplication.

\\SELECT *
^^^^^^^^^

Blue is a platform designed for enterprises working with cloud-based data lake architectures, or those considering a move to the cloud. The product includes a range of features to streamline workflows, gain deeper insights into data, and perform real-time data analysis.

One key feature of Blue is its support for data integration use cases that require complex data flows ranging from 2TB to petabyte-scale. This makes it an ideal choice for businesses that need to process large volumes of data quickly and efficiently. Additionally, Blue includes support for both datalake house and query engine technologies. These features enable businesses to gain a deeper understanding of their data and analyze it in real-time, allowing for faster and more informed decision-making.

Whether your enterprise is already using AWS or GCP, or considering a move to the cloud, Blue is a valuable tool for optimizing data workflows and maximizing the benefits of cloud-based data storage and processing.

Main Features and Capabilities:


+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Feature**                  | **Description**                                                                                                                                                                                                                                                                                                                                 |
+==============================+=================================================================================================================================================================================================================================================================================================================================================+
| GPU Optimization Engine      | Blue's performance relies on a patented GPU acceleration technology that synchronizes all available resources (CPU, GPU, RAM) and utilizes the GPU's processing power for even the most complex analytical tasks.                                                                                                                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parallelism                  | SQream uses the GPU to achieve parallel data processing. By breaking large tasks into smaller processes, SQream distributes operations across multiple GPU cores, allowing administrators to balance parallelism and concurrency according to their business needs.                                                                             |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Optimized for Apache Parquet | Blue's processing engine utilizes Parquet's column-oriented structure and metadata to avoid unnecessary data reads, resulting in optimized processing times.                                                                                                                                                                                    |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Connectivity                 | Blue easily integrates with common open-source workflow management and orchestration tools, such as Apache Airflow, Dgaster, and Prefect. It also supports industry-standard ODBC, JDBC, and Python connectors, and provides a REST API for cluster management.                                                                                 |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Architecture                 | SQream Blue does not require data ingestion or movement and relies on direct access to data in open-standard formats. Throughout the data preparation cycle, all data remains in the customer's low-cost cloud storage, ensuring privacy and ownership while preserving a single source of truth and eliminating the need for data duplication. |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   login_and_connectors/index
   getting_started/index
   data_ingestion/index
   loading_and_unloading_data/index
   feature_guides/index
   operational_guides/index
   configuration_guides/index
   reference/index
   data_type_guides/index
   releases/index
   troubleshooting/index
   glossary

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
