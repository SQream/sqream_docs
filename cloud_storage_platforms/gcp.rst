.. _gcp:

******************************************
Google Cloud Platform
******************************************

Ingesting data using Google Cloud Platform (GCP) requires configuring Google Cloud Storage (GCS) bucket access. You may configure BLUE to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket be individually configured.    
   
Before You Begin   
================  

It is essential that you have a GCP service account string.

String example:

.. code-block:: console

	sample_service_account@sample_project.iam.gserviceaccount.com
 
Granting GCP access
===================

Optimize access time to your data by configuring the location of your bucket according to `Google Cloud location considerations. <https://cloud.google.com/storage/docs/locations#location-r>`_

#. In your Google cloud console, go to **Select a project** and select the desired project.

#. From the **PRODUCTS** menu, select **Cloud Storage** > **Buckets**.

#. Select the bucket you wish to configure; or create a new bucket by selecting **CREATE** and following the **Create a bucket** procedure, and select the newly created bucket.

#. Select **UPLOAD FILES** and upload the data files you wish BLUE to ingest.

#. Go to **PERMISSIONS** and select **GRANT ACCESS**.

#. Under **Add principals**, in the **New principals** box, paste your service account string.

#. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.

#. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.

#. Select **SAVE**.


Examples
========

Creating a ``FOREIGN TABLE``:

.. code-block:: postgres

	CREATE or REPLACE FOREIGN TABLE "public"."nba"
	WRAPPER
	  csv_fdw
	OPTIONS
	  (LOCATION = 'gs://blue_docs/nba.csv');
	  
Executing a ``COPY TO`` command:

.. code-block:: postgres

	COPY
	  nba TO
	WRAPPER
	  csv_fdw
	OPTIONS
	  (
	    LOCATION = 'gs://blue_docs/nba.csv',
	    DELIMITER = '\t',
	    HEADER = true
	  );
  
