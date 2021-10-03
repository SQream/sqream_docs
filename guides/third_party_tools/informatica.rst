.. _informatica:


*************************
Connecting to SQream Using Informatica
*************************

Overview
=========
This document is a viability report on Informatica as an ETL tool for Big Data and its compatibility with SQreamDB. It provides documentation for stakeholders using SQreamDB.

It includes the following:

.. contents:: In this topic:
   :local:


.. _quickstart_guide:

Quick Start Guide
-----------------
This Quick Start Guide describes how to establish a connection between SQream and the Informatica data integration Cloud.

**To get establish a connection between Sqream and the Informatica data integration Cloud:**

1. Go to the `Informatica Cloud homepage <https://emw1.dm-em.informaticacloud.com/diUI/products/integrationDesign/main/home>`_.

    ::

2. Do one of the following:

   1. Log in using your credentials.
   
    ::

   2. Log in using your SAML Identity Provider.
   
    ::

   3. If you are a new user, click **Don't have an account?**
   
3. From the **Select a trial** menu, select **Cloud Data Integration** and click **Select Trial**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_1.png

4. Fill out the profile information and click **START YOUR FREE TRIAL**.

    ::

5. If the company confirmation panel is displayed, confirm the company. Informatica administration sends an automatic email to your email address.

    ::

6. Follow the instructions in the automatically generated email. Click **Confirm Account link**.

    ::

7. Define your credentials and click **Log In**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_2.png

8. When the following message is displayed, click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_3.png

9. When the following message is displayed, click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_4.png

10. Select a source and target system(s) (maximum three) and click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_5.png

11. From the **Sample Use-Cases** window, select a sample use-case or click **Don't show this again.**

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_6.png

12. From the **Services** window, select **Administrator** or click **Show all services** to show all services.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_7.png

The Sqream dashboard is displayed.
   
.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_8.png

13. In the menu on the left, click **Runtime Environments**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_9.png

The **Runtime Environments** panel is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_10.png

14. Click **Download Secure Agent**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_11.5.png

15. When the **Download the Secure Agent** panel is displayed, do the following:

    1. Select a platform (Windows 64 or Linux 64).
	
     ::

	
    2. Click **Copy** and save the token locally. The token is used in combination with your user name to authorize the agent to access your account.
	
.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.5.png

16. Click **Download**. The installation begins.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.6.png

17. When the Informatica Cloud Secure Agent Setup panel is displayed, click **Next**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.7.png

18. Provide your **User Name** and **Install Token** and click **Register**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.8.png

19. From the Runtime Environments panel, click **New Runtime Environment**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_11.png

**Comment - This step was located here in the Confluence doc, but I think this is the wrong place. See Step 19.**

The **New Secure Agent Group** window is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.png

20. On the New Secure Agent Group window, click **OK** to connect your Runtime Environment with the running agent.

**NOTE:** If you do not download Secure Agent, you will not be able to connect your Runtime Environment with the running agent and continue establishing a connection between Sqream and the Informatica data integration Cloud.

21. Establish ODBC DSN in your environment by doing the following:

    1. Click **Add**.
	   
    ::
	
    2. Click **Configure**.
	
**NOTE:** Verify that **Use Server Picker** is selected.

22. To create a new DB connection, click **Connections** and click **New Connection**.

    The JDBC window is displayed.
	
  **Comment - I need to see this window to identify its name.**

23. In the **JDBC_IC Connection Properties** Establish a JDBC connection by providing the correct connection string.

    For connection string examples, see `Connection Strings <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-string>`_.

Establishing a Connection between the Secure Agent and Runtime Environment
-----------------
After configuring the JDBC you must establish a connection between the secure agent and the runtime environment.

If you have not configured a login for a Windows secure agent service, see `Configure a login for a Windows Secure Agent Service <https://docs.informatica.com/integration-cloud/cloud-data-integration/current-version/getting-started/installing-secure-agents/secure-agent-installation-on-windows/configure-a-login-for-a-windows-secure-agent-service.html>`_.

**To establish a connection between the secure agent and runtime environment:**

1. Click **Data Integration** to create a new data integration project.

    ::

2. Click **Mappings.**

   **Comment - in this case we have table as data source and a table for target**
   
3. Click **Mapping**.

    ::

4. Click **Create**.

    ::

5. Set the data source as follows:

   1. Click **Source**.
      
    ::

   2. In the **Design** dialog box, select the connection and the source table.
   
   **Comment - Can you provide me with a screenshot of this? See #4 in the screenshot in the source doc.**

6. Set the target as follows:

   1. Click **Target**.
   
    ::

   2. In the **Design** dialog box, select the connection and the source table.
   
   **Comment - Is this screenshot relevant to both steps 5 and 6?**

7. Click **Field Mapping**.

    ::

8. In the **Properties** tab, from the **Field map options** dropdown menu, select **Automatic**.

    ::

9. Click **Save**.

    ::

10. Click **Run**.

    **Comment - What is the result?**

11. From the **Definition** window, from the **Runtime Environment** dropdown menu, select the correct runtime environment and click **Run**.
 





 

Supported SQream Drivers (Versions)
-----------------
**Comment - do we need this section?**

SQream supports the following SQream driver versions: 

* **JDBC** - Version 4.3.4 and above.

* **ODBC** - Version 4.0.0 and above. 

For more information on configuring an ODBC connection on Windows, see `Configure ODBC Connections on Windows <https://docs.informatica.com/data-integration/data-services/10-2/sql-data-service-guide/installing-and-configuring-drivers-for-powercenter/configure-odbc-connections-on-windows.html>`_.


 
Supported Data Sources
-----------------
**Comment - This section can probably be deleted.**

Informatica Cloud allows you to create reusable connections to a wide variety of systems and environments and thus access and read records of extremely diverse data.

Add-On Connectors: Add-on connectors provide connectivity for connection types that are not installed by default in Informatica Intelligent Cloud Services. Click here for more information.

Dataset: Database tables, file names, etc. 

Click here to view, the full list of cloud connectors and datasets supported by Informatica.







Related Links
-----------------
**Comment - do we need this section?**

* **Home page** - https://www.informatica.com/

* **Documentation page** - https://docs.informatica.com/




Download Links
-----------------
**Comment - do we need this section?**

* **Informatica free trail link**  (here)

* **Latest SQream JDBC version** (Download here)