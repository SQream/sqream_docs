:orphan:

.. _metadata_read_pool_enabled:

**************************
Metadata Read Pool Enabled
**************************

The ``metadataReadPoolEnabled`` flag enables the metadata server read pool, which handles read-only metadata requests on a parallel queue instead of the metadata server's single serial queue. Disabling it returns every request type to the serial queue.

* **Data type** - boolean
* **Default value** - ``true``
* **Allowed values** - ``true``, ``false``

This flag applies to the metadata server, and is set in the ``metadata_server_config.json`` file used by :ref:`metadata_server<metadata_server_cli_reference>`. It is not a session or cluster flag, so it cannot be set using ``SET`` or ``ALTER SYSTEM SET``, and it does not appear in the ``sqream_catalog.parameters`` catalog table.

For related flags, see :ref:`metadata_read_pool_size`.
