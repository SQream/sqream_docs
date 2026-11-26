:orphan:

.. _in_list_join_max_metadata_filters:

**********************************************
Setting the IN List Join Metadata Filter Limit
**********************************************
The ``inListJoinMaxMetadataFilters`` flag sets the largest number of distinct values per column that an ``IN`` list
compiled as a join keeps as metadata filters, so that the scan still skips chunks that none of the values can match.

An ``IN`` list longer than :ref:`inListJoinThreshold<in_list_join_threshold>` is compiled as an inner join against the
listed values. The join form carries one metadata filter per value, which the scan evaluates with a single binary
search per chunk. Past this limit the values of the column are kept as ranges instead, governed by
:ref:`inListJoinMaxMetadataRanges<in_list_join_max_metadata_ranges>`.

The following describes the ``inListJoinMaxMetadataFilters`` flag:

* **Data type** - int
* **Default value** - ``1000``
* **Allowed values** - ``0`` or any positive integer

Setting the flag to ``0`` keeps no per-value filters, leaving only the ranges.

Chunk skipping applies to ``INT``, ``FLOAT``, ``NUMERIC``, ``DATE``, ``DATETIME`` and ``TEXT`` columns. Chunks are
skipped when the table is clustered on the column the list filters.

The flag may be set for the session:

.. code-block:: postgres

   SET inListJoinMaxMetadataFilters = 2000;

For the three forms an ``IN`` list is compiled into, and where this flag applies among them, see
:ref:`Compiling IN Lists<compiling_in_lists>`.
