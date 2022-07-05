.. _mounting_an_nfs_shared_drive:

**********************************
Mounting an NFS Shared Drive
**********************************
The **Mounting an NFS Shared Drive** page describes how to use your existing NFS share drives when reading data from or exporting to external files, and describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
==============   
SQream supports reading external tables and/or writing exported data to **NFS (Network File System)** shared drives. Because SQream runs microservices as Dockerized containers, NFS shared drives must be mounted to the relevant Docker pods. Note that mounted shared drives are persistent. SQream provides a script used to map NFS shared drives. This script is called **update-nfs-share.sh** and is located in the ``utilities/nfsshares/`` folder.

Script Prerequisites
==============
The following list describes the prerequisites required to run the **update-nfs-share.sh** script:

* Permissions to execute **kubectl** commands.

   ::
   
* Execution permissions (``chmod +x update-nfs-share.sh``).

   ::
   
* Verification that **NFS shared drive** is shared with your SQream cluster.

.. tip::  Using your NFS server IP address(es), you can run the following Linux command to verify that your NFS is shared with your SQream cluster:

          .. code-block:: console

             $ showmount -e 192.168.4.28
             >Export list for 192.168.4.28:
             >/mnt/shares/csv     192.168.4.0/24
             >/newdir/myshareddir 192.168.4.0/24
             >/mnt/myshareddir    192.168.4.0/24
	 
Script Input Parameters
==============
The following list describes the script input parameters for verifying that your NFS is shared with your SQream cluster:

* **The NFS server IP address** - The IP address of the NFS server.

   ::
   
* **The NFS directory path** - The mount directory path used for copying data from external sources or exporting data.

For more information, see the following:

 * :ref:`copy_from`
 
    ::
	
 * :ref:`copy_to`

Syntax
==============
The following is an example of the syntax used for executing the script:

.. code-block:: console

   $ ./update-nfs-share.sh <NFS server IP address> <shared folder path>

Example
==============
The following is an example the syntax used for verifying that your NFS is shared with your SQream cluster:

.. code-block:: console

   $ ./update-nfs-share.sh 192.168.4.28 /mnt/shares/csv
 
Output
==============
The following is an example of the output generated from verifying that your NFS is shared with your SQream cluster:

.. code-block:: console

   --------------------------------------------------------------------------------
   --This script will add customer nfs shares (folders) to sqream GPU worker pods--
   --------------------------------------------------------------------------------
   --Important! Mapping new NFS share requires cluster services restart - any running statements will be terminated!
   --You have requested to mount folder /mnt/shares/csv for nfs server 192.168.4.28 - Please confirm all details correct and you wish to proceed Y / N?
   
If the mounting destination folder above is correct and you wish to proceed, press ``Y``.

The following is displayed:

.. code-block:: console

   --Mounting nfs server - 192.168.4.28 & folder /mnt/shares/csv
   --Creating templates folder
   --Deployment to patch is sqream-worker-0, patching deployment with added folders
   deployment.apps/sqream-worker-0 patched
   --Deployment patched successfully! :-)
   
When you have finished mounting your NFS shared drives on your SQream cluster, you can use them with **COPY FROM** or **COPY TO** statements, as shown in the following example:

.. code-block:: console

   $ COPY table1 from wrapper csv_fdw options (location = '/mnt/nfs_shares/csv/t_a.csv' , quote='@');