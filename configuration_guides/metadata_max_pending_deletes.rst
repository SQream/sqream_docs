:orphan:

.. _metadata_max_pending_deletes:

****************************
Metadata Max Pending Deletes
****************************

The ``metadataMaxPendingDeletes`` flag sets the maximum number of metadata objects that may wait in the deferred delete queue. While the queue holds fewer objects than this value, the metadata server destroys objects on a background thread. Once the queue reaches the limit, the metadata server destroys the object immediately instead and writes a warning to its log.

* **Data type** - size_t
* **Default value** - ``10000``
* **Allowed values** - 0 and above

This flag applies to the metadata server, and is set in the ``metadata_server_config.json`` file used by :ref:`metadata_server<metadata_server_cli_reference>`. It is not a session or cluster flag, so it cannot be set using ``SET`` or ``ALTER SYSTEM SET``, and it does not appear in the ``sqream_catalog.parameters`` catalog table.
