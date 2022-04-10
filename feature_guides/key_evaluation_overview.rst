.. _key_evaluation_overview:

**************************
Overview
**************************
The **Key Evaluation** feature resolves conflicts caused by ingesting and deleting data at the same time. Although this rarely occurs, it causes the leveldb to restore keys pointing to deleted data. In turn, this causes SQream metadata to search for deleted files.

An indication that this conflict has occurred is SQream's inability to retrieve deleted data pointers, generating the type of error shown below:

.. code-block:: console
   
   Internal Runtime Error *** Error opening [errno 2 No such file or directory] file name /mnt/disk1/sqream_cluster/databases/******/tables/289/17/17-391270
   
In addition, key evaluation prevents the database from creating phantom keys, which are duplicate chunk keys generated when data is ingested. Under normal circumstances ingesting data creates incrementing chunk keys.

**Comment** - *Please confirm the reason I provided based on my understanding of the source doc.*