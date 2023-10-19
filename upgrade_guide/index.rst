.. _upgrade_guide:

*****************
Upgrade Guide
*****************

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