.. _index:

*************************
SQream DB Documentation
*************************


SQream DB is a columnar analytic SQL database management system. SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements. Even a :ref:`basic SQream DB machine<hardware_guide>` can support tens to hundreds of terabytes of data. SQream DB easily plugs in to third-party tools like :ref:`Tableau<connect_to_tableau>` comes with standard SQL client drivers, including :ref:`JDBC<java_jdbc>`, :ref:`ODBC<odbc>`, and :ref:`Python DB-API<pysqream>`.


+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Topic                                             | Description                                                                                                                            |
+===================================================+========================================================================================================================================+
| **Getting Started**                                                                                                                                                                        |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`preparing_your_machine_to_install_sqream`   | Set up your local machine according to SQream’s recommended pre-installation configurations.                                           |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`executing_statements_in_sqream`             | Provides more information about the available methods for executing statements in SQream.                                              |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`performing_basic_sqream_operations`         | Provides more information on performing basic operations.                                                                              |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`hardware_guide`                             | Describes SQream’s mandatory and recommended hardware settings, designed for a technical audience.                                     |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Installation Guides**                                                                                                                                                                    |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`installing_and_launching_sqream`            | Refers to SQream’s installation guides.                                                                                                |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`sqream_studio_installation`                 | Refers to all installation guides required for installations related to Studio.                                                        |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Ingesting Data**                                                                                                                                                                         |
+--------------------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`csv`               | :ref:`avro`            |                                                                                                                                        |
+--------------------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parquet`           | :ref:`orc`             |                                                                                                                                        |
+--------------------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Connecting to SQream**                                                                                                                                                                   |
+--------------------------+------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`client_platforms`                           | Describes how to install and connect a variety of third party connection platforms and tools.                                          |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`client_drivers`                             | Describes how to use the SQream client drivers and client applications with SQream.                                                    |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **External Storage Platforms**                                                                                                                                                             |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`s3`                                         | Describes how to insert data over a native S3 connector.                                                                               |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`hdfs`                                       | Describes how to configure an HDFS environment for the user sqream and is only relevant for users with an HDFS environment.            |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+


.. only:: html

   .. tip::
      Want to read this offline?
      `Download the documentation as a single PDF <https://docs.sqream.com/_/downloads/en/latest/pdf/>`_ .

.. only:: pdf or latex
   
   .. tip:: This documentation is available online at https://docs.sqream.com/


.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://sqream.atlassian.net/servicedesk/>`_ for additional support.


.. rubric:: Looking for older versions?


If you're looking for an older version of the documentation, go to http://previous.sqream.com .

.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   getting_started/index
   installation_guides/index
   data_ingestion/index
   connecting_to_sqream/index
   external_storage_platforms/index
   loading_and_unloading_data/index
   feature_guides/index
   operational_guides/index
   sqream_studio_5.4.7/index
   architecture/index
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
