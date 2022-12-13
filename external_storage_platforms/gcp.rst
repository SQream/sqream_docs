.. _gcp:

***********************
Ingesting Data Using Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires GCP bucket access configurations. You may configure BLUE to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket is individually configured.    

.. contents::
   :local:
   
Granting access to GCP
======================

1. In your Google console, go to **Select a project** and select the desired project.
2. From the **PRODUCTS** menu select **Cloud Storage**.
3. Under the **Cloud Storage** menu, select **Buckets*.
4. Select the bucket you wish to configure or otherwise create a new bucket by selecting **CREATE**, follow the **Create a bucket** procedure, and select the newly created bucket.
5. Select **UPLOAD FILES** and upload the data files you wish to grant BLUE access to.
6. Go to **PERMISSIONS** and select **GRANT ACCESS**.
7. Under **Add principals**, in the **New principals** box, paste the following string:

.. code-block:: console

   tf-gke-blue-appnext-pr-gcv6@blue-appnext-prod-sandbox.iam.gserviceaccount.com
   
7. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.
8. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.
9. Select **SAVE**

.. note:: To minimize access time to your data, configure bucket location to **us-east-1**. If not possible, please contact SQream help desk.

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

   

Example
==============
The following is an example of the syntax used for verifying that your GCP is shared with your SQream cluster:

.. code-block:: console

   
 
Output
==============
The following is an example of the output generated from verifying that your GCP is shared with your SQream cluster:

.. code-block:: console

 

The following is displayed:

.. code-block:: console

  
   
When you have finished mounting your GCP shared drives on your SQream cluster, you can use them with :ref:`copy_from` or :ref:`copy_to` statements, as shown in the following example:

.. code-block:: console

   
   
