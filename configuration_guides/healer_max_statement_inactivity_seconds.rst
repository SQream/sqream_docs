.. _healer_max_statement_inactivity_seconds:

*************************
Configuring the Query Healer
*************************
The ``maxStatementInactivitySeconds`` flag is used for defining the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.

The following describes the ``maxStatementInactivitySeconds`` worker level flag:

* **Data type** - size_t
* **Default value** - ``5``
* **Allowed values** - 1-4000000000

For related flags, see :ref:`is_healer_on`.