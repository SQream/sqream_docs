.. _connect_to_tableau:

*************************
Connecting to Tableau
*************************

You can use Tableau to connect to a SQream DB cluster. This tutorial is a guide that will show you how to connect to Tableau, as well as provide some guidelines and best practices for exploring data with Tableau and SQream DB.

.. note:: SQream does not currently support Tableau on MacOS. SQream DB supports both Tableau Desktop and Tableau Server on Windows and Linux distributions.

.. contents:: In this topic:
   :local:

Installing Tableau Desktop
============================

SQream DB has been tested with versions 9.2 and newer.
If you do not already have Tableau Desktop installed, download and install Tabelau Desktop. https://www.tableau.com/products/trial

Tableau offers a time-limited trial version.


Installing the ODBC driver and customizations
===============================================

If you've already installed the SQream DB ODBC driver, we recommend that you :ref:`re-run the ODBC driver installer <install_odbc_windows>` after installing Tableau, and select the Tableau customizations checkbox, as in the image below:

.. image:: /_static/images/odbc_windows_installer_tableau.png

This is necessary because by default, Tableau has a tendency to create temporary tables and run lots of discovery queries which could impact performance.
The ODBC driver installer installs customizations for Tableau automatically.

If you want to perform this step manually, follow the instructions in the next section.

The TDC file
---------------

The TDC file (Tableau Datasource Customization) helps Tableau make full use of SQream DB's features and capabilities.

Before you start, check which version of Tableau is used. The version needs to be placed in the TDC file.

#. Download the TDC file to your computer :download:`odbc-sqream.tdc <odbc-sqream.tdc>`.
   
   Alternatively, copy the text below to a text editor.
   
   .. literalinclude:: odbc-sqream.tdc
      :language: xml
      :caption: SQream DB ODBC TDC
      :emphasize-lines: 2


#. Change the highlighted line to match your major Tableau version. For example, if you're on Tableau ``2019.2.1``, writing ``2019.2`` is enough.

#. Save the TDC file into ``C:\Users\<user name>\Documents\My Tableau Repository\Datasources``, where ``<user name>`` is the Windows username Tableau is installed in.

#. (Optional) If Tableau Server is going to be used, it is imperative that, after installing the ODBC driver, the tdc file is copied to the following path with administration rights ``C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Datasources``. The tdc file version field needs to be adapted to the Tableau server version.

Configure the ODBC connection (DSN)
======================================

Create an ODBC DSN before connecting Tableau with SQream DB. See the section titled :ref:`create_windows_odbc_dsn` for information about creating an ODBC DSN in Windows.

Remember to test the connectivity before saving the DSN.

Connecting Tableau to SQream DB
=================================

#. Start Tableau Desktop and select "Other Database (ODBC)", by navigating :menuselection:`Connect --> To a server --> More --> Other Database (ODBC)`
   
   .. image:: /_static/images/tableau_more_servers.png
   
#. In the DSN selection window, select the DSN that you created earlier and select :menuselection:`Connect --> OK`. 
   
   If prompted by Tableau, you may need to specify the user name and password again after clicking Connect.
   
   .. image:: /_static/images/tableau_choose_dsn_and_connect.png
   

Setting up SQream DB tables as data sources
==============================================

Once connected, you are taken to the data source page.

The left side of the screen contains a database and schema drop-down. Select the database name and schema name you wish to use (``public`` is the default schema in SQream DB).

   .. image:: /_static/images/tableau_data_sources.png


Drag tables you wish to use to the main area, marked as **Drag tables here**. This is also where you specify joins and data source filters.

When data source setup is completed, navigate to a new sheet to start analyzing data.

.. tip:: 
   * Read more about configuring data sources, joining, filtering, and more on `Tableau's Set Up Data Sources <https://help.tableau.com/current/pro/desktop/en-us/datasource_prepare.htm>`_ tutorials.
   * Rename the connection with a descriptive name for other users to understand. Alternatively, Tableau will generate a default name based on the DSN and tables.

Tableau best practices
========================

Cut out what you don't need
-----------------------------

* Bring only the data sources you need into Tableau. As a best practice, do not bring in tables that you don't intend to explore.

* Add filters before exploring. Every change you make while exploring data will query SQream DB, sometimes several times. Add filters to the datasource before exploring, so that the queries sent to SQream DB run faster.

Let Tableau create the queries
--------------------------------

Create pre-optimized views (see :ref:`create_view`) and point the datasource at these views.

some cases, using views or custom SQL as a datasoruce can actually degrade performance. 

We recommend testing performance of custom SQL and views, and compare with Tableau's generated SQL.

Create a separate service for Tableau
---------------------------------------

SQream recommends that Tableau get a separate service with the DWLM. This will reduce the impact of Tableau on other applications and processes, such as ETL.
This works in conjunction with the load balancer to ensure good performance.


Troubleshoot workbook performance before deploying to Tableau Server
-----------------------------------------------------------------------

Tableau has a built in `performance recorder <https://help.tableau.com/current/pro/desktop/en-us/perf_record_create_desktop.htm>`_ that shows how time is being spent. If you're seeing slow performance, this could be the result of a misconfiguration such as setting concurrency too low.

Use the Tableau Performance Recorder to view the performance of the queries that Tableau runs. Using this information, you can identify queries that can be optimized with the use of views.
