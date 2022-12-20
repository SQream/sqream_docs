.. _trino:

*************************
Connecting to SQream Using Trino
*************************

Overview
=====================
SQream's Trino connector plugin, based on standard JDBC, enables storing and fast querying large volumes of data.

The **Connecting to SQream Using Trino** page is a Quick Start Guide that describes how to install Trino and the JDBC driver and connect to SQream for data analysis. It also describes using best practices and troubleshoot issues that may occur while installing Trino.



.. contents::
   :local:
   :depth: 1

Prerequisites
-------------

SQream version xxxxx
JDBC version 4.5.6 or later
Trino version 403 or later

   
Installing the Trino Connector Plugin
-------------------------------------

Install the Trino plugin on all nodes dedicated to Trino within your cluster.

1. Create a dedicated directory for the Trino plugin.

2. Download the latest version of Trino plugin.

3. Extract the Trino plugin ZIP file and copy the extracted directory into the Trino plugin directory.

.. code-block:: postgres

	trino-server/
	└── plugin
		└── sqream
			├── sqream-jdbc.jar
			├── trino-sqream-services.jar
			├── trino-sqream-SNAPSHOT.jar
			└── all dependencies



Connecting to SQream
--------------------

Under ``trino-server/etc/catalog``, create a ``sqream.properties`` file.

.. code-block:: postgres

	connector.name=sqream
	connection-url=jdbc:Sqream://<host>:<port>/<database>...
	
Supported Data Types and Mapping
--------------------------------

When executing queries in Trino, use Trino data types. The plugin converts them into SQream data types.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Trino type
     - SQream type
   * - ``BOOLEAN``
     - ``BOOL``
   * - ``TINYINT``
     - ``TINYINT``
   * - ``SMALLINT``
     - ``SMALLINT``
   * - ``INT``
     - ``INT``
   * - ``BIGINT``
     - ``BIGINT``
   * - ``REAL``
     - ``REAL``   
   * - ``DOUBLE``
     - ``DOUBLE``  
   * - ``DATE``	 
     - ``DATE``
   * - ``TIMESTAMP``
     - ``DATETIME``
   * - ``VARCHAR(N)``
     - ``VARCHAR(N)``
   * - ``VARCHAR``
     - ``TEXT``
   * - ``DECIMAL(P,S)``
     - ``NUMERIC(P,S)``

