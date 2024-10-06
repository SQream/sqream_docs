.. _releases:

*************
Release Notes
*************

:ref:`Version 4.8 - October 06, 2024<4.8>`

* Prepared statements are now supported by our `Python <../connecting_to_sqream/client_drivers/python/index.html#prepared-statements>`_ and `JDBC <../connecting_to_sqream/client_drivers/jdbc/index.html#prepared-statements>`_ client drivers.
* `PIVOT <../reference/sql/sql_syntax/pivot_unpivot.html#syntax>`_ and `UNPIVOT <../reference/sql/sql_syntax/pivot_unpivot.html#syntax>`_.
* `Window funtion alias  <../reference/sql/sql_syntax/window_functions.html#window-funtion-alias>`_ allows to specify a parameter within the window function definition. This eliminates the need to repeatedly input the same SQL code in queries that use multiple window functions with identical definitions.
* `CONCAT <../reference/sql/sql_functions/scalar_functions/string/concat_function.html#concat-function>`_ function concatenates one or more strings, or concatenates one or more binary values.

:ref:`Version 4.7 - September 01, 2024<4.7>`

* :ref:`AWS private cloud deployment<sqreamdb_on_aws>` is now available for SQreamDB on AWS Marketplace.
* Execute a single SQL statement across your SQreamDB cluster using the new :ref:`Cross-Database<cross_database_query>` syntax.
* Safely cast data types with the new :ref:`IsCastable<is_castable>` function.
* Automatically delete source files being copied into SQreamDB using the :ref:`copy_from` command.

:ref:`Version 4.6 - August 20, 2024<4.6>`

* You can now sign in to SQreamDB Studio using your universal :ref:`Single Sign-On (SSO)<sso>` provider authentication

* Announcing a new :ref:`Activity Report<view_activity_report>` reflecting your storage and resource usage 

* Announcing a new Java-based cross-platform :ref:`SQream SQL CLI<sqream_sql_cli_reference>` 

* ``TOP`` clause enhancements

* :ref:`Saved Query<saved_queries>` command permission enhancements

:ref:`Version 4.5 - December 5, 2023<4.5>`

* Introducing a new :ref:`Health-Check Monitor<select_health_check_monitoring>` utility command empowers administrators to oversee the database's health. This command serves as a valuable tool for monitoring, enabling administrators to assess and ensure the optimal health and performance of the database

* A new :ref:`Query Timeout<query_timeout_minutes>` session flag designed to identify queries that have exceeded a specified time limit. Once the flag value is reached, the query automatically stops

:ref:`Version 4.4 - September 28, 2023<4.4>`

* `Enhancing storage efficiency and performance with the newly supported ARRAY data type <https://docs.sqream.com/en/latest/releases/4.4.html#new-features-and-enhancements>`_
* `New integration with Denodo Platform <https://docs.sqream.com/en/latest/releases/4.4.html#new-features-and-enhancements>`_

:ref:`Version 4.3 - June 11, 2023<4.3>`

* `Access Control Permission Expansion <https://docs.sqream.com/en/latest/releases/4.3.html#new-features-and-enhancements>`_
* `New AWS S3 Access Configurations <https://docs.sqream.com/en/latest/releases/4.3.html#configuration-adjustments>`_

:ref:`Version 4.2 - April 23, 2023<4.2>`

* `New Apache Spark Connector <https://docs.sqream.com/en/latest/releases/4.2.html#new-features>`_
* `Physical Deletion Performance Enhancement <https://docs.sqream.com/en/latest/releases/4.2.html#new-features>`_

:ref:`Version 4.1 - March 01, 2023<4.1>`

* `LDAP Management Enhancements <https://docs.sqream.com/en/latest/releases/4.1.html#new-features>`_
* `New Trino Connector <https://docs.sqream.com/en/latest/releases/4.1.html#new-features>`_
* `Brute-Force Attack Protection <https://docs.sqream.com/en/latest/releases/4.1.html#new-features>`_

:ref:`Version 4.0 - January 25, 2023<4.0>`

* `SQreamDB License Storage Capacity <https://docs.sqream.com/en/latest/releases/4.0.html#new-features>`_
* `LDAP Authentication <https://docs.sqream.com/en/latest/releases/4.0.html#new-features>`_
* `Physical Deletion Performance Enhancement <https://docs.sqream.com/en/latest/releases/4.0.html#new-features>`_


.. toctree::
   :maxdepth: 2
   :glob:
   :hidden:

   4.0_index
   2022.1_index

   
 
