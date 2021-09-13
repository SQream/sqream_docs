.. _talend:

*************************
Connecting to SQream Using Talend
*************************

.. _top:

Overview
=================

This page describes how to use Talend to interact with a SQream DB cluster. The Talend connector is used for reading data from a SQream DB cluster and loading data into SQream DB. 

In addition, this page provides a viability report on Talend's comptability with SQream DB for stakeholders.

It includes the following:

* :ref:`A Quick Start guide <quickstart_guide>`
* :ref:`Information about supported SQream drivers <supported_sqream_drivers>`
* :ref:`Supported data sources <supported_data_sources>` and :ref:`tool and operating system versions <supported_tools_os_sys_versions>`
* :ref:`A description of known issues <known_issues>`
* :ref:`Related links <related_links>`


About Talend
=================
Talend is an open-source data integration platform. It provides various software and services for Big Data integration and management, enterprise application integration, data quality and cloud storage.

For more information about Talend, see `Talend <http://www.talend.com/>`_.


.. _quickstart_guide:

Quick Start Guide
=======================

Creating a New Metadata JDBC DB Connection
-------------
**To create a new metadata JDBC DB connection:**

1. In the **Repository** panel, nagivate to **Metadata** and right-click **Db connections**.

::
   
2. Select **Create connection**.

::
  
3. In the **Name** field, type a name.

   The name cannot contain spaces.

4. In the **Purpose** field, type a purpose and click **Next**. You cannot go to the next step until you define both a Name and a Purpose.

::
  
5. In the **DB Type** field, select **JDBC**.

::
  
6. In the **JDBC URL** field, type the relevant connection string.

   For connection string examples, see `Connection Strings <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-string>`_.
   

7. In the **Drivers** field, click the **Add** button.

   The **"newLine"** entry is added.

8. One the **"newLine"** entry, click the ellipsis.

.. image:: /_static/images/Third_Party_Connectors/Creating_a_New_Metadata_JDBC_DB_Connection_8.png

   The **Module** window is displayed.

9. From the Module window, select **Artifact repository(local m2/nexus)** and select **Install a new module**.

::
  
10. Click the ellipsis.

.. image:: /_static/images/Third_Party_Connectors/Creating_a_New_Metadata_JDBC_DB_Connection_9.5.png

   Your hard drive is displayed.	

11. Navigate to a **JDBC jar file** (such as **sqream-jdbc-4.4.0.jar**)and click **Open**.

::
  
12. Click **Detect the module install status** and click **OK**.

    The JDBC that you selected is displayed in the **Drivers** field.

13. Click **Select class name**.

::
  
14. Click **Test connection**.

    If a driver class is not found (for example, you didn't select a JDBC jar file), the following error message is displayed:

    .. image:: /_static/images/Third_Party_Connectors/Creating_a_New_Metadata_JDBC_DB_Connection_15.png

After creating a new metadata JDBC DB connection, you can do the following:

 * Use your new metadata connection.
 * Drag it to the **job** screen.
 * Build Talend components.
 
For more information on loading data from JSON files to the Talend Open Studio, see `How to Load Data from JSON Files in Talend <https://www.youtube.com/watch?v=qNt9CYZFFqQ&list=PLOr008ImHvfan_fuDr5RVyexpeYJAp9FX&index=6>`_.

:ref:`Back to top <top>`

.. _supported_sqream_drivers:
 
Supported SQream Drivers
================

The following list shows the supported SQream drivers and versions:

* **JDBC** - Version 4.3.3 and higher.
* **ODBC** - Version 4.0.0. This version requires a Bridge to connect. For more information on the required Bridge, see `Connecting Talend on Windows to an ODBC Database <https://www.easysoft.com/blog/talend.html>`_.

:ref:`Back to top <top>`


.. _supported_data_sources:

Supported Data Sources
============================
Talend Cloud connectors let you create reusable connections with a wide variety of systems and environments, such as those shown below. This lets you access and read records of a range of diverse data.

* **Connections:** Connections are environments or systems for storing datasets, including databases, file systems, distributed systems and platforms. Because these systems are reusable, you only need to establish connectivity with them once.

* **Datasets:** Datasets include database tables, file names, topics (Kafka), queues (JMS) and file paths (HDFS). For more information on the complete list of connectors and datasets that Talend supports, see `Introducing Talend Connectors <https://help.talend.com/r/vqIZei8ynfi_BaDCg3d~_g/M0qzU1kTnL0bPou7OuxJfw>`_.

:ref:`Back to top <top>`


.. _supported_tools_os_sys_versions:

Supported Tool and Operating System Versions
======================
Talend was tested using the following:

* Talend version 7.4.1M6
* Windows 10
* SQream version 2021.1
* JDBC version <version number>

	


:ref:`Back to top <top>`
 

.. _known_issues:

Known Issues
===========================  
The the list below describes the following known issues as of 6/1/2021:

* Schemas not displayed for tables with identical names.

:ref:`Back to top <top>`


.. _related_links:

Related Links
===============
The following is a list of links relevant to the Talend connector:

* `Talend Home page <https://www.talend.com/>`_
* `Talend Community page <https://community.talend.com/s/>`_
* `Talend BugTracker <https://jira.talendforge.org/secure/Dashboard.jspa>`_


Download Links
==================
The following is a list of download links relevant to the Talend connector:

* `Talend Open Studio for Big Data <https://www.talend.com/products/talend-open-studio/>`_
* `Latest version of SQream JDBC <https://docs.sqream.com/en/latest/guides/client_drivers/index.html#client-drivers>`_

:ref:`Back to top <top>`


	 
.. contents:: In this topic:
   :local:
