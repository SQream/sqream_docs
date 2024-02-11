.. _version_upgrade_configurations:

******************************************
Upgrade-Related Configuration Changes
******************************************

	   
	   
.. list-table::
   :widths: auto
   :header-rows: 1
      
   * - SQreamDB Version
     - Storage Version
     - Configurations and Changes
   * - 4.4
     - 50
     - New Releases:
	   * Pysqream 5.0.0 Connector is released
	   
	   * JDBC 5.0.0 Connector is released
   * - 4.3
     - 50
     - Configuration:
	   * Two new :ref:`AWS S3<s3>` object access style and endpoint URL with Virtual Private Cloud (VPC) configuration flags: ``AwsEndpointOverride``, ``AwsObjectAccessStyle``
	   * **REHL 8.x** is now officially supported
   * - 4.2
     - 46
     - New Releases:
	   * Pysqream 3.2.5 Connector is released
	   
	   * ODBC 4.4.4 Connector is released
	   
	   * JDBC 4.5.8 Connector is released
	   
	   * Apache Spark 5.0.0 Connector is released
	   
	   * The ``INT96`` data type is deprecated
	   
	   Configuration:
	   
	   * :ref:`Access control permissions<access_control_permissions>` in SQreamDB have been expanded. Learn how to reconfigure access control permissions when :ref:`upgrading from version 4.2<upgrade_to_4.3>` 
   * - 4.1
     - 45
     - New Releases:
	   * JDBC 4.5.7 Connector
	   
	   * SQream Studio v5.5.4
   * - 4.0
     - 45
     - None
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
     - The ``VARCHAR`` data type has been deprecated and replaced with ``TEXT``.
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


