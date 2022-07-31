.. _informatica:

*************************
Connecting to SQream Using Informatica Cloud Services
*************************

Overview
=========
The **Connecting to SQream Using Informatica Cloud Services** page is quick start guide for connecting to SQream using Informatica cloud services.

It describes the following:

.. contents::
   :local:

Establishing a Connection between SQream and Informatica
-----------------
The **Establishing a Connection between SQream and Informatica** page describes how to establish a connection between SQream and the Informatica data integration Cloud.

**To establish a connection between SQream and the Informatica data integration Cloud:**

1. Go to the `Informatica Cloud homepage <https://emw1.dm-em.informaticacloud.com/diUI/products/integrationDesign/main/home>`_.

    ::

2. Do one of the following:

   1. Log in using your credentials.
   
    ::

   2. Log in using your SAML Identity Provider.
   
3. From the **Services** window, select **Administrator** or click **Show all services** to show all services.


   The SQream dashboard is displayed.
   
     
    ::
   

4. In the menu on the left, click **Runtime Environments**.


   The **Runtime Environments** panel is displayed.

     ::

5. Click **Download Secure Agent**.

    ::

6. When the **Download the Secure Agent** panel is displayed, do the following:

    1. Select a platform (Windows 64 or Linux 64).
	
     ::

	
    2. Click **Copy** and save the token on your local hard drive.
	
       The token is used in combination with your user name to authorize the agent to access your account.
	

7. Click **Download**.

   The installation begins.
   
     ::

8. When the **Informatica Cloud Secure Agent Setup** panel is displayed, click **Next**.


    ::


9. Provide your **User Name** and **Install Token** and click **Register**.

    ::



10. From the Runtime Environments panel, click **New Runtime Environment**.


    The **New Secure Agent Group** window is displayed.
	
     ::

11. On the New Secure Agent Group window, click **OK** to connect your Runtime Environment with the running agent.

    .. note:: If you do not download Secure Agent, you will not be able to connect your Runtime Environment with the running agent and continue establishing a connection between SQream and the Informatica data integration Cloud.
	
Establishing a Connection In Your Environment
-----------------

The **Establishing a Connection In Your Environment** describes the following:

.. contents::
   :local:

Establishing an ODBC DSN Connection In Your Environment
~~~~~~~~~~~~~
After establishing a connection between SQream and Informatica you can establish an ODBC DSN connection in your environment.

**To establish an ODBC connection in your environment:**

1. Click **Add**.
	   
    ::
	
2. Click **Configure**.
	
   .. note:: Verify that **Use Server Picker** is selected.
	
3. Click **Test**.

    ::
	
4. Verify that the connection has tested successfully.

    ::
   
5. Click **Save**.

    ::
	
6. Click **Actions** > **Publish**.
	
Establishing a JDBC Connection In Your Environment
~~~~~~~~~~~~~
After establishing a connection between SQream and Informatica you can establish a JDBC connection in your environment.

**To establish a JDBC connection in your environment:**

1. Create a new DB connection by clicking **Connections** > **New Connection**.

   The **New Connection** window is displayed.
   
     ::

	
2. In the **JDBC_IC Connection Properties** section, in the **JDBC Connection URL** field, establish a JDBC connection by providing the correct connection string.

   For connection string examples, see `Connection Strings <https://docs.sqream.com/en/2021.2.1/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string-examples>`_.
	
	 ::
	
3. Click **Test**.

    ::
	
4. Verify that the connection has tested successfully.

    ::
   
5. Click **Save**.

    ::
	
6. Click **Actions** > **Publish**.

Supported SQream Driver Versions
---------------

SQream supports the following SQream driver versions: 

* **JDBC** - Version 4.3.4 and above.

    ::

* **ODBC** - Version 4.0.0 and above.
