:orphan:

.. _skip_chunks_using_dict_column:

************************************
Skipping Chunks Using a Dictionary
************************************
The ``skipChunksUsingDictColumn`` flag controls whether the dictionary chunk filter runs. The filter reads the
stored values of a compressed chunk directly, without decompressing it, and skips the chunk when it can prove that
no row in it satisfies every filter condition at once.

The filter reads the following chunks:

* ``TEXT`` columns compressed with dictionary compression, whether the values in a chunk are all the same length or
  vary in length
* ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``, ``DATE``, ``DATETIME``, and ``REAL`` columns compressed with dictionary,
  RLE, or P4D compression
* ``DOUBLE`` columns compressed with RLE compression

A P4D chunk holds no dictionary, so it cannot rule out a chunk on its own. When a statement filters on several
columns, it narrows the rows another column's dictionary has already matched, and the chunk is skipped when none of
those rows is left. A P4D chunk of values that were sorted when loaded is stored as differences between rows, and is
not narrowed.

It tests the comparisons ``=``, ``<>``, ``<``, ``<=``, ``>``, and ``>=``, and the conditions built from them, such as
``BETWEEN``, ``IN`` lists, and ``OR`` between conditions on the same column. ``<>`` is not tested on ``TEXT`` columns,
and ``BOOL`` columns are not tested.

This is a third chunk-skipping layer, beside min/max metadata pruning and the chunk index. It answers a question
the other two cannot: where each value on its own appears in nearly every chunk, only the combination of
conditions is selective, so min/max comparison leaves every chunk in the scan.

The filter skips a chunk only on a proven negative. Anything it cannot prove keeps the chunk, so a statement
returns the same rows whether the flag is on or off.

The following describes the ``skipChunksUsingDictColumn`` flag:

* **Data type** - bool
* **Default value** - ``true``
* **Allowed values** - ``true``, ``false``

Not every chunk can be decided. A ``TEXT`` column that permits nulls is filtered only where a chunk is known to hold
none, and a chunk whose dictionary was written by another compression path is read rather than skipped. A query over
such a column sees no change in the number of chunks scanned.

Setting the flag to ``false`` turns the filter off, which is the baseline a result can be compared against. The
flag is developer-only, so a session must have :ref:`developerMode<developer_mode>` set before it can be changed.

The pool width used to read dictionaries is set by :ref:`skipChunksUsingDictThreads<skip_chunks_using_dict_threads>`.

When a statement filters on several columns, the developer-only ``skipChunksUsingDictMaxMatchPercent`` flag (default
``5``) sets the largest share of a column's distinct values that a condition other than an equality may match and
still be used as the starting point for this test. Raising it lets broader conditions skip chunks, at the cost of
extra work where none can be skipped, and it never changes a result.

Reading Only the Rows That Can Match
------------------------------------
A chunk the filter keeps is not always read whole. While testing a chunk, the filter also learns which of its rows
might satisfy the conditions, and only those rows are passed on: the columns are recompressed to hold just those
rows before the chunk is copied to the GPU. A ``SELECT`` that keeps a small share of each chunk's rows copies and
processes correspondingly less. Statements that rewrite whole chunks, such as ``UPDATE`` and ``DELETE``, always read
every row.

The following developer-only flags control this behavior. Like ``skipChunksUsingDictColumn``, none of them changes a
result:

.. list-table::
   :widths: 35 10 55
   :header-rows: 1

   * - Flag
     - Default
     - Description
   * - ``skipChunksUsingDictKeptRowsMaxPercent``
     - ``50``
     - The largest share of a chunk's rows, as a percentage, for which the rows that might match are passed on. A
       chunk where more rows might match is read whole. ``0`` turns row passing off, while chunks are still skipped.
   * - ``skipChunksUsingDictCompactKeptRows``
     - ``true``
     - Recompresses a chunk to the rows that might match before it is copied to the GPU. When ``false``, every column
       is copied as stored, and the rows are dropped after decompression instead, under the limit set by
       ``skipChunksUsingDictDecompressKeptRowsMaxPercent``.
   * - ``skipChunksUsingDictDecompressKeptRowsMaxPercent``
     - ``15``
     - The largest share of a chunk's rows, as a percentage, for which the rows that might match are dropped during
       decompression on the GPU, where they were not recompressed beforehand.
   * - ``skipChunksUsingDictMixedWidthText``
     - ``true``
     - Filters ``TEXT`` chunks whose values vary in length. When ``false``, such a chunk is always read, and only
       ``TEXT`` chunks whose values share one length are filtered.
