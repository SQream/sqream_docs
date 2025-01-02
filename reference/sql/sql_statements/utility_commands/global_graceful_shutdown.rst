:orphan:

.. _global_graceful_shutdown:

************************
GLOBAL GRACEFUL SHUTDOWN
************************


SQream's method for gracefully stopping the all SQream servers in the cluster. Once executed, it causes the servers to wait for any queued statements to complete before shutting down.

.. contents:: 
   :local:
   :depth: 1


How Does it Work?
========================
Running the ``GLOBAL GRACEFUL SHUTDOWN`` command gives you more control over the following:

* Preventing new queries from connecting to the server by:

  * Setting the servers as unavailable in the metadata server.

      ::

  * Unsubscribing the servers from there services.

* Preventing users from opening new connections to the server. Attempting to connect to the server after activating a graceful shutdown displays the following message:

  .. code-block:: postgres

     Server is shutting down, no new connections are possible at the moment.
  

Syntax
==========
The following is the syntax for using the ``GLOBAL GRACEFUL SHUTDOWN`` command:

.. code-block:: postgres

   select global_graceful_shutdown();
   
Returns
==========
Running the ``GLOBAL GRACEFUL SHUTDOWN`` command returns no output.

Parameters
============
``GLOBAL GRACEFUL SHUTDOWN`` has no input parameters:


Permissions
=============
Using the ``shutdown_server`` command requires no special permissions.