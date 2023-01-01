.. _nodejs:

*************************
Connecting to SQream Using Node.JS
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

Install with NPM
-------------------

Installing with npm is the easiest and most reliable method.
If you need to install the driver in an offline system, see the offline method below.

.. code-block:: console
   
   $ npm install @sqream/sqreamdb

Install from an offline package
-------------------------------------

The Node driver is provided as a tarball for download from the `SQream Drivers page <http://sqream.com/product/client-drivers>`_ .

After downloading the tarball, use ``npm`` to install the offline package.

.. code-block:: console

   $ sudo npm install sqreamdb-4.0.0.tgz


Connect to SQream DB with a Node.JS application
====================================================

Create a simple test
------------------------------------------

Replace the connection parameters with real parameters for a SQream DB installation.

.. code-block:: javascript
   :caption: sqreamdb-test.js

   const Connection = require('@sqream/sqreamdb');

   const config  =  {
     host: 'localhost',
     port: 3109,
     username: 'rhendricks',
     password: 'super_secret_password',
     connectDatabase: 'raviga',
     cluster: true,
     is_ssl: true,
     service: 'sqream'  
     };
     
   const query1  =  'SELECT 1 AS test, 2*6 AS "dozen"';
   
   const sqream = new Connection(config);
   sqream.execute(query1).then((data) => {
      console.log(data);
   }, (err) => {
      console.error(err);
   });


Run the test
----------------

A successful run should look like this:

.. code-block:: console

   $ node sqreamdb-test.js
   [  { test: 1, dozen: 12  }  ]


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
   * - ``is_ssl``
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

Input placeholders
-------------------------

The Node.JS driver can replace parameters in a statement.

Input placeholders allow values like user input to be passed as parameters into queries, with proper escaping.

The valid placeholder formats are provided in the table below.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Placeholder
     - Type
   * - ``%i``
     - Identifier (e.g. table name, column name)
   * - ``%s``
     - A text string
   * - ``%d``
     - A number value
   * - ``%b``
     - A boolean value

See the :ref:`input placeholders example<input_placeholders_example>` below.

Examples
===============

Setting configuration flags
-----------------------------------

SQream DB configuration flags can be set per statement, as a parameter to ``runQuery``.

For example:

.. code-block:: javascript

   const setFlag  =  'SET showfullexceptioninfo = true;';
   
   const query_string = 'SELECT 1';
   
   const myConnection  = new Connection(config);
   myConnection.runQuery(query_string, function  (err, data){
     console.log(err, data);  
   }, setFlag);


Lazyloading
-----------------------------------

To process rows without keeping them in memory, you can lazyload the rows with an async:

.. code-block:: javascript
   
   
   const Connection = require('@sqream/sqreamdb');

   const config  =  {
     host: 'localhost',
     port: 3109,
     username: 'rhendricks',
     password: 'super_secret_password',
     connectDatabase: 'raviga',
     cluster: true,
     is_ssl: true,
     service: 'sqream'  
     };
     
   const sqream = new Connection(config);

   const query = "SELECT * FROM public.a_very_large_table";

   (async () => {
     const cursor = await sqream.executeCursor(query);
     let count = 0;
     for await (let rows of cursor.fetchIterator(100)) { 
       // fetch rows in chunks of 100
       count += rows.length;
     }
     await cursor.close();
     return count;
   })().then((total) => {
     console.log('Total rows', total);
   }, (err) => {
     console.error(err);
   });
   

Reusing a connection
-----------------------------------

It is possible to execeute multiple queries with the same connection (although only one query can be executed at a time).

.. code-block:: javascript
   
   const Connection = require('@sqream/sqreamdb');

   const config  =  {
     host: 'localhost',
     port: 3109,
     username: 'rhendricks',
     password: 'super_secret_password',
     connectDatabase: 'raviga',
     cluster: true,
     is_ssl: true,
     service: 'sqream'  
     };
     
   const sqream = new Connection(config);

   (async () => {

     const conn = await sqream.connect();
     try {
       const res1 = await conn.execute("SELECT 1");
       const res2 = await conn.execute("SELECT 2");
       const res3 = await conn.execute("SELECT 3");
       conn.disconnect();
       return {res1, res2, res3};
     } catch (err) {
       conn.disconnect();
       throw err;
     }

   })().then((res) => {
     console.log('Results', res)
   }, (err) => {
     console.error(err);
   });


.. _input_placeholders_example:

Using placeholders in queries
-----------------------------------

Input placeholders allow values like user input to be passed as parameters into queries, with proper escaping.

.. code-block:: javascript
   
   const Connection = require('@sqream/sqreamdb');

   const config  =  {
     host: 'localhost',
     port: 3109,
     username: 'rhendricks',
     password: 'super_secret_password',
     connectDatabase: 'raviga',
     cluster: true,
     is_ssl: true,
     service: 'sqream'
     };
     
   const sqream = new Connection(config);

   const sql = "SELECT %i FROM public.%i WHERE name = %s AND num > %d AND active = %b";
   
   sqream.execute(sql, "col1", "table2", "john's", 50, true);


The query that will run is ``SELECT col1 FROM public.table2 WHERE name = 'john''s' AND num > 50 AND active = true``


Troubleshooting and recommended configuration
================================================


Preventing ``heap out of memory`` errors
--------------------------------------------

Some workloads may cause Node.JS to fail with the error:

.. code-block:: none

   FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory

To prevent this error, modify the heap size configuration by setting the ``--max-old-space-size`` run flag.

For example, set the space size to 2GB:

.. code-block:: console
   
   $ node --max-old-space-size=2048 my-application.js

BIGINT support
------------------------

The Node.JS connector supports fetching ``BIGINT`` values from SQream DB. However, some applications may encounter an error when trying to serialize those values.

The error that appears is:
.. code-block:: none
   
   TypeError: Do not know how to serialize a BigInt

This is because JSON specification do not support BIGINT values, even when supported by Javascript engines.

To resolve this issue, objects with BIGINT values should be converted to string before serializing, and converted back after deserializing.

For example:

.. code-block:: javascript

   const rows = [{test: 1n}]
   const json = JSON.stringify(rows, , (key, value) =>
     typeof value === 'bigint'
         ? value.toString()
         : value // return everything else unchanged
   ));
   console.log(json); // [{"test": "1"}]

