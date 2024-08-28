.. _version_upgrade:

*****************
Version Upgrade 
*****************

Upgrading your SQreamDB version requires stopping all running services.

1. Stop all actively running SQreamDB services.
   
   Ensuring that SQreamDB services are at a halt depends on the tool being used.
   
2. Verify that SQreamDB has stopped listening on ports **500X**, **510X**, and **310X**:

.. code-block:: console

      $ sudo netstat -nltp    #to make sure SQreamDB stopped listening on 500X, 510X and 310X ports.

3. Replace the old SQreamDB version with the new version, such as in the following example:

.. code-block:: console
    
      $ cd /home/sqream
      $ mkdir tempfolder
      $ mv sqream-db-v2021.1.tar.gz tempfolder/
      $ cd tempfolder/
      $ tar -xf sqream-db-v2021.1.tar.gz
      $ sudo mv sqream /usr/local/sqream-db-v2021.1
      $ cd /usr/local
      $ sudo chown -R sqream:sqream sqream-db-v2021.1
   
4. Remove the symbolic link:

.. code-block:: console
   
      $ sudo rm sqream
   
5. Create a new symbolic link named "sqream" pointing to the new version:

.. code-block:: console  

      $ sudo ln -s sqream-db-v2021.1 sqream

6. Verify that the symbolic SQreamDB link points to the real folder:

.. code-block:: console  

      $ ls -l
	 
      -- Output example:

      $ sqream -> sqream-db-v2021.1

7. Upgrade your version of SQreamDB storage.
	  
  a. SQreamDB recommends storing the generated back-up locally in case needed. To generate a back-up of the metadata, run the following command:

  .. code-block:: console

      $ select backup_metadata('out_path');

  SQreamDB runs the Garbage Collector and creates a clean backup tarball package.
   
  b. Shut down all SQreamDB services.

  c. Extract the recently created back-up file.

  d. Replace your current metadata with the metadata you stored in the back-up file.

  e. Navigate to the new SQreamDB package bin folder.

  f. Get the cluster path
	
  .. code-block:: console

    $ cat /etc/sqream/sqream1_config.json |grep cluster

  g. Run the following command:

  .. code-block:: console

      $ ./upgrade_storage <RocksDB path>
	  
      -- Output example:

	  get_leveldb_version path{<cluster path>}
	  current storage version 23
      upgrade_v24
      upgrade_storage to 24
	  upgrade_storage to 24 - Done
	  upgrade_v25
	  upgrade_storage to 25
	  upgrade_storage to 25 - Done
	  upgrade_v26
	  upgrade_storage to 26
	  upgrade_storage to 26 - Done
	  validate_leveldb
	  ...
      upgrade_v37
	  upgrade_storage to 37
	  upgrade_storage to 37 - Done
	  validate_leveldb
      storage has been upgraded successfully to version 37
 
8. Verify that the latest version has been installed:

.. code-block:: console
    
      $ ./sqream sql --username sqream --password sqream --host localhost --databasename master -c "SELECT SHOW_VERSION();"
	  
      -- Output example:
    
      v2021.1
      1 row
      time: 0.050603s 
 
For more information, see the :ref:`upgrade_storage<upgrade_storage_cli_reference>` command line program.

9. After completing the upgrade process, ensure that ALL :ref:`operational and configuration<version_upgrade_configurations>` changes introduced in versions newer than the version you are upgrading from are applied before returning to regular SQreamDB operations.

