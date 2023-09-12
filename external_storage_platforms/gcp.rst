.. _gcp:

***********************
Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires configuring Google Cloud Storage (GCS) bucket access. You may configure SQreamDB to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket be individually configured.


Google Cloud Platform URI Format
=================================

Specify a location for a file (or files) when using :ref:`copy_from` or :ref:`foreign_tables`.

The following is an example of the general GCP syntax:

.. code-block:: console
 
	gs://<gcs path>/<gcs_bucket>/
   
Granting GCP access
====================

#. In your Google Cloud console, go to **Select a project** and select the desired project.

#. From the **PRODUCTS** menu, select **Cloud Storage** > **Buckets**.

#. Select the bucket you wish to configure; or create a new bucket by selecting **CREATE** and following the **Create a bucket** procedure, and select the newly created bucket.

#. Select **UPLOAD FILES** and upload the data files you wish SQreamDB to ingest.

#. Go to **PERMISSIONS** and select **GRANT ACCESS**.

#. Under **Add principals**, in the **New principals** box, paste the following string:

.. code-block::

	sample_service_account@sample_project.iam.gserviceaccount.com

7. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.

8. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.

9. Select **SAVE**.

.. note::

	Optimize access time to your data by configuring the location of your bucket according to `Google Cloud location considerations <https://cloud.google.com/storage/docs/locations#location-r>`_.
   
Example
============

.. code-block::

	COPY table_name FROM WRAPPER csv_fdw OPTIONS(location = 'gs://mybucket/sqream-demo-data/file.csv');
    
