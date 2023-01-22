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
* You must have `JDBC <java_jdbc>`_ installed
* Your network bandwidth must be at least 100 mega per second
* Supported data formats for streamed data is JSON

Installation and Configuration
==============================

.. contents:: 
   :local:
   :depth: 1

Sink Connector
---------------

.. contents:: 
   :local:
   :depth: 1

The Sink Connector reads Kafka topics and writes messages into text files in either CSV, JSON, or Avro format. The files are created with the extension ``.tmp`` and stored in the specified directory. The ``sqream.batchRecordCount`` parameter defines the number of records to be written to each file. When the specified number of records is reached, the Sink Connector closes the file, renames it to the ``sqream.fileExtension``, and then creates a new file.

SQream tables must be created according to the columns configured in ``csvorder``.

.. figure:: /_static/images/kafka_flow.png

Sink Connector Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~



Sink Connector Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
 


Running commands:

 .. code-block:: postgres
 
	export JAVA_HOME=/home/sqream/copy-from-util/jdk-11;export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar;cd /home/sqream/kafkaconnect1/kafka/bin/ && ./connect-standalone.sh /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/connect-standalone.properties  /home/sqream/kafkaconnect1/sqream-kafka-connector/sqream-kafkaconnect/config/sqream-filesink.properties &




SQream Loader
-------------

.. contents:: 
   :local:
   :depth: 1

SQream Loader Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sqream loader credentials:
ip machine: 192.168.0.102
user = sqream
pass = sqprj2021$

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

Limitations
===========

Latency
Retention

Examples
=========
