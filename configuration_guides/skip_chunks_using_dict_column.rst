:orphan:

.. _skip_chunks_using_dict_column:

************************************
Skipping Chunks Using a Dictionary
************************************
The ``skipChunksUsingDictColumn`` flag controls whether the dictionary chunk filter runs. The filter reads the
dictionary of a dictionary-compressed ``TEXT`` column directly, without decompressing the chunk, and skips the
chunk when it can prove that no row in it satisfies every equality condition at once.

This is a third chunk-skipping layer, beside min/max metadata pruning and the chunk index. It answers a question
the other two cannot: where each value on its own appears in nearly every chunk, only the combination of
conditions is selective, so min/max comparison leaves every chunk in the scan.

The filter skips a chunk only on a proven negative. Anything it cannot prove keeps the chunk, so a statement
returns the same rows whether the flag is on or off.

The following describes the ``skipChunksUsingDictColumn`` flag:

* **Data type** - bool
* **Default value** - ``true``
* **Allowed values** - ``true``, ``false``

Not every chunk can be decided. A column that permits nulls is filtered only where a chunk is known to hold none,
and a chunk whose dictionary was written by another compression path is read rather than skipped. A query over
such a column sees no change in the number of chunks scanned.

Setting the flag to ``false`` turns the filter off, which is the baseline a result can be compared against. The
flag is developer-only, so a session must have :ref:`developerMode<developer_mode>` set before it can be changed.

The pool width used to read dictionaries is set by :ref:`skipChunksUsingDictThreads<skip_chunks_using_dict_threads>`.
