.. _upgrade_guide:

*****************
Upgrade Guide
*****************

Upgrading your SQream version requires stopping all running services.

1. Stop all actively running SQream services.
   
   All SQream services must remain stopped while the upgrade is in process. Ensuring that SQream services remain stopped depends on the tool being used.
   
2. Verify that SQream has stopped listening on ports **500X**, **510X**, and **310X**:

.. code-block:: console

      $ sudo netstat -nltp    #to make sure sqream stopped listening on 500X, 510X and 310X ports.

3. Replace the old version ``sqream-db-v2021.1``, with the new version ``sqream-db-v2021.1``:

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

6. Verify that the symbolic SQream link points to the real folder:

.. code-block:: console  

      $ ls -l
	 
      -- Output example:

      $ sqream -> sqream-db-v2021.1

7. Upgrade your version of SQream storage.
	  
  a. Generate a back-up of the metadata by running the following command:

  .. code-block:: console

      $ select backup_metadata('out_path');
	  
  SQream recommends storing the generated back-up locally in case needed.

  SQream runs the Garbage Collector and creates a clean backup tarball package.
   
  b. Shut down all SQream services.

  c. Extract the recently created back-up file.

  d. Replace your current metadata with the metadata you stored in the back-up file.

  e. Navigate to the new SQream package bin folder.

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



Upgrading to Version 2022.1.7
------------------------------

Version 2022.1.7 uses storage version 43. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <RocksDB path>

Upgrading to Version 2022.1.6
---------------------------------

Version 2022.1.6 uses storage version 42. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <RocksDB path>

Upgrading to Version 2022.1.5
-------------------------------

Version 2022.1.5 uses storage version 42. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <RocksDB path>

Upgrading to Version 2022.1.4
------------------------------

Version 2022.1.4 uses storage version 42. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <levelDB path>

Upgrading to Version 2022.1.3
---------------------------------

Version 2022.1.3 uses storage version 42. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

In SQream version 2022.1.3 the ``VARCHAR`` data type has been deprecated and replaced with ``TEXT``.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <levelDB path>

Upgrading to Version 2022.1.2
-------------------------------

Version 2022.1.2 uses storage version 41. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <levelDB path>

Upgrading to Version 2022.1.1
------------------------------

Operation and Configuration Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Version 2022.1.1 uses storage version 40. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

In compliance with GDPR standards, version 2022.1.1 requires a strong password policy when accessing the CLI and Studio. For more information, see :ref:`Password Policy<access_control_password_policy>`.

The ``login_max_retries`` configuration flag is required for adjusting the permitted log-in attempts. For more information, see :ref:`Adjusting the Permitted Log-In Attempts<login_max_retries>`.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a back-up of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created back-up file.

4. Replace your current metadata with the metadata you stored in the back-up file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <levelDB path>
  
Upgrading to Version 2022.1
-----------------------------

Operation and Configuration Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Version 2022.1 uses storage version 40. If you're using an older storage version, you need to upgrade to the latest one using the :ref:`Upgrading SQreamDB Version<installing_sqream_with_binary>` guide.

In SQream version 2022.1 the ``VARCHAR`` data type has been deprecated and replaced with ``TEXT``. SQream will maintain ``VARCHAR`` in all previous versions until completing the migration to ``TEXT``, at which point it will be deprecated in all earlier versions. SQream also provides an automated and secure tool to facilitate and simplify migration from ``VARCHAR`` to ``TEXT``.

If you are using an earlier version of SQreamDB, see the :ref:`Using Legacy String Literals<use_legacy_string_literals>` configuration flag.

Upgrade Procedure
^^^^^^^^^^^^^^^^^^

1. Generate a backup of the metadata by running the following command:

   .. code-block:: console

      $ select backup_metadata('out_path', 'single_file');
	  
   SQream recommends storing the generated back-up locally in case needed.
   
   SQream runs the Garbage Collector and creates a clean backup tarball package.
   
2. Shut down all SQream services.

3. Extract the recently created backup file.

4. Replace your current metadata with the metadata you stored in the backup file.

5. Navigate to the new SQream package bin folder.

6. Run the following command:

   .. code-block:: console

      $ ./upgrade_storage <levelDB path>