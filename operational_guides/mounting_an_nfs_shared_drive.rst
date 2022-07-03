.. _mounting_an_nfs_shared_drive:

**********************************
Mounting an NFS Shared Drive
**********************************
**IN PROGRESS**


The **Mounting an NFS Shared Drive** guide describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
==============   
SQream supports reading external tables and / or write exports to NFS (Network File System) shared drives. As SQream DB microservices run as Dockerized containers these NFS shares should first be mounted to the SQream DB cluster. Once mounted, mount is persistent.

Mapping is performed using a script that is delivered with the SQream DB deployment package, script may be found at utilities/nfsshares/update-nfs-share.sh


Script Prerequisites
==============
The following list describes the script prerequisites:

Permissions to execute kubectl commands
Executable permissions (chmod +x update-nfs-share.sh )
Verify NFS share is shared with the SQream cluster, may be done by executing the following Linux command and verifying the NFS share is listed when specifying the relevant NFS Server IP address:
$ showmount -e 192.168.4.28
>Export list for 192.168.4.28:
>/mnt/shares/csv     192.168.4.0/24
>/newdir/myshareddir 192.168.4.0/24
>/mnt/myshareddir    192.168.4.0/24


Script input parameters
==============
NFS Server IP address
NFS share path - this is the path that will be mounted and should later be used for copy from or export statements.

Syntax
==============
./update-nfs-share.sh <<NFS Server IP>> <<Customer Shared Folder Path>>

Example
==============
$ ./update-nfs-share.sh 192.168.4.28 /mnt/shares/csv
 
Output
==============
--------------------------------------------------------------------------------
--This script will add customer nfs shares (folders) to sqream GPU worker pods--
--------------------------------------------------------------------------------
--Important! Mapping new NFS share requires cluster services restart - any running statements will be terminated!
--You have requested to mount folder /mnt/shares/csv for nfs server 192.168.4.28 - Please confirm all details correct and you wish to proceed Y / N?
Y
--Mounting nfs server - 192.168.4.28 & folder /mnt/shares/csv
--Creating templates folder
--Deployment to patch is sqream-worker-0, patching deployment with added folders
deployment.apps/sqream-worker-0 patched
--Deployment patched successfully! :-)
 
Once mounted the share may be used in COPY FROM or COPY TO SQL Statements, example:
COPY table1 from wrapper csv_fdw options (location = '/mnt/nfs_shares/csv/t_a.csv' , quote='@');