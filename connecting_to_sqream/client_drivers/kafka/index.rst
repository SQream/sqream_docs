.. _kafka:

*************************
Connecting to SQream Using Kafka
*************************

If you are using Kafka Apache for distributed streaming and wish to use it with SQream, follow these instructions.


.. contents:: 
   :local:
   :depth: 1


Installation and Configuration
=============

.. contents:: 
   :local:
   :depth: 1

Prerequisites
----------------
 * JAVA 11
 * Network bandwidth should be not less than X Giga/Sec
 
Supported Data Formats
----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Data Format
     - Specification
   * - JSON
     -
   * - CSV
     - 
   * - Avro
     -

Kafka Producer
--------------

The Kafka Producer requires both the Kafka producer and Zookeeper processes to be running in order to create new topics, read data from existing topics, and load data from files. If Zookeeper is not running, the Kafka producer will not start.

.. contents:: 
   :local:
   :depth: 1

Kafka Producer Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kafka Producer is installed on the 192.168.0.125 server.

Kafka Producer Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Running Zookeeper:

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
	
Running Kafka producer:	

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-server-start.sh -daemon  config/server.properties
	
Verifying that both Zookeeper and Kafka producer are running:

1. Log in to your machine.
 
2. Run the following string:
 
 .. code-block:: postgres
 
	[sqream@metadata-0-125 ~]$ ps -ef |grep java
	
The following is an example of an output indicating that both processes are running:

 .. code-block:: postgres
 
	<JAVA_HOME>/bin/java...  org.apache.zookeeper.server.quorum.QuorumPeerMain config/zookeeper.properties
	<JAVA_HOME>/bin/java... kafka.Kafka config/server.properties
	
Creating a new topic:

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-topics.sh --create --bootstrap-server localhost:2181 --replication-factor 1 --partitions 1 --topic <topic name>
	
Reading data from a topic:

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	./kafka-console-consumer.sh --topic <topic name> --from-beginning --bootstrap-server localhost:9092
	
Loading data from a file:

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic <topic name> < <full path to file>

Terminating the Kafka Producer requires that both the Kafka Producer and Zookeeper be terminated. To avoid data inconsistency and potential data loss, terminate the Kafka Producer before terminating the Zookeeper.

Terminating the Kafka Producer: 

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-server-stop.sh

SQream Consumer
---------------

.. contents:: 
   :local:
   :depth: 1

The SQream Consumer converts data formatted as CSV and JSON into ``.tmp`` files and saves it in a predefined directory. 
You must define the number of files to be converted before they are saved as a ``sqream.batchRecordCount`` file. Once reaching the defined number of files, the consumer saves the converted files and begins the process all over again.

SQream Consumer Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SQream Consumer version is located under /home/sqream/kafkaconnect1, machine IP 192.168.0.102
Credentials:
user = sqream
pass = sqprj2021$

SQream Consumer Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What needs to be configured:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - Topic
     - A category or feed name to which messages are published and subscribed to
   * - ``sqream.batchrecordcount``
     - Preferably configured according to an estimated number of messages
   * - ``outputdir``
     - Copy the ``sqream.outputdir`` path, from its beginning and until ``outputs``, included, and save it to a known location. It is required to configure SQream loader to use this section of the path
   * - ``csvorder``
     - Create table columns


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
 
SQream tables must be created according to the columns configured in ``csvorder``.

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

Building SQream loader:

 .. code-block:: postgres
 
	git clone -b develop http://gitlab.sq.l/java/copy-from-util.git
	mvn clean package


Running SQream loader:

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
