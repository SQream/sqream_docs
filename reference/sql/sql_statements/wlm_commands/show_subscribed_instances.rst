.. _show_subscribed_instances :

***************************
SHOW_SUBSCRIBED_INSTANCES
***************************

``SHOW_SUBSCRIBED_INSTANCES`` lists the cluster workers and their service queues.

.. note:: If you haven't already, read the :ref:`Workload manager guide<workload_manager>`.

See also :ref:`subscribe_service`, :ref:`unsubscribe_service`.

Permissions
=============

To list the service queues, the current role must have the ``SUPERUSER`` permission.

Syntax
==========

.. code-block:: postgres

   show_subscribed_instances_statement ::=
      SELECT SHOW_SUBSCRIBED_INSTANCES();

Parameters
============

None

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
   service | servernode | serverip      | serverport
   --------+------------+---------------+-----------
   sqream  | node_9383  | 192.168.0.111 |       5000
   report  | node_9384  | 192.168.0.111 |       5001
   ingest  | node_9385  | 192.168.0.111 |       5002
   bi      | node_9551  | 192.168.1.91  |       5000

This list shows all cluster nodes, their service names, IPs, and ports.
