:orphan:

.. _odbc:

=============================
Connecting to BLUE Using ODBC
=============================

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:


Connection String Syntax
------------------------

.. code-block:: java

   odbc:Sqream://<host and port>/<database name>;--access-token=<YourToken>;[<optional parameters>; ...]

Connection Parameters
---------------------
The following table shows the connection string parameters:

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
   * - ``access token=<YourToken>``
     - Mandatory
     - None
     - A BLUE client access token 
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
     - Enables on-demand loading, and defines double buffer size for result. The ``fetchSize`` parameter is rounded according to chunk size. For example, ``fetchSize=1`` loads one row and is rounded to one chunk. If the fetchSize is 100,600, a chunk size of 100,000 loads, and is rounded to, two chunks.
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
