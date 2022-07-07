.. _shutdown_server:

********************
SHUTDOWN SERVER
********************
**Comment** - When finished, add command to Utility Commands > shutdown_server.

The **SHUTDOWN_SERVER** guide describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
===============
SQream's current method for stopping the SQream server is running the ``shutdown_server ()`` utility command. Because this command abruptly shuts down the server while executing operations, it has been modified to perform a graceful shutdown, giving you more control over the following:

* Preventing new queries from connecting to the server.

   ::
   
* The amount of time to wait before shutting down the server.

   ::
   
* Configurations related to shutting down the server.


Stop new queries from entering the server. This will be done by:

Setting the server as unavailable in the metadata server.

Unsubscribing the server from its service 

Stop new connections from being made to the server. A user trying to connect to the server after starting graceful shutdown will recieve the message "Server is shutting down, no new connections are possible at the moment .

Wait for emptying of statement queue. The graceful shutdown will wait for queries that have been compiled on the server leave the statement queue and start executing on other available servers.

How Does it Work?
========================
Running the ``SHUTDOWN_SERVER`` command does the following:

* Prevents new queries from entering the server by doing the following:

  * Makes the SQream server unavailable in the metadata server.

    :: 

  * Unsubscribing the server from its service.

* Preventing new connections from being made to the server - attempting to establish a connection with the server after initiating a graceful shutdown displays the "Server is shutting down, no new connections are possible at the moment" messsge.

   ::
   
* Waiting for the statement queue to be cleared - the graceful shutdown waits for queries that have been compiled on the server to be cleared from the statement queue. During this time - start executing on other available servers.

* You start running a query on a server.
* The server compiles the query.
* When finished, the statement enters teh statement queue.
* When the server is ready to take the sentence from the queue, the compilation data on teh server is passed to another server, which allows it to begin on another server.

Tachlis - the server waits for any queued statements that depend on the server to leave the queue.

Graceful shutdown lets me finish what the first server is already working on without taking on any new work.

Why would you want to shut down a server? 





The graceful shutdown will wait for queries that have been compiled on the server leave the statement queue and start executing on other available servers.

**Comment** - *The last bullet requires clarification.*

Syntax
==========
The following is the syntax for using the ``SHUTDOWN_SERVER`` command:

.. code-block:: postgres

   select shutdown_server([true/false, [timeout]]);
   
**Comment** - *Update Configuration page with this flag. NOT RN 2022.1*

Returns
==========
Running the ``shutdown_server`` command returns no output.

Parameters
============
The following table shows the ``shutdown_server`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Example
     - Default
   * - ``is_graceful``
     - Determines the method used to shut down the server.
     - Selecting ``false`` shuts down the server while queries are running. Selecting ``true`` uses the graceful shutdown method.
     - NA
   * - ``timeout``
     - Sets the maximum amount of minutes for the graceful shutdown method to run before the server is shut down using the standard method.
     - ``30``
     - Five minutes.
	 
.. note:: Setting ``is_graceful`` to ``false`` and defining the ``timeout`` value shuts the server down mid-query after the defined time.

It is possible to pass as the second argument the timeout in minutes after which a forceful shutdown will run, regardless of the progression of the graceful shutdown.

**Comment** - *How can the above be true given the following, "Note that running forced shutdown with a timeout, i.e. select shutdown_server(false, 30) will return an error message; forced shutdown has no timeout timer"?*
	 
Note that you set the timeout value using the ``defaultGracefulShutdownTimeoutMinutes`` flag in Studio.

For more information, see :ref:`graceful_shutdown`.

**Comment** - *I have not yet created the ``graceful_shutdown`` configuration flag. I need to know what category it belongs in before doing so.*

Like shutdown_server() graceful shutdown will stop any query currently running on the server.

Permissions
=============
Using the ``shutdown_server`` command requires no special permissions.