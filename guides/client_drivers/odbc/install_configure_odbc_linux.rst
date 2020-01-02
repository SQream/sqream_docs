.. _install_odbc_linux:

****************************************
Install and configure ODBC on Linux
****************************************

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:


The ODBC driver for Windows is provided as a shared library.

This tutorial shows you how to install and configure ODBC on Linux.

.. contents:: In this topic:
   :local:
   :depth: 2

Prerequisites
==============

.. _unixODBC:

unixODBC
------------

The ODBC driver requires a driver manager to manage the DSNs. SQream DB's driver is built for unixODBC.

Verify unixODBC is installed by running:

.. code-block:: console
   
   $ odbcinst -j
   unixODBC 2.3.4
   DRIVERS............: /etc/odbcinst.ini
   SYSTEM DATA SOURCES: /etc/odbc.ini
   FILE DATA SOURCES..: /etc/ODBCDataSources
   USER DATA SOURCES..: /home/rhendricks/.odbc.ini
   SQLULEN Size.......: 8
   SQLLEN Size........: 8
   SQLSETPOSIROW Size.: 8

Take note of the location of ``odbc.ini`` and ``odbcinst.ini``. In this case, ``/etc``. If ``odbcinst`` is not installed, follow the instructions for your platform below:

.. contents:: Install unixODBC on:
   :local:
   :depth: 1

Install unixODBC on RHEL 7 / CentOS 7
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ yum install -y unixODBC unixODBC-devel

Install unixODBC on Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ sudo apt-get install unixodbc unixodbc-dev


Install the ODBC driver with a script
=======================================

Use this method if you have never used ODBC on your machine before. If you have existing DSNs, see the manual install process below.

#. Unpack the tarball
   Copy the file you downloaded to any directory, and untar it:
   
   .. code-block:: console

      $ tar xf sqream_2019.2.1_odbc_3.0.0_x86_64_linux.tar.gz -C sqream_odbc64

#. Run the first-time installer. The installer will create a DSN you can edit.
   
   .. code-block:: console
      
      $ cd sqream_odbc64
      ./odbc_install.sh --install
      

#. Edit the DSN created by editing ``/etc/odbc.ini``. See the parameter explanation in the section :ref:`ODBC DSN Parameters <dsn_params>`. 


Install the ODBC driver manually
=======================================

Use this method when you have existing ODBC DSNs on your machine.

#. Unpack the tarball
   Copy the file you downloaded to the directory where you want to install it, and untar it:
   
   .. code-block:: console

      $ tar xf sqream_2019.2.1_odbc_3.0.0_x86_64_linux.tar.gz -C sqream_odbc64

   Take note of the directory where you unpacked the driver. For example, ``/home/rhendricks/sqream_odbc64``

#. Locate the ``odbc.ini`` and ``odbcinst.ini`` files, using ``odbcinst -j``.

   #. In ``odbcinst.ini``, add the following lines to register the driver (change the highlighted paths to match your specific driver):
      
      .. code-block:: ini
         :emphasize-lines: 6,7
         
         [ODBC Drivers]
         SqreamODBCDriver=Installed
         
         [SqreamODBCDriverDriver]
         Description=Driver DSII SqreamODBC 64bit
         Driver=/home/rhendricks/sqream_odbc64/sqream_odbc64.so
         Setup=/home/rhendricks/sqream_odbc64/sqream_odbc64.so
         APILevel=1
         ConnectFunctions=YYY
         DriverODBCVer=03.80
         SQLLevel=1
         IconvEncoding=UCS-4LE

   #. In ``odbc.ini``, add the following lines to configure the DSN (change the highlighted parameters to match your installation):
      
      .. code-block:: ini
         :emphasize-lines: 6,7,8,9,10,11,12,13,14
      
         [ODBC Data Sources]
         MyTest=SqreamODBCDriver
         
         [MyTest]
         Description=64-bit Sqream ODBC
         Driver=/home/rhendricks/sqream_odbc64/sqream_odbc64.so
         Server="127.0.0.1"
         Port="5000"
         Database="raviga"
         Service=""
         User="rhendricks"
         Password="Tr0ub4dor&3"
         Cluster=false
         Ssl=false

      Parameters are in the form of ``parameter = value``. For details about the parameters that can be set for each DSN, see the section :ref:`ODBC DSN Parameters <dsn_params>`.


   #. Create a file called ``sqream_odbc.ini`` for managing the driver settings and logging.
      This file should be created alongside the other files, and add the following lines (change the highlighted parameters to match your installation):
      
         .. code-block:: ini
            :emphasize-lines: 5,7
            
            # Note that this default DriverManagerEncoding of UTF-32 is for iODBC. unixODBC uses UTF-16 by default.
            # If unixODBC was compiled with -DSQL_WCHART_CONVERT, then UTF-32 is the correct value.
            # Execute 'odbc_config --cflags' to determine if you need UTF-32 or UTF-16 on unixODBC
            [Driver]
            DriverManagerEncoding=UTF-16
            DriverLocale=en-US
            ErrorMessagesPath=/home/rhendricks/sqream_odbc64/ErrorMessages
            LogLevel=0
            LogNamespace=
            LogPath=/tmp/
            ODBCInstLib=libodbcinst.so

#. Finally, Add a new path to LB_LIBRARY_PATH to include prerequisite libraries (change the path to match your installation):
   
   .. code-block:: console
   
      $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/rhendricks/sqream_odbc64/lib

Testing the connection
========================

Test the driver using ``isql``.

If the DSN created is called ``MyTest`` as the example, run isql in this format:

.. code-block:: console
   
   $ isql MyTest


.. _dsn_params:

ODBC DSN Parameters
=======================

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Default
     - Description
   * - Data Source Name
     - None
     - An easily recognizable name that you'll use to reference this DSN.
   * - Description
     - None
     - A description of this DSN for your convenience. You can leave this blank.
   * - User
     - None
     - Username of a role to use for connection. For example, ``User="rhendricks"``
   * - Password
     - None
     - Specifies the password of the selected role. For example, ``User="Tr0ub4dor&3"``
   * - Database
     - None
     - Specifies the database name to connect to. For example, ``Database="master"``
   * - Service
     - ``sqream``
     - Specifices :ref:`service queue<workload_manager>` to use. For example, ``Service="etl"``. Leave blank (``Service=""``) for default service ``sqream``.
   * - Server
     - None
     - Hostname of the SQream DB worker. For example, ``Server="127.0.0.1"`` or ``Server="sqream.mynetwork.co"``
   * - Port
     - None
     - TCP port of the SQream DB worker. For example, ``Port="5000"`` or ``Port="3108"`` for the load balancer
   * - Cluster
     - ``false``
     - Connect via load balancer (use only if exists, and check port). For example, ``Cluster=true``
   * - Ssl
     - ``false``
     - Specifies SSL for this connection. For example, ``Ssl=true``
   * - DriverManagerEncoding
     - ``UTF-16``
     - Depending on how unixODBC is installed, you may need to change this to ``UTF-32``.
   * - ErrorMessagesPath
     - None
     - Location where the driver was installed. For example, ``ErrorMessagePath=/home/rhendricks/sqream_odbc64/ErrorMessages``.
   * - LogLevel
     - 0
     - Set to 0-6 for logging. Use this setting when instructed to by SQream Support. For example, ``LogLevel=1``

         .. hlist::
            :columns: 3

            * 0 = Disable tracing
            * 1 = Fatal only error tracing
            * 2 = Error tracing
            * 3 = Warning tracing
            * 4 = Info tracing
            * 5 = Debug tracing
            * 6 = Detailed tracing



