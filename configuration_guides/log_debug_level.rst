:orphan:

.. _log_debug_level:

***************************
Setting the Debug Log Level
***************************

The ``logDebugLevel`` flag sets the most detailed level of message that a worker writes to its debug log, the ``sqdebug_*.log`` files next to the worker's ``sqream_*.log`` files. Messages less severe than this level are not written.

The levels are as follows. For what each level contains, see the :ref:`Information Level<information_level>` table.

* **0** - ``SYSTEM``
* **1** - ``FATAL``
* **2** - ``ERROR``
* **3** - ``WARNING``
* **4** - ``INFO``
* **5** - ``DEBUG``
* **6** - ``TRACE``

The following describes the ``logDebugLevel`` flag:

* **Data type** - size_t
* **Default value** - ``4`` (``INFO``)
* **Allowed values** - ``0``-``6``

The level is applied when the worker starts, so set the flag in the worker's configuration file. A change applies to workers started afterwards.

Levels ``5`` (``DEBUG``) and ``6`` (``TRACE``) write more messages, so the debug log grows faster and rotates sooner. For log rotation settings, see :ref:`log_rotation`.
