.. _gcp:

***********************
Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires configuring Google Cloud Storage (GCS) bucket access. You may configure SQreamDB to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket be individually configured.


GCP Bucket File Location
=================================

GCP syntax to be used for specifying a single or multiple file location within a GCP bucket:

.. code-block:: sql
 
	gs://<gcs path>/<gcs_bucket>/
   
GCP Access
====================

Before You Begin
----------------

It is essential that you have a GCP service account string.

String example:

.. code-block::

	sample_service_account@sample_project.iam.gserviceaccount.com

Granting GCP Access
---------------------

#. In your Google Cloud console, go to **Select a project** and select the desired project.

#. From the **PRODUCTS** menu, select **Cloud Storage** > **Buckets**.

#. Select the bucket you wish to configure; or create a new bucket by selecting **CREATE** and following the **Create a bucket** procedure, and select the newly created bucket.

#. Select **UPLOAD FILES** and upload the data files you wish SQreamDB to ingest.

#. Go to **PERMISSIONS** and select **GRANT ACCESS**.

#. Under **Add principals**, in the **New principals** box, paste your service account string.

#. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.

#. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.

#. Select **SAVE**.

.. note::

	Optimize access time to your data by configuring the location of your bucket according to `Google Cloud location considerations <https://cloud.google.com/storage/docs/locations#location-r>`_.
   
   
   
Examples
============

Using the ``COPY FROM`` command:

.. code-block:: sql

	CREATE TABLE nba
	  (
	    name     TEXT,
	    team     TEXT,
	    number   TEXT,
	    position TEXT,
	    age      TEXT,
	    height   TEXT,
	    weight   TEXT,
	    college  TEXT,
	    salary   TEXT
	  ); 

.. code-block:: sql

	COPY nba FROM
	WRAPPER csv_fdw
	OPTIONS(location = 'gs://blue_docs/nba.csv');
	
Using the ``CREATE FOREIGN TABLE`` command:

.. code-block:: sql

	CREATE FOREIGN TABLE nba
	(
	  Name       TEXT,
	  Team       TEXT,
	  Number     TEXT,
	  Position   TEXT,
	  Age        TEXT,
	  Height     TEXT,
	  Weight     TEXT,
	  College    TEXT,
	  Salary     TEXT
	 )
	 WRAPPER csv_fdw
	 OPTIONS
	 (
	   LOCATION =  'gs://blue_docs/nba.csv'
	 );
    
