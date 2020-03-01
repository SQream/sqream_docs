.. _concurrency_and_scaling_in_sqream:

***************************************
Concurrency and scaling in SQream DB
***************************************

A SQream DB cluster can concurrently run one regular statement per worker process. A number of small statements will execute alongside these statements without waiting or blocking anything. 

SQream DB supports ``n`` concurrent statements by having ``n`` workers in a cluster. Each worker uses a fixed slice of a GPU's memory, with usual values are around 8-16GB of GPU memory per worker. This size is ideal for queries running on large data with potentially large row sizes.

Scaling when data sizes grow
--------------------------------

For many statements, SQream DB scales linearly when adding more storage and querying on large data sets. It uses very optimised 'brute force' algorithms and implementations, which don't suffer from sudden performance cliffs at larger data sizes.

Scaling when queries are queueing
---------------------------------------

SQream DB scales well by adding more workers, GPUs, and nodes to support more concurrent statements.

What to do when queries are slow
----------------------------------

Adding more workers or GPUs does not boost the performance of a single statement or query. 

To boost the performance of a single statement, start by examining the :ref:`best practices<sql_best_practices>` and ensure the guidelines are followed.

.. TODO: we have a lot of techniques to speed up statements which aren't ready for customers to use without support - add something here and in the best practices about this

Adding additional RAM to nodes, using more GPU memory, and faster CPUs or storage can also sometimes help.

.. rubric:: Need help?

Analyzing complex workloads can be challenging. SQream's experienced customer support has the experience to advise on these matters to ensure the best experience.

Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.
