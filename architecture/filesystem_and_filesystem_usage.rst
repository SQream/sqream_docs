.. _filesystem_and_filesystem_usage:

********************
Filesystem and Usage
********************

SQreamDB writes and reads data from disk.

The SQreamDB storage directory, sometimes referred to as a **storage cluster** is a collection of database objects, metadata database, and logs.

Each SQreamDB worker and the metadata server must have access to the storage cluster in order to function properly.

.. _storage_cluster:

Directory organization
======================

.. figure:: /_static/images/storage_organization.png

The **cluster root** is the directory in which all data for SQreamDB is stored.

.. contents:: SQreamDB storage cluster directories
   :local:

``databases``
-------------

The databases directory houses all of the actual data in tables and columns.

Each database is stored as its own directory. Each table is stored under its respective database, and columns are stored in their respective table.

.. figure:: /_static/images/table_columns_storage.png

In the example above, the database named ``retail`` contains a table directory with a directory named ``23``. 

.. tip:: To find table IDs, use a catalog query:
   
   .. code-block:: psql
   
      master=> SELECT table_name, table_id FROM sqream_catalog.tables WHERE table_name = 'customers';
      table_name | table_id
      -----------+---------
       customers |      23 


Each table directory contains a directory for each physical column. An SQL column may be built up of several physical columns (e.g. if the data type is nullable).

.. tip:: To find column IDs, use a catalog query:
   
   .. code-block:: psql
   
      master=> SELECT column_id, column_name FROM sqream_catalog.columns WHERE table_id=23;
      column_id | column_name
      ----------+------------
              0 | name@null  
              1 | name@val   
              2 | age@null   
              3 | age@val    
              4 | email@null 
              5 | email@val  

Each column directory will contain extents, which are collections of chunks.

.. figure:: /_static/images/chunks_and_extents.png

``metadata`` or ``rocksdb``
---------------------------

SQreamDB's metadata is an embedded key-value store, based on RocksDB. RocksDB helps SQreamDB ensure efficient storage for keys, handle atomic writes, snapshots, durability, and automatic recovery.

The metadata is where all database objects are stored, including roles, permissions, database and table structures, chunk mappings, and more.

``temp``
--------

The ``temp`` directory is where SQreamDB writes temporary data.

The directory to which SQreamDB writes temporary data can be changed to any other directory on the filesystem. SQreamDB recommends remapping this directory to a fast local storage to get better performance when executing intensive larger-than-RAM operations like sorting. SQreamDB recommends an SSD or NVMe drive, in mirrored RAID 1 configuration.

If desired, the ``temp`` folder can be redirected to a local disk for improved performance, by setting the ``tempPath`` setting in the :ref:`legacy configuration<current_method_modification_methods>` file.


``logs``
--------

The logs directory contains logs produced by SQreamDB.

See more about the logs in the :ref:`logging` guide.

.. what kind of access patterns for different files to optimise for

.. putting temp on local when using shared storage
