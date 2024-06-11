.. _architecture:

************
Architecture
************

Blue leverages Kubernetes architecture to provide scalability and agility. All microservices run as Dockerized Kubernetes pods. Most of the services' horizontal scaling is managed by Kubernetes.

.. figure:: /_static/images/architecture.png

Edge Controller
===============

The Edge Controller is an ingress service that acts as the single entry point to the cluster, directing all communications to the relevant microservices. It validates users by communicating with the authentication service and is powered by the `Gate Ambassador <https://www.getambassador.io/>`_ framework. Designed to handle thousands of requests simultaneously, the Edge Controller efficiently manages high volumes of traffic with internal load balancing, ensuring fast response times. Additionally, it encrypts external communications using the Transport Layer Security (TLS) protocol.

Cloud Object Storage
====================

SQream Blue integrates with the following object storage platforms: 

* Google Cloud Storage (GCS)
* Simple Storage Services (S3)

This integration enables SQream Blue services to read and write data to and from cloud object storage. It supports foreign and internal tables, SQL and Python scripts, and other operational data needed by services like AirFlow.

Redis
=====

Redis is an open-source key-value store used for storing live sessions, request information, and cluster-level configuration. It facilitates sharing session data between microservices and handles other session information, such as parallelism policies.

User Interface
==============

The SQream Blue web user interface includes a Dashboard, SQL workbench, workflow manager (Jobs), cluster activity monitor, cluster permissions board, and an administration panel.

Jobs
====

Jobs orchestrate and schedule repetitive workflows composed of SQL and/or Python tasks. The Flows service, an Apache AirFlow-based Jobs engine, uses a custom SQream Blue AirFlow provider with PySQream to execute SQL scripts.

System
======

Authentication Service
----------------------

Auth0, a leading cloud authentication solution, allows you to use your organization’s Identity Provider (IDP) for authentication. The Authentication Service handles authentication via JSON Web Token (JWT).

Healer (Health Monitoring)
--------------------------

The Healer service actively monitors the health of various SQream Blue microservices, overseeing ongoing sessions and ensuring the absence of hung sessions while verifying continuous operational status. In the event of an identified issue with a hung query, corrective actions are promptly executed to restore normal operation.

GPU Statement Execution
=======================

The GPU is designed for high-throughput and parallel processing, making it perfect for data-intensive tasks such as complex queries, data analytics, and batch processing. By offloading these workloads to GPUs, SQream Blue achieve faster query execution, improved scalability, and efficient handling of large-scale data operations, resulting in significant performance gains.

Query Handler
-------------

The Query Handler serves as the entry point for all SQream Blue operations, routing incoming client requests to relevant microservices such as CBO, Queue Manager, and Workers.

Queue Manager
-------------

The Queue Manager is the queuing mechanism for the served queries, serving as the system's load balancer to effectively handle large volumes of requests concurrently.

Flow Manager
------------

The Flow Manager operates as a decision-making mechanism, prioritizing tasks and efficiently managing resources. Queries are initially directed to the Query Handler, which then routes them to the Flow Manager to ascertain their workflow.

Metadata Server
---------------

The Metadata Server stores metadata which is data about the data stored in the database. This includes information about the structure of the data using a key/value store, such as DDL and statistics. The underlying storage engine for managing metadata is RocksDB. The main consumer of the Metadata Server is the Cost-Based Optimizer (CBO) which uses metadata for creating execution plans.

Cost-Based Optimizer
--------------------

The Cost-Based Optimizer (CBO) parses, interprets, and optimizes SQL statements. It generates execution plans for the Workers and refines them using pre-calculated column statistics. Utilizing Apache Calcite as its compiler, the CBO handles SQL parsing, desugaring, optimization, and relational algebra tasks.

Statistics Collector
--------------------

The Statistics Collector (connected via JDBC) generates column histograms (statistics) to aid the CBO in query plan optimization.

GPU Worker
----------

The Worker serves as the core component of SQream Blue, responsible for executing SQL statements. It handles reading and writing data from external files, databases, and temporary storage areas, with each Worker leveraging an Nvidia Tesla T4 GPU. By working in groups, Workers can execute statements collectively, parallelizing tasks and reducing overall execution time. One Worker is designated as the master, distributing tasks among the remaining slave Workers.

Execution Space Manager
-----------------------

As Workers rely on cloud GPU resources, which can be subject to availability constraints, the Execution Space Manager (ESM) ensures efficient resource allocation based on business policies. It optimizes resource allocation per query, considering factors such as concurrency, performance, and cost. Additionally, ESM provisions Resource Token Containers (RTCs) shared among tenants, facilitating effective resource management.

CPU Statement Execution
=======================

The CPU excels in handling complex, control-oriented tasks, making it ideal for transaction management and system administration. It is efficient at executing single-threaded operations and managing low-latency processes.

SQream Transform
----------------

The SQream Transform microservice executes administrative statements such as ``DESCRIBE`` and ``AUDITLOG``.

Monitor
-------

The Monitor microservice gathers monitoring and audit data, which is accessible through ``DESCRIBE`` and ``AUDITLOG`` statements, as well as the SQream Blue Dashboard.








