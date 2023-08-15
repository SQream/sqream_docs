.. _describe_configuration:

**********************
DESCRIBE CONFIGURATION
**********************

The ``DESCRIBE CONFIGURATION`` command is used for showing all configurations set on the session level using the ``SET`` command. Closing a session restores all configurations to their default settings.

.. note:: The ``DESCRIBE CONFIGURATION`` command replaces the ``SHOW_CONF`` command. 
.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE CONFIGURATION`` command:

.. code-block:: postgres

   DESCRIBE CONFIGURATION [PARAMETER <parameter>] [LIKE 'pattern']
   DESC CONFIG [PARAM <parameter>] [LIKE 'pattern']
   
Parameters
==========

The following parameters can be used when switching databases with the ``DESCRIBE CONFIGURATION`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``PARAMETER``
     - Describes the specified configuration parameter, listing all parameters if nothing is specified.
   * - ``LIKE``
     - The ``LIKE`` operator is used to perform pattern matching within strings.
   * - ``%``
     - The ``%`` wildcard is used in conjunction with the ``LIKE`` operator to match any sequence of characters (including none) within a string.

Output
======


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``flag_name``
     - Displays the name of the flag.
     - Text
     - portSsl
   * - ``flag_value``
     - Displays the value of the flag.
     - Numeric
     - 433
   * - ``def_flag_value``
     - Displays the default value of the flag.
     - Numeric
     - 433
   * - ``flag_category``
     - Displays the category of the flag.
     - Text
     - RND
   * - ``flag_type``
     - Displays the type of the flag.
     - Text
     - worker
   * - ``data_type``
     - Displays the data type.
     - Text
     - 
   * - ``description``
     - Displays the description of the flag.
     - Text
     - Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as CLI.

Example
=======

.. code-block:: sql

	   DESCRIBE CONFIGURATION;
 
.. code-block:: postgres   

	DESCRIBE CONFIGURATION PARAMETER PORT LIKE '%PORT%';

Output:

.. code-block:: none  

   flag_name                         |flag_value                                     |def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
   ----------------------------------+-----------------------------------------------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   gpu                               |0                                              |0             |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   port                              |5000                                           |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   portSsl                           |433                                            |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as Cli|
   cluster                           |"\/mnt\/sqream\/sqreamdb"                      |              |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   metadataPath                      |"\/mnt\/sqream\/sqreamdb\/leveldb"             |              |RND          |worker   |         |                                                                                                                                                                                                                                                               |
DESCRIBE CONFIGURATION PARAMETER
--------------------------------

The following is an example of the ``DESCRIBE CONFIGURATION PARAMETER`` command:
 
.. code-block:: postgres   
	 
	DESCRIBE CONFIGURATION PARAMETER PORT;
   
Output:

.. code-block:: none  

   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description|
   ---------+----------+--------------+-------------+---------+---------+-----------+
   port     |5000      |5000          |RND          |worker   |         |           |


.. code-block:: sql   
	 
   DESCRIBE CONFIGURATION LIKE '%port%';
   
Output

.. code-block:: none

   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
   ---------+----------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   port     |5000      |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   portSsl  |433       |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as Cli|

Permissions
===========

Using the ``DESCRIBE CONFIGURATION`` command requires ``SUPERUSER`` permissions.
