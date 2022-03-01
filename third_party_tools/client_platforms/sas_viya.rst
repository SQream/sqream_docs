.. _connect_to_sas_viya:

*************************
Connect to SQream Using SAS Viya
*************************

Overview
==========
SAS Viya is a cloud-enabled analytics engine used for procuding useful insights. The **Connecting to SQream Using SAS Viya** page describes how to connect to SAS Viya:

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
After installing SAS Viya, you must install the JDBC driver.

**To install the JDBC driver:**

#. Download the `JDBC driver <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    ::

#. Unzip the JDBC driver into a location on the SAS Viya server.
   
   SQream recommends creating the directory ``/opt/sqream`` on the SAS Viya server.
   
Configuring SAS Viya from the SAS Studio
---------------------
After installing the JDBC driver, you must configure the JDBC driver from the SAS Studio.

**To configure the JDBC driver from the SAS Studio:**

#. Sign in to the SAS Studio.

    ::

#. From the **New** menu, click **SAS Program**.
   
    ::  
   
#. Create a sample program to explore the data, as shown below: tt

   .. literalinclude:: connect_2.sas
      :language: php
      :emphasize-lines: 4
      :linenos:



   The sample program above does the following:
      
    * **Line 8**: Starts a JDBC session named ``sqlib`` associated with the SQream driver. This statement extends the SAS global ``libname`` statement so you can assign a **libref** to your data source. The libref feature lets you reference a table in SQream directly from a DATA step or SAS procedure.
	
     ::
	 
    * **Line 10**: Provides SAS Viya with the location of the SQream JDBC driver. This step is required because SAS Viya does not support the SAS_ACCESS_CLASSPATH environment variable for this connection.
	
     ::

    * **Lines 8-15**: Associates the libref with the SQream driver to be used as ``sqlib.tablename``. The libref is ``sqlib`` and uses the JDBC engine to connect to the ``sqream-cluster.piedpiper.com`` SQream cluster.
	
     ::

    * The database name is ``master`` and the schema is ``public``. 
	
      For more information about writing a connection string, see **Connect to SQream DB with a JDBC Application** and navigate to `Connection String <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-string>`_.

     ::
	 
    * **Lines 17-20**: Prepares data by loading it from the customer's table into the in-memory space in SAS Viya.
	
     ::
	 

     
    * **Lines 21-23**: DATA step. In this step, standard SAS naming conventions are used to reference the data, with ``sqlib`` as the libref and ``nba`` as the table name.

4. Run the program by clicking **Run**.

   The current SAS program is run.

   If the sample runs correctly, the following new tabs appear:
   
   * Log
   
   * Results
   
   * Output Data
   
   The query results are displayed in the **Results** tab, which shows your query results.

Operating SAS Viya
--------------------  
The **Operating SAS Viya** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Browsing Your Data and Workbooks
~~~~~~~~~~~~~~~~~~
After configuring the JDBC driver from the SAS Studio, you can browse your data and workbooks.

**To browse your data and workbooks:**

#. From the panel on the left, **Libraries**.

   The library that you created (``SQLIB``) is populated, and the ``nba`` table is displayed. You can double-click the table name to expand the table and show the columns.

    ::

#. Locate the workbook you created in the :ref:`data step <data_step>` in the **WORK** tree item.

   The workbook is named ``sqlib.nba``. You can double-click the table name to expand the table tree.
   
Using SAS Viya Visual Analytics
~~~~~~~~~~~~~~~~~~
This section describes how to use SAS visual analytics.

**To use SAS visual analytics:**

#. Log in to `SAS Visual Analytics <http://192.168.4.63/SASLogon/login>`_ using your credentials:

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
     - /opt/sqream/sqream-jdbc-4.5.0.jar   
   * - url
     - \jdbc:Sqream://<IP>:<port>/<database>;cluster=true
   * - username
     - sqream
   * - password
     - sqream
   
10. Click **Test Connection**.

     ::

11. If the connection is successful, click **Save**.

If your connection is not successful, see :ref:`best_practices_and_troubleshooting` below.

.. _best_practices_and_troubleshooting:

Best Practices and Troubleshooting
--------------------
The **Best Practices and Troubleshooting** section describes the following best practices and troubleshooting procedures when connecting to SQream using SAS Viya:

.. contents:: 
   :local:
   :depth: 1

Inserting Only Required Data
~~~~~~~~~~~~~~~~~~
When using Tableau, SQream recommends using only data that you need, as described below:

* Insert only the data sources you need into SAS Viya, excluding tables that don’t require analysis.

    ::


* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQream database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyze and increases query performance.

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