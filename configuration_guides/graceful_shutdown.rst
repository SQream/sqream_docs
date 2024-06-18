.. _graceful_shutdown:

*************************
Setting the Graceful Server Shutdown
*************************
The ``defaultGracefulShutdownTimeoutMinutes`` flag is used for setting the amount of time to pass before SQream performs a graceful server shutdown.

The following describes the ``defaultGracefulShutdownTimeoutMinutes`` flag: 

* **Data type** - size_t
* **Default value** - ``5``
* **Allowed values** - 1-4000000000

For more information, see :ref:`shutdown_server_command`.

For related flags, see the folowing:

* :ref:`is_healer_on`

* :ref:`current_method_flag_types`