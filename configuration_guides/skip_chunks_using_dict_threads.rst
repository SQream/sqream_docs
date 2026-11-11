:orphan:

.. _skip_chunks_using_dict_threads:

*****************************************
Skip Chunks Using Dictionary Thread Count
*****************************************
The ``skipChunksUsingDictThreads`` flag sets the number of threads the dictionary chunk filter uses to read the
stored values of compressed chunks: the dictionaries of dictionary-compressed chunks, the runs of RLE-compressed
chunks, and the packed values of P4D-compressed chunks. The filter is controlled by
:ref:`skipChunksUsingDictColumn<skip_chunks_using_dict_column>`, and this flag has no effect when that filter
is off.

Chunks are read in batches across the pool rather than one chunk at a time, which is where most of the
filter's benefit on a wide scan comes from.

The following describes the ``skipChunksUsingDictThreads`` flag:

* **Data type** - size_t
* **Default value** - ``8``
* **Allowed values** - Any positive integer, in threads

Raising the value above the default was measured to give no further improvement. The flag is developer-only, so
a session must have :ref:`developerMode<developer_mode>` set before it can be changed.
