.. _shutdown_server:

********************
SHUTDOWN SERVER
********************
The **SHUTDOWN_SERVER** guide describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
===============
SQream's current method for stopping the SQream server is running the ``shutdown_server()`` utility command. Because this command abruptly shuts down the server while executing operations, it has been modified to perform a graceful shutdown, giving you more control over the following:

* Preventing new queries from connecting to the server.

   ::
   
* The amount of time to wait before shutting down the server.

   ::
   
* Configurations related to shutting down the server.

How Does it Work?
========================
Running the ``SHUTDOWN_SERVER`` command does the following:

* Prevents new queries from entering the server by doing the following:

  * Disabling incoming queries.

    :: 

  * Unsubscribing the server from its service.

* Preventing new connections from being made to the server - attempting to establish a connection with the server after initiating a graceful shutdown displays the "Server is shutting down, no new connections are possible at the moment" messsge.

   ::
   
* Waits for any queries that depend on server being shut down to leave the statement queue.

Syntax
==========
The following is the syntax for using the ``SHUTDOWN_SERVER`` command:

.. code-block:: postgres

   select shutdown_server([is_graceful, [timeout]]);
   
The following is example of the ``SHUTDOWN_SERVER`` command:
   
.. code-block:: postgres

   select shutdown_server([true/false, [timeout]]);
   
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
 	 - ``false``
   * - ``timeout``
     - Sets the maximum amount of minutes for the graceful shutdown method to run before the server is shut down using the standard method.
	 - ``30``
	 - Five minutes.
	 
.. note:: Setting ``is_graceful`` to ``false`` and defining the ``timeout`` value shuts the server down mid-query after the defined time.

It is possible to pass as the second argument the timeout in minutes after which a forceful shutdown will run after defining the graceful shutdown value, regardless of the progression of the graceful shutdown.
 
Note that you set the timeout value using the ``defaultGracefulShutdownTimeoutMinutes`` flag in Studio.

For more information, see :ref:`graceful_shutdown`.

**Comment** - *I have not yet created the ``graceful_shutdown`` configuration flag. I need to know what category it belongs in before doing so.*

Like shutdown_server() graceful shutdown will stop any query currently running on the server.

Permissions
=============
Using the ``shutdown_server`` command requires no special permissions.