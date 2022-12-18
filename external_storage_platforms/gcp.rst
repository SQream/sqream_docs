.. _gcp:

***********************
Ingesting Data Using Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires Google Cloud Storage (GCS) bucket access configurations. You may configure BLUE to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket is individually configured.    

.. contents::
   :local:
   
Granting GCP access
===================

1. In your Google console, go to **Select a project** and select the desired project.
2. From the **PRODUCTS** menu select **Cloud Storage**.
3. Under the **Cloud Storage** menu, select **Buckets**.
4. Select the bucket you wish to configure or otherwise create a new bucket by selecting **CREATE**, follow the **Create a bucket** procedure, and select the newly created bucket.
5. Select **UPLOAD FILES** and upload the data files you wish to grant BLUE access to.
6. Go to **PERMISSIONS** and select **GRANT ACCESS**.
7. Under **Add principals**, in the **New principals** box, paste the following string:

.. code-block:: postgres

   sample_service_account@sample_project.iam.gserviceaccount.com
   
8. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.
9. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.
10. Select **SAVE**

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
  