.. _semarchy:

***************
Semarchy
***************

Semarchy's Intelligent Data eXchange (IDX) facilitates seamless data integration and interoperability across systems. IDX ensures reliable data exchange between different applications, enhancing overall data quality, governance, and adaptability for critical business operations.

Before You Begin
================

It is essential that you use Semarchy version 2023.01 or later.

Setting Up a Connection to SQreamDB
===================================

#. Install the Semarchy SQreamDB component as described in `Semarchy documentation <https://www.semarchy.com/doc/semarchy-xdi/xdi/latest/Components/sqreamdb/overview.html>`_.

#. Install SQreamDB :ref:`java_jdbc`.

JDBC Connection String
======================

The following is a SQreamDB JDBC connection string template:

.. code-block:: text

   jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...]

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - State
     - Default
     - Description
   * - ``<host and port>``
     - Mandatory
     - None
     - Hostname and port of the SQream DB worker. For example, ``127.0.0.1:5000``, ``sqream.mynetwork.co:3108``
   * - ``<database name>``
     - Mandatory
     - None
     - Database name to connect to. For example, ``master``
   * - ``username=<username>``
     - Optional
     - None
     - Username of a role to use for connection. For example, ``username=SqreamRole`` 
   * - ``password=<password>``
     - Optional
     - None
     - Specifies the password of the selected role. For example, ``password=SqreamRolePassword2023``
   * - ``service=<service>``
     - Optional
     - ``sqream``
     - Specifices service queue to use. For example, ``service=etl``
   * - ``<ssl>``
     - Optional
     - ``false``
     - Specifies SSL for this connection. For example, ``ssl=true``
   * - ``<cluster>``
     - Optional
     - ``true``
     - Connect via load balancer (use only if exists, and check port).
   * - ``<fetchSize>``
     - Optional
     - ``true``
     - Enables on-demand loading, and defines double buffer size for the result. The ``fetchSize`` parameter is rounded according to chunk size. For example, ``fetchSize=1`` loads one row and is rounded to one chunk. If the ``fetchSize`` is 100,600, a chunk size of 100,000 loads, and is rounded to, two chunks.
   * - ``<insertBuffer>``
     - Optional
     - ``true``
     -  Defines the bytes size for inserting a buffer before flushing data to the server. Clients running a parameterized insert (network insert) can define the amount of data to collect before flushing the buffer.
   * - ``<loggerLevel>``
     - Optional
     - ``true``
     -  Defines the logger level as either ``debug`` or ``trace``.
   * - ``<logFile>``
     - Optional
     - ``true``
     -  Enables the file appender and defines the file name. The file name can be set as either the file name or the file path.
   * - ``<idleconnectiontimeout>``
     - Optional
     - 0
     - Sets the duration, in seconds, for which a database connection can remain idle before it is terminated. If the parameter is set to its default value, idle connections will not be terminated. The idle connection timer begins counting after the completion of query execution.

