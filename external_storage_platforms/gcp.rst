.. _gcp:

***********************
Ingesting Data Using Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires that BLUE is granted read and/or write access to a GCP bucket. You may configure BLUE to separate between source and destination by granting read access to one bucket and write access to a different bucket. If you choose to separate between source and destination, it is required to configure each bucket individually.    

.. contents::
   :local:
   
Granting access to GCP
======================

1. In your Google console, go to **Your Account** and select the desired project.
2. Under **Cloud Storage**, select **Buckets*.
3. Select the bucket you wish to configure or otherwise create a bucket:
	a. Hit **CREATE**, name the bucket, and specify its location.
	b. Hit **Confirm**.
4. Select the bucket you wish to grant access to and hit **UPLOAD FILES**.
5. Under **Bucket details**, select **PERMISSIONS** and then **GRANT ACCESS**.
6. Under **NEW PRINCIPALS** attach the following string:

.. code-block:: console

   tf-gke-blue-appnext-pr-gcv6@blue-appnext-prod-sandbox.iam.gserviceaccount.com
7. Under **Assign roles**, select **Select role** and configure **Storage Admin**.
8. Hit **save**


Script Input Parameters
=======================
The following list describes the script input parameters for verifying that your GCP is shared with your SQream cluster:

* **The GCP server IP address** - The IP address of the GCP server.

   ::
   
* **The GCP directory path** - The mount directory path used for copying data from external sources or exporting data.

For more information, see the following:

 * :ref:`copy_from`
 
    ::
	
 * :ref:`copy_to`

Syntax
==============
The following is an example of the syntax used for executing the script:

.. code-block:: console

   $ ./update-gcp-share.sh <GCP server IP address> <shared folder path>

Example
==============
The following is an example of the syntax used for verifying that your GCP is shared with your SQream cluster:

.. code-block:: console

   $ ./update-gcp-share.sh 192.168.4.28 /mnt/shares/csv
 
Output
==============
The following is an example of the output generated from verifying that your GCP is shared with your SQream cluster:

.. code-block:: console

   --------------------------------------------------------------------------------
   --This script will add customer gcp shares (folders) to sqream GPU worker pods--
   --------------------------------------------------------------------------------
   --Important! Mapping new GCP share requires cluster services restart - any running statements will be terminated!
   --You have requested to mount folder /mnt/shares/csv for gcp server 192.168.4.28 - Please confirm all details correct and you wish to proceed Y / N?
   
If the mounting destination folder above is correct and you wish to proceed, press ``Y``.

The following is displayed:

.. code-block:: console

   --Mounting gcp server - 192.168.4.28 & folder /mnt/shares/csv
   --Creating templates folder
   --Deployment to patch is sqream-worker-0, patching deployment with added folders
   deployment.apps/sqream-worker-0 patched
   --Deployment patched successfully! :-)
   
When you have finished mounting your GCP shared drives on your SQream cluster, you can use them with :ref:`copy_from` or :ref:`copy_to` statements, as shown in the following example:

.. code-block:: console

   $ COPY table1 from wrapper csv_fdw options (location = '/mnt/gcp_shares/csv/t_a.csv' , quote='@');
   
