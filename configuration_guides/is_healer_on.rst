:orphan:

.. _is_healer_on:

************
Is Healer On
************

The ``is_healer_on`` flag enables the Query Healer, which periodically examines the progress of running statements and logs statements exceeding the ``maxStatementInactivitySeconds`` flag setting.

* **Data type** - boolean
* **Default value** - ``true``
* **Allowed values** - ``true``, ``false``

For related flags, see :ref:`max_statement_inactivity_seconds`.