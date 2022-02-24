.. _resolving_common_issues:

***********************
Resolving Common Issues
***********************

The **Resolving Common Issues** page describes how to resolve the following common issues:

.. toctree::
   :maxdepth: 2
   :glob:
   :titlesonly:


Troubleshooting Cluster Setup and Configuration
-----------------------------------------------------

#. Note any errors - Make a note of any error you see, or check the :ref:`logs<logging>` for errors you might have missed.

#. If SQream DB can't start, start SQream DB on a new storage cluster, with default settings. If it still can't start, there could be a driver or hardware issue. :ref:`Contact SQream support<information_for_support>`.

#. Reproduce the issue with a standalone SQream DB - starting up a temporary, standalone SQream DB can isolate the issue to a configuration issue, network issue, or similar.

#. Reproduce on a minimal example - Start a standalone SQream DB on a clean storage cluster and try to replicate the issue if possible.


Troubleshooting Connectivity Issues
-----------------------------------

#. Verify the correct login credentials - username, password, and database name.

#. Verify the host name and port

#. Try connecting directly to a SQream DB worker, rather than via the load balancer

#. Verify that the driver version you're using is supported by the SQream DB version. Driver versions often get updated together with major SQream DB releases.

#. Try connecting directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If you can connect with the local SQL client, check network availability and firewall settings.

Troubleshooting Query Performance
------------------------------------

#. Use :ref:`show_node_info` to examine which building blocks consume time in a statement. If the query has finished, but the results are not yet materialized in the client, it could point to a problem in the application's data buffering or a network throughput issue..

#. If a problem occurs through a 3\ :sup:`rd` party client, try reproducing it directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If the performance is better in the local client, it could point to a problem in the application or network connection.

#. Consult the :ref:`sql_best_practices` guide to learn how to optimize queries and table structures.


Troubleshooting Query Behavior
---------------------------------

#. Consult the :ref:`sql` reference to verify if a statement or syntax behaves correctly. SQream DB may have some differences in behavior when compared to other databases.

#. If a problem occurs through a 3\ :sup:`rd` party client, try reproducing it directly with :ref:`the built in SQL client<sqream_sql_cli_reference>`. If the problem still occurs, file an issue with SQream support.

File an issue with SQream support
------------------------------------

To file an issue, follow our :ref:`information_for_support` guide.