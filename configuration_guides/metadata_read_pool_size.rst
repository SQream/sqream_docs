:orphan:

.. _metadata_read_pool_size:

***********************
Metadata Read Pool Size
***********************

The ``metadataReadPoolSize`` flag sets the number of read threads the metadata server starts for each accepted connection. Increasing it allows more read-only metadata requests to be served concurrently.

* **Data type** - int
* **Default value** - ``4``
* **Allowed values** - 1 and above. A value below ``1`` is treated as ``1``

This flag applies to the metadata server, and is set in the ``metadata_server_config.json`` file used by :ref:`metadata_server<metadata_server_cli_reference>`. It is not a session or cluster flag, so it cannot be set using ``SET`` or ``ALTER SYSTEM SET``, and it does not appear in the ``sqream_catalog.parameters`` catalog table.

The read threads are started when a connection is accepted, so a change to this flag applies to connections opened after the metadata server is restarted.

For related flags, see :ref:`metadata_read_pool_enabled`.
