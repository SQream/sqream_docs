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
	
5. Navigate to *Generic* > *Generic JDBC Drivers* > *JDBC Drivers* and click **Next**.

    ::
	
6. Provide the required credentials, described below:

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
		
7. Click **Finish**.

    ::

8. Select **Test Connection** to verify that your connection is established.

   If your connection is established, the **Test Successful** message is displayed.
   
   If your connection is not established, do the following:
   
   1. Verify that all of the information above is correct and typed as described above.
   
       ::
	   
   2. Verify that you've saved your jar file in the correct location.
   
      If you cannot connect after trying the above, contact a SQream support representative.