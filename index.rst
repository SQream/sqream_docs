.. _index:

***********************
SQream DB documentation
***********************

.. only:: html

   .. tip::
      Want to read this offline?
      `Download the documentation as a single PDF <https://readthedocs.org/projects/sqream-docs/downloads/pdf/latest/>`_ .

.. only:: pdf or latex
   
   .. tip:: This documentation is available online at https://docs.sqream.com/

SQream DB is a columnar analytic SQL database management system. 

SQream DB supports regular SQL including :ref:`a substantial amount of ANSI SQL<sql_feature_support>`, uses :ref:`serializable transactions<transactions>`, and :ref:`scales horizontally<concurrency_and_scaling_in_sqream>` for concurrent statements.

.. TODO: something about a single node of sqream being able to support 10 or even 100TB of data as long as it has enough storage.

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
         
         :ref:`Bulk load CSVs<csv>`
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
