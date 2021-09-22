.. _connect_to_power_bi:

*************************
Connecting to SQream Using Power BI
*************************

.. contents:: In this topic:
   :local:
   
   
Overview
=====================

This page describes 

It includes the following:




   
   


Configuring Your ODBC Driver
=================

Getting started using Power BI requires you to configure your ODBC drivers. ODBC drivers are configured using DSNs, and each DSN represents one SQream database.

**To configure your ODBC driver:**

#. Install **Visual C++ Redistributable for Visual Studio 2015**. For more information, see `Install Instructions <https://www.microsoft.com/en-us/download/details.aspx?id=48145>`_.

    ::


#. Run the Windows installer.

   .. image:: /_static/images/odbc_windows_installer_screen1.png

   .. note:: The default installation location is ``C:\Program Files\SQream Technologies\ODBC Driver``, but you can modify this path during installation.

3. From the **SQream Drivers Setup** dialog box, select your components.

   .. image:: /_static/images/odbc_windows_installer_screen2.png

   You can clear items you don't need, but you must install the **ODBC Driver DLL** and **ODBC Driver Registry Keys** items to correctly install the ODBC driver.

.. _create_windows_odbc_dsn:

Configuring the ODBC Driver DSN
======================================
You can configure your ODBC driver via DSNs. Each DSN represents one SQream DB database.

**To configure your ODBC Driver DSN:**

#. Open the Windows menu.

    ::

#. Type **ODBC** and select **ODBC Data Sources (64-bit)**.
   
   During the installation, a sample User DSN named **SQreamDB** was created.
   
#. *Optional* - Modify the DSN or create a new one by clicking **Add**, **SQream ODBC Driver**, and **Next**.
   
   .. image:: /_static/images/odbc_windows_dsns.png
   
 ::

4. Enter your connection parameters as shown below:

   .. list-table:: 
      :widths: auto
      :header-rows: 1
   
      * - Item
        - Description
      * - Data Source Name
        - Lets you define a name for referencing your DSN. Once set, the name cannot be modified.
      * - Description
        - Describes your DSN connection (optional).
      * - User
        - Sets the username of the role used for connecting.
      * - Password
        - Sets the password of the selected role.
      * - Database
        - Specifies the database name to connect to.
      * - Service
        - Specifices the :ref:`service queue<workload_manager>`. Leaving this field blank uses the default service ``sqream``.
      * - Server
        - Sets the hostname of the SQream worker.
      * - Port
        - Sets the TCP port of the SQream DB.
      * - User Server Picker
        - Connects via the load balancer (use only if exists, and check port) **Comment - what condition would cause this to not exist?**
      * - SSL
        - Specifies SSL for this connection
      * - Logging options
        - Use this screen to alter logging options when tracing the ODBC connection for possible connection issues.
   
#. When completed, save the DSN by selecting :menuselection:`OK`

.. tip:: Test the connection by clicking :menuselection:`Test` before saving. A successful test looks like this:
   
   .. image:: /_static/images/odbc_windows_dsn_test.png

#. You can now use this DSN in ODBC applications like :ref:`Tableau <connect_to_tableau>`.



Connection Parameters
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
     - Hostname of the SQream DB worker. For example, ``127.0.0.1`` or ``sqream.mynetwork.co``
   * - Port
     - TCP port of the SQream DB worker. For example, ``5000`` or ``3108``
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


#. Access the Windows menu. You can use the (:kbd:`⊞ Win`) shortcut on your keyboard to access the Windows menu.

    ::

#. In the **Type here to search** field, type **ODBC** and click **ODBC Data Sources (64-bit)**. The installer has created a sample User DSN named **SQreamDB**

 
    ::
    
#. The installer has created a sample User DSN named **SQreamDB**
   
   You can modify this DSN, or create a new one (:menuselection:`Add --> SQream ODBC Driver --> Next`)
   
   .. image:: /_static/images/odbc_windows_dsns.png

#. Enter your connection parameters. See the reference below for a description of the parameters.
   
   .. image:: /_static/images/odbc_windows_dsn_config.png

#. When completed, save the DSN by selecting :menuselection:`OK`

.. tip:: Test the connection by clicking :menuselection:`Test` before saving. A successful test looks like this:
   
   .. image:: /_static/images/odbc_windows_dsn_test.png

#. You can now use this DSN in ODBC applications like :ref:`Tableau <connect_to_tableau>`.