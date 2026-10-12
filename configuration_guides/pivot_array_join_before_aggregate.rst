:orphan:

.. _pivot_array_join_before_aggregate:

*******************************************
Matching PIVOT ARRAY Values Before Grouping
*******************************************
The ``pivotArrayJoinBeforeAggregate`` flag changes the order of the two main steps of a
:ref:`PIVOT ARRAY<pivot_unpivot_array>` statement.

By default, ``PIVOT ARRAY`` first aggregates the source rows, then matches each group against the listed values, and
then sorts the result so that each group's rows arrive together before they are written into the array. With the flag
set, the rows are matched against the listed values first, and then aggregated. The aggregation already delivers each
group's rows together, so the sort is no longer needed.

Matching first also means that the pivoted column is grouped as a small integer position rather than as its own
type, which helps most when it is ``TEXT``, and that every value of a group outside the list collapses into one row.
The cost is that matching sees every source row instead of only the aggregated ones. Whether the trade pays off
depends on the data, so compare a statement with the flag on and off before relying on it.

The following describes the ``pivotArrayJoinBeforeAggregate`` flag:

* **Data type** - bool
* **Default value** - ``false``
* **Allowed values** - ``true``, ``false``

The flag affects ``PIVOT ARRAY`` with an aggregation only. It has no effect on ``PIVOT``, or on
``PIVOT DISTINCT ARRAY``, which does not aggregate. The result of a statement is the same whether the flag is on or
off.

The flag may be set for the session:

.. code-block:: postgres

   SET pivotArrayJoinBeforeAggregate = true;
