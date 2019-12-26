.. _concurrency_and_scaling_in_sqream:

***************************************
Concurrency and scaling in SQream DB
***************************************

The number of queries that a SQream DB cluster can process is determined by the complexity of the workload and the size of the cluster. 

In general, SQream DB supports ``n`` concurrent statements by having ``n`` workers in a cluster. Each worker uses a fixed slice of a GPU's memory, with usual values are around 8-16GB of GPU memory per worker.

Scaling when data sizes grow
--------------------------------

SQream DB scales well by adding more storage and querying on large data sets - more or less linearly.

Scaling when queries are queueing
---------------------------------------

SQream DB scales well by adding more workers, GPUs, and finally nodes to support more concurrent statements.

What to do when queries are slow
----------------------------------

Adding more workers or GPUs does not boost the performance of a single statement or query. 

To boost the performance of a single statement, start by examining the :ref:`best practices<sql_best_practices>` and ensure the guidelines are followed.

Adding additional RAM to nodes, using more GPU memory, and faster CPUs or storage can also help.



.. rubric:: Need help?

   Analyzing complex workloads can be challenging. SQream's experienced customer support has the experience to advise on these matters to ensure the best experience.

   Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.