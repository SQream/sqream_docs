.. _troubleshooting:

***********************
Troubleshooting
***********************

Troubleshooting common issues
======================================

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

