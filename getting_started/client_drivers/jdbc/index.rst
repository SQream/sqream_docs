.. _java_jdbc:

*************************
JDBC
*************************
The SQream JDBC driver lets you connect to SQream using many Java applications and tools. This page describes how to write a Java application using the JDBC interface. The JDBC driver requires Java 1.8 or newer.

.. contents:: 
   :local:
   :depth: 1

Prerequisites
----------------
The SQream JDBC driver requires Java 1.8 or newer, and SQream recommends using Oracle Java or OpenJDK.:

Connecting to SQream Using a JDBC Application
==============================================
You can connect to SQream using one of the following JDBC applications:

.. contents:: 
   :local:
   :depth: 1
   
Driver Class
--------------
Use ``com.sqream.jdbc.SQDriver`` as the driver class in the JDBC application.

Connection String
--------------------
JDBC drivers rely on a connection string.

The following is the syntax for BLUE:

.. code-block:: text

   jdbc:Sqream://<host and port>/<database name>;access token=<access token>sqream;[<optional parameters>; ...]

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^
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
   * - ``access token=<access token>``
     - Mandatory
     - None
     - The generated access token when creating a new client in the **Access Token Management** section, under :ref:`Settings<>`. 
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

Connection String Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following is an example of a SQream cluster with load balancer and no service queues (with SSL):

.. code-block:: text

   jdbc:Sqream://sqream.mynetwork.co:3108/master;user=rhendricks;password=Tr0ub4dor&3;ssl=true;cluster=true

The following is a minimal example for a local standalone SQream database:

.. code-block:: text 

   jdbc:Sqream://127.0.0.1:5000/master;user=rhendricks;password=Tr0ub4dor&3

The following is an example of a SQream cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: text

   jdbc:Sqream://sqream.mynetwork.co:3108/raviga;user=rhendricks;password=Tr0ub4dor&3;cluster=true;service=etl

Sample Java Program
--------------------
You can download the :download:`JDBC Application Sample File <sample.java>` below by right-clicking and saving it to your computer.

.. literalinclude:: sample.java
    :language: java
    :caption: JDBC Application Sample
    :linenos:
