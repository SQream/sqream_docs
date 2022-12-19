.. _gcp:

******************************************
Ingesting Data Using Google Cloud Platform
******************************************

Ingesting data using Google Cloud Platform (GCP) requires configuring Google Cloud Storage (GCS) bucket access. You may configure BLUE to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket be individually configured.    

.. contents::
   :local:
   
Granting GCP access
===================

	1. In your Google Cloud console, go to **Select a project** and select the desired project.
	1. From the **PRODUCTS** menu, select **Cloud Storage** > **Buckets**.
	1. Select the bucket you wish to configure or otherwise create a new bucket by selecting **CREATE**, follow the **Create a bucket** procedure, and select the newly created bucket.
	1. Select **UPLOAD FILES** and upload the data files you wish to grant BLUE access to.
	1. Go to **PERMISSIONS** and select **GRANT ACCESS**.
	1. Under **Add principals**, in the **New principals** box, paste the following string:

		.. code-block:: postgres

		   sample_service_account@sample_project.iam.gserviceaccount.com
   
	1. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.
	1. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.
	1. Select **SAVE**

	



.. note:: Optimize access time to your data by configuring the location of your bucket according to `Google Cloud location considerations. <https://cloud.google.com/storage/docs/locations#location-r>`_

   

Example
=======
The following is an example of the syntax used for executing a ``CREATE FOREIGN TABLE`` statement:

.. code-block:: postgres

	CREATE or REPLACE FOREIGN TABLE "public"."transactions_fh_json"
	wrapper
	  json_fdw
	options
	  (location = 'gs://<gcs path>/<gcs_bucket>/*');
  