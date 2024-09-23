.. _index:

*************************
SQreamDB Documentation
*************************


SQreamDB is a columnar analytic SQL database management system. SQreamDB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements. Even a :ref:`basic SQreamDB machine<hardware_guide>` can support tens to hundreds of terabytes of data. SQreamDB easily plugs in to third-party tools like :ref:`Tableau<tableau>` comes with standard SQL client drivers, including :ref:`JDBC<java_jdbc>`, :ref:`ODBC<odbc>`, and :ref:`Python DB-API<pysqream>`.


+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Topic                                                       | Description                                                                                                                              |
+=============================================================+==========================================================================================================================================+
| **Getting Started**                                                                                                                                                                                    |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preparing_your_machine_to_install_sqream`             | Set up your local machine according to SQreamDB’s recommended pre-installation configurations.                                           |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`executing_statements_in_sqream`                       | Provides more information about the available methods for executing statements in SQreamDB.                                              |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`performing_basic_sqream_operations`                   | Provides more information on performing basic operations.                                                                                |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`hardware_guide`                                       | Describes SQreamDB’s mandatory and recommended hardware settings, designed for a technical audience.                                     |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Installation Guides**                                                                                                                                                                                |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`installing_and_launching_sqream`                      | Refers to SQreamDB’s installation guides.                                                                                                |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`sqream_studio_installation`                           | Refers to all installation guides required for installations related to Studio.                                                          |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| **Ingesting Data**                                                                                                                                                                                     |
+--------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`csv`               | :ref:`avro`                      |                                                                                                                                          |
+--------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parquet`           | :ref:`orc`                       |                                                                                                                                          |
+--------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`json`              | :ref:`sqloader_as_a_service`    |                                                                                                                                          |
+--------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| **Connecting to SQreamDB**                                                                                                                                                                             |
+--------------------------+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`client_platforms`                                     | Describes how to install and connect a variety of third party connection platforms and tools.                                            |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`client_drivers`                                       | Describes how to use the SQreamDB client drivers and client applications with SQreamDB.                                                  |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| **External Storage Platforms**                                                                                                                                                                         |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`s3`                                                   | Describes how to insert data over a native S3 connector.                                                                                 |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`hdfs`                                                 | Describes how to configure an HDFS environment for the user sqream and is only relevant for users with an HDFS environment.              |
+-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+


.. only:: html

.. only:: pdf or latex

.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQreamDB's support portal <https://sqream.atlassian.net/servicedesk/>`_ for additional support.


.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   getting_started/index
   installation_guides/index
   sqreamdb_on_aws/index
   operational_guides/index
   configuration_guides/index
   architecture/index
   sqream_studio/index
   connecting_to_sqream/index
   data_ingestion/index
   external_storage_platforms/index
   feature_guides/index
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
