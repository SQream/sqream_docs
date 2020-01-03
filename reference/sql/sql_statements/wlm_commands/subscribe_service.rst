.. _subscribe_service :

*******************
SUBSCRIBE_SERVICE
*******************

``SUBSCRIBE_SERVICE`` subscribes a worker to a service queue for the duration of the connected session.

See also :ref:`unsubscribe_service`, :ref:`show_subscribed_instances`.

Permissions
=============

To subscribe a worker to a service, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   subscribe_service_statement ::=
      SELECT SUBSCRIBE_SERVICE( worker_id, service_name );


   worker_id ::= text
   
   service_name ::= text

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``worker_id``
     - The name of the worker to subscribe
   * - ``service_name``
     - The service name to subscribe to. If the service does not exist, it will be created

Notes
==========

* If the service name does not currently exist, it will be created

.. warning:: ``SUBSCRIBE_SERVICE`` applies the service subscription immediately, but the setting applies for the duration of the session. To apply a persistent setting, use the ``initialSubscribedServices`` configuration setting.

Examples
===========

Subscribing a worker to a service queue
-----------------------------------------

A common use of the workload manager is to separate ETL tasks from BI tasks.

Each worker is assigned an automatic ID, and is subscribed to the ``'sqream'`` queue upon start.

.. code-block:: psql
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service | servernode | serverip      | serverport
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   sqream  | node_9384  | 192.168.0.111 |       5001
   sqream  | node_9385  | 192.168.0.111 |       5002
   sqream  | node_9551  | 192.168.1.91  |       5000

We want to modify `node_9551` to join the ETL queue, which will be created when we subscribe it:

.. code-block:: psql
   
   t=> SELECT SUBSCRIBE_SERVICE('node_9551','etl');
   executed
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service | servernode | serverip      | serverport
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   sqream  | node_9384  | 192.168.0.111 |       5001
   sqream  | node_9385  | 192.168.0.111 |       5002
   sqream  | node_9551  | 192.168.1.91  |       5000
   etl     | node_9551  | 192.168.1.91  |       5000

To connect to the new queue, use the ``service`` parameter in the connection string. A statement executed from a connections to the ``etl`` service will be routed to an available worker that is subscribed to the ``etl`` service queue.
