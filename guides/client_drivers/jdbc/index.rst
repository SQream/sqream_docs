.. _java_jdbc:

*************************
JDBC
*************************

The SQream DB JDBC driver allows many Java applications and tools connect to SQream DB.
This tutorial shows how to write a Java application using the JDBC interface.

The JDBC driver requires Java 1.8 or newer.

.. contents:: In this topic:
   :local:

Installing the JDBC Driver
==================================

Prerequisites
----------------

The SQream DB JDBC driver requires Java 1.8 or newer. We recommend either Oracle Java or OpenJDK.

**Oracle Java**

Download and install Java 8 from Oracle for your platform

https://www.java.com/en/download/manual.jsp

**OpenJDK**

For Linux and BSD, see https://openjdk.java.net/install/

For Windows, SQream recommends Zulu 8 https://www.azul.com/downloads/zulu-community/?&version=java-8-lts&architecture=x86-64-bit&package=jdk

.. _get_jdbc_jar:

Getting the JAR file
---------------------

The JDBC driver is provided as a zipped JAR file, available for download from the :ref:`client drivers download page<client_drivers>`. This JAR file can integrate into your Java-based applications or projects.


Extract the ZIP Archive
-------------------------

Extract the JAR file from the zip archive

.. code-block:: console

   $ unzip sqream-jdbc-4.3.0.zip

Setting up the Class Path
----------------------------

To use the driver, the JAR named ``sqream-jdbc-<version>.jar`` (for example, ``sqream-jdbc-4.3.0.jar``) needs to be included in the class path, either by putting it in the ``CLASSPATH`` environment variable, or by using flags on the relevant Java command line.

For example, if the JDBC driver has been unzipped to ``/home/sqream/sqream-jdbc-4.3.0.jar``, the application should be run as follows:

.. code-block:: console

   $ export CLASSPATH=/home/sqream/sqream-jdbc-4.3.0.jar:$CLASSPATH
   $ java my_java_app

An alternative method is to pass ``-classpath`` to the Java executable:

.. code-block:: console

   $ java -classpath .:/home/sqream/sqream-jdbc-4.3.0.jar my_java_app


Connect to SQream DB with a JDBC Application
==============================================

Driver Class
--------------

Use ``com.sqream.jdbc.SQDriver`` as the driver class in the JDBC application.


.. _connection_string:

Connection String
--------------------

JDBC drivers rely on a connection string. Use the following syntax for SQream DB

.. code-block:: text

   jdbc:Sqream://<host and port>/<database name>;user=<username>;password=<password>sqream;[<optional parameters>; ...]

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Optional
     - Default
     - Description
   * - ``<host and port>``
     - ✗
     - None
     - Hostname and port of the SQream DB worker. For example, ``127.0.0.1:5000``, ``sqream.mynetwork.co:3108``
   * - ``<database name>``
     - ✗
     - None
     - Database name to connect to. For example, ``master``
   * - ``username=<username>``
     - ✗
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``password=<password>``
     - ✗
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
   * - ``service=<service>``
     - ✓
     - ``sqream``
     - Specifices service queue to use. For example, ``service=etl``
   * - ``<ssl>``
     - ✓
     - ``false``
     - Specifies SSL for this connection. For example, ``ssl=true``
   * - ``<cluster>``
     - ✓
     - ``true``
     - Connect via load balancer (use only if exists, and check port).

Connection String Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a SQream DB cluster with load balancer and no service queues, with SSL

.. code-block:: text

   jdbc:Sqream://sqream.mynetwork.co:3108/master;user=rhendricks;password=Tr0ub4dor&3;ssl=true;cluster=true

Minimal example for a local, standalone SQream DB

.. code-block:: text 

   jdbc:Sqream://127.0.0.1:5000/master;user=rhendricks;password=Tr0ub4dor&3

For a SQream DB cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: text

   jdbc:Sqream://sqream.mynetwork.co:3108/raviga;user=rhendricks;password=Tr0ub4dor&3;cluster=true;service=etl


Sample Java Program
--------------------

Download this file by right clicking and saving to your computer :download:`sample.java <sample.java>`.

.. literalinclude:: sample.java
    :language: java
    :caption: JDBC application sample
    :linenos:
