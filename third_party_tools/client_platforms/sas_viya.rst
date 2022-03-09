.. _connect_to_sas_viya:

*************************
Connect to SQream Using SAS Viya
*************************

Overview
==========
SAS Viya is a cloud-enabled analytics engine used for producing useful insights. The **Connect to SQream Using SAS Viya** page describes how to connect to SAS Viya, and describes the following:

.. contents:: 
   :local:
   :depth: 1

Installing SAS Viya
-------------------
The **Installing SAS Viya** section describes the following:

.. contents:: 
   :local:
   :depth: 1 

Downloading SAS Viya
~~~~~~~~~~~~~~~~~~
Integrating with SQream has been tested with SAS Viya v.03.05 and newer.

To download SAS Viya, see `SAS Viya <https://www.sas.com/en_us/software/viya.html>`_.

Installing the JDBC Driver
~~~~~~~~~~~~~~~~~~
The SQream JDBC driver is required for establishing a connection between SAS Viya and SQream.

**To install the JDBC driver:**

#. Download the `JDBC driver <https://docs.sqream.com/en/v2020.3/third_party_tools/client_drivers/jdbc/index.html>`_.

    ::

#. Unzip the JDBC driver into a location on the SAS Viya server.
   
   SQream recommends creating the directory ``/opt/sqream`` on the SAS Viya server.
   
Configuring SAS Viya
-------------------
After installing the JDBC driver, you must configure the JDBC driver from the SAS Studio so that it can be used with SQream Studio.

**To configure the JDBC driver from the SAS Studio:**

#. Sign in to the SAS Studio.

    ::

#. From the **New** menu, click **SAS Program**.
   
    ::
	
#. Configure the SQream JDBC connector by adding the following rows:

   .. literalinclude:: connect3.sas
      :language: php

For more information about writing a connection string, see **Connect to SQream DB with a JDBC Application** and navigate to `Connection String <https://docs.sqream.com/en/v2020.3/third_party_tools/client_drivers/jdbc/index.html#connection-string-examples>`_.

Operating SAS Viya
--------------------  
The **Operating SAS Viya** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Using SAS Viya Visual Analytics
~~~~~~~~~~~~~~~~~~
This section describes how to use SAS Viya Visual Analytics.

**To use SAS Viya Visual Analytics:**

#. Log in to `SAS Viya Visual Analytics <http://192.168.4.63/SASLogon/login>`_ using your credentials:

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
     - com.sqream.jdbc.SQDriver
   * - classPath
     - *<path_to_jar_file>*   
   * - url
     - \jdbc:Sqream://*<IP>*:*<port>*/*<database>*;cluster=true
   * - username
     - <username>
   * - password
     - <password>
   
10. Click **Test Connection**.

     ::

11. If the connection is successful, click **Save**.

If your connection is not successful, see :ref:`troubleshooting_sas_viya` below.

.. _troubleshooting_sas_viya:

Troubleshooting SAS Viya
-------------------------
The **Best Practices and Troubleshooting** section describes the following best practices and troubleshooting procedures when connecting to SQream using SAS Viya:

.. contents:: 
   :local:
   :depth: 1

Inserting Only Required Data
~~~~~~~~~~~~~~~~~~
When using SAS Viya, SQream recommends using only data that you need, as described below:

* Insert only the data sources you need into SAS Viya, excluding tables that don’t require analysis.

    ::

* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQream database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyzed and increases query performance.

Creating a Separate Service for SAS Viya
~~~~~~~~~~~~~~~~~~
SQream recommends creating a separate service for SAS Viya with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

Locating the SQream JDBC Driver
~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~
In SAS Viya versions lower than 4.0, casting ``TEXT`` to ``CHAR`` changes the size to 1,024, such as when creating a table including a ``TEXT`` column. This is resolved by casting ``TEXT`` into ``CHAR`` when using the JDBC driver.