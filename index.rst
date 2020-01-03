.. _index:

***********************
SQream DB documentation
***********************

What is SQream DB
===================

SQream DB is a columnar analytic SQL database management system. SQream DB uses GPUs to load and analyze large amounts of data.

Customers with SQream DB deploy it for sizes ranging from 5TB to 1PB. Depending on the workload, 1PB can be supported on a single node, with a fast and large enough storage. A common deployment motivation for SQream DB is for expanding historical analytics by orders of magnitude, such as expanding from 3 day windows to 3 months.

SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements.


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


Using this documentation
============================

The documentation contains a few main sections:
   
   * :ref:`Getting started<first_steps>` guides
   * :ref:`Operation guides<operations>` and :ref:`data management guides<data_management>`
   * :ref:`SQL reference<sql>`
   * :ref:`CLI reference<cli_reference>`
   * and more...

.. only:: html
   
   Use the navigation pane to the left to browse topics and guides, or use the search bar.

Each section contains several topics and guides intended to help a database user, administrator, or system engineer find information about using, managing, and deploying SQream DB.

Experience with SQL is not required, but helpful.

Some experience with Linux is recommended for system administrators.

.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.


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

   guides/first_steps
   guides/features_tour
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
