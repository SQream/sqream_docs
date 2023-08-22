.. _java_jdbc:

*****************************
Connecting to BLUE Using JDBC
*****************************

The SQream JDBC driver lets you connect to SQream using many Java applications and tools. This page describes how to write a Java application using the JDBC interface. The JDBC driver requires Java 1.8 or newer.


Before You Begin
================

* The BLUE JDBC driver requires Java 1.8 or newer
* Download the BLUE JDBC driver :ref:`here<client_drivers>` 
* We recommend using Oracle Java or OpenJDK

Connecting to SQream Using a JDBC Application
==============================================

Connection String
-----------------
JDBC drivers rely on a connection string.

URL Template:

.. code-block:: Java

   jdbc:Sqream://{host}:{port}/{database};accessToken=<access-token>;[<optional parameters>; ...]
   
JDBC driver class name:

.. code-block:: Java

	com.sqream.jdbc.BlueDriver
   
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
   * - ``host:port``
     - Mandatory
     - None
     - FQDN and port of the Blue cluster. For example, ``blue-cluster.isqream.com:443``
   * - ``database``
     - Mandatory
     - None
     - Database name to connect to. For example, ``master``
   * - ``accessToken``
     - Mandatory
     - None
     - The generated access token when creating a new client in the **Access Token Management** section, under :ref:`Settings<>`. 
   * - ``fetchSize``
     - Optional
     - ``true``
     - Enables on-demand loading, and defines double buffer size for the result. The ``fetchSize`` parameter is rounded according to chunk size. For example, ``fetchSize=1`` loads one row and is rounded to one chunk. If the ``fetchSize`` is 100,600, a chunk size of 100,000 loads, and is rounded to, two chunks.
   * - ``insertBuffer``
     - Optional
     - ``true``
     -  Defines the bytes size for inserting a buffer before flushing data to the server. Clients running a parameterized insert (network insert) can define the amount of data to collect before flushing the buffer.
   * - ``loggerLevel``
     - Optional
     - ``true``
     -  Defines the logger level as either ``debug`` or ``trace``.
   * - ``logFile``
     - Optional
     - ``true``
     -  Enables the file appender and defines the file name. The file name can be set as either the file name or the file path.


Sample Java Program
--------------------

You can download the :download:`JDBC Application Sample File <sample.java>` 

.. literalinclude:: sample.java
    :language: java
    :caption: JDBC Application Sample
    :linenos:
