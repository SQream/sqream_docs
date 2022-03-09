.. _power_bi:

*************************
Connect to SQream Using Power BI Desktop
*************************

Overview
=========
**Power BI Desktop** lets you connect to SQream and use underlying data as with other data sources in Power BI Desktop.

SQream integrates with Power BI Desktop to do the following:

* Extract and transform your datasets into usable visual models in approximately one minute.

   ::

* Use **DAX** functions **(Data Analysis Expressions)** to analyze your datasets.

   ::

* Refresh datasets as needed or by using scheduled jobs.

SQream uses Power BI for extracting data sets using the following methods:

* **Direct query** - Direct queries lets you connect easily with no errors, and refreshes Power BI artifacts, such as graphs and reports, in a considerable amount of time in relation to the time taken for queries to run using the `SQream SQL CLI Reference guide <https://docs.sqream.com/en/v2021.2/reference/cli/sqream_sql.html>`_.

   ::

* **Import** - Lets you extract datasets from remote databases.

The **Connect to SQream Using Power BI** page describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Prerequisites
-------------------
To connect to SQream, the following must be installed:

* **ODBC data source administrator** - 32 or 64, depending on your operating system. For Windows users, the ODBC data source administrator is embedded within the operating system.

* **SQream driver** - The SQream application required for interacting with the ODBC according to the configuration specified in the ODBC administrator tool.

Installing Power BI Desktop
-------------------
**To install Power BI Desktop:**

1. Download `Power BI Desktop 64x <https://powerbi.microsoft.com/en-us/downloads/>`_.

    ::

2. Download and configure your ODBC driver.

   For more information about configuring your ODBC driver, see `ODBC <https://docs.sqream.com/en/v2021.2/third_party_tools/client_drivers/odbc/index.html>`_.
   
3. Navigate to **Windows** > **Documents** and create a folder called **Power BI Desktop Custom Connectors**.

    ::
	
4. In the **Power BI Desktop** folder, create a folder called **Custom Connectors**.


5. From the Client Drivers page, download the **PowerQuery.mez** file.

    ::

5. Save the PowerQuery.mez file in the **Custom Connectors** folder you created in Step 3.

    ::

6. Open the Power BI application.

    ::

7. Navigate to **File** > **Options and Settings** > **Option** > **Security** > **Data Extensions**, and select **(Not Recommended) Allow any extension to load without validation or warning**.

    ::

8. Restart the Power BI Desktop application.

    ::

9. From the **Get Data** menu, select **SQream**.

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
      * - Passwords
        - Provide a password for your user.

11. Under **Data Connectivity mode**, select **DirectQuery mode**.

     ::

12. Click **Connect**.

     ::

13. Provide your user name and password and click **Connect**.

Best Practices for Power BI
---------------
SQream recommends using Power BI in the following ways for acquiring the best performance metrics:

* Creating bar, pie, line, or plot charts when illustrating one or more columns.

   ::
   
* Displaying trends and statuses using visual models.

   ::
   
* Creating a unified view using **PowerQuery** to connect different data sources into a single dashboard.	   

Supported SQream Driver Versions
---------------
SQream supports the following SQream driver versions: 

* The **PowerQuery Connector** is an additional layer on top of the ODBC. 

    ::

* SQream Driver Installation (ODBC v4.1.1) - Contact your administrator for the link to download ODBC v4.1.1.

Related Information
-------------------
For more information, see the `Glossary <https://docs.sqream.com/en/v2021.2/glossary.html>`_.