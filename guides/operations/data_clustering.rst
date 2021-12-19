.. _data_clustering:

***********************
Data clustering
***********************

Together with the :ref:`chunking<chunks_and_extents>` and :ref:`metadata_system`, SQream DB uses information to execute queries efficiently.

SQream DB automatically collects metadata on incoming data. This works well when the data is naturally ordered (e.g. :ref:`with time-based data<time_based_data_management>`).

There are situations where you know more about the incoming data than SQream DB. If you help by defining **clustering keys**, SQream DB can automatically improve query processing. SQream DB's query optimizer typically selects the most efficient method when executing queries. If no clustering keys are available, it may have to scan tables physically.

Clustered tables
======================

A table is considered "clustered" by one or more clustering keys if rows containing similar values with regard to these expressions are more likely to be located together on disk.

For example, a table containing a date column whose values cover a whole month but each chunk on disk covers less than a specific day is considered clustered by this column. 

Good clustering has a significant positive impact on query performance.

When does clustering help?
===================================

When a table is well-clustered, the metadata collected for each chunk is much more effective (the ranges are more localized).

In turn, SQream DB's query engine chooses to read fewer irrelevant chunks (or just avoid processing them).

Here are some common scenarios in which data clustering is beneficial:

* 
   When a query contains a ``WHERE`` predicate of the form ``column COMPARISON value``.
   For example, ``date_column > '2019-01-01'`` or  ``id = 107`` and the columns referenced are clustering keys/
   
   SQream DB will only read the portion of the data containing values matching these predicates.

* When two clustered tables are joined on their respective clustering keys, SQream DB will utilize the metadata to identify the matching chunks more easily.


Controlling data clustering
=================================

Some tables are naturally clustered. For example - a call log table containing CDRs can be naturally clustered by call date if data is inserted as it is generated, or bulk loaded in batches. Data can also be clustered by a region ID, per city, or customer type, depending on the source.


If the incoming data is not well-clustered (by the desired key), it is possible to tell SQream DB which keys it should cluster by.

This can be done upon table creation (:ref:`create_table`), or retroactively (:ref:`cluster_by`). New data will be clustered upon insert.

When data is loaded to an explicitly clustered table, SQream DB partially sorts it. While this slows down the insert time, it is often beneficial for subsequent queries.

.. note:: 

   Some queries significantly benefit from the decision to use clustering. 
   For example, queries that filter or join extensively on clustered columns will benefit.  
   
   
   However, clustering can slow down data insertion. Some insert workloads can be up to 75% slower.
   
   If you are not sure whether or not a specific scenario will benefit from clustering, we recommended testing end-to-end (both insert and query performance) on a small subset of the data before commiting to permanent clustering keys.


Examples
==========

Creating a clustered table
-----------------------------

Even when the table is naturally ordered by ``start_date``, we can specify a cluster key that is different. This will likely improve performance for queries that order by or rely on users' ``country``.

.. code-block:: postgres

   CREATE TABLE users (
      name VARCHAR(30) NOT NULL,
      start_date datetime not null,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY country;


