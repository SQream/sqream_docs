.. _client_drivers:

**************
Client Drivers
**************

The guides on this page describe how to use the Sqream DB client drivers and client applications with SQream.

Client Driver Downloads
=============================

All Operating Systems 
---------------------------
The following are applicable to all operating systems:

.. _jdbc:

* **JDBC** - recommended installation via ``mvn``:

  * `JDBC .jar file <https://sq-ftp-public.s3.amazonaws.com/sqream-jdbc-4.5.6.jar>`_ - sqream-jdbc-4.5.3 (.jar)
  * :ref:`java_jdbc`

.. _.net:

* **.NET**:

  * `.NET .dll file <https://get.sqream-share.com/share/sIsu8fxv>`_ 
  * :ref:`net`


.. _python:

* **Python** - Recommended installation via ``pip``:

  * `Python .tar file <https://github.com/SQream/pysqream/releases/tag/v3.1.3>`_ - pysqream v3.1.3 (.tar.gz)
  * :ref:`pysqream`


.. _nodejs:

* **Node.JS** - Recommended installation via ``npm``:

  * `Node.JS <https://sq-ftp-public.s3.amazonaws.com/sqream-sqreamdb-4.2.4.tgz>`_ - sqream-v4.2.4 (.tar.gz)
  * :ref:`nodejs`


.. _tableau_connector:   

* **Tableau**:

  * `Tableau connector <https://sq-ftp-public.s3.amazonaws.com/SQreamDB.taco>`_ - SQream (.taco)
  * :ref:`tableau`

  
.. _powerbi_connector:   

* **Power BI**:

  * `Power BI PowerQuery connector <https://sq-ftp-public.s3.amazonaws.com/SqlODBC__v1.0.mez>`_ - SQream (.mez)
  * :ref:`power_bi`


Windows
--------------
The following are applicable to Windows:

* **ODBC installer** - SQream Drivers v2020.2.0, with Tableau customizations. Please contact your `Sqream represenative <https://sqream.atlassian.net/servicedesk/customer/portal/2>`_ for this installer.

  For more information on installing and configuring ODBC on Windows, see :ref:`Install and configure ODBC on Windows <install_odbc_windows>`.


* **Net driver** - `SQream .Net driver v3.0.2 <https://sq-ftp-public.s3.amazonaws.com/SqreamNet_net48_3.0.2.zip>`_
   
   

Linux
--------------
The following are applicable to Linux:

* `SQream SQL (x86_64) <https://sq-ftp-public.s3.amazonaws.com/sqream-sql-v2020.1.1_stable.x86_64.tar.gz>`_ - sqream-sql-v2020.1.1_stable.x86_64.tar.gz
* :ref:`sqream_sql_cli_reference` - Interactive command-line SQL client for Intel-based machines

   ::

* `SQream SQL*(IBM POWER9) <https://sq-ftp-public.s3.amazonaws.com/sqream-sql-v2020.1.1_stable.ppc64le.tar.gz>`_ - sqream-sql-v2020.1.1_stable.ppc64le.tar.gz
* :ref:`sqream_sql_cli_reference` - Interactive command-line SQL client for IBM POWER9-based machines
   
   ::

* ODBC Installer  - Please contact your SQream representative for this installer.



.. toctree::
   :maxdepth: 4
   :caption: Client Driver Documentation:
   :titlesonly:
   
   jdbc/index
   python/index
   dotnet/index
   kafka/index
   nodejs/index
   odbc/index
   dotnet/index



.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit :ref:`information_for_support` for additional support.

.. rubric:: Looking for older drivers?

If you're looking for an older version of SQream DB drivers, versions 1.10 through 2019.2.1 are available at https://sqream.com/product/client-drivers/.