.. _connect_to_sas_viya:

********
SAS Viya
********

SAS Viya is a cloud-enabled analytics engine used for producing useful insights.

.. contents:: 
   :local:
   :depth: 1

Installing SAS Viya
===================

The **Installing SAS Viya** section describes the following:

Downloading SAS Viya
--------------------

Integrating with SQreamDB has been tested with SAS Viya v.03.05 and newer.

To download SAS Viya, see `SAS Viya <https://www.sas.com/en_us/software/viya.html>`_.

Installing the JDBC Driver
----------------------------

The SQreamDB JDBC driver is required for establishing a connection between SAS Viya and SQreamDB.

**To install the JDBC driver:**

#. Download the :ref:`JDBC driver<java_jdbc>`.

    ::

#. Unzip the JDBC driver into a location on the SAS Viya server.
   
   SQreamDB recommends creating the directory ``/opt/sqream`` on the SAS Viya server.
   
Configuring SAS Viya
======================

After installing the JDBC driver, you must configure the JDBC driver from the SAS Studio so that it can be used with SQreamDB BStudio.

**To configure the JDBC driver from the SAS Studio:**

#. Sign in to the SAS Studio.

    ::

#. From the **New** menu, click **SAS Program**.
   
    ::
	
#. Configure the SQreamDB JDBC connector by adding the following rows:

   .. literalinclude:: connect3.sas
      :language: php

Operating SAS Viya
===================
 
The **Operating SAS Viya** section describes the following:
   
Using SAS Viya Visual Analytics
-----------------------------------

This section describes how to use SAS Viya Visual Analytics.

**To use SAS Viya Visual Analytics:**

#. Log in to SAS Viya Visual Analytics using your credentials:

    ::

2. Click **New Report**.

    ::

3. Click **Data**.

    ::

4. Click **Data Sources**.

    ::

5. Click the **Connect** icon.

    ::

6. From the **Type** menu, select **Database**.

    ::

7. Provide the required information and select **Persist this connection beyond the current session**.

    ::

8. Click **Advanced** and provide the required information.

    ::

9. Add the following additional parameters by clicking **Add Parameters**:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - Name
     - Value
   * - class
     - ``com.sqream.jdbc.SQDriver``
   * - classPath
     - ``<path_to_jar_file>``   
   * - url
     - ``\jdbc:Sqream://*<IP>*:*<port>*/*<database>*;cluster=true``
   * - username
     - ``<username>``
   * - password
     - ``<password>``
   
10. Click **Test Connection**.

     ::

11. If the connection is successful, click **Save**.


.. _troubleshooting_sas_viya:

Troubleshooting SAS Viya
==========================

The **Best Practices and Troubleshooting** section describes the following best practices and troubleshooting procedures when connecting to SQreamDB using SAS Viya:

Inserting Only Required Data
-------------------------------

When using SAS Viya, SQreamDB recommends using only data that you need, as described below:

* Insert only the data sources you need into SAS Viya, excluding tables that don’t require analysis.

    ::

* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQreamDB database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyzed and increases query performance.

Creating a Separate Service for SAS Viya
------------------------------------------

SQreamDB recommends creating a separate service for SAS Viya with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

Locating the SQreamDB JDBC Driver
----------------------------------

In some cases, SAS Viya cannot locate the SQreamDB JDBC driver, generating the following error message:

.. code-block:: text

   java.lang.ClassNotFoundException: com.sqream.jdbc.SQDriver

**To locate the SQreamDB JDBC driver:**

1. Verify that you have placed the JDBC driver in a directory that SAS Viya can access.

    ::

2. Verify that the classpath in your SAS program is correct, and that SAS Viya can access the file that it references.

    ::

3. Restart SAS Viya.

For more troubleshooting assistance, see the `SQreamDB Support Portal <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.

Supporting TEXT
-----------------

In SAS Viya versions lower than 4.0, casting ``TEXT`` to ``CHAR`` changes the size to 1,024, such as when creating a table including a ``TEXT`` column. This is resolved by casting ``TEXT`` into ``CHAR`` when using the JDBC driver.