.. _sap_universe_designer_tool:

*************************
Using the Universe Designer Tool
*************************

The **Information Design Tool (IDT)** supports the following:

.. contents::
   :local:
   :depth: 1

Overview
=====================
SAP Universe Design tool allows users to create, edit or delete existing models published in BO repository. With Universe Designer, you can build data foundation and business layer to meet your BI report requirements and perform different functions available in UDT tool before you develop BI reports and dashboards on top of these Universes. Universe Designer helps you to create semantic layer between your Relational database and BI tool.

With Universe Designer, you can build the semantic layer for non-SAP and SAP data sources to build data models for DB objects. Once Semantic later is built, you can publish it to BO server repository and it can be used by different users to create BI reports in Web intelligence/Desktop intelligence tool and also can be used with other SAP BusinessObjects tools.
   
Creating a Connection with the Universe Designer Tool 
--------------------------------------------------------
This section describes how to connect to SQream using the Universe Designer Tool.

**To create a connection with the Universe Designer Tool:**

1. Click **Universe Design Tool**.

    ::

2. Click *File* > *New*.

    ::

3. When the **Quick Design Wizard** is displayed, do one of the following:

    ::

   * Create a **new connection**:

     1. Create a universe by typing a name in the **Enter the universe name** field.
	 
	     ::
   
     2. Create a new connection by clicking **New**.
	 
	     ::
   
     3. Click **Next**.
	 
   * Use an **existing connection** by selecting one from the drop-down list located near the bottom of the wizard.

4. When the **Welcome to the New Connection Wizard (1/2)** window is displayed, from the **Connection Type** drop-down select **As Secured**.

    ::
	
5. From the **Connection Name** field, type a connection name.

    ::

6. Click **Next**.

    ::

7. When the **Database Middleware Selection (2/2)** window is displayed, select **SQream JDBC datasource**.

    ::

8. Click **Next**.

    ::

9. Provide the required credentials, described below:

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
		
10. *(Optional)* - Select **Test Connection** to verify that your connection is established, and click **Next**.

     ::

11. Do one of the following:

    * If your universe has been created, continue to Step 12.
	
	   ::
	   
    * If your universe has not been created, verify that all of the information above is correct and typed as described above, and that you've saved your jar file in the correct location. If you cannot connect after trying the above, contact a SQream support representative.

12. Publish your universe by navigating to *File* > *Export* and select an available domain from the list. **Comment** - *Please demonstrate.*

     ::

13. *(Optional)* Create a schema by doing the following:

    1. Click **Save**.
	
        ::

    2. Click **File**, save and enter (**Comment** - *enter and save?*) the name of the universe file, and click **Save**. **Comment** - *Convoluted, please demonstrate.*
	
14. Select one of the following connection types:

   * **Personal** - Personal connections are not used for building and distributing universes in your SAP BO environment. Personal connections are unsecured connections that are available to the users who create them on their local machine.

      ::

   * **Shared** - Shared connections are unsecured connections used for making data accessible to all users.

      ::

   * **Secured** - Secured connections are used for controlling data access, and are created using the **Universe Design Tool (UDT)**. SQream recommends using a secured connection for distributing a universe over a CMS. This options lets you set a password on any universe you've built over a Personal or Shared connection.
	
15. Set a password by navigating to *Tools* > *Options* > *Save*.

     ::

16. Do one of the following:

    * In the **Protection Password** field, type a protection password.
	
       ::
  
    * In the **Write Reservation Password** field, type a write reservation password.
	
.. note:: Your passwords can be a maximum of 40 alphanumeric characters.

17. Click **OK**.

**Comment** - *What happens when you click OK?*

18. From the menu, click **Insert** and select **Tables**.

    The **Table Browser** window is displayed.
	
19. Do one of the following:

**Comment** - *The action required in the first option is not clear. See source doc.*
	
     ::

   * Click the empty space on the right panel of the Table Browser.
	
      ::

   * Click **Table Browser**.
	
**Comment** - *I don't see a "Table Browser" button.*

     The Table Browser window is displayed.
	 
**Comment** - *This was getting convoluted here so I stopped. We need to review the steps in the source doc here together.*





 


For more information about the UDT, see :ref:`sap_connect_using_information_design_tool`.










