.. _troubleshooting:

***********************
Troubleshooting
***********************

Follow this checklist if you find that the performance is slower than you expect.

.. list-table:: Troubleshooting checklist
   :widths: auto
   :header-rows: 1
   
   * - Step
     - Description
     - Results
   * - 1
     - A single query is slow
     - 
         If a query isn't performing as you expect, follow the :ref:`Query best practices<query_best_practices>` part of the :ref:`sql_best_practices` guide.
         
         If all queries are slow, continue to step 2.
   * - 2
     - All queries on a specific table are slow
     - 
         #. If all queries on a specific table aren't performing as you expect, follow the :ref:`Table design best practices<table_design_best_practices>` part of the :ref:`sql_best_practices` guide.
         #. Check for active delete predicates in the table. Consult the :ref:`delete_guide` guide for more information.
         
         If the problem spans all tables, continue to step 3.
   * - 3
     - Check that all workers are up
     - 
         Use ``SELECT show_cluster_nodes();`` to list the active cluster workers.
         
         If the worker list is incomplete, follow the :ref:`cluster troubleshooting<cluster_troubleshooting>` section below.
         
         If all workers are up, continue to step 4.
   * - 4
     - Check that all workers are performing well
     - 
         #. Identify if a specific worker is slower than others by running the same query on different workers. (e.g. by connecting directly to the worker or through a service queue)
         #. If a specific worker is slower than others, investigate performance issues on the host using standard monitoring tools (e.g. ``top``).
         #. Restart SQream DB workers on the problematic host.
         
         If all workers are performing well, continue to step 5.
   * - 5 
     - Check if the workload is balanced across all workers
     - 
         #. Run the same query several times and check that it appears across multiple workers (use ``SELECT show_server_status()`` to monitor)
         #. If some workers have a heavier workload, check the service queue usage. Refer to the :ref:`workload_manager` guide.
         
         If the workload is balanced, continue to step 6.
   * - 6
     - Check if there are long running statements
     - 
         #. Identify any currently running statements (use ``SELECT show_server_status()`` to monitor)
         #. If there are more statements than available resources, some statements may be in an ``In queue`` mode.
         #. If there is a statement that has been running for too long and is blocking the queue, consider stopping it (use ``SELECT stop_statement(<statement id>)``).
         
         If the statement does not stop correctly, contact SQream support.
         
         If there are no long running statements or this does not help, continue to step 7.
   * - 7
     - Check if there are active locks
     - 
         #. Use ``SELECT show_locks()`` to list any outstanding locks.
         #. If a statement is locking some objects, consider waiting for that statement to end or stop it.
         #. If after a statement is completed the locks don't free up, refer to the :ref:`concurrency_and_locks` guide.
         
         If performance does not improve after the locks are released, continue to step 8.
   * - 8
     - Check free memory across hosts
     - 
         #. Check free memory across the hosts by running ``$ free -th`` from the terminal.
         #. If the machine has less than 5% free memory, consider **lowering** the ``limitQueryMemoryGB`` and ``spoolMemoryGB`` settings. Refer to the :ref:`configuration` guide.
         #. If the machine has a lot of free memory, consider **increasing** the ``limitQueryMemoryGB`` and ``spoolMemoryGB`` settings.
         
         If performance does not improve, contact SQream support for more help.



Troubleshooting common issues
======================================

.. _cluster_troubleshooting:

Troubleshoot cluster setup and configuration
-----------------------------------------------------

#. Note any errors - Make a note of any error you see, or check the :ref:`logs<logging>` for errors you might have missed.

.. note:: Logs are generated per-worker, so you will need to identify the worker on which the error occured, or collect logs from all nodes.

#. If SQream DB can't start, start SQream DB on a new storage cluster, with default settings. If it still can't start, there could be a driver or hardware issue. :ref:`Contact SQream support<information_for_support>`.

#. Reproduce the issue with a standalone SQream DB - starting up a temporary, standalone SQream DB can isolate the issue to a configuration issue, network issue, or similar.

#. Reproduce on a minimal example - Start a standalone SQream DB on a clean storage cluster and try to replicate the issue if possible.


Troubleshoot connectivity issues
-----------------------------------

#. Verify the correct login credentials - username, password, and database name.

#. Verify the host name and port

#. Try connecting directly to a SQream DB worker, rather than via the load balancer

#. Verify that the driver version you're using is supported by the SQream DB version. Driver versions often get updated together with major SQream DB releases.

#. Try connecting directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If you can connect with the local SQL client, check network availability and firewall settings.

Troubleshoot query performance
------------------------------------

#. Use :ref:`show_node_info` to examine which building blocks consume time in a statement. If the query has finished, but the results are not yet materialized in the client, it could point to a problem in the application's data buffering or a network throughput issue..

#. If a problem occurs through a 3\ :sup:`rd` party client, try reproducing it directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If the performance is better in the local client, it could point to a problem in the application or network connection.

#. Consult the :ref:`sql_best_practices` guide to learn how to optimize queries and table structures.


Troubleshoot query behavior
---------------------------------

#. Consult the :ref:`sql` reference to verify if a statement or syntax behaves correctly. SQream DB may have some differences in behavior when compared to other databases.

#. If a problem occurs through a 3\ :sup:`rd` party client, try reproducing it directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If the problem still occurs, file an issue with SQream support.

File an issue with SQream support
------------------------------------

To file an issue, follow our :ref:`information_for_support` guide.

Examining logs
========================

See the :ref:`collecting_logs` section of the :ref:`information_for_support` guide for information about collecting logs for support.


Start a temporary SQream DB for testing
===============================================

Starting a SQream DB temporarily (not as part of a cluster, with default settings) can be helpful in identifying configuration issues.

Example:

.. code-block:: console

   $ sqreamd /home/rhendricks/raviga_database 0 5000 /home/sqream/.sqream/license.enc

.. tip:: 
   
   * Using ``nohup`` and ``&`` sends SQream DB to run in the background.
   
   * 
      It is safe to stop SQream DB at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
      
      .. code-block:: console
      
         $ kill -9 $SQREAM_PID

