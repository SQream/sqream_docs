.. _index:

***********************
SQream DB documentation
***********************

SQream DB is a GPU-accelerated analytics SQL database for massive data.

SQream DB is a columnar analytic relational database management system.

SQream DB is built to use GPU acceleration to load and analyze large amounts of data, in excess of the RAM resources for the machine. SQream DB scales horizontally for adding concurrent statements, has serializable transactions, and provides a SQL interface for querying data.

SQream DB is a columnar SQL RDBMS. It is is built to use GPU acceleration to load and analyze large amounts of data, in excess of the RAM resources for the machine. SQream DB scales horizontally for added concurrency, supports isolated serializable transactions, and provides a common SQL interface for querying data.


..

  Features tour

  This page gives an overview of the major features that SQream DB supports.

  Getting started

  This page shows you how to get started running SQL statements with SQream DB.

  Guides

  The guides section gives more detailed information and context for a
  range of features and aspects of the system.

  Reference

  This contains references for all the SQL statements, command line
  programs, catalog, supported sql feature checklist, and configuration.

  todo: insert complete toc here in nice sections and formating

.. list-table::
   :widths: 33 33 33
   :header-rows: 0

   * - **Get started**
     - **Reference**
     - **Guides**
   * -
         :ref:`first_steps`
         
         :ref:`features_tour`
         
         :ref:`sql_feature_support`
     - 
         :ref:`SQL reference<sql>`
         
         :ref:`sql_statements`
         
         :ref:`sql_functions`
     - 
         :ref:`setup`
         
         :ref:`Best practices<sql_best_practices>`
         
         :ref:`connect_to_tableau`

   * - **Releases**
     - **Driver and deployment**
     - **Help & Support**
   * -
         :ref:`2020.1<2020.1>`
         
         :ref:`2019.2.1<2019.2.1>`
         
         :ref:`All recent releases<releases>`

     - 
         :ref:`Client drivers<client_drivers>`

         :ref:`Third party tools integration<third_party_tools>`

         :ref:`connect_to_tableau`
     - 
         :ref:`information_for_support`
         
         :ref:`troubleshooting`




.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.

What is SQream DB
=================

SQream DB is a columnar SQL RDBMS. It is is built to use GPU acceleration to load and analyze large amounts of data, in excess of the RAM resources for the machine. SQream DB scales horizontally for added concurrency, supports isolated serializable transactions, and provides a common SQL interface for querying data.

Customers with SQream DB deploy it for sizes ranging from 5TB to 1PB. Depending on the workload, 1PB can be supported on a single node, with a fast and large enough storage. 

A common deployment motivation for SQream DB is for expanding historical analytics by orders of magnitude, such as expanding from 3 day windows to 3 months.


.. 
   Common data sizes for SQream DB
   
   columnar SQL DBMS

   runs on GPUs

   5TB to 500TB+

   can support 100TB+ on a single node depending on workload

   can support 30+ concurrent users

   has high availability

   runs on prem or on the cloud

   we see customers able to go from 3 months to 12 years data, and stuff like that

   extremely fast data loading speed

* a range of data types
* tables
* schemas
* roles and permissions
* sequences
* views
* saved queries
* external tables
* python udfs
* aggregates
* window functions

no limit to nested queries
   
join any amount of tables

catalog

robust serializable transactions and concurrency control

something about the data management/metadata skipping

wide range of client drivers

integrates with a wide range of third party components

performance
cost/ tco

highly responsive team, including new feature development




.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   guides/index
   reference/index
   releases/index
   glossary

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
