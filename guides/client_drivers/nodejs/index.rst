.. _nodejs:

*************************
Node.JS
*************************

The SQream DB Node.JS driver allows Javascript applications and tools connect to SQream DB.
This tutorial shows you how to write a Node application using the Node.JS interface.

The driver requires Node 10 or newer.

.. contents:: In this topic:
   :local:

Installing the Node.JS driver
==================================

Prerequisites
----------------

* Node.JS 10 or newer. Follow instructions at `nodejs.org <https://nodejs.org/en/download/package-manager/>`_ .

Getting the tarball
---------------------

The Node driver is provided as a tarball for download from the `SQream Drivers page <http://sqream.com/product/client-drivers>`_ .

Install with NPM
-------------------------

.. code-block:: console

   $ sudo npm install sqreamdb-3.0.0.tgz


Connect to SQream DB with a Node.JS application
==============================================

Create a simple test
------------------------------------------

Replace the connection parameters with real parameters for a SQream DB installation.

.. code-block:: javascript
   :caption: sqreamdb-test.js

   const Connection  = require('sqreamdb');
   const config  =  {
     host: '<host>',
     port: <port>,
     username: '<username>',
     password: '<password>',
     connectDatabase: '<database>',
     cluster: '<true | false>',
     ssl: '<true | false>',
     service: '<workload manager service>'  
     };
     
   const query1  =  'SELECT 1 AS test, 2*6 AS "dozen"';
   
   const myConnection  = new Connection(config);
   myConnection.runQuery(query1, function  (err, data){
      console.log(err, data);  
   });


Run the test
----------------

A successful run should look like this:

.. code-block:: console

   $ node sqreamdb-test.js
   null [  { test: 1, dozen: 12  }  ]


API reference
====================

Connection parameters
---------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Optional
     - Default
     - Description
   * - ``host``
     - ✗
     - None
     - Hostname for SQream DB worker. For example, ``127.0.0.1``, ``sqream.mynetwork.co``
   * - ``port``
     - ✗
     - None
     - Port for SQream DB end-point. For example, ``3108`` for the load balancer, ``5000`` for a worker.
   * - ``username``
     - ✗
     - None
     - Username of a role to use for connection. For example, ``rhendricks``
   * - ``password``
     - ✗
     - None
     - Specifies the password of the selected role. For example, ``Tr0ub4dor&3``
   * - ``connectDatabase``
     - ✗
     - None
     - Database name to connect to. For example, ``master``
   * - ``service``
     - ✓
     - ``sqream``
     - Specifices service queue to use. For example, ``etl``
   * - ``ssl``
     - ✓
     - ``false``
     - Specifies SSL for this connection. For example, ``true``
   * - ``cluster``
     - ✓
     - ``false``
     - Connect via load balancer (use only if exists, and check port). For example, ``true``

Events
-------------

The connector handles event returns with an event emitter

getConnectionId
   The ``getConnectionId`` event returns the executing connection ID.

getStatementId
   The ``getStatementId`` event returns the executing statement ID.

getTypes
   The ``getTypes`` event returns the results columns types.

Example
^^^^^^^^^^^^^^^^^

.. code-block:: javascript

   const myConnection  = new Connection(config);

   myConnection.runQuery(query1, function  (err, data){
     myConnection.events.on('getConnectionId', function(data){
         console.log('getConnectionId', data);  
     });

     myConnection.events.on('getStatementId', function(data){
         console.log('getStatementId', data);  
     });

     myConnection.events.on('getTypes', function(data){
         console.log('getTypes', data);  
     });  
   });

Setting flags
---------------------

SQream DB configuration flags can be set per statement, as a parameter to ``runQuery``.

For example:

.. code-block:: javascript

   const setFlag  =  'SET showfullexceptioninfo = true;';
   
   const query_string = 'SELECT 1';
   
   const myConnection  = new Connection(config);
   myConnection.runQuery(query_string, function  (err, data){
     console.log(err, data);  
   }, setFlag);


Recommended Node configuration
======================================

Preventing ``heap out of memory`` errors
--------------------------------------------

Some workloads may cause Node.JS to fail with the error:

.. code-block:: none

   FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory

To prevent this error, modify the heap size configuration by setting the ``--max-old-space-size`` run flag.

For example, set the space size to 2GB:

.. code-block:: console
   
   $ node --max-old-space-size=2048 my-application.js

