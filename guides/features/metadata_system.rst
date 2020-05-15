.. _metadata_system:

***********************
Metadata system
***********************

SQream DB contains a transparent and automatic system that collects metadata describing each :ref:`chunk<chunks_and_extents>`.

The collected metadata enables effective skipping of chunks and extents when queries are executed. 

How is metadata collected?
==============================

When data is inserted into SQream DB, the load process splits data into chunks.

Several parameters are collected and stored for later use, including:

* Range of values for each column chunk (minimum, maximum)
* The number of values
* Additional information for query optimization

Data is collected automatically and transparently on every column type.

.. figure:: /_static/images/chunking.png
   
   Chunks are collections of rows from a column

.. figure:: /_static/images/chunking_metadata.png

   Metadata is automatically added to each chunk


How is metadata used?
===========================

Chunk metadata is collected for identifying column values and potentially skipping accessing them, to reduce unnecessary I/O operations. For example, when a query specifies a filter (e.g. ``WHERE`` or ``JOIN`` condition) on a range of values that spans a fraction of the table values, SQream DB will optimally scan only that fraction of the table chunks.

Queries that filter on fine-grained date and time ranges will be the most effective, particularly when :ref:`data is timestamped<time_based_data_management>`, and when tables contain a large amount of historical data.

Why is metadata always on?
=============================

Metadata collection adds very little overhead to data load. WHen possible, most metadata collection is performed in the GPU.

Metadata is collected for every chunk, and adds a handful of kilobytes at most per million values, and very few compute cycles.

At scale, metadata collection is often negligible, resulting in a 0.005% overhead.

For a 10TB dataset, the metadata storage overhead is estimated at 0.5GB.

Because SQream DB's metadata collection is so light-weight and often results in effective data skipping, it is always-on.


.. show the metadata system in action:
.. describe a scenario
.. show a statement which is accelerated via the metadata system
.. do this for a bunch of variants

.. * where
.. * count
.. * delete support

.. collects size, and min and max metadata per chunk and extent, for
.. every column

.. can easily skip reading chunks and extents when running statements
.. with the right shape

.. this is cheap to do, and cheap to store, and it is always on

.. best practice notes

