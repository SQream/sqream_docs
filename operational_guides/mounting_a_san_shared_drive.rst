.. _mounting_a_san_shared_drive:

**********************************
Mounting a SAN Shared Drive
**********************************
The **Mounting a SAN Shared Drive** page describes how to use your existing SAN share drives when reading data from or exporting to external files, and describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
==============   
SQream supports reading external tables and/or writing exported data to **SAN (Storage Area Network)** shared drives. Because SQream runs microservices as Dockerized containers, SAN shared drives must be mounted to the relevant Docker pods. Note that mounted shared drives are persistent. SQream provides a script used to map SAN shared drives. This script is called **update-san-share.sh** and is located in the ``utilities/sanshares/`` folder.

Script Prerequisites
==============
The following list describes the prerequisites required to run the **update-san-mountpoint.sh** script:

* Permissions to execute **kubectl** commands.

   ::
   
* Execution permissions (``chmod +x update-san-mountpoint.sh``).

   ::
   
* Verification that **SAN shared drive** is shared with your SQream cluster.

Script Input Parameters
==============
When verifying that your SAN is shared with your SQream cluster, you can use the **The SAN directory path** input parameter. This is used for mounting the directory path used for copying data from external sources or exporting data.

For more information, see the following:

 * :ref:`copy_from`
 
    ::
	
 * :ref:`copy_to`

Syntax
==============
The following is an example of the syntax used for executing the script:

.. code-block:: console

   $ ./update-san-mountpoint.sh <shared folder path>

Example
==============
The following is an example the syntax used for verifying that your SAN is shared with your SQream cluster:

.. code-block:: console

   $ ./update-san-mountpoint.sh /mnt/shares/csv
    
Output
==============
The following is an example of the output generated from verifying that your SAN is shared with your SQream cluster:

.. code-block:: console

   --------------------------------------------------------------------------------
   --This script will add customer SAN mountpoint (folder) to sqream GPU worker pods--
   --------------------------------------------------------------------------------
   --Please ensure the required folder has relevant permissions (reading/writing)--
   --------------------------------------------------------------------------------
   --Important! Mapping new mountpoint requires cluster services restart - any running statements will be terminated!
   --You have requested to mount folder /mnt/share/ - Please confirm all details correct and you wish to proceed Y / N?

If the mounting destination folder above is correct and you wish to proceed, press ``Y``.

The following is displayed:

.. code-block:: console

   --Mounting required folder /mnt/share/
   --Creating templates folder
   --Deployment to patch is sqream-worker-0, patching deployment with added folders
   --current revision is 1
   deployment.apps/sqream-worker-0 patched
   --Deployment patched with required parameters, validating deployment is running..
   deployment.apps/sqream-worker-0 annotated
   ---
   --Deployment is running successfully with required parameters!
   
When you have finished mounting your SAN shared drives on your SQream cluster, you can use them with **COPY FROM** or **COPY TO** statements, as shown in the following example:

.. code-block:: console

   $ COPY table1 from wrapper csv_fdw options (location = '/mnt/san_shares/csv/t_a.csv' , quote='@');