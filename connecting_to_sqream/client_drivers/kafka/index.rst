.. _kafka:

*************************
Connecting to SQream Using Kafka
*************************

Intro to Kafka producer, consumer, and loader.
Data formats
Confluent GUI


The Kafka page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Getting Started
==================================
System requirements
-------------------
No system requirements


Download Kafka connector files
------------------------------


Installation and configuration
=============

Prerequisites
----------------
Both Kafka consumer and SQream loader require JAVA 11.



Kafka producer
==============

Installing Kafka producer
---------------------------
The Kafka producer is installed on the 192.168.0.125 server.

Operating Kafka producer
--------------------------

For the producer to properly function, two processes must continuously be running: Kafka producer and Zookeeper. Note that Kafka producer will not run unless Zookeeper is already running.

Running Zookeeper:

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
	
Running Kafka producer:	

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-server-start.sh -daemon  config/server.properties
	
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

To close Kafka producer, you must first stop the producer and only then stop Zookeeper. 

Closing Kafka producer: 

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-server-stop.sh
	
Verifying that the producer is running
--------------------------------------


Known Driver Limitations
----------------------------
 * Unicode characters are not supported when using ``INSERT INTO AS SELECT``.

 * To avoid possible casting issues, use ``getDouble`` when using ``FLOAT``.

Connecting to SQream For the First Time
==============================================
An initial connection to SQream must be established by creating a **SqreamConnection** object using a connection string.

.. contents:: 
   :local:
   :depth: 1
   

Connection String
--------------------
To connect to SQream, instantiate a **SqreamConnection** object using this connection string.

The following is the syntax for SQream:

.. code-block:: text

   "Data Source=<hostname or ip>,<port>;User=<username>;Password=<password>;Initial Catalog=<database name>;Integrated Security=true";

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - State
     - Default
     - Description
   * - ``<data source>``
     - Mandatory
     - None
     - Hostname/IP/FQDN and port of the SQream DB worker. For example, ``127.0.0.1:5000``, ``sqream.mynetwork.co:3108``
   * - ``<initial catalog>``
     - Mandatory
     - None
     - Database name to connect to. For example, ``master``
   * - ``<username>``
     - Mandatory
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``<password>``
     - Mandatory
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
   * - ``<service>``
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

Connection String Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following is an example of a SQream cluster with load balancer and no service queues (with SSL):

.. code-block:: text

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;Integrated Security=true;ssl=true;cluster=true;
    

The following is a minimal example for a local standalone SQream database:

.. code-block:: text 

  
   Data Source=127.0.0.1,5000;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;

The following is an example of a SQream cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: text

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=raviga;Integrated Security=true;service=etl;cluster=true;

Sample C# Program
--------------------
You can download the :download:`.NET Application Sample File <sample.cs>` below by right-clicking and saving it to your computer.

.. literalinclude:: sample.cs
    :language: C#
    :caption: .NET Application Sample
    :linenos:
