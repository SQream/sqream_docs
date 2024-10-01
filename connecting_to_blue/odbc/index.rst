:orphan:

.. _odbc_windows:

****************************************
Install and Configure ODBC on Windows
****************************************

The ODBC driver for Windows is provided as a self-contained installer. 

This tutorial shows you how to install and configure ODBC on Windows.

Installing the ODBC Driver
==================================

Prerequisites
----------------
Download the BLUE ODBC Windows driver `here <https://sq-ftp-public.s3.amazonaws.com/SQream_ODBC_Blue_Driver_v5.0.6.exe>`_


Administrator Privileges
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SQream Blue ODBC driver requires administrator privileges on your computer to add the DSNs (data source names).


Running the Windows Installer
------------------------------

Install the driver by following the on-screen instructions in the easy-to-follow installer.


Configuring the ODBC Driver DSN
======================================

ODBC driver configurations are done via DSNs. Each DSN represents one SQream Blue.

#. Open up the Windows menu by clicking the Windows button on your keyboard (:kbd:`⊞ Win`) or pressing the Windows button with your mouse.

#. Type **ODBC** and select **ODBC Data Sources (64-bit)**. Click the item to open up the setup window.
   

#. The installer has created a sample User DSN named **SQreamBlueODBC**
   
   You can modify this DSN, or create a new one (:menuselection:`Add --> SQream Blue Driver --> Next`)
   

#. Enter your connection parameters. See the reference below for a description of the parameters.
   

#. When completed, save the DSN by selecting :menuselection:`OK`

.. tip:: Test the connection by clicking :menuselection:`Test` before saving. A successful test looks like this:
   





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
   * - Token
     - `Access Token <../blue-review/access_tokens/index.html#generating-access-tokens>`_
   * - Database
     - Specifies the database name to connect to. For example, ``master``
   * - Server
     - URL of the SQream Blue worker. For example, ``aws-purple.isqream.com``
   * - Port
     - TCP port of the SQream Blue worker. For example, ``443`` 



Troubleshooting
==================

Solving "Code 126" ODBC errors
---------------------------------

After installing the ODBC driver, you may experience the following error: 

.. code-block:: none

   The setup routines for the SQreamDriver64 ODBC driver could not be loaded due to system error
   code 126: The specified module could not be found.
   (c:\Program Files\SQream Technologies\ODBC Driver\sqreamOdbc64.dll)

This is an issue with the Visual Studio Redistributable packages. Verify you've correctly installed them.

Limitations
===============

Please note that the ODBC protocol does not support the use of ARRAY data type. If your database schema includes ARRAY columns, you may encounter compatibility issues when using ODBC to connect to the database.