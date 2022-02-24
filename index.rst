.. _index:

*************************
SQream DB Documentation
*************************

For SQream version 2021.2.

.. only:: html

   .. tip::
      Want to read this offline?
      `Download the documentation as a single PDF <https://docs.sqream.com/_/downloads/en/latest/pdf/>`_ .

.. only:: pdf or latex
   
   .. tip:: This documentation is available online at https://docs.sqream.com/

SQream DB is a columnar analytic SQL database management system. 

SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements.

Even a :ref:`basic SQream DB machine<hardware_guide>` can support tens to hundreds of terabytes of data.

SQream DB easily plugs in to third-party tools like :ref:`Tableau<connect_to_tableau>` comes with standard SQL client drivers, including :ref:`JDBC<java_jdbc>`, :ref:`ODBC<odbc>`, and :ref:`Python DB-API<pysqream>`.

.. 
   .. ref`features_tour`

.. list-table::
   :widths: 33 33 33
   :header-rows: 0

   * - **Get Started**
     - **Reference**
     - **Guides**
   * -
         :ref:`first_steps`
         
         :ref:`sql_feature_support`
         
         :ref:`Bulk load CSVs<csv>`
     - 
         :ref:`SQL Reference<sql>`
         
         :ref:`sql_statements`
         
         :ref:`sql_functions`
     - 
         `Setting up SQream <https://docs.sqream.com/en/latest/installation_guides/index.html>`_
         
         :ref:`Best practices<sql_best_practices>`
         
         :ref:`connect_to_tableau`

   * - **Releases**
     - **Driver and Deployment**
     - **Help and Support**
   * -
         :ref:`2021.2<2021.2>`

         :ref:`2021.1<2021.1>`
        
         :ref:`2020.3<2020.3>`

         :ref:`2020.2<2020.2>`
         
         :ref:`2020.1<2020.1>`
                  
         :ref:`All recent releases<releases>`

     - 
         :ref:`Client drivers<client_drivers>`

         :ref:`Third party tools integration<third_party_tools>`

         :ref:`connect_to_tableau`
     - 
         :ref:`troubleshooting` guide
         
         :ref:`information_for_support`



.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://sqream.atlassian.net/servicedesk/>`_ for additional support.


.. rubric:: Looking for older versions?

This version of the documentation is for SQream DB Version 2021.2.

If you're looking for an older version of the documentation, versions 1.10 through 2019.2.1 are available at http://previous.sqream.com .

.. toctree::
   :caption: Contents:
   :glob:
   :maxdepth: 6
   :titlesonly:
   :hidden:

   getting_started/index
   installation_guides/index
   data_ingestion/index
   third_party_tools/index
   feature_guides/index
   operational_guides/index
   sqream_studio_5.4.3/index
   architecture/index
   configuration_guides/index
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
