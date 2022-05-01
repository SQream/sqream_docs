.. _java_jdbc:

*************************
JDBC
*************************
The SQream JDBC driver lets you connect to SQream using a variety of tools and Java applications. The **JDBC** page shows you how to write a Java application from the JDBC interface and describes the following:

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
The SQream JDBC driver requires Java 1.8 or newer, and SQream recommends using Oracle Java or OpenJDK.

* **Oracle** - `Oracle Java 8 <https://www.java.com/en/download/manual.jsp>`_

* **Linux and BSD** - `OpenJDK Preriquisites <https://openjdk.java.net/install/>`_

* **Windows** - `Zulu 8 <https://www.azul.com/downloads/zulu-community/?&version=java-8-lts&architecture=x86-64-bit&package=jdk>`_

.. _get_jdbc_jar:

Getting the JAR File
---------------------
SQream provides the JDBC driver as a zipped JAR file, which can be integrated into your Java-based applications or projects.

To download the JAR file, see :ref:`Client Drivers<client_drivers>`.

Extracting the Zip Archive
-------------------------
You can extract the JAR file from the zip archive with the following command:

.. code-block:: console

   $ unzip sqream-jdbc-4.3.0.zip

Setting Up the Class Path
----------------------------
To use the driver, you must include the jar called ``sqream-jdbc-<version>.jar`` in the class path. You can do this by using it in the ``CLASSPATH`` environment variable, or using flags on the relevant Java command line.

The following example shows how to set up the class pathwhen the JDBC driver has been unzipped to ``/home/sqream/sqream-jdbc-4.3.0.jar``:

.. code-block:: console

   $ export CLASSPATH=/home/sqream/sqream-jdbc-4.3.0.jar:$CLASSPATH
   $ java my_java_app

Alternatively, you can pass ``-classpath`` to the Java executable:

.. code-block:: console

   $ java -classpath .:/home/sqream/sqream-jdbc-4.3.0.jar my_java_app

Connecting to SQream DB with a JDBC Application
==============================================
The **Connecting to SQream DB with a JDBC Application** section describes the following:

.. contents::
   :local:
   :depth: 1
   
Connecting with a Driver Class
--------------
You can use ``com.sqream.jdbc.SQDriver`` as the driver class in the JDBC application.

.. _connection_string:

Connecting with a Connection String
--------------------
JDBC drivers rely on a connection string.

You can use the following syntax for SQream:

.. code-block:: text

   jdbc:Sqream://<host>[:<port>][/<database>];user=<user>

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^
The following table shows the connection parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Optional
     - Default
     - Description
   * - ``<host and port>``
     - Not supported
     - None
     - Hostname and port of the SQream DB worker. For example, ``127.0.0.1:5000``, ``sqream.mynetwork.co:3108``
   * - ``<database name>``
     - Not supported
     - None
     - Database name to connect to. For example, ``master``
   * - ``username=<username>``
     - Not supported
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``password=<password>``
     - Not supported
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
   * - ``service=<service>``
     - Supported
     - ``sqream``
     - Specifices service queue to use. For example, ``service=etl``
   * - ``<ssl>``
     - Supported
     - ``false``
     - Specifies SSL for this connection. For example, ``ssl=true``
   * - ``<cluster>``
     - Supported
     - ``true``
     - Connect via load balancer (use only if exists, and check port).

Connection String Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following example shows how to create a standard connection stream to the host using username and password:

.. code-block:: text

   jdbc:Sqream://192.168.4.89:80/master;user=rhendricks;password=Tr0ub4dor&3

Connecting with a Sample Java Program
--------------------
Download this file by right clicking and saving to your computer :download:`sample.java <sample.java>`.

.. literalinclude:: sample.java
    :language: java
    :caption: JDBC application sample
    :linenos: