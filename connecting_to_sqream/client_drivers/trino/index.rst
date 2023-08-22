.. _trino:

*****
Trino
*****


If you are using Trino for distributed SQL query processing and wish to use it to connect to BLUE, follow these instructions. 


.. contents::
   :local:
   :depth: 1

Prerequisites
-------------

To use Trino with BLUE, you must have the following installed:

* SQream version 4.1 or later
* Trino version 403 or later
* Trino Connector xxxx
* JDBC version 4.5.6 or later



Installation
------------

.. contents::
   :local:
   :depth: 1

JDBC
~~~~

In case JDBC is not yet configured, follow the :ref:`JDBC Client Drivers page<java_jdbc>` for registration and configuration guidance.


Trino Connector
~~~~~~~~~~~~~~~

The Trino Connector must be installed on each cluster node dedicated to Trino.

1. Create a dedicated directory for the Trino Connector.

2. Download the `Trino Connector<...>` and extract the content of the ZIP file to the dedicated directory, as shown in the example:


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

Trino uses catalogs for referencing stored objects such as tables, databases, and functions. Each Trino catalog may be configured with access to a single SQream database. If you wish Trino to have access to more than one SQream database or server, you must create additional catalogs.
 
Catalogs may be created using ``properties`` files. Start by creating a ``sqream.properties`` file and placing it under ``trino-server/etc/catalog``. 

The following is an example of a properties file:

.. code-block:: postgres

	connector.name=<name>
	connection-url=jdbc:Sqream://<host and port>/<database name>;[<optional parameters>; ...]
	connection-user=<user>
	connection-password=<password>
	
Syntax examples
---------------

The following is an example of the ``SHOW SCHEMAS FROM`` statement:

.. code-block:: postgres

	SHOW SCHEMAS FROM sqream;

The following is an example of the ``SHOW TABLES FROM`` statement:
	
.. code-block:: postgres	

	SHOW TABLES FROM sqream.public;

The following is an example of the ``DESCRIBE sqream.public.t`` statement:

.. code-block:: postgres

	DESCRIBE sqream.public.t;

	
Supported Data Types and Mapping
--------------------------------

Use the appropriate Trino data type for executing queries. Upon execution, incompatible data types will be converted by Trino to SQream data types.  

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
   * - ``VARCHAR``
     - ``TEXT``
   * - ``DECIMAL(P,S)``
     - ``NUMERIC(P,S)``

Limitations
-----------

The Trino Connector does not support the following SQL statements:

* ``GRANT``
* ``REVOKE``
* ``SHOW GRANTSHOW ROLES``
* ``SHOW ROLE GRANTS``
