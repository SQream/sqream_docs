.. _informatica:


*************************
Connecting to SQream Using Informatica
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
7. Define your credentials. 

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_2.png

8. When the following message is displayed, click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_3.png

9. When the following message is displayed, click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_4.png

10. Select a source and target system(s) (maximum three) and click **Continue**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_5.png

11. From the **Sample Use-Cases** window, select a sample use-case or click **Don't show this again.**

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_6.png

12. From the **Services** window, select **Administrator** or click **See all services** to see all services.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_7.png

The Sqream dashboard is displayed.
   
.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_8.png

13. In the menu item on the left, click **Runtime Environments**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_9.png

The **Runtime Environments** panel is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_10.png

14. From the Runtime Environments panel, click **New Runtime Environment**.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_11.png

15. Click **Download Secure Agent**.

    The **New Secure Agent Group** window is displayed.

.. image:: /_static/images/third_party_connectors/informatica/quickstartguide_12.png

16. Copy the token and store it. The token is required for installing Informatica.

17. Install the Secure Agent on one of the following operating systems:

A Secure Agent is a lightweight program that runs all tasks that you configure in Informatica Intelligent Cloud Services and processes your company's data locally and securely. A Secure Agent must be running to run tasks.

Verify that you have the following prerequisites before installing the Secure Agent on your machine:

   * Windows
   * Linux

Verify the following requirements before you install the Secure Agent on Windows:
Verify that the machine on which you install the Secure Agent uses a supported operating system. For the list of supported operating systems for the Secure Agent, see the Product Availability Matrix (PAM) for Informatica Intelligent Cloud Services on the Product Availability Matrices page on Informatica Network.
Verify that the machine where you install the Secure Agent has at least 5 GB of free disk space.
Verify that the account you use to install the Secure Agent has access to all remote directories that contain flat source or target files.
Verify that no other Secure Agent is installed on the machine. If another Secure Agent is installed on the machine, you must uninstall it first.
 


A Secure Agent is a lightweight program that runs all tasks that you configure in Informatica Intelligent Cloud Services and processes your company's data locally and securely. A Secure Agent must be running to run tasks. The following link will guide you through the prerequisites before you install a Secure Agent on your machines, such as the operating system that will support the Secure Agent, access to all remote directories, and more. 

Windows installation process

Linux installation process

Agent Installation and Ports Needed

Using the following links, understand how to download and install a Secure Agent, configure the proxy settings, configure login, and also uninstall the Secure Agent in Linux and Windows.

Windows

Linux

 

Install the Agent and start the service.

Create “New Runtime environment” 

 


 

Connect Runtime Environment with the running agent 

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