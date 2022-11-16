.. _client_drivers:

************************************
Client Drivers for 2022.1.6
************************************

The guides on this page describe how to use the Sqream DB client drivers and client applications with SQream.

Client Driver Downloads
=============================

All Operating Systems 
---------------------------
The following are applicable to all operating systems:

.. _jdbc:

* **JDBC** - recommended installation via ``mvn``:

  * `JDBC .jar file <https://sq-ftp-public.s3.amazonaws.com/sqream-jdbc-4.5.3.jar>`_ - sqream-jdbc-4.5.3 (.jar)
  * `JDBC driver <https://docs.sqream.com/en/v2021.1/third_party_tools/client_drivers/jdbc/index.html#>`_

.. _.net:

* **.NET**:

  * `.NET integration


.. _python:

* **Python** - Recommended installation via ``pip``:

  * `Python .tar file <https://github.com/SQream/pysqream/releases/tag/v3.1.3>`_ - pysqream v3.1.3 (.tar.gz)
  * `Python driver <https://docs.sqream.com/en/v2021.1/third_party_tools/client_drivers/python/index.html>`_


.. _nodejs:

* **Node.JS** - Recommended installation via ``npm``:

  * `Node.JS <https://sq-ftp-public.s3.amazonaws.com/sqream-sqreamdb-4.2.4.tgz>`_ - sqream-v4.2.4 (.tar.gz)
  * `Node.JS driver <https://docs.sqream.com/en/v2021.1/third_party_tools/client_drivers/nodejs/index.html>`_


.. _tableau_connector:   

* **Tableau**:

  * `Tableau connector <https://sq-ftp-public.s3.amazonaws.com/SQreamDB.taco>`_ - SQream (.taco)
  * `Tableau manual installation <https://docs.sqream.com/en/v2021.1/third_party_tools/client_platforms/tableau.html#>`_

  
.. _powerbi_connector:   

* **Power BI**:

  * `Power BI PowerQuery connector <https://sq-ftp-public.s3.amazonaws.com/SqlODBC__v1.0.mez>`_ - SQream (.mez)
  * `Power BI manual installation <https://docs.sqream.com/en/v2021.1/third_party_tools/client_platforms/power_bi.html>`_


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
* `Sqream SQL CLI Reference <https://docs.sqream.com/en/v2021.1/reference/cli/sqream_sql.html#sqream-sql-cli-reference>`_ - Interactive command-line SQL client for Intel-based machines

   ::

* `SQream SQL*(IBM POWER9) <https://sq-ftp-public.s3.amazonaws.com/sqream-sql-v2020.1.1_stable.ppc64le.tar.gz>`_ - sqream-sql-v2020.1.1_stable.ppc64le.tar.gz
* `Sqream SQL CLI Reference <https://docs.sqream.com/en/v2021.1/reference/cli/sqream_sql.html#sqream-sql-cli-reference>`_ - Interactive command-line SQL client for IBM POWER9-based machines
   
   ::

* ODBC Installer  - Please contact your SQream representative for this installer.



.. toctree::
   :maxdepth: 4
   :caption: Client Driver Documentation:
   :titlesonly:
   
   jdbc/index
   python/index
   nodejs/index
   odbc/index



.. rubric:: Need help?

If you couldn't find what you're looking for, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.

.. rubric:: Looking for older drivers?

If you're looking for an older version of SQream DB drivers, versions 1.10 through 2019.2.1 are available at https://sqream.com/product/client-drivers/.