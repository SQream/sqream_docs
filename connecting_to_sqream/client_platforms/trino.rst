.. _trino:

*************************
Connecting to SQream Using Trino
*************************


If you are using Trino for distributed SQL query processing and wish to use it to connect to a SQream, follow these instructions. 


.. contents::
   :local:
   :depth: 1

Prerequisites
-------------
To use Trino with SQream, you must have the following installed:

* SQream version 2022.1.8 or later
* Trino version 403 or later
* SQream Trino plugin xxxx
* JDBC version 4.5.6 or later



Installation
------------

.. contents::
   :local:
   :depth: 1

JDBC
~~~~

In case JDBC is not yet configured, follow the `JDBC Client Drivers page <https://docs.sqream.com/en/v2021.1/third_party_tools/client_drivers/jdbc/index.html>`_ for registration and configuration guidance.


SQream Trino Plugin
~~~~~~~~~~~~~~~~~~~

The SQream Trino plugin must be installed on each cluster node dedicated to Trino.

1. Create a dedicated directory for the SQream Trino plugin.

2. Download the `SQream Trino Plugin<...>` and extract the content of the ZIP file to the dedicated directory, as shown in the example:


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
   * - ``VARCHAR(N)``
     - ``VARCHAR(N)``. 
   * - ``VARCHAR``
     - ``TEXT``
   * - ``DECIMAL(P,S)``
     - ``NUMERIC(P,S)``

.. note:: ``VARCHAR`` is soon to be deprecated and may not be used in SQream DB.

Limitations
-----------

The SQream Trino plugin does not support the following SQL statements:

* ``GRANT``
* ``REVOKE``
* ``SHOW GRANTSHOW ROLES``
* ``SHOW ROLE GRANTS``