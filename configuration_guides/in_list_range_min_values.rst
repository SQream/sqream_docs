:orphan:

.. _in_list_range_min_values:

****************************************
Setting the IN List Range Minimum Values
****************************************
The ``inListRangeMinValues`` flag sets the number of distinct values from which an ``IN`` list, or a chain of equality
comparisons, on a nearly consecutive ``INT`` or ``DATE`` column is compiled as the range its values span.

A dense list of values is cheaper to evaluate as a pair of bounds than as a list or a join. Any values missing from
inside the range stay in the condition as individual comparisons, governed by
:ref:`inListRangeMaxMissingPercent<in_list_range_max_missing_percent>` and
:ref:`inListRangeMissingMultiplier<in_list_range_missing_multiplier>`.

The following describes the ``inListRangeMinValues`` flag:

* **Data type** - int
* **Default value** - ``20``
* **Allowed values** - ``0`` or any positive integer

Setting the flag to ``0`` turns off compilation as a range.

The flag may be set for the session:

.. code-block:: postgres

   SET inListRangeMinValues = 50;

For the three forms an ``IN`` list is compiled into, and where this flag applies among them, see
:ref:`Compiling IN Lists<compiling_in_lists>`.
