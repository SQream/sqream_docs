.. _java_jdbc:

*************************
JDBC
*************************
The SQream JDBC driver lets you connect to SQream using many Java applications and tools. This page describes how to write a Java application using the JDBC interface. The JDBC driver requires Java 1.8 or newer.

The JDBC page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Installing the JDBC Driver
==================================
The **Installing the JDBC Driver** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Prerequisites
----------------
The SQream JDBC driver requires Java 1.8 or newer, and SQream recommends using Oracle Java or OpenJDK.:

* **Oracle Java** - Download and install `Java 8 <https://www.java.com/en/download/manual.jsp>`_ from Oracle for your platform.

   ::
   
* **OpenJDK** - Install `OpenJDK <https://openjdk.java.net/install/>`_

   ::
   
* **Windows** - SQream recommends installing `Zulu 8 <https://www.azul.com/downloads/zulu-community/?&version=java-8-lts&architecture=x86-64-bit&package=jdk>`_

Getting the JAR file
---------------------
The SQream JDBC driver is available for download from the :ref:`client drivers download page<client_drivers>`. This JAR file can be integrated into your Java-based applications or projects.


Setting Up the Class Path
----------------------------
To use the driver, you must include the JAR named ``sqream-jdbc-<version>.jar`` in the class path, either by inserting it in the ``CLASSPATH`` environment variable, or by using flags on the relevant Java command line.

For example, if the JDBC driver has been unzipped to ``/home/sqream/sqream-jdbc-4.3.0.jar``, the following command is used to run application:

.. code-block:: console

   $ export CLASSPATH=/home/sqream/sqream-jdbc-4.3.0.jar:$CLASSPATH
   $ java my_java_app

Alternatively, you can pass ``-classpath`` to the Java executable file:

.. code-block:: console

   $ java -classpath .:/home/sqream/sqream-jdbc-4.3.0.jar my_java_app

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

The following is the syntax for SQream:

.. code-block:: text

   jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>sqream;[<optional parameters>; ...]

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
   * - ``username=<username>``
     - Mandatory
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``password=<password>``
     - Mandatory
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
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
   * - ``<idleconnectiontimeout>``
     - Optional
     - 0
     - Sets the duration, in seconds, for which a database connection can remain idle before it is terminated. If the parameter is set to its default value, idle connections will not be terminated. The idle connection timer begins counting after the completion of a query execution.

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
