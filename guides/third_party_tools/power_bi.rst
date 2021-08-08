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




   
   
Installing the ODBC Driver
===========================
You must install the ODBC driver before configuring it. For more information about installing the ODBC driver, see `Installing the ODBC Driver <https://docs.sqream.com/en/latest/guides/client_drivers/odbc/install_configure_odbc_windows.html#installing-the-odbc-driver>`_.




Configuring your ODBC Drivers
=================

Getting started using Power BI requires you to configure your ODBC drivers. ODBC drivers are configured using DSNs, and each DSN represents one SQream database.

**To configure your ODBC drivers:**

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