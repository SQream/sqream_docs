.. _bucket_integration:

**************************
Bucket Integration
**************************
 
.. contents:: 
   :local:
   :depth: 1


Overview
----------


Making Parquet Files Accessible to Workers
================================================================
To give workers access to files every node must have the same view of the storage being used.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS name node with the correct user-id. For more information, see :ref:`hdfs` guide for more information.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3` guide for more information.


Place ORC files where SQream DB workers can access them
================================================================

Any worker may try to access files (unless explicitly specified with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream DB servers can access the HDFS name node with the correct user-id. See our :ref:`hdfs` guide for more information.

* For S3, ensure network access to the S3 endpoint. See our :ref:`s3` guide for more information.


Making JSON Files Accessible to Workers
=======================================

To give workers access to files, every node in your system must have access to the storage being used.

The following are required for JSON files to be accessible to workers:

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS NameNode with the correct **user-id**. For more information, see :ref:`hdfs`.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3`.

For more information about configuring worker access, see :ref:`workload_manager`.


Place CSVs where SQream DB workers can access
=======================================================

During data load, the :ref:`copy_from` command can run on any worker (unless explicitly speficied with the :ref:`workload_manager`).
It is important that every node has the same view of the storage being used - meaning, every SQream DB worker should have access to the files.

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream DB servers can access the HDFS name node with the correct user-id. See our :ref:`hdfs` guide for more information.

* For S3, ensure network access to the S3 endpoint. See our :ref:`s3` guide for more information.