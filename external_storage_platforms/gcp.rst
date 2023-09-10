.. _gcp:

***********************
Google Cloud Platform
***********************

Google Cloud Platform (GCP) offers a robust and scalable cloud infrastructure for various computing and data storage needs.


Google Cloud Platform URI Format
=================================

Specify a location for a file (or files) when using :ref:`copy_from` or :ref:`foreign_tables`.

The following is an example of the general GCP syntax:

.. code-block:: console
 
	gs://<gcs path>/<gcs_bucket>/
   
Example
============

.. code-block::

	COPY table_name FROM WRAPPER csv_fdw OPTIONS(location = 'gs://mybucket/sqream-demo-data/file.csv');
    
