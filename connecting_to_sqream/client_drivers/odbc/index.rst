.. _odbc:

****
ODBC
****

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:
   
   install_configure_odbc_windows
   install_configure_odbc_linux

SQream has an ODBC driver to connect to SQream DB. This tutorial shows how to install the ODBC driver for Linux or Windows for use with applications like Tableau, PHP, and others that use ODBC.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Platform
     - Versions supported

   * - Windows
     -    * Windows 7 (64 bit)
          * Windows 8 (64 bit)
          * Windows 10 (64 bit)
          * Windows Server 2008 R2 (64 bit)
          * Windows Server 2012
          * Windows Server 2016
          * Windows Server 2019

   * - Linux
     -    * Red Hat Enterprise Linux (RHEL) 8.9

Other distributions may also work, but are not officially supported by SQream.


Getting the ODBC driver
=======================

The SQream ODBC driver is distributed by your SQream account manager. Before contacting your account manager, verify which platform the ODBC driver will be used on. Go to `SQream Support <https://sqream.atlassian.net/servicedesk/>`_ or contact your SQream account manager to get the driver.

The driver is provided as an executable installer for Windows, or a compressed tarball for Linux platforms.
After downloading the driver, follow the relevant instructions to install and configure the driver for your platform:

Install and configure the ODBC driver
=======================================

Continue based on your platform:

* :ref:`install_odbc_windows`
* :ref:`install_odbc_linux`