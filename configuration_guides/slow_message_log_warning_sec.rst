:orphan:

.. _slow_message_log_warning_sec:

****************************
Slow Message Log Warning Sec
****************************

The ``slowMessageLogWarningSec`` flag sets the processing time above which the metadata server records a warning in its log for a message it handled. Lowering the value records more messages, which is useful when investigating metadata server response times.

* **Data type** - int
* **Default value** - ``1`` (second)
* **Allowed values** - Any positive integer, in seconds

Messages handled on the parallel queue are not measured against this threshold.

This flag applies to the metadata server, and is set in the ``metadata_server_config.json`` file used by :ref:`metadata_server<metadata_server_cli_reference>`. It is not a session or cluster flag, so it cannot be set using ``SET`` or ``ALTER SYSTEM SET``, and it does not appear in the ``sqream_catalog.parameters`` catalog table.
