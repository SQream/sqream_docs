:orphan:

.. _max_metadata_message_bytes:

**************************
Max Metadata Message Bytes
**************************

The ``maxMetadataMessageBytes`` flag sets the maximum size in bytes of a single metadata server response page.

A response page is bounded by both a key count and this byte budget, and is returned as soon as either is reached. The byte budget is what keeps a response from growing without limit when the values themselves are large, because the metadata server serializes a whole page before writing it to the socket.

The following describes the ``maxMetadataMessageBytes`` flag:

* **Data type** - size_t
* **Default value** - ``16777216`` (16 MB)
* **Allowed values** - Any positive integer, in bytes

Every page carries at least one key, so a scan continues to make progress even when a single key and value together exceed the budget.

For the key count bounding the same response, see the ``maxMetadataMessageKeys`` flag.
