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

* **Data type** - uint
* **Default value** - ``100``
* **Allowed values** - Any positive integer

The flag may be set for the session:

.. code-block:: postgres

   SET inListJoinThreshold = 50;
