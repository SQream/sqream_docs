.. _version_upgrade_configurations:

******************************************
Version History and Configuration Changes
******************************************

.. list-table::
   :widths: auto
   :header-rows: 1
      
   * - SQreamDB Version
     - Storage Version
     - Configurations and Changes
   * - 2022.1.7
     - 43
     - None
   * - 2022.1.6
     - 42
     - None
   * - 2022.1.5
     - 42
     - None
   * - 2022.1.4
     - 42
     - None
   * - 2022.1.3
     - 42
     - In SQream version 2022.1.3 the ``VARCHAR`` data type has been deprecated and replaced with ``TEXT``.
   * - 2022.1.2
     - 41
     - None
   * - 2022.1.1
     - 40
     - * In compliance with GDPR standards, version 2022.1.1 requires a strong password policy when accessing the CLI and Studio. For more information, see :ref:`Password Policy<access_control_password_policy>`.

       * The ``login_max_retries`` configuration flag is required for adjusting the permitted log-in attempts. For more information, see :ref:`Adjusting the Permitted Log-In Attempts<login_max_retries>`.
   * - 2022.1
     - 40
     - * In SQream version 2022.1 the ``VARCHAR`` data type has been deprecated and replaced with ``TEXT``. SQream will maintain ``VARCHAR`` in all previous versions until completing the migration to ``TEXT``, at which point it will be deprecated in all earlier versions. SQream also provides an automated and secure tool to facilitate and simplify migration from ``VARCHAR`` to ``TEXT``.

       * If you are using an earlier version of SQreamDB, see the :ref:`Using Legacy String Literals<use_legacy_string_literals>` configuration flag.


