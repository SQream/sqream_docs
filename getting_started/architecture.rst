.. _architecture:

************
Architecture
************

Blue leverages Kubernetes architecture to provide scalability and agility. All microservices run as Dockerized Kubernetes pods. Most of the services' horizontal scaling is managed by Kubernetes.

The following figure shows the Blue microservice Kubernetes architecture:

.. figure:: /_static/images/architecture.png

Edge Controller
===============

The Edge Controller is an ingress service that serves as the single point of entry to the cluster. It directs all communications to relevant microservices and communicates with the authentication service to validate users. The Edge Controller is powered by the `Gate Ambassador <https://www.getambassador.io/>`_ framework.
Built to serve thousands of requests simultaneously, the Edge Controller serves high volumes of requests and internal load balancing to address all requests without compromising response time. It also encrypts external communication using the Transport Layer Security (TLS) protocol.

Authentication Service
======================

Auth0, a leading cloud authentication solution, enables you to use your organization’s Identity Provider (IDP) authentication. The Kubernetes Authentication Service manages authentication through JSON Web Token (JWT) sessions. Horizontal service scaling is managed by Kubernetes.


User Interface
==============

SQream Blue is a web user interface employing a SQL workbench. It is deployed and maintained as an independent component. 

Jobs
====

Jobs orchestrate and schedule repetitive workflows that are made up of SQL and/or Python tasks. The Flows service utilizes Apache AirFlow as the Jobs engine. AirFlows utilizes a custom SQream Blue AirFlow provider that utilizes PySQream to execute SQL scripts.

Cloud Object Storage
====================

SQream Blue integrates with the following Object Storage platforms: 

* Google cloud platform (GCP)
* Simple Storage Services (S3)

This enables read and write from and to foreign and internal tables. Read and write AirFlow Job operational data and SQL \ Python scripts.

System
======

Healer (Health Monitoring)
--------------------------

The Healer is a self-healing service that proactively monitors the health of the different SQream Blue microservices by keeping track of ongoing sessions, verifying that no hung sessions exist, and that all microservices are fully operational at all times. When an unhealthy microservice is identified, a corrective action is performed to restore the microservice to normal operation.

GPU Statement Execution
=======================

Metadata Server
---------------

The Metadata server persists SQream Blue storage metadata such as DDL and statistics for raw data using a key/value store. This service’s main user is the Cost-Based Optimizer (CBO), which uses the metadata for creating execution plans. RocksDB open-source software is used as the key/value store.

Cost-Based Optimizer
--------------------

The Cost-Based Optimizer (CBO) is responsible for parsing, interpreting, and optimizing SQL statements, as well as creating the execution plans to be used by the Worker(s). The CBO utilizes Apache Calcite as its compiler, for actions like SQL Parsing, Desugar and Optimization & Relational Algebra. The CBO will later optimize the execution plan based on pre-created column statistics.

Queue Manager
-------------

Queue Manager is the queuing mechanism for the served queries, used as the system load balancer to concurrently handle large volumes of requests.

Flow Manager
------------

The Flow Manager is a decision-making mechanism based on prioritization and effective resource management. The Query Handler first sends queries to the Flow Manager to determine their workflow.

Execution Space Manager
-----------------------

As Workers use cloud GPU resources that may have limited availability, the Execution Space Manager (ESM) provides business policy-driven resource allocation, specifically the ability to allocate resources per query optimized for concurrency, performance, and cost. ESM is responsible for provisioning RTCs that are shared between tenants.

Query Handler
-------------

The query handler serves as the entry point for all SQream Blue operations, routing incoming client requests to relevant microservices such as CBO, Queue Manager, and Workers.

Statistics Collector
--------------------

Used for the creation of column histograms (statistics) to be later used by the CBO for query plan optimization. The Statistics execute statements to create a histogram, using a JDBC connection.

GPU Worker
----------

The Worker is the heart of SQream Blue. It executes SQL statements. The Worker reads and writes data from external files, databases, and temporary storage areas. Each Worker utilizes an Nvidia Tesla T4 GPU.
A group of Workers are able to execute statements together, paralleling actions and shortening overall execution time. One Worker is set as a master, and it distributes work to the rest of the slave Workers.

Redis
=====

Redis is a key-value open-source software used for storing live sessions or request information as well as cluster-level configuration. Redis is used for sharing session data between microservices as well as other session information such as parallelism policies.

Non-GPU Statement Execution
===========================

SQream Transform
----------------

CPU-based microservice that executes administrative statements such as ``DESCRIBE`` and ``AUDITLOG``.

Monitor
-------

This microservice is responsible for collecting monitoring and audit information to be later used by ``DESCRIBE`` and ``AUDITLOG`` statements as well as the Blue Studio Dashboard.






