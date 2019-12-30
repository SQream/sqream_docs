.. _install_odbc_windows:

****************************************
Install and configure ODBC on Windows
****************************************

The ODBC driver for Windows is provided as a self-contained installer.

This tutorial shows you how to install and configure ODBC on Windows.

.. contents:: In this topic:
   :local:
   :depth: 2

Installing the ODBC driver
==================================

Prerequisites
----------------

.. _vcredist:

Visual Studio 2015 Redistributables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ODBC driver requires Microsoft's Visual Studio 2015 Redistributable packages installed.

Follow the instructions for download and installation on Microsoft's website https://www.microsoft.com/en-us/download/details.aspx?id=48145


Administrator privileges
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SQream DB ODBC driver requires administrator privileges on your computer to add the DSNs (data source names).


1. Run the Windows installer
------------------------------

Install the driver by following the on-screen instructions in the easy-to-follow installer.

.. image:: /_static/images/odbc_windows_installer_screen1.png

.. note:: The installer will install the driver in ``C:\Program Files\SQream Technologies\ODBC Driver`` by default. You can change this path during the installation.

2. Selecting components
^^^^^^^^^^^^^^^^^^^^^^^^^^

The installer includes additional components, like JDBC and Tableau customizations.

.. image:: /_static/images/odbc_windows_installer_screen2.png

You can deselect items you don't want to install, but the items named **ODBC Driver DLL** and **ODBC Driver Registry Keys** must remain selected for a complete installation of the ODBC driver.

Once the installer finishes, you will be ready to configure the DSN for connection.

.. _create_windows_odbc_dsn:

3. Configuring the ODBC Driver DSN
======================================

ODBC driver configurations are done via DSNs. Each DSN represents one SQream DB database.

#. Open up the Windows menu by clicking the Windows button on your keyboard (:kbd:`⊞ Win`) or pressing the Windows button with your mouse.

#. Type **ODBC** and select **ODBC Data Sources (64-bit)**. Click the item to open up the setup window.
   
   .. image:: /_static/images/odbc_windows_startmenu.png

#. The installer has created a sample User DSN named **SQreamDB**
   
   You can modify this DSN, or create a new one (:menuselection:`Add --> SQream ODBC Driver --> Next`)
   
   .. image:: /_static/images/odbc_windows_dsns.png

#. Enter your connection parameters. See the reference below for a description of the parameters.
   .. image:: /_static/images/odbc_windows_dsn_config.png

#. When completed, save the DSN by selecting :menuselection:`OK`

.. tip:: Test the connection by clicking :menuselection:`Test` before saving. A successful test looks like this:
   
   .. image:: /_static/images/odbc_windows_dsn_test.png

#. You can now use this DSN in ODBC applications like :ref:`Tableau <connect_to_tableau>`.



Connection parameters
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Description
   * - Data Source Name
     - An easily recognizable name that you'll use to reference this DSN. Once you set this, it can not be changed.
   * - Description
     - A description of this DSN for your convenience. You can leave this blank.
   * - User
     - Username of a role to use for connection. For example, ``rhendricks``
   * - Password
     - Specifies the password of the selected role. For example, ``Tr0ub4dor&3``
   * - Database
     - Specifies the database name to connect to. For example, ``master``
   * - Service
     - Specifices :ref:`service queue<workload_manager>` to use. For example, ``etl``. Leave blank for default service ``sqream``.
   * - Server
     - Hostname of the SQream DB instance. For example, ``127.0.0.1`` or ``sqream.mynetwork.co``
   * - Port
     - TCP port of the SQream DB instance. For example, ``5000`` or ``3108``
   * - User server picker
     - Connect via load balancer (use only if exists, and check port)
   * - SSL
     - Specifies SSL for this connection
   * - Logging options
     - Use this screen to alter logging options when tracing the ODBC connection for possible connection issues.


Troubleshooting
==================

Solving "Code 126" ODBC errors
---------------------------------

After installing the ODBC driver, you may experience the following error: 

.. code-block:: none

   The setup routines for the SQreamDriver64 ODBC driver could not be loaded due to system error
   code 126: The specified module could not be found.
   (c:\Program Files\SQream Technologies\ODBC Driver\sqreamOdbc64.dll)

This is an issue with the Visual Studio Redistributable packages. Verify you've correctly installed them, as described in the :ref:`Visual Studio 2015 Redistributables <vcredist>` section above.