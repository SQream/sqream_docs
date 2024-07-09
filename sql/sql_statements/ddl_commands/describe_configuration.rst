:orphan:

.. _describe_configuration:

**********************
DESCRIBE CONFIGURATION
**********************

The ``DESCRIBE CONFIGURATION`` command is used for showing all session level configurations. Closing a session restores all configurations to their default settings.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] CONFIGURATION [PARAMETER <"ConfigurationParameter">] [LIKE <'pattern'>]
   
Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type 
     - Description
   * - ``PARAMETER``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - Filters by configuration parameter. If none specified, it lists all configuration parameters
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match


Output
======


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``flag_name``
     - ``TEXT``
     - Displays the name of the flag.
   * - ``flag_value``
     - ``NUMERIC``
     - Displays the value of the flag.
   * - ``def_flag_value``
     - ``NUMERIC``
     - Displays the default value of the flag.
   * - ``flag_category``
     - ``TEXT``
     - Displays the category of the flag.
   * - ``flag_type``
     - ``TEXT``
     - Displays the type of the flag.
   * - ``data_type``
     - ``TEXT``
     - Displays the data type.
   * - ``description``
     - ``TEXT``
     - Displays the description of the flag.

Example
=======
	   
.. code-block:: sql   
	   
	DESCRIBE CONFIGURATION PARAMETER "useGrpcCompiler";

	flag_name           |flag_value|def_flag_value|flag_category|flag_type|data_type|description|
	--------------------+----------+--------------+-------------+---------+---------+-----------+
	useGrpcCompiler     |false     |false         |RND          |regular  |         |           |
	
.. code-block:: sql   
	   
	DESCRIBE CONFIGURATION PARAMETER port;

	flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description|
	---------+----------+--------------+-------------+---------+---------+-----------+
	port     |5000      |5000          |RND          |worker   |         |           |


.. code-block:: sql   
	 
	DESCRIBE CONFIGURATION LIKE '%port%';

	flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
	---------+----------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	port     |5000      |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
	portSsl  |433       |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as Cli|


Permissions
===========

This command requires a ``SUPERUSER`` permission.
