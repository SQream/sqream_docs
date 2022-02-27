.. _connect_to_sql_workbench:

*****************************
Connect to SQream Using SQL Workbench
*****************************
SQL Workbench/J is a free SQL query tool designed to run on any JRE-enabled environment. You can use SQL Workbench to interact with a SQream cluster.

The **Connect to SQream Using SQL Workbench** page describes how to connect to SQream using SQL Workbench.

.. contents:: 
   :local:
   :depth: 1

Installing SQL Workbench
=====================================================================
The **Installing SQL Workbench** section describes the following installation methods:

.. contents:: 
   :local:
   :depth: 1

Installing SQL Workbench Using the SQream Installer
-------------------
Installing SQL Workbench using the SQream installer automates the installation process and configures all of the needed Java and SQL Workbench prerequisites. Installing SQL Worbench using the installer is relevant for Windows only.

**To install the SQL Workbench using the SQream installer:**

1. Download the JDBC driver installer from the `SQream Drivers page <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

   The Windows installer selects the required Java prerequisites and configuration settings.   

#. Install the JDBC driver by following the on-screen instructions.
   
   .. note:: The installer does not automatically select **Install SQL Workbench**.
   
    ::
	   
   The SQL Workbench is installed with the required configuration for connecting to SQream clusters.
      
   .. note:: The default location for SQL Workbench is **C:\Program Files\SQream Technologies\SQLWorkbench**. You can modify this path during the installation.

Installing SQL Workbench Manually
--------------------
Installing the SQL Workbench manually is relevant for Linux and MacOS, and can be done using one of the following methods:

.. contents:: 
   :local:
   :depth: 1

Installing Java Runtime 
~~~~~~~~~~~~~
Both SQL Workbench and the SQream JDBC driver require Java 1.8 or newer.

You can install Java Runtime depending on the following platforms:

* **For Java 8** - `Oracle Java <https://www.java.com/en/download/manual.jsp>`_

* **For Linux and BSD** - `OpenJDK <https://openjdk.java.net/install/>`_

* **For Windows** - `Zulu 8 <https://www.azul.com/downloads/zulu-community/?&version=java-8-lts&architecture=x86-64-bit&package=jdk>`_ - for Linux and BSD

Downloading the SQream JDBC Driver
~~~~~~~~~~~~~
You can download the SQream JDBC driver as a zipped JAR file from the Client Drivers page.

**To download the SQream JDBC driver:**

#. See `JDBC <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    :: 

#. Download and extract the JAR file from the zipped archive.

Installing SQL Workbench
~~~~~~~~~~~~~

#. Download the latest stable release from the `SQL Workbench downloads page <https://www.sql-workbench.eu/downloads.html>`_.

   SQream recommends using the `Generic package for all systems <https://www.sql-workbench.eu/Workbench-Build128.zip>`_. option.   

#. Extract the downloaded ZIP archive into a directory on your local machine.

    ::

#. Launch SQL Workbench.

   If you are using 64-bit Windows, you must run **SQLWorkbench64.exe** instead of **SQLWOrkbench.exe**.
   
   For more information, see :ref:`launching_sql_workbench`.

Configuring SQL Workbench
============
The **Setting Up Your SQream JDBC Driver Profile** describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Setting Up Your SQream JDBC Driver Profile
---------------------------------------------


   
**To set up your SQream JDBC driver profile:**

#. From the File menu, select **Connect window** to define a connection profile.
   
   .. image:: /_static/images/sql_workbench_connect_window1.png

#. From the **Select Connection Profile** screen, click **Manage Drivers**.

   The drivers management screen is displayed:
   
   .. image:: /_static/images/sql_workbench_manage_drivers.png   
   
#. Create the SQream DB driver profile |icon_sql_wb_create_sqream_driver_profile|.




   
   .. image:: /_static/images/sql_workbench_create_driver.png
   
   #. Click on the Add new driver button ("New" icon)
   
   #. Name the driver as you see fit. We recommend calling it SQream DB <version>, where <version> is the version you have installed.
   
   #. 
      Add the JDBC drivers from the location where you extracted the SQream DB JDBC JAR.
      
      If you used the SQream installer, the file will be in ``C:\Program Files\SQream Technologies\JDBC Driver\``
   
   #. Click the magnifying glass button to detect the classname automatically. Other details are purely optional
   
   #. Click OK to save and return to "new connection screen"


.. _new_connection_profile:


.. |icon-icon_sql_wb_create_sqream_driver_profile| image:: /_static/images/icon_sql_wb_create_sqream_driver_profile.png
   :align: middle


Suggested optional configuration
----------

If you installed SQL Workbench manually, you can set a customization to help SQL Workbench show information correctly in the DB Explorer panel.

#. Locate your workbench.settings file
   On Windows, typically: ``C:\Users\<user name>\.sqlworkbench\workbench.settings``
   On Linux, ``$HOME/.sqlworkbench``
   
#. Add the following line at the end of the file:
   
   .. code-block:: text
      
      workbench.db.sqreamdb.schema.retrieve.change.catalog=true

#. Save the file and restart SQL Workbench

.. _launching_sql_workbench:

Launching SQL Workbench
=====================================================================
The **Launching SQL Workbench** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Selecting Your SQL Workbench Desktop Application
------------------------------------------------ 
After installing the SQL Workbench, you can launch it by selecting one of the following desktop applications from the Windows Start menu:

* SQL Workbench

   ::
   
* SQL Workbench (64) - for 64-bit Windows


   
   .. image:: /_static/images/launch_sql_workbench.png
      :align: center

Creating a New Connection Profile for Your Cluster	  
------------------------------------------------


   .. image:: /_static/images/sql_workbench_connection_profile.png
	  
#. From the **Select Connection Profile** screen, create a new connection by clicking |icon-sql_workbench_launch_icon|.

   The **Default group** screen is displayed.

#. In the name field, give your connection a descriptive name.

#. Select the SQream Driver that was created in the previous screen

#. Type in your connection string. To find out more about your connection string (URL), see the :ref:`Connection string documentation <connection_string>`.

#. Text the connection details

#. Click OK to save the connection profile and connect to SQream DB
   
You are now ready to create a profile for your cluster. Continue to :ref:`Creating a new connection profile <new_connection_profile>`.



.. |icon-sql_workbench_launch_icon| image:: /_static/images/sql_workbench_launch_icon.png
   :align: middle
   
