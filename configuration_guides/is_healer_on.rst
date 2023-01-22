.. _is_healer_on:

*************************
Is Healer On
*************************
The ``is_healer_on`` flag enables the Query Healer, which periodically examines the progress of running statements and logs statements exceeding the ``maxStatementInactivitySeconds`` flag setting.

The following describes the ``is_healer_on`` flag:

* **Data type** - boolean
* **Default value** - ``true``
* **Allowed values** - ``true``, ``false``

For related flags, see :ref:`healer_max_statement_inactivity_seconds`.