.. _unsubscribe_service :

********************
UNSUBSCRIBE_SERVICE
********************

``UNSUBSCRIBE_SERVICE`` unsubscribes a worker from a service queue for the duration of the connected session.

.. note:: If you haven't already, read the :ref:`Workload manager guide<workload_manager>`.

See also :ref:`subscribe_service`, :ref:`show_subscribed_instances`.

Permissions
=============

To unsubscribe a worker from a service, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   subscribe_service_statement ::=
      SELECT UNSUBSCRIBE_SERVICE( worker_id, service_name );


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
     - The name of the worker to unsubscribe
   * - ``service_name``
     - The service name to unsubscribe from

Notes
==========

* If the service name does not currently exist, it will be created

.. warning:: ``UNSUBSCRIBE_SERVICE`` removes the service subscription immediately, but the setting applies for the duration of the session. To apply a persistent setting, use the ``initialSubscribedServices`` configuration setting. Read the :ref:`Workload manager guide<workload_manager>` for more information.

Examples
===========

Unsubscribing a worker from a service queue
-----------------------------------------------

Each worker is assigned an automatic ID, and is subscribed to the ``'sqream'`` queue upon start.

.. code-block:: psql
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service | servernode | serverip      | serverport
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   sqream  | node_9384  | 192.168.0.111 |       5001
   sqream  | node_9385  | 192.168.0.111 |       5002
   sqream  | node_9551  | 192.168.1.91  |       5000
   etl     | node_9551  | 192.168.1.91  |       5000

We want to modify `node_9551` to leave the ETL queue:

.. code-block:: psql
   
   t=> SELECT UNSUBSCRIBE_SERVICE('node_9551','etl');
   executed
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service | servernode | serverip      | serverport
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   sqream  | node_9384  | 192.168.0.111 |       5001
   sqream  | node_9385  | 192.168.0.111 |       5002
   sqream  | node_9551  | 192.168.1.91  |       5000
