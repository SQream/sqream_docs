.. _compiling_in_lists:

******************
Compiling IN Lists
******************

An ``IN`` list is written the same way whatever its length, but SQreamDB does not compile every
list the same way. A list of five values and a list of fifty thousand values are different
problems, and the compiler picks one of three forms for each. This page describes the three
forms, how the compiler chooses between them, what each one costs, and the flags that move the
boundaries.

.. contents::
   :local:
   :depth: 1

Why the form matters
====================

A filter such as ``WHERE x IN (...)`` has to answer one question per row: is this row's value one
of the listed values? The cost of answering it depends on how the condition is compiled, and the
difference grows with both the length of the list and the size of the table.

The form also decides whether the scan can skip chunks. A filter that keeps its metadata filters
prunes chunks before reading them, so the query reads less from disk. A filter that loses them
reads the whole table and discards most of it. On a large table this is usually a larger effect
than the per-row cost.

The three forms
===============

Comparison chain
----------------

The default form for a short list. The list becomes a chain of equality comparisons:

.. code-block:: postgres

   x IN (3, 7, 11)
   -- compiled as
   x = 3 OR x = 7 OR x = 11

Each value costs one comparison on every row, so the work is the number of values multiplied by
the number of rows. That is cheap for a short list and expensive for a long one.

Inner join
----------

Past :ref:`inListJoinThreshold<in_list_join_threshold>`, the list becomes an inner join against
the values:

.. code-block:: postgres

   SELECT * FROM t WHERE x IN (1, 2, ..., 100000)
   -- compiled as
   SELECT t.* FROM t
     INNER JOIN (VALUES (1), ..., (100000)) v (in_list_value_0) ON x = in_list_value_0
     WHERE x >= 1 AND x <= 100000

A join is a hash lookup, so its cost per row does not grow with the length of the list. The
bounds on the last line are kept deliberately: they are what lets the scan prune chunks once the
list itself has moved into the join.

A multi-column list such as ``(x, y) IN ((1, 2), (3, 4), ...)`` joins on one key per column,
against one value column per subject.

Range
-----

A list of nearly consecutive ``INT`` or ``DATE`` values becomes the range it spans:

.. code-block:: postgres

   x IN (3, 4, 5, ..., 40)             -- compiled as  x >= 3 AND x <= 40
   x = 3 OR x = 4 OR ... OR x = 40     -- compiled as  x >= 3 AND x <= 40
   x IN (3, 4, 6, ..., 40)             -- compiled as  x >= 3 AND x <= 40 AND NOT (x IN (5))

A range costs two comparisons per row, however many values it covers. Any value missing from
inside the range stays in the condition as its own comparison, because the bounds alone would let
it through, so a sparse range costs more than a dense one.

This form applies to integer and date columns only. Those are the types where the values lying
between two others are a known set, which is what makes the rewrite safe.

How the compiler chooses
========================

The three forms are decided in this order:

#. **A dense list of integer or date values becomes a range**, from
   :ref:`inListRangeMinValues<in_list_range_min_values>` distinct values upwards. This is decided
   before the join form, so a list long enough to join becomes a range instead when it is dense
   enough to qualify.
#. **Otherwise, a list past the threshold becomes a join**, where the threshold is
   :ref:`inListJoinThreshold<in_list_join_threshold>`.
#. **Otherwise the list stays a comparison chain.**

The threshold counts comparisons, not values. For a list on a single column the two are the same,
but a multi-column list costs one comparison per column in each row, so the compiler divides the
threshold by the number of columns. With the default of ``100``, a two-column list is compiled as
a join once it has more than ``50`` rows. See :ref:`in_subqueries`.

How dense is dense enough
-------------------------

Two flags bound how many values may be missing from a range:

* :ref:`inListRangeMaxMissingPercent<in_list_range_max_missing_percent>` caps the missing values
  as a percentage of the range. Whatever it allows, the values missing are never as many as the
  values present.
* :ref:`inListRangeMissingMultiplier<in_list_range_missing_multiplier>` caps them against
  ``inListJoinThreshold``: the missing values, multiplied by this flag, may not exceed the
  threshold. Past the threshold the list would have been a join, which costs no comparison per
  value, while each missing value in a range does.

A set with wide gaps stays a list. Under an ``OR``, several ranges would multiply out when the
statement is put into conjunctive normal form, so a range beside another condition in its ``OR``
takes holes only while the result stays within the conjunctive normal form limit. Past that limit
the statement would lose its metadata filters, which costs more than the range form saves.

Chunk skipping
==============

When a list is compiled as a join, the list itself is no longer on the scan, but the information
needed to skip chunks is kept behind as metadata filters. Two things stay on the scan:

* **The bounds**, ``x >= min AND x <= max``, which skip any chunk lying entirely outside them.
* **The values**, as one metadata filter per value, which skip a chunk holding none of them. The
  scan evaluates these with a single binary search per chunk.

Per-value filters are kept for up to
:ref:`inListJoinMaxMetadataFilters<in_list_join_max_metadata_filters>` distinct values per column.
They are the only pruning a ``TEXT`` key gets.

Past that limit, keeping one filter per value costs more than it saves, so the column's values are
covered by at most :ref:`inListJoinMaxMetadataRanges<in_list_join_max_metadata_ranges>` ranges
instead, split at the widest gaps between them. The scan then skips a chunk falling between two of
the ranges. Each range past the first costs two comparisons per chunk.

Chunk skipping applies to ``INT``, ``FLOAT``, ``NUMERIC``, ``DATE``, ``DATETIME`` and ``TEXT``
columns. It prunes most when the table is clustered on the column the list filters.
See :ref:`accelerating_filtered_statements` and
:ref:`skipChunksUsingDictColumn<skip_chunks_using_dict_column>`.

When the rewrites do not apply
==============================

Filter position only
--------------------

A list is rewritten only where it is a filter condition, meaning a conjunct of a ``WHERE``. There
a value that does not match drops the row, and ``NULL`` drops it too, so the join agrees with
``IN``. In any other position ``IN`` yields ``NULL`` rather than dropping a row, and a join would
not give the same answer, so the list keeps its comparison form.

Column types
------------

The join form needs a key the runtime can compare exactly:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Type
     - Compiled as a join
   * - ``BOOL``, ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``, ``REAL``, ``DOUBLE``, ``NUMERIC``, ``DATE``, ``DATETIME``
     - Yes
   * - ``TEXT``
     - Only when ``useCrcForTextJoinKeys`` is enabled, which is what makes a text key joinable
   * - ``ARRAY``, ``BLOB``, ``DATETIME2``
     - No. These cannot serve as a join key, so the list keeps its comparison form

Values the list cannot carry into a join
----------------------------------------

Before building the join the compiler converts every value to the column's type. Along the way:

* **Rows holding** ``NULL`` **are dropped.** A null satisfies neither the join nor ``IN``.
* **Duplicate values are removed.** A duplicate key would multiply the rows it matches.
* **A value that does not fit the column's type abandons the rewrite**, leaving the list as a
  comparison chain. It does not fail the statement: a comparison against an out-of-range value is
  folded away quietly, and failing here would reject a statement that used to work.

Configuration flags
===================

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Flag
     - Default
     - Controls
   * - :ref:`inListJoinThreshold<in_list_join_threshold>`
     - ``100``
     - The number of comparisons above which a list is compiled as an inner join
   * - :ref:`inListJoinMaxMetadataFilters<in_list_join_max_metadata_filters>`
     - ``1000``
     - How many distinct values per column are kept as per-value metadata filters
   * - :ref:`inListJoinMaxMetadataRanges<in_list_join_max_metadata_ranges>`
     - ``32``
     - How many ranges are kept once the per-value limit is passed
   * - :ref:`inListRangeMinValues<in_list_range_min_values>`
     - ``20``
     - The number of distinct values from which a dense list is compiled as a range
   * - :ref:`inListRangeMaxMissingPercent<in_list_range_max_missing_percent>`
     - ``10``
     - The share of a range, as a percentage, that may be missing
   * - :ref:`inListRangeMissingMultiplier<in_list_range_missing_multiplier>`
     - ``2``
     - The missing values of a range, against ``inListJoinThreshold``

Each flag may be set for the session:

.. code-block:: postgres

   SET inListJoinThreshold = 50;

Tuning
======

The defaults suit most workloads, and these flags are worth moving only against a measurement.

Before changing anything, look at the execution plan. A list compiled as a join shows the join in
the plan, and the rows the scan produced show whether chunks were skipped. See
:ref:`monitoring_query_performance`.

Lowering ``inListJoinThreshold`` applies the join form to shorter lists, and raising it keeps the
comparison form for longer ones. Lowering it far affects every query on the system, not only the
one being tuned, which is the usual way this flag causes trouble: a threshold chosen for one
long-list query turns short lists elsewhere into joins that cost more than they save.

Raising ``inListJoinMaxMetadataFilters`` keeps exact per-value pruning for longer lists, at one
binary search per chunk. Lowering it moves to the cheaper range form sooner, which prunes less but
costs less per chunk.

Setting a flag to ``0`` turns its mechanism off, which is the quickest way to find out whether
that mechanism is responsible for a regression:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Setting
     - Effect
   * - ``SET inListJoinMaxMetadataFilters = 0``
     - No per-value filters, leaving only the ranges
   * - ``SET inListJoinMaxMetadataRanges = 0``
     - No ranges, so no chunk skipping past the per-value limit
   * - ``SET inListRangeMinValues = 0``
     - No range form, so lists stay lists or become joins
   * - ``SET inListRangeMissingMultiplier = 0``
     - Lifts the cap on missing values, leaving only ``inListRangeMaxMissingPercent``

See also
========

* :ref:`accelerating_filtered_statements` - chunk indexes, and how filtered statements prune chunks
* :ref:`in_subqueries` - ``IN`` over a subquery, and
  :ref:`inSubqueryNullJoinLimit<in_subquery_null_join_limit>`
* :ref:`Joins<inner_joins>` - the join form this rewrite produces
* :ref:`Optimization and Best Practices<sql_best_practices>` - general query tuning
