.. _flexible_data_clustering_data_rechunking_data:

***********************
Rechunking Data
***********************
SQream performs background storage reorganization operations to optimize I/O and read patterns.

For example, when small batches of data are inserted, SQream runs two background processes called **rechunk** and **reextent** to reorganize the data into larger contiguous chunks and extents. This is also what happens when data is deleted.


Instead of overwriting data, SQream writes new optimized chunks and extents to replace old ones. After rewriting all old data, SQream switches to the new optimized chunks and extents and deletes the old data.