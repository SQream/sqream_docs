:orphan:

.. _in_list_join_max_metadata_ranges:

*********************************************
Setting the IN List Join Metadata Range Limit
*********************************************
The ``inListJoinMaxMetadataRanges`` flag sets the largest number of ranges kept as metadata filters for a column of an
``IN`` list whose distinct values outnumber :ref:`inListJoinMaxMetadataFilters<in_list_join_max_metadata_filters>`.

Rather than drop chunk skipping for a very long list, the compiler covers the column's values with a small number of
ranges, split at the widest gaps between them. The scan skips a chunk that falls between two of the ranges. Each range
past the first costs two comparisons per chunk, so a higher value prunes more chunks at a higher cost per chunk.

The following describes the ``inListJoinMaxMetadataRanges`` flag:

* **Data type** - int
* **Default value** - ``32``
* **Allowed values** - ``0`` or any positive integer

Setting the flag to ``0`` keeps no ranges, which turns off chunk skipping for a list past the per-value filter limit.

The flag may be set for the session:

.. code-block:: postgres

   SET inListJoinMaxMetadataRanges = 64;

For the three forms an ``IN`` list is compiled into, and where this flag applies among them, see
:ref:`Compiling IN Lists<compiling_in_lists>`.
