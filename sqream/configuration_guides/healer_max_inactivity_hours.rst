.. _healer_max_inactivity_hours:

*************************
Query Healer
*************************
The ``healerMaxInactivityHours`` flag is used for defining the threshold for creating a log recording a slow statement. The log includes information about the log memory, CPU and GPU.

The following describes the ``healerMaxInactivityHours`` flag:

* **Data type** - size_t
* **Default value** - ``5``
* **Allowed values** - 1-4000000000

For related flags, see :ref:`is_healer_on`.