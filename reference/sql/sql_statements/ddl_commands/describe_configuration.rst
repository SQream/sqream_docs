.. _describe_configuration:

*****************
DESCRIBE CONFIGURATION
*****************
The ``DESCRIBE CONFIGURATION`` command is used for showing all configurations set on the session level using the ``SET`` command. Closing a session restores all configurations to their default settings.

.. note:: The ``DESCRIBE CONFIGURATION`` command replaces the ``SHOW_CONF`` command. 

For more information, see :ref:`configuring_sqream`.

Syntax
==========
The following is the syntax for the ``DESCRIBE CONFIGURATION`` command:

.. code-block:: postgres

   DESCRIBE CONFIGURATION [PARAMETER <parameter>] [LIKE 'pattern']
   
The ``[LIKE 'pattern']`` is used to define a wildcard pattern containing one or more characters in a string. For example, defining it as ``'%port%'`` will describe all configurations containing the string ``port,`` as in ``portSsl``.

For an example of an output, see the :ref:`Output<output>` section below.
     
.. note::  The ``DESCRIBE_CONFIGURATION`` arguments (``CONFIGURATION`` and ``PARAMETER``) can be written in either short (``CONFIG``, ``PARAM``) or long format (``CONFIGURATION``, ``PARAMETER``).
   
Parameters
============
The following parameters can be used when switching databases with the ``DESCRIBE CONFIGURATION`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``PARAMETER``
     - ``parameter``
     - Describes the specified configuration parameter, listing all parameters if nothing is specified.
     - Text
   * - ``LIKE 'pattern'``
     - ``'pattern'``
     - Describes all configurations containing the defined string.
     - Text

Example
==============
The following is an example of the ``DESCRIBE CONFIGURATION`` command:

.. code-block:: postgres   

   DESCRIBE CONFIGURATION PARAMETER PORT LIKE '%PORT%';

.. _output:
	 
Output
=============
The **Output** section shows individual output examples of the following arguments:

.. contents:: 
   :local:
   :depth: 1
   
DESCRIBE CONFIGURATION
-------------------------
Using the ``DESCRIBE CONFIGURATION`` command generates the following output:

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
	 
The following is an example of the ``DESCRIBE CONFIGURATION`` command:
 
.. code-block:: postgres   
	 
   describe configuration;
 
The following is an example of the generated output of the ``DESCRIBE CONFIGURATION`` command:

.. code-block:: postgres   

   flag_name                         |flag_value                                     |def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
   ----------------------------------+-----------------------------------------------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   gpu                               |0                                              |0             |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   port                              |5000                                           |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   portSsl                           |433                                            |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as Cli|
   cluster                           |"\/mnt\/sqream\/sqreamdb"                      |              |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   metadataPath                      |"\/mnt\/sqream\/sqreamdb\/leveldb"             |              |RND          |worker   |         |                                                                                                                                                                                                                                                               |
DESCRIBE CONFIGURATION PARAMETER
------------------------
The following is an example of the ``DESCRIBE CONFIGURATION PARAMETER`` command:
 
.. code-block:: postgres   
	 
   describe config param port;
   
The following is an example of the generated output of the ``DESCRIBE CONFIGURATION PARAMETER`` command:

.. code-block:: postgres   

   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description|
   ---------+----------+--------------+-------------+---------+---------+-----------+
   port     |5000      |5000          |RND          |worker   |         |           |

DESCRIBE CONFIGURATION LIKE PATTERN
------------------------
The following is an example of the ``DESCRIBE CONFIGURATION LIKE PATTERN`` command:
 
.. code-block:: postgres   
	 
   describe config like '%port%';
   
The following is an example of the generated output of the ``DESCRIBE CONFIGURATION LIKE PATTERN`` command:

.. code-block:: postgres
   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
   ---------+----------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   port     |5000      |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   portSsl  |433       |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start. If the daemon has started, this was probably set correctly. Connect with a client such as Cli|

Permissions
=============
Using the ``DESCRIBE CONFIGURATION`` command requires ``SUPERUSER`` permissions.