.. _client_drivers:

************************************
Client drivers for |latest_version|
************************************

These guides explain how to use the SQream DB client drivers, and how to use client applications with SQream DB.

Client driver downloads
=============================

All operating systems 
---------------------------

* 
   **JDBC** - `sqream-jdbc-4.4.0 (.jar) <https://sq-ftp-public.s3.amazonaws.com/sqream-jdbc-4.4.0.jar>`_
   
   :ref:`java_jdbc` Driver
   
   (SQream recommends installing via ``mvn``)

* 
   **Python** - `pysqream v3.1.3 (.tar.gz) <https://github.com/SQream/pysqream/releases/tag/v3.1.3>`_
   
   :ref:`pysqream` - Python driver
   
   (SQream recommends installing via ``pip``)

* 
   **Node.JS** - `sqream-v4.2.4 (.tar.gz) <http://downloads.sqream.com/drivers/2020.3/sqream-sqreamdb-4.2.4.tgz>`_
   
   :ref:`nodejs` - Node.JS driver
   
   (SQream recommends installing via ``npm``)

* 
   **Tableau Connector** - `SQreamDB (.taco) <http://downloads.sqream.com/drivers/2020.3/SQreamDB.taco>`_
   
   :ref:`Tableau connector<tableau_manual_installation>` - Tableau connector for manual installation

Windows
--------------

* 
   **JDBC installer** - `SQream_JDBC_Driver_v2020.2.0.exe <http://downloads.sqream.com/drivers/2020.3/SQream_JDBC_Driver_v2020.2.0.exe>`_ 
   
   Windows installer for JDBC driver, with Tableau connector.

* 
   **ODBC installer** - ``SQream Drivers v2020.2.0``
   
   :ref:`Windows installer for ODBC and JDBC<install_odbc_windows>`, with Tableau customizations. Please contact your SQream representative to get this installer.

* **.Net driver** - `SQream .Net driver v3.0.2 <http://downloads.sqream.com/drivers/2020.2/SqreamNet_net48_3.0.2.dll>`_
   
   

Linux
--------------

* 
   **SQream SQL** (x86) - `sqream-sql-v2020.1.1_stable.x86_64.tar.gz <https://sq-ftp-public.s3.amazonaws.com/sqream-sql-v2020.1.1_stable.x86_64.tar.gz>`_ 
   
   :ref:`sqream sql<sqream_sql_cli_reference>` - Interactive command-line SQL client for Intel-based machines
   
* 
   **SQream SQL** (IBM POWER9) - `sqream-sql-v2020.1.1_stable.ppc64le.tar.gz <https://sq-ftp-public.s3.amazonaws.com/sqream-sql-v2020.1.1_stable.ppc64le.tar.gz>`_ 
   
   :ref:`sqream sql<sqream_sql_cli_reference>` - Interactive command-line SQL client for IBM POWER9-based machines
   
* 
   **ODBC installer** - ``sqream_odbc_4.0.0_x86_64_linux.tar.gz``
   
   :ref:`Linux installer for ODBC<install_odbc_linux>`. Please contact your SQream representative to get this installer.

* 
   **C++ connector** - `libsqream-4.0 <https://sq-ftp-public.s3.amazonaws.com/libsqream-4.0.tar.gz>`_ 
   
   :ref:`C++ shared object<cpp_native>` library


.. toctree::
   :maxdepth: 4
   :caption: Client driver documentation:
   :titlesonly:
   
   python/index
   cpp/index
   jdbc/index
   odbc/index
   nodejs/index



.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.

.. rubric:: Looking for older drivers?

If you're looking for an older version of SQream DB drivers, versions 1.10 through 2019.2.1 are available at https://sqream.com/product/client-drivers/ .
