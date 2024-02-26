.. _describe_configuration:

**********************
DESCRIBE CONFIGURATION
**********************

The ``DESCRIBE CONFIGURATION`` command is used for showing all session level configurations. Closing a session restores all configurations to their default settings.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] CONFIGURATION [PARAMETER <"parameter">] [LIKE <'pattern'>]
   
Parameters
==========

The following parameters can be used when switching databases with the ``DESCRIBE CONFIGURATION`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Type
     - Description
     - Example	 
   * - ``PARAMETER``
     - Identifier
     - Specifies a particular configuration parameter. If no parameter is specified, it lists all configuration parameters.
     - ``"useGrpcCompiler"``	 
   * - ``LIKE``
     - String literal
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.
     - ``'%port%'``	


Output
======


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Data Type
     - Example
   * - ``flag_name``
     - Displays the name of the flag.
     - ``TEXT``
     - portSsl
   * - ``flag_value``
     - Displays the value of the flag.
     - ``NUMERIC``
     - 433
   * - ``def_flag_value``
     - Displays the default value of the flag.
     - ``NUMERIC``
     - 433
   * - ``flag_category``
     - Displays the category of the flag.
     - ``TEXT``
     - RND
   * - ``flag_type``
     - Displays the type of the flag.
     - ``TEXT``
     - worker
   * - ``data_type``
     - Displays the data type.
     - ``TEXT``
     - 
   * - ``description``
     - Displays the description of the flag.
     - ``TEXT``
     - Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as CLI.

Example
=======
	   
.. code-block:: sql   
	   
	DESCRIBE CONFIGURATION PARAMETER "useGrpcCompiler";
   
Output:

.. code-block:: none  

   flag_name           |flag_value|def_flag_value|flag_category|flag_type|data_type|description|
   --------------------+----------+--------------+-------------+---------+---------+-----------+
   useGrpcCompiler     |false     |false         |RND          |regular  |         |           |


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

This command requires a ``SUPERUSER`` permission.
