.. _connect_to_tableau:

*************************
Connecting to Tableau
*************************

You can use Tableau to connect to a SQream DB cluster. This tutorial is a guide that will show you how to connect to Tableau, as well as provide some guidelines and best practices for exploring data with Tableau and SQream DB.

SQream DB supports both Tableau Desktop and Tableau Server on Windows, MacOS, and Linux distributions.

.. contents:: In this topic:
   :local:

Installing Tableau Desktop
============================

SQream DB has been tested with versions 9.2 and newer.
If you do not already have Tableau Desktop installed, download and install Tabelau Desktop. https://www.tableau.com/products/trial

Tableau offers a time-limited trial version.

Installing the JDBC driver and connector
=================================================

Starting from Tableau v2019.4, SQream DB recommends using the JDBC driver instead of the previously recommended ODBC driver.

If you have Tableau Desktop on Windows, we recommend using the :ref:`JDBC installer method<tableau_jdbc_installer>`. 

If you have Tableau Server or Tableau on MacOS and Linux follow the instructions for a :ref:`manual installation<tableau_manual_installation>`.

.. _tableau_jdbc_installer:

Installing with the Windows installer
-----------------------------------------

1. Close Tableau Desktop

2. Download the JDBC installer :ref:`from the client drivers page<client_drivers>`.

3. 
   Start the installer, and ensure that the "**Tableau Desktop Connector**" item is selected, as in the image below.
   
   .. image:: /_static/images/jdbc_windows_installer_screen.png

4. Restart Tableau Desktop, continue to :ref:`connecting to SQream DB<tableau_connect_to_sqream_db>`.

.. _tableau_manual_installation:

Installing the JDBC driver manually (MacOS, Linux, Tableau Server)
-----------------------------------------------------------------------

Download the JDBC and Tableau Connector (taco)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download the JDBC installer :ref:`from the client drivers page<client_drivers>`.

2. Download the SQream DB Tableau connector (.taco) :ref:`from the client drivers page<client_drivers>`.

Install JDBC driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unzip the JDBC driver into a Tableau drivers directory. Based on your installation of Tableau, this may be at:

* Tableau Desktop on Windows: ``c:\Program Files\Tableau\Drivers``

* Tableau Desktop on MacOS: ``~/Library/Tableau/Drivers``

* Tableau on Linux: ``/opt/tableau/tableau_driver/jdbc``

Install taco
^^^^^^^^^^^^^^^^^^

Place the ``SQreamDB.taco`` file in the Tableau connectors directory. Based on your installation of Tableau, this may be at:

* Tableau Desktop on Windows: ``C:\Users\<your user>\My Tableau Repository\Connectors``

* Tableau Desktop on MacOS: ``~/My Tableau Repository/Connectors``

* Tableau Server:
   
   1. Create a directory for Tableau connectors. For example: ``C:\tableau_connectors``
   
   2. Copy the ``SQreamDB.taco`` file into the directory you created
   
   3. Set the ``native_api.connect_plugins_path`` option with ``tsm``. For example:
      
      ``tsm configuration set -k native_api.connect_plugins_path -v C:/tableau_connectors``
      
      Then, apply the pending configuration changes with ``tsm pending-changes apply``
      
      .. warning:: This restarts the server.

 

You can now restart Tableau Desktop or Server to begin using the SQream DB driver. Continue to :ref:`connecting to SQream DB<tableau_connect_to_sqream_db>`.

Legacy method - ODBC for Tableau versions before v2019.3
==================================================================

Installing the ODBC driver and customizations
--------------------------------------------------

If you've already installed the SQream DB ODBC driver, we recommend that you :ref:`re-run the ODBC driver installer <install_odbc_windows>` after installing Tableau, and select the Tableau customizations checkbox, as in the image below:

.. image:: /_static/images/odbc_windows_installer_tableau.png

This is necessary because by default, Tableau has a tendency to create temporary tables and run lots of discovery queries which could impact performance.
The ODBC driver installer installs customizations for Tableau automatically.

If you want to perform this step manually, follow the instructions in the next section.

The TDC file
^^^^^^^^^^^^^^^^^^^

The TDC file (Tableau Datasource Customization) helps Tableau make full use of SQream DB's features and capabilities.

Before you start, check which version of Tableau is used. The version needs to be placed in the TDC file.

#. Download the TDC file to your computer :download:`odbc-sqream.tdc <odbc-sqream.tdc>`.
   
   Alternatively, copy the text below to a text editor.
   
   .. literalinclude:: odbc-sqream.tdc
      :language: xml
      :caption: SQream DB ODBC TDC
      :emphasize-lines: 2


#. Change the highlighted line to match your major Tableau version. For example, if you're on Tableau ``2019.2.1``, writing ``2019.2`` is enough.

#. 
   * For **Tableau Desktop** - save the TDC file to ``C:\Users\<user name>\Documents\My Tableau Repository\Datasources``, where ``<user name>`` is the Windows username Tableau is installed in.
   
   * For **Tableau Server** - save the TDC file to ``C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Datasources``.

Configure the ODBC connection (DSN)
------------------------------------------

Create an ODBC DSN before connecting Tableau with SQream DB. See the section titled :ref:`create_windows_odbc_dsn` for information about creating an ODBC DSN in Windows.

Remember to test the connectivity before saving the DSN.

Connecting Tableau to SQream DB
---------------------------------------

#. Start Tableau Desktop and select "Other Database (ODBC)", by navigating :menuselection:`Connect --> To a server --> More --> Other Database (ODBC)`
   
   .. image:: /_static/images/tableau_more_servers.png
   
#. In the DSN selection window, select the DSN that you created earlier and select :menuselection:`Connect --> OK`. 
   
   If prompted by Tableau, you may need to specify the user name and password again after clicking Connect.
   
   .. image:: /_static/images/tableau_choose_dsn_and_connect.png
   

.. _tableau_connect_to_sqream_db:

Connecting to SQream DB
===========================

#. Start Tableau Desktop.

#. Select "More", by navigating :menuselection:`Connect --> To a server --> More`
   
   .. image:: /_static/images/tableau_more_servers_2.png

#. Select "SQream DB by SQream Technologies"
   
   .. image:: /_static/images/tableau_more_servers_3.png

#. Fill in the details for your SQream DB installation and click :menuselection:`Sign In`.
   
   .. image:: /_static/images/tableau_new_connection.png
   

.. list-table:: Connection parameters reference
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Description
   * - Server
     - Hostname of the SQream DB worker. For example, ``127.0.0.1`` or ``sqream.mynetwork.co``
   * - Port
     - TCP port of the SQream DB worker. For example, ``3108`` when using a load balancer or ``5100`` when connecting directly to a worker with SSL
   * - Database
     - Specifies the database name to connect to. For example, ``master``
   * - Cluster
     - Connect via load balancer. Accepts ``true`` and ``false``. Double check the connection port when setting this.
   * - Username
     - Username of a role to use for connection. For example, ``rhendricks``
   * - Password
     - Specifies the password of the selected role. For example, ``Tr0ub4dor&3``
   * - Require SSL
     - Specifies SSL for this connection


Setting up SQream DB tables as data sources
======================================================
Once connected, you are taken to the data source page.

The left side of the screen contains a database and schema drop-down. Select the database name and schema name you wish to use (``public`` is the default schema in SQream DB).

   .. image:: /_static/images/tableau_data_sources.png

Drag tables you wish to use to the main area, marked as **Drag tables here**. This is also where you specify joins and data source filters.

When data source setup is completed, navigate to a new sheet to start analyzing data.

.. tip:: 
   * Read more about configuring data sources, joining, filtering, and more on `Tableau's Set Up Data Sources <https://help.tableau.com/current/pro/desktop/en-us/datasource_prepare.htm>`_ tutorials.
   * Rename the connection with a descriptive name for other users to understand. Alternatively, Tableau will generate a default name based on the DSN and tables.

Tableau best practices and troubleshooting
=================================================

Cut out what you don't need
-----------------------------

* Bring only the data sources you need into Tableau. As a best practice, do not bring in tables that you don't intend to explore.

* Add filters before exploring. Every change you make while exploring data will query SQream DB, sometimes several times. Add filters to the datasource before exploring, so that the queries sent to SQream DB run faster.

Let Tableau create the queries
--------------------------------

Create pre-optimized views (see :ref:`create_view`) and point the datasource at these views.

In some cases, using views or custom SQL as a datasource can actually degrade performance. 

We recommend testing performance of custom SQL and views, and compare with Tableau's generated SQL.

Create a separate service for Tableau
---------------------------------------

SQream recommends that Tableau get a separate service with the DWLM. This will reduce the impact of Tableau on other applications and processes, such as ETL.
This works in conjunction with the load balancer to ensure good performance.


Troubleshoot workbook performance before deploying to Tableau Server
-----------------------------------------------------------------------

Tableau has a built in `performance recorder <https://help.tableau.com/current/pro/desktop/en-us/perf_record_create_desktop.htm>`_ that shows how time is being spent. If you're seeing slow performance, this could be the result of a misconfiguration such as setting concurrency too low.

Use the Tableau Performance Recorder to view the performance of the queries that Tableau runs. Using this information, you can identify queries that can be optimized with the use of views.

Troubleshooting ``Error Code: 37CE01A3``, ``No suitable driver installed or the URL is incorrect``
--------------------------------------------------------------------------------------------------------

In some cases, Tableau may have trouble finding the SQream DB JDBC driver. This message explains that the driver can't be found.

To solve this issue, try two things:

1. Verify that the JDBC driver was placed in the correct directory:

   * Tableau Desktop on Windows: ``c:\Program Files\Tableau\Drivers``

   * Tableau Desktop on MacOS: ``~/Library/Tableau/Drivers``

   * Tableau on Linux: ``/opt/tableau/tableau_driver/jdbc``

2. Find the file path for the JDBC driver and add it to the Java classpath:
   
   * On Linux, ``export CLASSPATH=<absolute path of SQream DB JDBC driver>;$CLASSPATH``
   
   * On Windows, add an envrionment variable for the classpath:
   
         .. image:: /_static/images/set_java_classpath.png

If you're still experiencing issues after restarting Tableau, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.
