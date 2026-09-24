:orphan:

.. _in_list_join_threshold:

**********************************
Setting the IN List Join Threshold
**********************************
The ``inListJoinThreshold`` flag sets the number of values above which an ``IN`` list is compiled as an inner join
against the listed values, instead of being expanded into a chain of equality comparisons.

Large ``IN`` lists compile faster as a join, because a join is a single hash lookup while the comparison chain grows
with both the number of values and the number of rows. Lowering the threshold applies the join form to smaller lists,
and raising it keeps the comparison form for larger ones.

The following describes the ``inListJoinThreshold`` flag:

* **Data type** - int
* **Default value** - ``100``
* **Allowed values** - Any positive integer

The join form applies to an ``IN`` list used as a filter condition, where a value that does not match drops the
row. An ``IN`` used elsewhere in a statement keeps the comparison form regardless of this flag, as do lists of
``ARRAY``, ``BLOB``, ``INTERVAL``, and ``DATETIME2`` values, which cannot serve as a join key.

The flag may be set for the session:

.. code-block:: postgres

   SET inListJoinThreshold = 50;
