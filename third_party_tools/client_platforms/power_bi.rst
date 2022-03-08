.. _power_bi:

*************************
Connect to SQream Using PowerBI
*************************

Overview
=========
**Comment** - After seeing Inon's PowerBI Specs doc, I added the **Best Practices** section. This should be added to the template. I also added the **Related Information** section and created a link to the updated `Glossary <https://docs.sqream.com/en/v2020-1/glossary.html>`_.

SQream integrates with **Power BI** do the following:

* Extract and transform your datasets into usable visual models in approximately one minute.

   ::

* Use **DAX** functions **(Data Analysis Expressions)** to analyze your datasets.

   ::

* Refresh datasets as needed or by using scheduled jobs.

SQream uses Power BI for extracting data sets using the following methods:

* **Direct query** - Direct queries lets you connect easily with no errors, and refreshes PowerBI artifacts, such as graphs and reports, in a considerable amount of time in relation to the time taken for queries to run using the `SQream SQL CLI Reference guide <https://docs.sqream.com/en/v2020-1/reference/cli/sqream_sql.html>`_. **Comment** - Do we want to mention in-memory here?

   ::

* **Import** - Lets you extract datasets from remote databases.

The **Connect to SQream Using Power BI** page describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Prerequisites
-------------------
To connect to SQream, the following must be installed:

* **ODBC data source administrator** - 32 or 62, depending on your operating system. For Windows users, the ODBC data source administrator is embedded within the operating system.

* **SQream driver** - The SQream application required for interacting with the ODBC according to the configuration specified in the ODBC administrator tool. This driver was built using the third party utility Simba, and is used to interact with the ODBC stack. **Comment** - Do we need the last sentence in this bullet, "This driver was built..."?

* **Configuration per the remote DB configured** - **Comment** - Unclear.

Installing Power BI
-------------------
**To install Power BI:**

1. Download `Power BI 64x <https://powerbi.microsoft.com/en-us/downloads/>`_.

    ::

2. Configure your ODBC driver.

   For more information about configuring your ODBC driver, see `ODBC <https://docs.sqream.com/en/v2020-1/third_party_tools/client_drivers/odbc/index.html>`_.  
  
3. Navigate to **File** > **Options and Settings** > **Option** > **Security** > **Data Extensions**, and click **(Not Recommended) Allow any extension to load without validation or warning**.

    ::

4. Close all open Power BI windows.

    ::

5. In **Windows Documents**, create a folder called **Power BI Desktop\Custom Connectors**.

    ::

6. From the **Client Drivers** page, download the SQream Custom Connector.

    ::

7. Save your **.mez** file in the **Power BI Desktop\Custom Connectors** folder you created in Step 5.

    ::

8. Open the **Power BI** application.

    ::

9. From the **Get Data** menu, click **SQream**.

    ::

10. Click **Connect** and provide the information shown in the following table:
    
   .. list-table:: 
      :widths: 6 31
      :header-rows: 1
   
      * - Element Name
        - Description
      * - Server
        - Provide the network address to your database server. You can use a hostname or an IP address. 
      * - Port
        - Provide the port that the database is responding to at the network address.
      * - Database
        - Provide the name of your database or the schema on your database server.
      * - User
        - Provide a SQreamdb username.
      * - Password
        - Provide a password for your user.

11. Under **Data Connectivity mode**, select **DierctQuery mode**.

     ::

12. Click **Connect**.

     ::

13. Provide your user name and password and click **Connect**.

Configuring Power BI
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Launching Power BI
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Operating Power BI
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Troubleshooting Power BI
-------------------------
**Comment** - The PowerBI Specs doc includes "When configure costume port (3108)- error pops up". Do we want to include this in this doc? If so, we need to include its resolution.

The **Troubleshooting Power BI** section describes the following best practices and troubleshooting procedures when connecting to SQream using Power BI:

.. contents:: 
   :local:
   :depth: 1

Enabling Querying Data Sets with More Than 100,000 Rows
~~~~~~~~~~~~~~~~
This section describes how to troubleshoot query result sets coming from an external data source that exceeds 100,000 rows.

**Comment** - The Known Limitations section in the **PowerBI Specs** doc says "1 million rows" instead of 100,000. Please verify the correct one: https://sqream.atlassian.net/wiki/spaces/PRODUCT/pages/2126774305/PowerBI+Specs

**To enable querying a data set with more than 100,000 rows**:

1. Create a rank column, as shown below:

   .. code-block:: console
   
      Rank= RANKX(FILTER(Table1 ,Table1 [Order# ]=EARLIER(Table1 [Order# ])),Table1 [Sales],, Desc, Dense)
	  
2. Create a filtered measure, as shown below:

   .. code-block:: console
   
      Filter1= IF(MAX(Table1[Rank])<=1000000, 1, BLANK())
	  
Importing Only Required Databases
~~~~~~~~~~~~~~~~~~~~~~	  
This section describes how to troubleshoot the scenario where the connector imports all databases, including those that were not configured.

This occurs when you select a table from an unconfigured database, resulting in the following error message:

.. code-block:: console
   
   DataSource.Error: ODBC: ERROR [HY000] [SQream DB Server][UltraLight] (1050) ..\SQream-cpp-connector.cc:1557 in sqream::new_query_execute(): ..\SQream-cpp-connector.cc:361 in sqream::connector::prepare_statement() returned error from SQream: Cannot access database 'nonmaster' from current database 'master'
   Details:
       DataSourceKind=SQreamODBC
       DataSourcePath={"server":"192.168.1.176","Port":5000,"Database":"master","User":"sqream","Password":"sqream"}
       OdbcErrors=[Table]

Best Practices for Power BI
---------------
SQream recommends using Power BI in the following ways for acquiring the best performance metrics:

* Creating bar, pie, line, or plot charts when illustrating one or more columns.

   ::
   
* Displaying trends and statuses using visual models.

   ::
   
* Creating a unified view using power queries to connect different data sources into a single dashboard.	   

Supported SQream Driver Versions
---------------
**Comment**- Do we need this section? If so, it belongs in **Overview**.

SQream supports the following SQream driver versions: 

* The Custom Connector is an additional layer on top of the ODBC. 

    ::

* SQream Driver Installation (ODBC v4.1.1) - **Comment** - Do we have a direct link to this? Our Drivers page has a link to **sqream_odbc_4.0.0_x86_64_linux.tar.gz**.

Related Information
-------------------
For more information, see the `Glossary <https://docs.sqream.com/en/v2020-1/glossary.html>`_.