.. _flexible_data_clustering_chunks:

***********************
What are Chunks?
***********************
Chunks, sometimes referred to as **partitions**, are a contiguous number of rows in a specific column. SQream relies on an advanced partitioning method called **chunking**, which provides all static partitioning capabilities without the known limitations.

The following figure shows a table rows grouped as chunks:

.. figure:: /_static/images/chunking2.png
   :scale: 75 %
   :align: center
   
The following figure shows the rows from the table above converted into chunks:
   
.. figure:: /_static/images/chunking_metadata2.png
   :scale: 75 %
   :align: center