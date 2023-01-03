.. _kafka:

*************************
Connecting to SQream Using Kafka
*************************

This page describes how to connect SQream with the Kafka Apache stream-processing software platform. 

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

The Kafka Producer can be used for creating new topics, reading data from existing topics, and loading data from files.

In order for the Kafka producer to operate correctly, both the Kafka producer and Zookeeper processes must be running simultaneously. If Zookeeper is not running, the Kafka producer will not start.

.. contents:: 
   :local:
   :depth: 1

Kafka Producer Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kafka producer is installed on the 192.168.0.125 server.

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

1. Log in to your machine using the following SQream credentials:

 * User: sqream
 * Password: sqream11
 
2. Run the following string:
 
 .. code-block:: postgres
 
	[sqream@metadata-0-125 ~]$ ps -ef |grep java
	
The following is an example of an output indicating that both processes are running:

 .. code-block:: postgres
 
	 sqream   63082     1  0 Sep11 ?        00:03:50 /usr/lib/jvm/jre-1.8.0-openjdk/bin/java -Xmx512M -Xms512M -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xloggc:/home/sqream/kafka_2.12-3.2.1/bin/../logs/zookeeper-gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/home/sqream/kafka_2.12-3.2.1/bin/../logs -Dlog4j.configuration=file:bin/../config/log4j.properties -cp /home/sqream/kafka_2.12-3.2.1/bin/../libs/activation-1.1.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/aopalliance-repackaged-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/argparse4j-0.7.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/audience-annotations-0.5.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/commons-cli-1.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/commons-lang3-3.8.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-api-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-basic-auth-extension-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-json-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-mirror-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-mirror-client-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-runtime-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-transforms-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-api-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-locator-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-utils-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-annotations-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-core-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-databind-2.12.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-dataformat-csv-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-datatype-jdk8-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-jaxrs-base-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-jaxrs-json-provider-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-module-jaxb-annotations-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-module-scala_2.12-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.activation-api-1.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.annotation-api-1.3.5.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.inject-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.validation-api-2.0.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.ws.rs-api-2.1.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.xml.bind-api-2.3.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javassist-3.27.0-GA.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javax.servlet-api-3.1.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javax.ws.rs-api-2.1.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jaxb-api-2.3.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-client-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-common-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-container-servlet-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-container-servlet-core-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-hk2-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-server-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-client-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-continuation-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-http-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-io-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-security-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-server-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-servlet-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-servlets-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-util-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-util-ajax-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jline-3.21.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jopt-simple-5.0.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jose4j-0.7.9.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka_2.12-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-clients-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-log4j-appender-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-metadata-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-raft-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-server-common-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-shell-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-storage-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-storage-api-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-examples-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-scala_2.12-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-test-utils-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-tools-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/lz4-java-1.8.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/maven-artifact-3.8.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/metrics-core-2.2.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/metrics-core-4.1.12.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-buffer-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-codec-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-common-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-handler-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-resolver-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-tcnative-classes-2.0.46.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-classes-epoll-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-native-epoll-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-native-unix-common-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/osgi-resource-locator-1.0.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/paranamer-2.8.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/plexus-utils-3.3.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/reflections-0.9.12.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/reload4j-1.2.19.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/rocksdbjni-6.29.4.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-collection-compat_2.12-2.6.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-java8-compat_2.12-1.0.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-library-2.12.15.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-logging_2.12-3.9.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-reflect-2.12.15.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/slf4j-api-1.7.36.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/slf4j-reload4j-1.7.36.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/snappy-java-1.1.8.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/trogdor-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zookeeper-3.6.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zookeeper-jute-3.6.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zstd-jni-1.5.2-1.jar org.apache.zookeeper.server.quorum.QuorumPeerMain config/zookeeper.properties
	sqream   63614     1  0 Sep11 ?        00:19:22 /usr/lib/jvm/jre-1.8.0-openjdk/bin/java -Xmx1G -Xms1G -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -XX:MaxInlineLevel=15 -Djava.awt.headless=true -Xloggc:/home/sqream/kafka_2.12-3.2.1/bin/../logs/kafkaServer-gc.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=100M -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dkafka.logs.dir=/home/sqream/kafka_2.12-3.2.1/bin/../logs -Dlog4j.configuration=file:bin/../config/log4j.properties -cp /home/sqream/kafka_2.12-3.2.1/bin/../libs/activation-1.1.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/aopalliance-repackaged-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/argparse4j-0.7.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/audience-annotations-0.5.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/commons-cli-1.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/commons-lang3-3.8.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-api-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-basic-auth-extension-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-json-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-mirror-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-mirror-client-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-runtime-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/connect-transforms-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-api-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-locator-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/hk2-utils-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-annotations-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-core-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-databind-2.12.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-dataformat-csv-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-datatype-jdk8-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-jaxrs-base-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-jaxrs-json-provider-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-module-jaxb-annotations-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jackson-module-scala_2.12-2.12.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.activation-api-1.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.annotation-api-1.3.5.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.inject-2.6.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.validation-api-2.0.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.ws.rs-api-2.1.6.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jakarta.xml.bind-api-2.3.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javassist-3.27.0-GA.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javax.servlet-api-3.1.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/javax.ws.rs-api-2.1.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jaxb-api-2.3.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-client-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-common-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-container-servlet-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-container-servlet-core-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-hk2-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jersey-server-2.34.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-client-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-continuation-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-http-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-io-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-security-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-server-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-servlet-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-servlets-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-util-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jetty-util-ajax-9.4.44.v20210927.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jline-3.21.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jopt-simple-5.0.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/jose4j-0.7.9.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka_2.12-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-clients-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-log4j-appender-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-metadata-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-raft-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-server-common-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-shell-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-storage-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-storage-api-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-examples-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-scala_2.12-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-streams-test-utils-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/kafka-tools-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/lz4-java-1.8.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/maven-artifact-3.8.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/metrics-core-2.2.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/metrics-core-4.1.12.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-buffer-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-codec-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-common-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-handler-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-resolver-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-tcnative-classes-2.0.46.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-classes-epoll-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-native-epoll-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/netty-transport-native-unix-common-4.1.73.Final.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/osgi-resource-locator-1.0.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/paranamer-2.8.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/plexus-utils-3.3.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/reflections-0.9.12.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/reload4j-1.2.19.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/rocksdbjni-6.29.4.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-collection-compat_2.12-2.6.0.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-java8-compat_2.12-1.0.2.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-library-2.12.15.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-logging_2.12-3.9.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/scala-reflect-2.12.15.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/slf4j-api-1.7.36.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/slf4j-reload4j-1.7.36.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/snappy-java-1.1.8.4.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/trogdor-3.2.1.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zookeeper-3.6.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zookeeper-jute-3.6.3.jar:/home/sqream/kafka_2.12-3.2.1/bin/../libs/zstd-jni-1.5.2-1.jar kafka.Kafka config/server.properties
	
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

Closing Kafka producer: 

To close the Kafka producer, you must first stop the producer and then stop Zookeeper.

.. code-block:: postgres

	cd /home/sqream/kafka_2.12-3.2.1/
	bin/kafka-server-stop.sh

Kafka Consumer
---------------

.. contents:: 
   :local:
   :depth: 1

The Kafka consumer converts data formatted as CSV and JSON into ``.tmp`` files and saves it in a predefined directory. 
You must define the number of files to be converted before they are saved as a ``sqream.batchRecordCount`` file. Once reaching the defined number of files, the consumer saves the converted files and begins the process all over again.

Kafka Consumer Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Kafka consumer version is located under /home/sqream/kafkaconnect1, machine IP 192.168.0.102
Credentials:
user = sqream
pass = sqprj2021$

Kafka Consumer Configuration
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
