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
SQream's current method for stopping the SQream server is running the ``shutdown_server ()`` utility command. Because this command abruptly shuts down the server while executing operations, it has been modified to perform a graceful shutdown by setting it to ``select shutdown_server([is_graceful, [timeout]]);``. This causes the server to wait for any queued statements to complete before shutting down.

How Does it Work?
========================
Running the ``SHUTDOWN_SERVER`` command gives you more control over the following:

* Preventing new queries from connecting to the server by:

   1. Setting the server as unavailable in the metadata server.

       ::

   2. Unsubscribing the server from its service.

* Stopping users from making new connections to the server. Attempting to connect to the server after activating a graceful shutdown displays the following message:

  ``Server is shutting down, no new connections are possible at the moment.``

   ::
   
* The amount of time to wait before shutting down the server.

   ::
   
* Configurations related to shutting down the server.

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

You can define the ``timeout`` argument as the amount minutes after which a forceful shutdown will run, even if a graceful shutdown is in progress.

Note that activating a forced shutdown with a timeout, such as ``select shutdown_server(false, 30)``, outputs the following error message:

``forced shutdown has no timeout timer"``

.. note:: You can set the timeout value using the ``defaultGracefulShutdownTimeoutMinutes`` flag in the Acceleration Studio.

For more information, see :ref:`graceful_shutdown`.

Permissions
=============
Using the ``shutdown_server`` command requires no special permissions.