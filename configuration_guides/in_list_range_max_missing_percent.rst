:orphan:

.. _in_list_range_max_missing_percent:

*************************************************
Setting the IN List Range Maximum Missing Percent
*************************************************
The ``inListRangeMaxMissingPercent`` flag sets the share of a range, as a percentage, that may be missing from a list
compiled as a range by :ref:`inListRangeMinValues<in_list_range_min_values>`.

Each missing value stays in the condition as its own comparison, so a sparser range costs more to evaluate. Whatever
this flag allows, the values missing from a range are never as many as the values present in it.

The following describes the ``inListRangeMaxMissingPercent`` flag:

* **Data type** - int
* **Default value** - ``10``
* **Allowed values** - ``0`` to ``100``

Setting the flag to ``0`` compiles a list as a range only when no values are missing between its bounds.

The flag may be set for the session:

.. code-block:: postgres

   SET inListRangeMaxMissingPercent = 25;

For the three forms an ``IN`` list is compiled into, and where this flag applies among them, see
:ref:`Compiling IN Lists<compiling_in_lists>`.
