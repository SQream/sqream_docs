.. _index:

***********************
SQream DB documentation
***********************

What is SQream DB
===================

SQream DB is a columnar analytic SQL database management system. SQream DB uses GPUs to load and analyze large amounts of data.

Customers with SQream DB deploy it for sizes ranging from 5TB to 1PB. Depending on the workload, 1PB can be supported on a single node, with a fast and large enough storage. A common deployment motivation for SQream DB is for expanding historical analytics by orders of magnitude, such as expanding from 3 day windows to 3 months.

SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements.

SQream DB comes with standard SQL client drivers, including :ref:`JDBC<java_jdbc>`, :ref:`ODBC<odbc>`, and :ref:`Python DB-API<pysqream>`.

.. 
   .. ref`features_tour`

.. list-table::
   :widths: 33 33 33
   :header-rows: 0

   * - **Get started**
     - **Reference**
     - **Guides**
   * -
         :ref:`first_steps`
         
         
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

.. rubric:: Looking for the old documentation?

If you're looking for an older version of the documentation, versions 1.10 through 2019.2.1 are available at http://previous.sqream.com .

.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   first_steps
   xxfeatures_tour
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
