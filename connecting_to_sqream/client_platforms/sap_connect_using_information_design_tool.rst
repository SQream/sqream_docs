.. _sap_connect_using_information_design_tool:

*************************
Using the Information Design Tool
*************************
The Connecting to SQream Using the **Information Design Tool (IDT)** describes the following:

.. contents::
   :local:
   :depth: 1

Establishing a Connection between SQream and SAP BusinessObjects
================
This section describes how to establish a connection between SQream and SAP BusinessObjects platform using the **Information Design Tool (IDT)**.

**To establish a connection using the IDT:**

1. Click **Information design tool**.
   
    ::
   
2. From the menu, click **File** and navigate to **New** > **Project**.
  
    ::
	
3. Type a project name (such as *UNI_SQreamDB*) and click **Finish**.  

    ::
	
   Your new project is created.
   
Creating a New Relational Connection
================
This section describes how to create a new relational connection. The user credentials and other information used to create your new relational connection depend on which database you use. Contact your system administrator for the information required to create a new relational connection.

**To create a new relational connection:**

1. Click the new project you created in **Establishing a Connection between SQream and SAP BusinessObjects** above.

    ::
	
2. From the menu, click **File** and navigate to **New** > **Relational Connection**.

    ::
	
3. In the **Source name** field, type **UNI_SQream_JDBC** and type a description.

    ::
	
4. Click **Next**.

    ::
	
5. Provide the required credentials, described below:

   .. list-table:: 
      :widths: 6 31
      :header-rows: 1
   
      * - **Field**
        - **Description**
      * - Authentication Mode
        - Provide your username and password.
      * - Data Source Reference
        - Use the displayed data source reference.
      * - User Name
        - Provide your SQreamdb user name. If you leave this blank, SAP BusinessObjects will prompt you to provide it when you connect.
      * - Password
        - Provide the password for your SQreamdb user name. If you leave this blank, SAP BusinessObjects will prompt you to provide it when you connect.
      * - JDBC URL
        - Provide your JDBC URL: **jdbc:Sqream://<host:port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...];** . The IP is a node in your SQream cluster. The name or schema of the database you want to connect to. Verify that you have not used any leading or trailing spaces. For more information, see `Connection String Parameters <https://docs.sqream.com/en/page_updater/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string-examples>`_.
      * - JDBC Class
        - Provide your JDBC class: com.sqream.jdbc.SQDriver. Verify that you have not used leading or trailing spaces.

6. Select **Test Connection** to verify that your connection is established.

   If your connection is established, the **Test Successful** message is displayed.
   
   If your connection is not established, do the following:
   
   1. Verify that all of the information above is correct and typed as described above.
   
       ::
	   
   2. Verify that you've saved your jar file in the correct location.
   
      If you cannot connect after trying the above, contact a SQream support representative.

Creating a Shortcut in Your Local Folder
================
This section describes how to create a shortcut in your local folder after publishing your connection to the BI platform repository.

**To create a shortcut in your local folder:**

1. Select the **UNI_SQream_JDBC** relational connection you created in **Creating a New Relational Connection** above.

    ::
	
2. From the menu, click **File** and navigate to **Publish** > **Publish Connection to a Repository**.

    ::
	
3. Provide your credentials and click **Connect**.

    ::
	
4. Click **Yes.**

   Your shortcut is created.

Creating a Single-Source Data Foundation
================
This section describes how to create a single-source data foundation called **UNI_SQream** based on the secure version of relational connection you created in the **Creating a New Relational Connection** section. The secure version of your relational connection is saved with the **.cns** file extension.

**Comment** - *Regarding .cns, confirm that this is what you meant.*

**To create a single-source data foundation:**

1. Include the  NBA tables (download the table from the preceding link).

    ::
	
**Comment** - *The above is unclear. Please demonstrate.*

2. Select the **UNI_SQreamDB** project and navigate to *File* > *NewData Foundation*.

    ::
	
3. Type **UNI_nba** as the resource name and click **Next**.

**Comment** - *We're only using the nba table as an example, correct? The user can use any resource name during this step...*

**Comment** - *What is the result?*

Creating a New Business Layer Using a File
================
**Comment** - *Why does it say "using a file"? Please demonstrate.*

After creating a single-source data foundation, you must create a new business layer called **UNI_eFashion** for the **UNI_eFashion** data foundation.

**Comment** - *The previous section doesn't say anything about UNI_eFashion, so why are we mentioning it in the line above?*

**To create a new business layer using a file:**

1. Select the local project folder called **UNI_relational_data**.

    ::
	
2. From the menu, click **File** and navigate to **New** > **Business Layer**.

    ::
	
3. Click **Relational Data Foundation** and click **Next**.

    ::
	
4. In the **Resource Name** field type **UNI_nba** and click **Next**.

   .. note:: You must set the primary keys for the database tables. In the **nba** table, you must set the **namefield** as the primary key by right-clicking the fields and selecting **Set as Key | Primary**.

   **Comment** - *Please demonstrate what the above note says.*

5. Select the **UNI_nba** data foundation.

    ::
	
6. Click **Finish** and **Save**.

    ::
	
7. In the **Business Layer** panel, click **UNI_nba** and click the arrow next to the **Insert Object** button.

    ::
	
8. Click **Folder**.

    ::
	
9. In the **Name** field, type **NBA**.

    ::
	
10. Add objects to your folders.

   A new business layer is created.
   
Creating a Query on the Business Layer Using the Query Panel
================
After creating a new business layer, you must create a query on the business layer you created in the previous section using the Query panel. After creating your query you can execute it.

**To create a query on your business layer using the Query panel:**

1. From the **Business Layer** panel, click **Queries**.

**Comment** - *From the Queries panel, select Business Layer and click Queries.*

2. Click **Insert Query** to display the Query Panel.

    ::
	
3. Do the following:

   1. Expand each of the folders listed in the previous table.
   
      **Comment** - *Which table?*.
   
       ::
	
   2. Drag the corresponding dimensions and measures to **Result Objects** to **Query Panel**.
   
      **Comment** - *Demonstrate.*
   
4. Click **OK**.

    ::
	
5. Execute the query by clicking **Execute Query**.

   The query is executed.
   
6. Publish the **Business Layer** as a **Universe** to the BI platform repository:

   **Comment** - *Demonstrate* 

   1. Click the project called **UNI_SQreamDB**.
   
       ::
	
   2. Navigate to *File* > *Save All*.
   
      **Comment** - *Confirm, was unclear in source doc.*
   
       ::
	
   3. Right-click **UNI_nba** and navigate to *Publish* > *To a Repository*.
   
       ::
	
   4. Click **Check all**.
   
       ::
	
   5. Click **Check Integrity** and click **Next**.
   
       ::
	
   6. Click **Finish**.
   
      A Universe is created with the IDT that accesses a SQream database.