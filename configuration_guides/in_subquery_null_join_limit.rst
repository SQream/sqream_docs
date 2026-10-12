:orphan:

.. _in_subquery_null_join_limit:

***************************************
Setting the IN Subquery Null Join Limit
***************************************
The ``inSubqueryNullJoinLimit`` flag sets the largest number of joins that a single ``IN`` or ``NOT IN`` over a
subquery may be compiled into.

An ``IN`` or ``NOT IN`` over columns declared ``NOT NULL`` compiles into a single join. Where a compared column can be
``NULL``, on either side of the ``IN``, a ``NULL`` may match any value, and every such column doubles the number of
joins needed to give a correct result. Comparing three nullable columns takes eight joins, and four takes sixteen.
The limit stops a statement from compiling into an ever wider plan; a statement over it fails with the following error:

.. code-block:: none

   This IN with a subquery needs 16 joins, more than inSubqueryNullJoinLimit (8) allows: every compared column that can be NULL on either side doubles them

The following describes the ``inSubqueryNullJoinLimit`` flag:

* **Data type** - int
* **Default value** - ``8``
* **Allowed values** - Any positive integer

Raising the limit lets the statement run, at the cost of the extra joins. Where the data allows it, declaring the
compared columns ``NOT NULL`` removes the extra joins altogether. See :ref:`in_subqueries`.

The flag may be set for the session:

.. code-block:: postgres

   SET inSubqueryNullJoinLimit = 16;
