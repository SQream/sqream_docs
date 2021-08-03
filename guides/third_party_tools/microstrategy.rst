.. _microstrategy:


*************************
Connecting to SQream Using Microstrategy
*************************

.. _top:

Overview
=================

This page describes how to use Microstrategy to interact with a SQream DB cluster. The Microstrategy connector is used for reading data from a SQream DB cluster and loading data into SQream DB.

In addition, this page provides a viability report on Talend's comptability with SQream DB for stakeholders.

It includes the following:

* :ref:`System requirements <system_requirements>`
* :ref:`A Quick Start guide <quickstart_guide>`
* :ref:`Information about supported SQream drivers <supported_sqream_drivers>`
* :ref:`A description of known issues <known_issues>`
* :ref:`Related links <related_links>`
* :ref:`Download links <download_links>`




About MicroStrategy
================
MicroStrategy is a Business Intelligence software offering a wide variety of data analytics capabilities. As an application suite, it provides the following:

* Data discovery
* Advanced analytics
* Data visualization
* Embedded BI
* Banded reports and statements

**Comment - I found the below content when I downloaded the MicroStrategy Workstation. I changed the wording a little, and I think it's good to include it in this doc, perhaps to even replace/merge with the content above. Thoughts?** 

* Create and manage users
* Assign roles, content permissions, and security
* Publish datasets and schedule updates
* Create, certify, and share dossiers
* Deploy, monitor, and manage services and applications

For more information about Microstrategy, see `MicroStrategy <https://www.microstrategy.com/>`_.

.. _system_requirements:

:ref:`Back to Overview <top>`


System Requirements
==================
The **System Requirements** section lists the minimal system requirements to support the MicroStrategy Secure Enterprise. The system requirements depend on certain factors, such as the complexity of your MicroStrategy environment, the deployment strategy of MicroStrategy features, user community requirements, expected peak usage requirements, and response time expectations.

**Comment - Is this section external or internal?**

The following list shows more detailed system requirements:

* `Evaluation deployment <https://doc-archives.microstrategy.com/producthelp/10.11/Readme/content/requirements_evaluation.htm>`_
* `Production deployment <https://doc-archives.microstrategy.com/producthelp/10.11/Readme/content/requirements_production.htm>`_

.. _quickstart_guide:

:ref:`Back to Overview <top>`


Quick Start Guide
=======================

1. Install `MicroStrategy Desktop <https://www2.microstrategy.com/producthelp/2020/Readme/en-us/Content/desktopclient.htm>`_.

2. Download the most current version of the `SQream JDBC driver <https://docs.sqream.com/en/latest/guides/client_drivers/index.html#client-drivers>`_. **Comment - See "drivers and connectors" in the ETA.**

3. Activate the **MicroStrategy Desktop** app. The app displays the Dossiers panel to the right.

4. Click **Dossiers** and **New Dossier**. The **Untitled Dossier** panel is displayed.

5. Click **New Data**.

6. From the **Data Sources** panel, select **Databases** to access data from tables. The **Select Import Options** panel is displayed.

7. Click **Select Tables** and click **Next**:

8. In the Data Source panel, do the following:

   1. From the **Database** dropdown menu, select **Generic**. The **Host Name**, **Port Number**, and **Database Name** fields are removed from the panel.

   2. In the **Version** dropdown menu, verify that **Generic DBMS** is selected.
   
   3. Click **Show Connection String**.

   4. Select the **Edit connection string** checkbox.

   5. From the **Driver** dropdown menu, select a driver for one of the following connectors:

      1. **JDBC** - Any driver, such as **Amazon Redshift (x64)(Certified)**
      2. **ODBC** - SQreamDB ODBC

       ::

   6. In the **Connection String** text box, type the relevant connection string and path to the JDBC jar file using the following syntax:

   .. code-block:: console

      $ jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>sqream;[<optional parameters>; ...]

   The following example shows the correct sytax for the JDBC connector:
 
   .. code-block:: console

      jdbc;MSTR_JDBC_JAR_FOLDER=C:\path\to\jdbc\folder;URL={jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...];}
	   
   The following example shows the correct sytax for the ODBC connector:

   .. code-block:: console

      odbc:Driver={SqreamODBCDriver};DSN={SQreamDB ODBC};Server=<Host>;Port=<Port>;Database=<database name>;User=<username>;Password=<password>;Cluster=<boolean>;

   To see the available **connection parameters** and other examples, see `Connection Parameters <https://docs.sqream.com/en/latest/guides/client_drivers/jdbc/index.html#connection-string>`_.

   7. In the **User** and **Password** fields, fill out your user name and password.
   
   8. In the **Data Source Name** field, type **SQreamDB**.
   
   9. Click **Save**. The SQreamDB that you picked in the Data Source panel is displayed.
   
.. image:: /_static/images/third_party_connectors/microstrategy/new_data_source.png


   
Now you can select your relevant schemas and tables by dragging and dropping the way you would like to connect to those tables.

**Comment - I keep getting the same error here. Demonstrate.**





.. _supported_sqream_drivers:

:ref:`Back to Overview <top>`

Supported SQream Drivers
================

The following list shows the supported SQream drivers and versions:

* **JDBC** - Version 4.3.3 and higher.
* **ODBC** - Version 4.0.0.
* **Drivers and Connectors** - For the official MicroStrategy drivers and donnectors, see `MicroStrategy Drivers and Connectors <https://www.microstrategy.com/en/support/drivers-and-connectors>`_.

.. _supported_tools_and_operating_systems:

:ref:`Back to Overview <top>`

Supported Tools and Operating System Versions
======================
MicroStrategy was tested using the following:

* Microstrategy Desktop version 11.2.200.10138
* Windows 10 Professional
* Framework Build 11.2.2 (Windows or MAC)
* SQream version 2021.1

.. _known_issues:

:ref:`Back to Overview <top>`

Known Issues
===========================  
The the list below describes the following known issues as of 6/1/2021:

* Connecting to a worker Port 5000 when the ``no explicit`` cluster is set to ``false``, the process would fail.
* Joining a large table from SQream with a table from a different database caused a crash due to low memory.
* Different SQream databases of the same cluster

**Comment - is the above known issue SQ-5499?**

* Different databases were using the same schema name and table name.
* Define data from different data sources external tables

.. _related_links:

:ref:`Back to Overview <top>`

Related Links
===============
The following is a list of links relevant to the MicroStrategy connector:

* `MicroStrategy Home page <https://www.microstrategy.com/en>`_
* `MicroStrategy Community page <https://community.microstrategy.com/s/?language=en_US>`_
* `MicroStrategy <https://doc-archives.microstrategy.com/producthelp/10.11/Readme/content/tools.htm>`_

.. _download_links:

:ref:`Back to Overview <top>`

Download Links
==================
The following is a list of download links relevant to the MicroStrategy connector:

* `MicroStrategy <https://www.microstrategy.com/en/get-started/workstation>`_
* `Latest version of SQream JDBC <https://docs.sqream.com/en/latest/guides/client_drivers/index.html#client-drivers>`_

:ref:`Back to Overview <top>`