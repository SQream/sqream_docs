:orphan:

.. _in_list_range_missing_multiplier:

********************************************
Setting the IN List Range Missing Multiplier
********************************************
The ``inListRangeMissingMultiplier`` flag caps the values missing from a list compiled as a range by
:ref:`inListRangeMinValues<in_list_range_min_values>`, relative to
:ref:`inListJoinThreshold<in_list_join_threshold>`.

The values missing from the range, multiplied by this flag, may not exceed ``inListJoinThreshold``. Past that
threshold the list would otherwise have been compiled as a join, which costs no comparison per value, while each
missing value in a range does.

The following describes the ``inListRangeMissingMultiplier`` flag:

* **Data type** - int
* **Default value** - ``2``
* **Allowed values** - ``0`` or any positive integer

Setting the flag to ``0`` lifts the cap, leaving
:ref:`inListRangeMaxMissingPercent<in_list_range_max_missing_percent>` as the only limit on missing values.

The flag may be set for the session:

.. code-block:: postgres

   SET inListRangeMissingMultiplier = 4;

For the three forms an ``IN`` list is compiled into, and where this flag applies among them, see
:ref:`Compiling IN Lists<compiling_in_lists>`.
