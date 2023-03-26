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

  * `JDBC .jar file <https://sq-ftp-public.s3.amazonaws.com/sqream-jdbc-4.5.6.jar>`_ - sqream-jdbc-4.5.6 (.jar)
  * :ref:`java_jdbc`

.. _.net:

* **.NET**:

  * `.NET .dll file <https://get.sqream-share.com/share/sIsu8fxv>`_ 
  * :ref:`net`

.. _trino:

* **Trino**:

  * `Trino Connector <>`_ 
  * :ref:`trino` 

.. _python:

* **Python** - Recommended installation via ``pip``:

  * `Python .tar file <https://github.com/SQream/pysqream/releases/tag/v3.2.4>`_ - pysqream v3.2.4 (.tar.gz)
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

  * `Power BI PowerQuery Connector <https://sq-ftp-public.s3.amazonaws.com/SqlODBC__v1.0.mez>`_ - SQream (.mez)
  * :ref:`power_bi`
  



Windows
--------------
The following are applicable to Windows:

* **ODBC installer** - SQream Drivers v2020.2.0, with Tableau customizations. Please contact your `Sqream represenative <https://sqream.atlassian.net/servicedesk/customer/portal/2>`_ for this installer.

  For more information on installing and configuring ODBC on Windows, see :ref:`Install and configure ODBC on Windows <install_odbc_windows>`.


* **Net driver** - `SQream .Net driver v3.0.2 <https://sq-ftp-public.s3.amazonaws.com/SqreamNet_net48_3.0.2.zip>`_



.. toctree::
   :maxdepth: 4
   :caption: Client Driver Documentation:
   :titlesonly:
   
   trino/index
   jdbc/index
   python/index
   nodejs/index
   odbc/index
   dotnet/index




.. rubric:: Need help?

If you couldn't find what you're looking for, contact `SQream Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_

.. rubric:: Looking for older drivers?

If you're looking for an older version of SQream DB drivers, versions 1.10 through 2019.2.1 are available at https://sqream.com/product/client-drivers/.