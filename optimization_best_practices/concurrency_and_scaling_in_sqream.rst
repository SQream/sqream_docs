.. _concurrency_and_scaling_in_sqream:

*******************************
Concurrency and Scaling in BLUE
*******************************

A BLUE cluster can concurrently run one regular statement per worker process. A number of small statements will execute alongside these statements without waiting or blocking anything.

BLUE supports ``n`` concurrent statements by having ``n`` workers in a cluster. Each worker uses a fixed slice of a GPU's memory, with usual values are around 8-16GB of GPU memory per worker. This size is ideal for queries running on large data with potentially large row sizes.

Scaling when data sizes grow
----------------------------

For many statements, BLUE scales linearly when adding more storage and querying on large data sets. It uses very optimised 'brute force' algorithms and implementations, which don't suffer from sudden performance cliffs at larger data sizes.

Scaling when queries are queueing
---------------------------------

BLUE scales well by adding more workers, GPUs, and nodes to support more concurrent statements.

What to do when queries are slow
--------------------------------

To boost statement performance, start by examining the :ref:`best practices<sql_best_practices>` and ensure the guidelines are followed.

.. rubric:: Need help?

Analyzing complex workloads can be challenging. BLUE's experienced customer support has the experience to advise on these matters to ensure the best experience.

Contact BLUE support at `blue_support@sqreamtech.com <blue_support@sqreamtech.com>`_
