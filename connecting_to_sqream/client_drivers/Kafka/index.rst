.. _kafka:

*************************
Connecting to SQream Using Kafka
*************************

If you are using Kafka Apache for distributed streaming and wish to use it with SQream, follow these instructions.


.. contents:: 
   :local:
   :depth: 1


Before You Begin
================

* You must have JAVA 11 installed
* You must have `JDBC <java_jdbc>`_ deployed
* You must have SQream Sink Connector and Loader downloaded
* Your network bandwidth must be at least 100 mega per second
* You must have Kafka 2.12-3.2.1
* Streamed data supported format is JSON
 
Installation and Configuration
==============================

Before you configure the Kafka Connector, make sure that Kafka and Zookeeper are both running. 

Kafka Connector workflow:

.. figure:: /_static/images/kafka_flow.png

.. contents:: 
   :local:
   :depth: 1

Sink Connector
---------------

Download sink connector

The Sink Connector reads JSON format Kafka topics and writes the messages inside each topic into text files. The files are created with the extension ``.tmp`` and stored in a specified directory. The ``sqream.batchRecordCount`` parameter defines the number of records to be written to each file, and when the specified number is reached, the Sink Connector closes the file, renames it to ``sqream.fileExtension``, and then creates a new file. Unlike data streaming, which continuously sends data from the Kafka topic to the database, the Sink Connector only sends the data when the file size reaches a predefined threshold. This means that data will arrive in batches. 

SQream tables must be created according to the columns configured in ``csvorder``.


Sink Connector Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration file structure:

 .. code-block:: postgres

	name=SQReamFileSink
	topics=topsqreamtest1
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
	sqream.outputdir=/home/sqream/kafkaconnect/outputs
	sqream.batchRecordCount =10
	sqream.fileExtension=csv
	sqream.removeNewline =false
	sqream.outputType=csv
	sqream.csvOrder=receivedTime,equipmentId,asdf,timestamp,intv

The following parameters require configuration.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - Topic
     - A category or feed name to which messages are published and subscribed to
   * - ``sqream.batchrecordcount``
     - The record count to be written to each file
   * - ``outputdir``
     - Copy the ``sqream.outputdir`` path, from its beginning and until ``outputs``, included, and save it to a known location. It is required to configure SQream loader to use this section of the path
   * - ``csvorder``
     - Defines table columns. SQream table columns must align with the ``csvorder`` table columns


Connection string:

 .. code-block:: postgres
 
	vi /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-filesink.properties
	
Running commands:

 .. code-block:: postgres
 
	export JAVA_HOME=/home/sqream/copy-from-util/jdk-11;export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar;cd /home/sqream/kafkaconnect1/kafka/bin/ && ./connect-standalone.sh /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/connect-standalone.properties  /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-filesink.properties &




JDBC
-------------

The JDBC connector can be used to ingest data from Kafka, allowing SQream DB to consume the messages directly. This enables efficient and secure data ingestion into SQream DB.

.. contents:: 
   :local:
   :depth: 1

JDBC Configuration
~~~~~~~~~~~~~~~~~~

.. code-block:: postgres
	vi /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-jdbcsink.properties
	
Example

.. code-block:: postgres
	
	name=SQReamJDBCSink
	topics=demo1
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
	#sqream.jdbc.connectionstring=jdbc:sqlserver://localhost;databaseName=TestDB;user=kafka;password=kafka;encrypt=true;trustServerCertificate=true;
	sqream.jdbc.connectionstring=jdbc:Sqream://192.168.0.102:5001/kafka;user=sqream;password=sqream;cluster=false
	sqream.input.inputfields=intStr,inInt,indateTime,inFloat
	sqream.jdbc.tablename=testtable
	sqream.jdbc.table.columnnames=colStr,colInt,Coldatetime,ColFloat
	sqream.jdbc.table.columntypes=VARCHAR,INTEGER,TIMESTAMP,FLOAT
	sqream.jdbc.dateformat=yyyy-MM-dd HH:mm:ss

SQream Loader Configuration 
~~~~~~~~~~~~~~~~~~~~~~~~~~~


Building the SQream Loader:

 .. code-block:: postgres
 
	git clone -b develop http://gitlab.sq.l/java/copy-from-util.git
	mvn clean package


Running the SQream Loader:

 .. code-block:: postgres

	git clone -b develop http://gitlab.sq.l/java/copy-from-util.git
	mvn clean package

What needs to be configured:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   
   * - Parameter
     - Description
   * - ``root``
     – paste copied path to root
   * - ``schema``
     -
   * - ``name``
     -    

Configuration file structure:

 .. code-block:: postgres

	#config.yaml

	com:
	  sqream:
		kafka:
		  common:
			root: "/home/sqream/copy_from_root"
			readyFileSuffix: ".csv"
		  connection:
			ip: "127.0.0.1"
			port: 3108
			database: "master"
			cluster: true
			user: sqream
			pass: sqream
			delimiter: ","
		  tables:
			- schema: "public"
			  name: "t1"
			  parallel: 5
			- schema: "public"
			  name: "t2"
			  parallel: 3
			- schema: "public"
			  name: "t3"
			  parallel: 1




Running commands:

 .. code-block:: postgres
 
	/home/sqream/copy-from-util/jdk-11/bin/java -jar /home/sqream/copy-from-util/copy-from-util/target/copy-from-util-0.0.1-SNAPSHOT.jar --spring.config.additional-location=/home/sqream/copy-from-util/config.yaml &

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

Examples
=========
