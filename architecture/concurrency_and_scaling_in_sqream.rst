.. _concurrency_and_scaling_in_sqream:

*********************************
concurrency_and_scaling_in_sqream
*********************************

the basic concept:

we support n concurrent statements by having n workers on the cluster

a worker uses a fixed slice of a gpu, usual values are around 8-16GB
of gpu per worker

we scale well by adding more storage and querying on large values -
more or less linearly

we scale well by adding more gpus/nodes to add more concurrent
statements

to boost the performance of a single statement, start with the best
practices, do things like add more memory, faster io, better gpus,
more gpu mem

sqream can advise on these matters which can be complex, we can make
it simple



