.. _connect_to_sql_workbench:

*****************************
Connect to SQream Using SQL Workbench/J
*****************************

Overview
==========
SQL Workbench/J is a free SQL query tool designed to run on any JRE-enabled environment, which you can use SQL Workbench/J to interact with a SQream cluster. The **Connect to SQream Using SQL Workbench/J** page describes how to connect to SAS Viya, and describes the following:

.. contents:: 
   :local:
   :depth: 1

Prerequisites
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Installing SQL Workbench/J
-------------------
The **Installing SQL Workbench/J** section describes the following installation methods:

.. contents:: 
   :local:
   :depth: 1

Installing SQL Workbench/J Using the SQream Installer
~~~~~~~~~~~~~~~~~~
Installing SQL Workbench/J using the SQream installer automates the installation process and configures all of the needed Java and SQL Workbench/J prerequisites. Installing SQL Worbench using the installer is relevant for Windows only.

**To install the SQL Workbench/J using the SQream installer:**

1. Download the JDBC driver installer from the `SQream Drivers page <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

   The Windows installer selects the required Java prerequisites and configuration settings.   

#. Install the JDBC driver by following the on-screen instructions.
   
   .. note:: The installer does not automatically select **Install SQL Workbench/J**.
   
    ::
	   
   The SQL Workbench/J is installed with the required configuration for connecting to SQream clusters.
      
   .. note:: The default location for SQL Workbench/J is **C:\Program Files\SQream Technologies\SQLWorkbench**. You can modify this path during the installation.

Installing SQL Workbench/J Manually
~~~~~~~~~~~~~~~~~~
Installing the SQL Workbench/J manually is relevant for Linux and MacOS, and can be done using one of the following methods:

.. contents:: 
   :local:
   :depth: 1

Installing Java Runtime 
^^^^^^^^^^^^^^^^^^^^^^
Both SQL Workbench/J and the SQream JDBC driver require Java 1.8 or newer.

You can install Java Runtime depending on the following platforms:

* **For Java 8** - `Oracle Java <https://www.java.com/en/download/manual.jsp>`_

* **For Linux and BSD** - `OpenJDK <https://openjdk.java.net/install/>`_

* **For Windows** - `Zulu 8 <https://www.azul.com/downloads/zulu-community/?&version=java-8-lts&architecture=x86-64-bit&package=jdk>`_ - for Linux and BSD

Downloading the SQream JDBC Driver
^^^^^^^^^^^^^^^^^^^^^^
You can download the SQream JDBC driver as a zipped JAR file from the Client Drivers page.

**To download the SQream JDBC driver:**

#. See `JDBC <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    :: 

#. Download and extract the JAR file from the zipped archive.

Installing SQL Workbench/J
^^^^^^^^^^^^^^^^^^^^^^
**To install SQL Workbench/J:**

#. Download the latest stable release from the `SQL Workbench/J downloads page <https://www.sql-workbench.eu/downloads.html>`_.

   SQream recommends using the `Generic package for all systems <https://www.sql-workbench.eu/Workbench-Build128.zip>`_. option.   

#. Extract the downloaded ZIP archive into a directory on your local machine.

    ::

#. Launch SQL Workbench/J.

   If you are using 64-bit Windows, you must run **SQLWorkbench64.exe** instead of **SQLWOrkbench.exe**.
   
Configuring SQL Workbench/J
------------------------
The **Setting Up Your SQream JDBC Driver Profile** describes the following:

.. contents:: 
   :local:
   :depth: 1
   
.. _setting_up_sqream_jdbc_driver_profile:
   
Setting Up Your SQream JDBC Driver Profile
~~~~~~~~~~~~~~~~~~~~~   
**To set up your SQream JDBC driver profile:**

#. From the File menu, select **Connect window** to define a connection profile.
   
   .. image:: /_static/images/sql_workbench_connect_window1.png

#. From the **Select Connection Profile** screen, click **Manage Drivers**.

   The drivers management screen is displayed:
   
   .. image:: /_static/images/sql_workbench_manage_drivers.png   
   
#. Create the SQream DB driver profile:
     
   #. Click add new driver |icon-icon_sql_wb_create_sqream_driver_profile|.
   
       ::
   
   #. In the name field, give your connection a descriptive name.
   
      SQream recommends calling it SQream DB *<version>*, where *<version>* is the version you have installed.   

   #. Add the JDBC drivers from the location to where you extracted the SQream JDBC .jar file.
      
      If you used the SQream installer, the file JDBC driver is located in *C:/Program Files/SQream Technologies/JDBC Driver/*.
   
   #. Click |icon-sql_workbench_detect_classname| to detect the classname automatically.
   
      The remaining information is optional.
   
   #. Click **OK**.

      Your information is saved and you are returned to the new connection screen.

.. _new_connection_profile:
  
.. |icon-icon_sql_wb_create_sqream_driver_profile| image:: /_static/images/icon_sql_wb_create_sqream_driver_profile.png
   :align: middle
   
.. |icon-sql_workbench_detect_classname| image:: /_static/images/sql_workbench_detect_classname.png
   :align: middle

Recommended Optional Configuration Settings
~~~~~~~~~~~~~~~~~~~~~~
If you installed SQL Workbench/J manually, you can set a customization to help SQL Workbench/J display information correctly in the DB Explorer panel.

**To define recommended optional configuration settings:**

#. Locate your workbench.settings file:

   * **On Windows**, typically: *C:/Users/<user name>/.sqlworkbench/workbench.settings* **Comment - Why "typically"?**
   
      ::
	  
   * **On Linux** - *$HOME/.sqlworkbench*
   
#. Add the following line at the end of the file:
   
   .. code-block:: text
      
      workbench.db.sqreamdb.schema.retrieve.change.catalog=true

#. Save the file and restart SQL Workbench/J.

.. _launching_sql_workbench:

Launching SQL Workbench/J
----------------------------
The **Launching SQL Workbench/J** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Selecting Your SQL Workbench/J Desktop Application
~~~~~~~~~~~~~~~~~~ 
After installing the SQL Workbench/J, you can launch it by selecting one of the following desktop applications from the Windows Start menu:

* SQL Workbench/J

   ::
   
* SQL Workbench/J (64) - for 64-bit Windows
   
   .. image:: /_static/images/launch_sql_workbench.png
      :align: center

Creating a New Connection Profile for Your Cluster	  
~~~~~~~~~~~~~~~~~~
**To create a new connection profile for your cluster:**

#. From the **Select Connection Profile** screen, create a new connection by clicking |icon-sql_workbench_launch_icon|.

   The **Default group** screen is displayed.

#. In the name field, give your connection a descriptive name.

    ::

#. From the **Driver** menu, select the SQream Driver that was created in :ref:`Setting Up Your SQream JDBC Driver Profile<setting_up_sqream_jdbc_driver_profile>`.

    ::

#. In the **URL** field, type your connection string.

   For more information about connection strings, see `Connection String Examples <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html#connection-string-examples>`_.

#. Click **Test** to test your connection details.

    ::

#. Click **OK**.

   Your connection profile is saved and you are connected to SQream.
   
.. |icon-sql_workbench_launch_icon| image:: /_static/images/sql_workbench_launch_icon.png
   :align: middle
   
Operating Informatica Cloud Services
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Troubleshooting Informatica Cloud Services
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.