.. _sap_bo:


*************************
Connecting to SQream Using SAP BusinessObject
*************************
The SAP BusinessObjects Business Intelligence platform is a centralized suite for reporting, visualizing, and sharing data.

**Comment - Some of the steps may be incorrect because I did not have access to the GUI and the steps in the source document were unclear. This document needs to be reviwed.**

Getting Started
=======================

.. contents::
   :local:
   
   
Creating a Project Using the Information Design Tool
-----------------------
This section describes how to get started using the **Information Design Tool**.

**To create a project using the Information Design Tool:**

1. Open the Information Design Tool and create a new project named **UNI_relational_data**:

    ::

   1. Click **Information design tool**.
   
       ::
	   
   #. From the **File** menu, navigate to **New > Project**.
   
       ::

   #. Provide the project name and click **Finish**.

**Comment - Is it called the "Project" field?**

   ::
   
**Comment - The original document said, "The following screenshot shows you the summary of the preceding steps (creating a project in IDT):", but did not include a screenshot.**

.. note:: Your user credentials and other details depend on the database. You can access this information from your system administrator.

Creating a New Relational Connection
-----------------------
After creating a project using the Information Design Tool you must create a new relational connection.
 
**To create a new relational connection:**

1. Select the project you created in **Using the Information Design Tool**.

   **Comment - The previous section says to name the project "UNI_relational_data," but the step above refers to "UNI_SQreamDB". Which is the correct one?**

#. From the **File** menu, navigate to **New** > **Relational Connection**.

    ::
	
#. Do the following:

   1. In the **Source name** field enter **UNI_SQream_JDBC**.
   
       ::
	  
   2. Add a description.
   
       ::
	  
   3. Click **Next**.
	
#. Select **Generic** > **Generic JDBC Drivers** > **JDBC Drivers**.

    ::
	
#. Select **Next**.

    ::
	
#. Provide your credentials and click **Finish**.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Field
     - Description
   * - Authentication Mode
     - Provide your user name and password
   * - Data Source Reference
     - Use the selected data source reference
   * - User Name
     - Provide your SQreamdb username. If you leave this field blank you will be prompted to provide your username before the connection be completed.
   * - Password
     - Provide your password. If you leave this field blank you will be prompted to provide your password before the connection can be completed.
   * - JDBC URL
     - ``jdbc:Sqream://<host:port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...];`` . The IP must be a node in your SQream cluster. **Comment - What is...** The name or schema of the database you want to connect to. Verify that you have not used any leading or trailing spaces.	 
   * - com.sqream.jdbc.SQDriver
     - Verify that you have not used any leading or trailing spaces.

Creating a Shortcut in Your Local Folder
-----------------------
After creating a new relational connection you must create a shortcut in your local folder.

**To create a shortcut in your local folder:**

1. In your local folder menu click **Publish**.

   The connection to the BI platform repository and a shortcut in your local folder is made.

    ::
   
#. Select the project you created in **Using the Information Design Tool**.

    ::
	
#. From the **File** menu navigate to **Publish** > **Publish Connection to a Repository**.
 
    ::
	
#. Provide your credentials and choose to connect. **Comment - "choose to connect" = "select Connect"?**

    ::
	
#. Navigate to **Connection folder** > **Insert folder** > **Finish**.

    ::

#. Select **Yes**.

   The shortcut is created.

Creating a Single-Source Data Foundation
-----------------------
After creating a shortcut in your local folder you must create a single-source data foundation.

**To create a single-source data foundation:**

1. Create a single-source data foundation called **UNI_SQream** based on the secured version of the relational connection (.cns).

    ::
	
#. Include the NBA tables (download the table from the preceding link): **Comment - From which link?**
	
  1. Select the **UNI_SQreamDB** project.
  
      ::
	  
  #. From the **File** menu select **NewData Foundation**.

      ::
	
  #. In the **Resource Name** field enter **UNI_nba** and select **Next**.

      ::
	
  #. In the **Select Data Foundation** type dialog box select **single source radio**.
	 
	  ::
	  
  #. Click **Next**.

Creating a New Business Layer with a File
-----------------------
After creating a single-source data foundation you must crate a new business layer with a file.

**To create a new business layer with a file:**

**Comment - I need to see the GUI to write this procedure correctly.**
	
1. In the **Business Layer Filename** field, create a new business layer called **UNI_eFashion** for the UNI_eFashion data foundation.
	
    ::
	
#. Select the local project folder.

    ::
	
#. From the **File** menu select **New** > **Business Layer**.

    ::
	
#. Select **Relational Data Foundation** and click **Next**.
   
    ::
	   
#. In the **Resource Name** field enter **UNI_nba** and click **Next**.

    ::
	
#. In the **nba table**, set the primary keys for the database tables by right-clicking the fields and selecting **Set as Key** > **Primary**.

    ::

#. In the **Foundation** field, select the **UNI_nba data** foundation. 

    ::
	
#. Click **Finish** and **Save**.

    ::
	
#. In the **Business Layer** panel, select **UNI_nba** and click **Insert Object**.

    ::
	
#. Select **Folder**.

    ::
	
#. In the **Name** field type **NBA**.

    ::
	
#. Add the objects to folders. **Comment - This is unclear without seeing the GUI.**

Creating a Query on the Business Layer from the Query Panel
-----------------------
After creating a new business layer with a file you must create a query from the Query Panel and execute it. 

**To create a query on the business layer from the Query Panel:**

1. From the **Business Layer** panel select **Queries**.

    ::
	
#. Click **Insert Query**.

   The **Query Panel** is displayed.

#. Do the following:

   1. In the previous table, expand each of the listed folders.
   
       ::
	   
   2. Drag the corresponding dimension and measures to **Result Objects for Query Panel**.

#. Select **OK**.

    ::

#. Click **Execute Query** button.

   The query is executed.

#. Publish the Business Layer as a **Universe** to the BI platform repository:

   1. From the **File** menu select the **UNI_SQreamDB** and click **Save All**. **Comment - I need to verify this on the GUI. This step was unclear.**
   
       ::

   #. Right-click **UNI_nba** and navigate to **Publish** > **To a Repository**.

       ::

   #. Select **Check all**.

       ::
	 
   #. Click **Check Integrity** and click **Next**.

       ::

   #. Click **Finish**.

      A Universe is created with an IDT that accesses the SQream database.