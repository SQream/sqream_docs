.. _architecture:

************
Architecture
************

Blue leverages Kubernetes architecture to provide scalability and agility. The Blue Microservices section describes the Blue microservices and their specific roles. All microservices run as Dockerized Kubernetes pods. Most of the services' horizontal scaling is managed by Kubernetes.

The following figure shows the Blue microservice Kubernetes architecture:

|architecture|

.. |architecture| image:: /_static/images/architecture.png
   :align: middle   
   
Microservices Running within a Kubernetes Cluster
=================================================

This section provides a detailed description of each microservice rule and key features.

Edge Controller
---------------

The Edge Controller is an ingress service that serves as the single point of entry to the cluster, directs all communications to relevant microservices, and communicates with the authentication service to validate users. The Edge Controller is powered by the `Gate Ambassador <https://www.getambassador.io/>`_ framework.
Built to serve thousands of requests simultaneously, the Edge Controller serves high volumes of requests and internal load balancing to address all requests without compromising response time.
Transport Layer Security (TLS) encryption of all external communications.

Authentication Service
----------------------

The Authentication Service manages user authentication through JSON web token (JWT) sessions. Authentication itself is done using Auth0 - a leading cloud authentication solution that enables Blue customers to use their organization’s IDP (Identity Provider i.e. Google Workspaces, Azure Active Directory, etc). Horizontal service scaling is managed by Kubernetes.

GPU Statements Execution
------------------------

Query Handler
^^^^^^^^^^^^^

The query handler serves as the entry point for all SQream operations, routing incoming client requests to relevant microservices, such as CBO, Queue Manager, or Worker.

This section describes the Query Handler services.

Redis
^^^^^

Redis is key-value open-source software used for storing live sessions or request information as well as cluster-level configuration. Redis is used for sharing session data between microservices as well as other session information such as parallelism policies.

Flow Manager
^^^^^^^^^^^^

The Flow Manager is a decision-making mechanism based on prioritization and effective resource management. The Query Handler first sends queries to the Flow Manager to determine their workflow.

CBO (Cost Based Optimizer)
^^^^^^^^^^^^^^^^^^^^^^^^^^

The CBO is responsible for parsing, interpreting, and optimizing SQL statements, as well as creating the execution plans to be used by the Worker(s). The CBO utilizes Apache Calcite as its compiler, for actions like SQL Parsing, Desugar and Optimization & Relational Algebra. The CBO will later optimize the execution plan based on pre-created column statistics.

Queue Manager
^^^^^^^^^^^^^

Queue Manager is the queuing mechanism for the served queries, used as the system load balancer to concurrently handle large volumes of requests.

GPU Worker
^^^^^^^^^^

The Worker is the heart of the SQream and executes the SQL statements. The worker reads and writes data from the external files, database, and temporary storage areas.
Each Worker utilizes an Nvidia Tesla T4 GPU.
A group of workers are able to execute statements together, paralleling actions and shortening overall execution time, one worker is set as a master, and it distributes work to the rest of the slave workers.

Metadata Server
^^^^^^^^^^^^^^^

The Metadata server persists SQream storage metadata, such as DDL and statistics, for the raw data using a key/value store. This service’s main user is the CBO, which uses the metadata for creating execution plans. RocksDB open-source software is used as the key/value store.

Execution Space Manager
^^^^^^^^^^^^^^^^^^^^^^^

As Workers use cloud GPU resources that may have limited availability, the Execution Space Manager (ESM) provides business policy-driven resource allocation, specifically the ability to allocate resources per query optimized for concurrency, performance, and cost. ESM is responsible for provisioning RTCs that are shared between tenants.

Statistics Collector
^^^^^^^^^^^^^^^^^^^^

Used for the creation of column histograms (statistics) to be later used by the CBO for query plan optimization. The Statistics execute statements to create a histogram, using a JDBC connection.

System
------

Healer (Health Monitoring)
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Healer is a self-healing service that keeps track of ongoing sessions, verifies that no hung sessions exist, and that all microservices are fully operational at all times.
Proactively monitors the health of the different SQream microservices. When an unhealthy microservice is identified, a corrective action is performed to restore the microservice to normal operation.

SQream Studio
-------------

SQream Studio is a SQream web user interface used as an SQL workbench for communicating with SQream clusters. It is deployed and maintained as an independent component. 

Flows
-----

Orchestrates and schedules repetitive workflows (jobs) made up of SQL or Python tasks. Flows services utilize Apache AirFlows as the jobs engine. AirFlows utilizes a custom SQream Blue AirFlow provider that utilizes PySQream to execute SQL scripts.

Non-GPU Statement Execution
---------------------------

SQream Transform
^^^^^^^^^^^^^^^^

CPU-based microservice that executes administrative statements such as DESCRIBEs and AUDITLOG

Monitor
^^^^^^^

This microservice is responsible for collecting monitoring and audit information to be later used by DESCRIBEs and AUDITLOG command as well as the Blue Studio Dashboard.


