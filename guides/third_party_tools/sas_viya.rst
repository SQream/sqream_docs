.. _connect_to_sas_viya:

*************************
Connecting to SAS Viya
*************************

You can use SAS Viya to connect to a SQream DB cluster. This tutorial is a guide that will show you how to connect to SAS Viya.

.. contents:: In this topic:
   :local:

Installing SAS Viya
============================
Integrating with SQream has been tested with SAS Viya v.03.05 and newer.

To install SAS Viya, see `SAS Viya <https://www.sas.com/en_us/software/viya.html>`_.

Installing the JDBC Driver
=================================================
After installing SAS Viya, you must install the JDBC driver.

**To install the JDBC driver:**

#. Download the `JDBC driver <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html>`_.

#. Unzip the JDBC driver into a location on the SAS Viya server.
   
   SQream recommends creating the directory ``/opt/sqream`` on the SAS Viya server.
   
Configuring the JDBC Driver from the SAS Studio
====================================================
After installing the JDBC driver, you must configure the JDBC driver from the SAS Studio.

**To configure the JDBC driver from the SAS Studio:**

#. Sign in to the SAS Studio.

    ::

#. From the **New** menu, click **SAS Program**.
   
    ::  
   
#. Create a sample program to explore the data, as shown below:

   .. literalinclude:: connect_2.sas
      :language: sas
      :caption: Sample SAS Program
      :linenos:
      :emphasize-lines: 9

   The sample program above does the following:
      
    * **Line 8**: Starts a JDBC session named ``sqlib`` associated with the SQream driver. This statement extends the SAS global ``libname`` statement so you can assign a **libref** to your data source. The libref feature lets you reference a table in SQream directly from a DATA step or SAS procedure.
	
     ::
	 
    * **Line 10**: Provides SAS Viya with the location of the SQream JDBC driver. This step is required because SAS Viya does not honor the SAS_ACCESS_CLASSPATH environment variable for this connection. **Comment** - *Using the word "honor" is strange in this context. Let's discuss this.*
	
     ::

    * **Lines 8-15**: Associates the libref **Comment** - *with what?* to be used as ``sqlib.tablename``. The libref is ``sqlib`` **Comment** - *only in the example above, or in general?* and uses the JDBC engine to connect to the ``sqream-cluster.piedpiper.com`` SQream cluster.
	
     ::

    * The database name is ``raviga`` and the schema is ``public``. 
	
      For more information about writing a connection string, see **Connect to SQream DB with a JDBC Application** and nagivate to `Connection String <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-string>`_.

     ::
         
    * **Lines 17-20**: Prepares data by loading it from the customer's table into the in-memory space in SAS Viya.
	
	 ::
	 
.. _data_step:
     
    * **Lines 21-23**: DATA step. **Comment** - *What was meant by "data step?"* In this step, standard SAS naming conventions are used to reference the data, with ``sqlib`` as the libref and ``customers`` as the table **Comment** - *...as the table name?*.

#. Run the program by clicking **Run**.

   The current SAS program is run.

   If the sample runs correctly, the following new tabs appear:
   
   * Log
   
   * Results
   
   * Output Data
   
   The query results are displayed in the **Results** tab, which shows your query results.   

Browsing Your Data and Workbooks
========================================
After configuring the JDBC driver from the SAS Studio, you can browse your data and workbooks.

**To browse your data and workbooks:**

#. From the panel on the left, navigate to (**Comment** - *Click on?*) **Libraries** to open the navigation tree.

   The library that you created (``SQLIB``) is populated, and the ``customers`` table is displayed. You can double-click the table name to expand the table and show the columns.

    ::

#. Locate the workbook you created in the :ref:`data step <data_step>`. It should appear under ``WORK``. **Comment** - *Please demonstrate. Is "WORK" a folder?*

   The workbook is named ``sqlib.customers``. You can double-click the table name to expand the table tree.

Best Practices and Troubleshooting
=================================================
This section describes the following best practices and troubleshooting procedures when connecting to SQream using SAS Viya:

.. contents::
   :local:

Inserting Only Required Data
------------------------------
When using Tableau, SQream recommends using only data that you need, as described below:

* Insert only the data sources you need into SAS Viya, excluding tables that don’t require analysis.

* To increase query performance, add filters before analyzing. Every modification you make while analyzing data queries the SQream database, sometimes several times. Adding filters to the datasource before exploring limits the amount of data analyze and increases query performance.

**Comment** - *I took this from Tableau, which was virtually identical.*

Creating a Separate Service for SAS Viya
----------------------------------------
SQream recommends creating a separate service for SAS Viya with the DWLM. This reduces the impact that Tableau has on other applications and processes, such as ETL. In addition, this works in conjunction with the load balancer to ensure good performance.

Locating the SQream JDBC Driver
--------------------------------------------------------------------------------------------------------
In some cases, SAS Viya cannot locate the SQream JDBC driver, generating the following error message:

.. code-block:: text

   java.lang.ClassNotFoundException: com.sqream.jdbc.SQDriver

**To locate the SQream JDBC driver:**

#. Verify that you have placed the JDBC driver in a directory that SAS Viya can access.

2. Verify that the classpath in your SAS program is correct, and that SAS Viya can access the file that it references.

3. Restart SAS Viya.

For more troubleshooting assistance, see the `SQream support portal <https://support.sqream.com>`_.