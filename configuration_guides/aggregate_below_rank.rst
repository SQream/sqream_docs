:orphan:

.. _aggregate_below_rank:

*****************************
Setting Aggregate Below Rank
*****************************
The ``aggregateBelowRank`` flag lets the compiler place an aggregation below a rank window function, so that the
window sorts groups rather than individual rows. The aggregation above the window then merges the partial results.

A dense rank depends on a row's partition and order values, and on the distinct order values within its partition.
Grouping by all of them preserves each row's rank, so the result is unchanged while the window has fewer rows to sort.

The following describes the ``aggregateBelowRank`` flag:

* **Data type** - boolean
* **Default value** - ``FALSE``
* **Allowed values** - ``TRUE``, ``FALSE``

The flag is off by default because the compiler cannot tell in advance how many groups the lower aggregation will
produce. When the groups are as many as the rows, the lower aggregation removes nothing and is pure overhead. Turn the
flag on for a query that aggregates many rows into few groups under a rank window, and compare the run time with it
off.

The flag may be set for the session:

.. code-block:: postgres

   SET aggregateBelowRank = true;
