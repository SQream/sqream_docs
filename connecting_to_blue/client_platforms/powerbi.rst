:orphan:

.. _powerbi_desktop:

**********************
PowerBI Desktop
**********************

**Power BI Desktop** lets you connect to SQream Blue and use underlying data as with other data sources in Power BI Desktop.

SQream Blue integrates with Power BI Desktop to do the following:

* Extract and transform your datasets into usable visual models in approximately one minute.

* Use **DAX** functions **(Data Analysis Expressions)** to analyze your datasets.

* Refresh datasets as needed or by using scheduled jobs.

SQream Blue uses Power BI for extracting data sets using the following methods:

* **Direct query** - Direct queries is the recommnended method for optimized performance.

* **Import** - Lets you extract datasets from remote databases.

The **Connect to SQream Blue Using Power BI** page describes the following:


Installing Power BI Desktop
---------------------------

**To install Power BI Desktop:**

#. Download `Power BI Desktop 64x <https://powerbi.microsoft.com/en-us/downloads/>`_.

#. Download and configure the :ref:`ODBC<odbc_windows>` driver.
   
#. Navigate to **Windows** > **Documents** and create a folder named **Power BI Desktop** with a subfolder named **Custom Connectors**.

#. Download the `Power BI file <https://sq-ftp-public.s3.amazonaws.com/SqreamBlue.mez>`_ .

#. Save the SqreamBlue.mez file in the **Custom Connectors** folder you created in Step 3.

#. Open the Power BI application.

#. Navigate to **File** > **Options and Settings** > **Option** > **Security** > **Data Extensions**, and select **(Not Recommended) Allow any extension to load without validation or warning**.

#. Restart the Power BI Desktop application.

#. From the **Get Data** menu, select **SQream Blue**.

#. Click **Connect** and provide the information shown in the following table:

.. list-table:: 
      :widths: 6 31
      :header-rows: 1
   
      * - Element Name
        - Description
      * - Server
        - Provide the network address to your database server. Use the SQream Blue cluster URL 
      * - Port
        - Provide the port that the database is responding to at the network address.
      * - Database
        - Provide the name of your database or the schema on your database server.
      * - Token
        - Provide an :ref:`access token<access_tokens>` to SQream Blue.


#. Under **Data Connectivity mode**, select **DirectQuery mode**.

#. Click **Connect**.

#. Provide your user name and password and click **Connect**.

Best Practices for Power BI
---------------------------

SQream recommends using Power BI in the following ways for acquiring the best performance metrics:

* Creating bar, pie, line, or plot charts when illustrating one or more columns.
   
* Displaying trends and statuses using visual models.
   
* Creating a unified view using **PowerQuery** to connect different data sources into a single dashboard.	   

