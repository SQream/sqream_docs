.. _shutdown_server:

********************
SHUTDOWN SERVER
********************
**Comment** - When finished, add command to Utility Commands > shutdown_server.

The **SHUTDOWN SERVER** guide describes the following:

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

How Does it Work?
========================
Running the ``SHUTDOWN_SERVER`` command does the following:

* Prevents new queries from entering the server by doing the following:

  * Setting the SQream server to unavailable in the metadata server. **Comment** - *Is "unavailable" the official server setting?*

    :: 

  * Unsubscribing the server from its service.

* Preventing new connections from being made to the server - attempting to establish a connection with the server after initiating a graceful shutdown displays the "Server is shutting down, no new connections are possible at the moment" messsge.

   ::
   
* Waiting for the statement queue to be cleared - the graceful shutdown waits for queries that have been compiled on the server to be cleared from the statement queue. During this time - start executing on other available servers.

**Comment** - *The last bullet requires clarification.*

Syntax
==========
The following is the syntax for using the ``SHUTDOWN_SERVER`` command:

.. code-block:: postgres

   select shutdown_server([is_graceful, [timeout]]);
   
**Comment** - *Is the below syntax correct?*

.. code-block:: postgres

   select shutdown_server([true/false, [timeout]]);
   
**Comment** - *Can you set the timeout as a flag in Studio, or only in the CLI?*

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
     - **Comment** - Is the default ``true`` or ``false``?
   * - ``timeout``
     - Sets the maximum amount of minutes for the graceful shutdown method to run before the server is shut down using the standard method.
     - ``30``
     - ``5``
	 
.. note:: Setting ``is_graceful`` to ``false`` and defining the ``timeout`` value shuts the server down mid-query after the defined time.

It is possible to pass as the second argument the timeout in minutes after which a forceful shutdown will run, regardless of the progression of the graceful shutdown.

**Comment** - *How can the above be true given the following, "Note that running forced shutdown with a timeout, i.e. select shutdown_server(false, 30) will return an error message; forced shutdown has no timeout timer"?*
	 
Note that you set the timeout value using the ``defaultGracefulShutdownTimeoutMinutes`` flag in Studio.

For more information, see :ref:`graceful_server_shutdown`.

Like shutdown_server() graceful shutdown will stop any query currently running on the server.

**Comment** - *The above makes it seem like it's a separate command, but that's not the case.*

Relationship to Healer & Use Case
============================
**Comment** - *Cannot document this section until I know what the Healer actually does.*

Currently the Healer will not trigger a graceful shutdown upon detection of a stuck query. It will however log detection of such a query, prompting the user to run a graceful shutdown of the server, possibly saving existing queued queries.

Permissions
=============
Using the ``shutdown_server`` command requires no special permissions.

**Comment** - *Confirm.*