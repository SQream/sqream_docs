.. _gcp:

***********************
Ingesting Data Using Google Cloud Platform
***********************

Ingesting data using Google Cloud Platform (GCP) requires GCP bucket access configurations. You may configure BLUE to separate source and destination by granting read access to one bucket and write access to a different bucket. Such separation requires that each bucket is individually configured.    

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

.. code-block:: console

   tf-gke-blue-appnext-pr-gcv6@blue-appnext-prod-sandbox.iam.gserviceaccount.com
   
8. Under **Assign roles**, in the **Select a role** box, select **Storage Admin**.
9. Select **ADD ANOTHER ROLE** and in the newly created **Select a role** box, select **Storage Object Admin**.
10. Select **SAVE**

.. note:: To minimize access time to your data, configure bucket location to **us-east-1**. If not possible, please contact SQream help desk.


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

   
   
