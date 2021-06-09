.. _pentaho_data_integration:


*************************
Connecting to SQream Using Pentaho Data Integration
*************************

Overview
=========
This document is a viability report on Informatica as an ETL tool for Big Data and its compatibility with SQreamDB. It provides documentation for stakeholders using SQreamDB.

It includes the following:

* :ref:`A Quick Start guide <quickstart_guide>`
* :ref:`Information about supported SQream drivers <supported_sqream_drivers>`
* :ref:`Information about supported data sources <supported_data_sources>`
* :ref:`Information about supported tools and operating system versions <supported_tool_os_versions>`
* :ref:`A description of known issues <known_issues>`
* :ref:`Related links <related_links>`
* :ref:`Download links <download_links>`

.. _quickstart_guide:

Quick Start Guide
-----------------
This Quick Start Guide describes how to establish a connection between Sqream and the Informatica data integration Cloud.

**To get establish a connection between Sqream and the Informatica data integration Cloud:**

1. Go to the `Informatica Cloud homepage <https://emw1.dm-em.informaticacloud.com/diUI/products/integrationDesign/main/home>`_.

2. Do one of the following:

   1. Log in using your credentials.
   2. Log in using your SAML Identity Provider.
   3. If you are a new user, click **Don't have an account?**
   
3. From the **Select a trial** menu, select **Cloud Data Integration** and click **Select Trial**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_1.png

4. Fill out the profile information and click **START YOUR FREE TRIAL**.
5. If the company confirmation panel is displayed, confirm the company. Informatica administration sends an automatic email to your email address.
6. Follow the instructions in the automatically generated email. Click **Confirm Account link**. 
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
	
    2. Click **Copy** and save the token locally. The token is used in combination with your user name to authorize the agent to access your account.
	
.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.5.png

16. Click **Download**. The installation begins.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.6.png

17. When the Informatica Cloud Secure Agent Setup panel is displayed, click **Next**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.7.png

18. Provide your **User Name** and **Install Token** and click **Register**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.8.png



14. From the Runtime Environments panel, click **New Runtime Environment**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_11.png

**Comment - This step was located here in the Confluence doc, but I think this is the wrong place. See Step 19.**

The **New Secure Agent Group** window is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.png




16. Download Agent.


The **Secure Agent** is a lightweight software that runs all tasks that you configure in Informatica Intelligent Cloud Services and processes your company's data locally and securely. The Secure Agent must be running to run tasks.

17. Verify the pre-installation requirements for your operating system before installing the Secure Agent on your machine:

* `Windows <https://docs.informatica.com/integration-cloud/cloud-platform/current-version/runtime-environments/secure-agent-installation/secure-agent-installation-on-windows/secure-agent-requirements-on-windows.html>`_

* `Linux <https://docs.informatica.com/integration-cloud/cloud-platform/current-version/runtime-environments/secure-agent-installation/secure-agent-installation-on-linux/secure-agent-requirements-on-linux.html>`_

18. Install the Secure Agent on your machine using your operating system:

* `Windows <https://docs.informatica.com/integration-cloud/cloud-platform/current-version/runtime-environments/secure-agent-installation/secure-agent-installation-on-windows.html>`_

* `Linux <https://docs.informatica.com/integration-cloud/cloud-platform/current-version/runtime-environments/secure-agent-installation/secure-agent-installation-on-linux.html>`_

In addition to installing the Secure Agent on your machine, the links above include information for configuring proxy settings, configuring a login, and uninstalling the Secure Agent.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_13.png

19. From the Runtime Environments panel, click **New Runtime Environment**.

The **New Secure Agent Group** window is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.png 

20. On the New Secure Agent Group window, click **OK** to connect your Runtime Environment with the running agent.

**NOTE:** If you do not download Secure Agent, you will not be able to connect your Runtime Environment with the running agent and continue establishing a connection between Sqream and the Informatica data integration Cloud.

Create database connection - Press New Connection

Establish ODBC DSN in your environment


** Only if Server Picker is listening 

Create new DB Connection: Press “New Connection”


Establish JDBC 


In JDBC URL attach the relevant connection string. (examples can be found here) 

After completing the setting for the JDBC we need to connect the secure agent with the runtime environment 

Click here to see how to configure a login for a Windows Secure Agent Service.

Create New “Data Integration” Project


 

New Mapping (in this case we have table as data source and a table for target)

 


Set the data source: Stand on the “source” → Go to the dialog box below → select the connection → select the source table

Set the Target: Stand on the “Target”→ Go to the dialog box below → select the connection → select the source table

On “Filed Mapping” set to “Automatic”


 

Save → Run

Select the relevant “Runtime environment” → And Run


.. _supported_sqream_drivers:
 

Supported SQream Drivers (Versions)
==============================
JDBC - Version 4.3.4 and above

ODBC - Version 4.0.0 and above. 

Click here for more information.

.. _supported_data_sources:
 
Supported Data Sources
============
Informatica Cloud allows you to create reusable connections to a wide variety of systems and environments and thus access and read records of extremely diverse data.

Add-On Connectors: Add-on connectors provide connectivity for connection types that are not installed by default in Informatica Intelligent Cloud Services. Click here for more information.

Dataset: Database tables, file names, etc. 

Click here to view, the full list of cloud connectors and datasets supported by Informatica.

.. _supported_tool_os_versions:

Supported Tool or Operating System Versions
=============
Tested on Informatica Cloud Integration (Chrome) 

.. _known_issues:

Known Issues
========= 
Unable to Log On to the secure agent




JDBC sends an error when trying to select a table as a Single Object in Sorce/Target type 


Multiple object function isn't working 


Create a target table at runtime



HOW TO: Increase Java heap size on IICS to allocate more memory to the JVM for large data processing with certain connectors

.. _related_links:

Related Links
============================
Home page - https://www.informatica.com/

Documentation page - https://docs.informatica.com/


.. _download_links:

Download Links
==================

Download links
Informatica free trail link  (here)

Latest SQream JDBC version. (Download here)