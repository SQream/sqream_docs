.. _kafka:

*************************
Connecting to SQream Using Kafka
*************************

The SQream Connector provides a file-based solution for storing and managing data that is being processed and streamed through Kafka. 


.. contents:: 
   :local:
   :depth: 1


Before You Begin
================

* You must have JAVA 11 installed
* You must have `JDBC <java_jdbc>`_ deployed
* You must have Kafka Connect installed
* Your network bandwidth must be at least 100 megabytes per second
* You must have Kafka 2.12—3.2.1
* Streamed data supported format is JSON
 
Kafka Connector Installation and Configuration
==============================================

Ensure that both Kafka and Zookeeper are running before starting the configuration of the Kafka Connector.

Kafka Connector workflow:

.. figure:: /_static/images/SQreamDB_connector_to_Kafka.png

.. contents:: 
   :local:
   :depth: 1

Configuring The Sink Connector
------------------------------

Sink Connector configuration file structure:

.. code-block:: postgres

	name=SQReamFileSink
	topics=<topic>
	tasks.max=4
	connector.class=tr.com.entegral.FileSinkConnector
	errors.tolerance=all
	errors.log.enable=true
	errors.log.include.messages=true
	value.converter=org.apache.kafka.connect.json.JsonConverter
	value.converter.schemas.enable=false
	transforms=flatten
	transforms.flatten.type=org.apache.kafka.connect.transforms.Flatten$Value
	transforms.flatten.delimiter=.
	sqream.outputdir=<full path to a staging area: example- /home/sqream/kafkaconnect/outputs>
	sqream.batchRecordCount =10
	sqream.fileExtension=csv
	sqream.removeNewline =false
	sqream.outputType=csv
	sqream.csvOrder=<column1, column2, column3, column4>

1. Open the Sink Connector configuration file:

.. code-block:: postgres

	vi /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-filesink.properties

2. Configure the following Sink Connector parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - Topic
     - A category or feed name to which messages are published and subscribed to.
   * - ``sqream.batchrecordcount``
     - The record count to be written to each folder.
   * - ``sqream.outputdir``
     - Full path to a staging area, the temporary location where files are stored before they are processed or moved to their final destination.
   * - ``sqream.csvOrder``
     - The table column names by which streamed data is arranged. The ``sqream.csvOrder`` column names must align with a SQream table.
	
3. Run the following command:

.. code-block:: postgres
 
	export JAVA_HOME=/home/sqream/copy-from-util/jdk-11;export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar;cd /home/sqream/kafkaconnect1/kafka/bin/ && ./connect-standalone.sh /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/connect-standalone.properties  /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-filesink.properties &

Configuring JDBC
----------------

The JDBC connector is used to ingest data from Kafka, allowing SQream DB to consume the messages directly. This enables efficient and secure data ingestion into SQream DB.
	
JDBC Configuration file structure:

.. code-block:: postgres
	
	name=SQReamJDBCSink
	topics=<topic>
	tasks.max=1
	connector.class=tr.com.entegral.JDBCSinkConnector
	errors.tolerance=all
	errors.log.enable=true
	errors.log.include.messages=true
	value.converter=org.apache.kafka.connect.json.JsonConverter
	value.converter.schemas.enable=false
	transforms=flatten
	transforms.flatten.type=org.apache.kafka.connect.transforms.Flatten$Value
	transforms.flatten.delimiter=.
	sqream.batchRecordCount =3
	sqream.jdbc.connectionstring=jdbc:Sqream://<host>:<port>/kafka;user=<user name>;password=<password>;cluster=false
	sqream.input.inputfields=<Column1, Column2, Column3, Column4>
	sqream.jdbc.tablename=testtable
	sqream.jdbc.table.columnnames=<Column1, Column2, Column3, Column4...>
	sqream.jdbc.table.columntypes=<data types>
	sqream.jdbc.dateformat=yyyy-MM-dd HH:mm:ss

1. Open the JDBC configuration file:

.. code-block:: postgres
	
	vi /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-jdbcsink.properties

2. Configure the following JDBC parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - Topic
     - Must be defined according to sink connector.
   * - ``sqream.jdbc.table.columntypes``
     - SQream data types which must match the columns that were defined in the Sink Connector sqream.csvOrder parameter.
   * - ``sqream.jdbc.table.columnnames``
     - The table column names by which streamed data is arranged. The ``sqream.jdbc.table.columnnames`` column names must align with the Sink Connector column names.
   * - ``sqream.input.inputfields``
     - Columns as defined in the original Kafka message.

Configuring The SQream Loader
---------------------------

SQream Loader configuration file structure:

.. code-block:: postgres

	#config.yaml

		com:
		  sqream:
			kafka:
			  common:
				root: "<full path to directory of utility>"
				readyFileSuffix: ".<suffix as configured in Sink Connector>"
			  connection:
				ip: "<host>"
				port: <port>
				database: "<database name>"
				cluster: true
				user: <username>
				pass: <password>
				delimiter: ","
			  tables:
				- schema: "<scema name>"
				  name: "<table name>"
				  parallel: <number of parallel processes>
				- schema: "<schema name>"
				  name: "<table name>"
				  parallel: <number of parallel processes>
				- schema: ...


1. Configure the following SQream Loader parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   
   * - Parameter
     - Description
   * - ``readyFileSuffix``
     -  Ensure that the SQream Loader ``readyFileSuffix`` parameter is configured with the same file extension as the Sink Connector ``qream.fileExtension`` parameter
   * - ``ip``
     - Host name of the machine where the Sink Connector is configured
   * - Connection parameters
     - Port, database, cluster, username, and password
   * - Table parameters
     - Schema, table name, number of parallel processes

2. Run the following command

 .. code-block:: postgres
 
	<full path to jdk11>/bin/java -jar <full path to copy from util jar>/copy-from-util-0.0.1-SNAPSHOT.jar --spring.config.additional-location=<full path to copy from util configuration yamel> &

Logging and Monitoring
========================

The following log files are created:
 * JAVA application fails (consumer or loader?)
 * Files cannot be saved to folder due to
Either
 * Folder permission issue
Or
 * SQream loader folder is not the same as Kenan folder 
 
Purging
=======
Ingested files are automatically zipped and archived for 60 days.  
User needs to prepare storage.
User may configure archive time.

Limitations
===========

Latency

Retention
