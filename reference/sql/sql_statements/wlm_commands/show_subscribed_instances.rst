.. _show_subscribed_instances :

***************************
SHOW SUBSCRIBED INSTANCES
***************************

``SHOW SUBSCRIBED INSTANCES`` lists the cluster workers and their service queues.

.. note:: If you haven't already, read the :ref:`Workload manager guide<workload_manager>`.

See also :ref:`subscribe_service`, :ref:`unsubscribe_service`.

Permissions
=============

Listing the service queues requires no special permissions.

Syntax
==========

.. code-block:: postgres

   show_subscribed_instances_statement ::=
      SELECT SHOW_SUBSCRIBED_INSTANCES( [ service_name ] );

   service_name ::= text

Parameters
============

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
   * - ``service_name``
     - Optional. A service name, to list only the workers subscribed to that service. If no worker is subscribed to it, the function returns ``There are no instances in the cluster subscribed to this service.``

Notes
==========

This function applies to clusters using the workload manager.

Examples
===========

List service queues and workers
-----------------------------------------

Each worker is assigned an automatic ID, and is subscribed to the ``'sqream'`` queue upon start.

.. code-block:: psql
   
   t=> SELECT SHOW_SUBSCRIBED_INSTANCES();
   service | server node | server ip     | server port
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   sqream  | node_9384  | 192.168.0.111 |       5001
   sqream  | node_9385  | 192.168.0.111 |       5002
   sqream  | node_9551  | 192.168.1.91  |       5000

This list shows all cluster nodes, their service names, IPs, and ports.