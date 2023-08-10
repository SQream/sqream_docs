.. _concurrency_and_scaling_in_sqream:

***********************************
Concurrency and Scaling in SQreamDB
***********************************

A SQreamDB cluster can concurrently run one regular statement per worker process. A number of small statements will execute alongside these statements without waiting or blocking anything.

SQreamDB supports ``n`` concurrent statements by having ``n`` workers in a cluster. Each worker uses a fixed slice of a GPU's memory, with usual values are around 8-16GB of GPU memory per worker. This size is ideal for queries running on large data with potentially large row sizes.

Scaling When Data Sizes Grow
----------------------------

For many statements, SQreamDB scales linearly when adding more storage and querying on large data sets. It uses very optimised 'brute force' algorithms and implementations, which don't suffer from sudden performance cliffs at larger data sizes.

Scaling When Queries Are Queuing
--------------------------------

SQreamDB scales well by adding more workers, GPUs, and nodes to support more concurrent statements.

What To Do When Queries Are Slow
--------------------------------

Adding more workers or GPUs does not boost the performance of a single statement or query. 

To boost the performance of a single statement, start by examining the :ref:`best practices<sql_best_practices>` and ensure the guidelines are followed.

Adding additional RAM to nodes, using more GPU memory, and faster CPUs or storage can also sometimes help.

.. rubric:: Need help?

Analyzing complex workloads can be challenging. SQreamDB's experienced customer support has the experience to advise on these matters to ensure the best experience.

Visit `SQreamDB Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_ for additional information.
