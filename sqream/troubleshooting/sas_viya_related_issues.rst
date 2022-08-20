.. _sas_viya_related_issues:

***********************
SAS Viya Related Issues
***********************

This section describes the following best practices and troubleshooting procedures when connecting to SQream using SAS Viya:

.. contents::
   :local:

Inserting Only Required Data
------
When using Tableau, SQream recommends using only data that you need, as described below:

* Insert only the data sources you need into SAS Viya, excluding tables that don’t require analysis.

    ::


* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQream database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyze and increases query performance.


Creating a Separate Service for SAS Viya
------
SQream recommends creating a separate service for SAS Viya with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

Locating the SQream JDBC Driver
------
In some cases, SAS Viya cannot locate the SQream JDBC driver, generating the following error message:

.. code-block:: text

   java.lang.ClassNotFoundException: com.sqream.jdbc.SQDriver

**To locate the SQream JDBC driver:**

1. Verify that you have placed the JDBC driver in a directory that SAS Viya can access.

    ::


2. Verify that the classpath in your SAS program is correct, and that SAS Viya can access the file that it references.

    ::


3. Restart SAS Viya.

For more troubleshooting assistance, see the `SQream Support Portal <https://sqream.atlassian.net/servicedesk/customer/portals>`_.


Supporting TEXT
------
In SAS Viya versions lower than 4.0, casting ``TEXT`` to ``CHAR`` changes the size to 1,024, such as when creating a table including a ``TEXT`` column. This is resolved by casting ``TEXT`` into ``CHAR`` when using the JDBC driver.
