.. _describe_configuration:

*****************
DESCRIBE CONFIGURATION
*****************
The ``DESCRIBE CONFIGURATION`` command is used for showing all RTC configurations set on the session level using the ``SET`` command. Closing a session restores all RTC configurations to their default settings.

**Comment** - *The SHOW_CONF command has to be added to the* `current configuration page <https://docs.sqream.com/en/latest/configuration_guides/current_configuration_method.html#regular-flag-types>`_,.

.. note:: The ``DESCRIBE CONFIGURATION`` command replaces the ``SHOW_CONF`` command. 

For more information, see :ref:`current_configuration_method`.

Syntax
==========
The following is the syntax for the ``DESCRIBE CONFIGURATION`` command:

.. code-block:: postgres

   DESCRIBE CONFIGURATION (PARAMETER <parameter>)* [LIKE 'pattern']
   
The ``[LIKE 'pattern']`` is used to define a wildcard pattern containing one or more characters in a string. For example, defining it as ``'%port%'`` will describe all configurations containing the string ``port,`` as in ``portSsl``.

For an example of an output, see the :ref:`Output<output>` section below.
     
.. note::  The ``DESCRIBE_CONFIGURATION`` arguments (``CONFIGURATION`` and ``PARAMETER``) can be written in either short (``CONFIG``, ``PARAM``) or long format (``CONFIGURATION``, ``PARAMETER``).
   
Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE CONFIGURATION** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``PARAMETER``
     - ``parameter``
     - Describes the specified configuration parameter(s), listing all parameters if nothing is specified.
     - Required **Comment** - *True?*
   * - ``LIKE 'pattern'``
     - ``'pattern'``
     - Describes all configurations containing the defined string.
     - Required **Comment** - *True?*

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
Defining the ``DESCRIBE CONFIGURATION`` argument generates the following output:

.. code-block:: postgres   

   DESCRIBE Configuration;

   flag_name                         |flag_value                                     |def_flag_value|flag_category|flag_type|data_type|description                                                                                                                                                                                                                                                    |
   ----------------------------------+-----------------------------------------------+--------------+-------------+---------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   gpu                               |0                                              |0             |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   port                              |5000                                           |5000          |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   portSsl                           |433                                            |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start.¶If the daemon has started, this was probably set correctly. Connect with a client such as Cli|
   cluster                           |"\/mnt\/sqream\/sqreamdb"                      |              |RND          |worker   |         |                                                                                                                                                                                                                                                               |
   metadataPath                      |"\/mnt\/sqream\/sqreamdb\/leveldb"             |              |RND          |worker   |         |  
   
DESCRIBE CONFIGURATION PARAMETER
------------------------
Defining the ``PARAMETER`` argument generates the following output:

.. code-block:: postgres   

   describe config param port;

   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description|
   ---------+----------+--------------+-------------+---------+---------+-----------+
   port     |5000      |5000          |RND          |worker   |         |           |

DESCRIBE CONFIGURATION LIKE PATTERN
------------------------   
Defining the ``LIKE PATTERN`` argument generates the following output:

.. code-block:: postgres   

   describe config like '%port%';

   flag_name|flag_value|def_flag_value|flag_category|flag_type|data_type|description|
   ---------+----------+--------------+-------------+---------+---------+-----------+
   port     |5000      |5000          |RND          |worker   |         |           |
   portSsl  |433       |433           |RND          |worker   |         |Configuration file only. This flag can only be set before the daemon starts. It cannot be changed dynamically. Port conflicts will cause the server not to start.¶If the daemon has started, this was probably set correctly. Connect with a client such as Cli|

**Comment** - *When you have access, populate the table according to the correct output.*

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``name``
     - Displays the name of the configuration.
     - Text
     - 
   * - ``value``
     - Displays the value of the configuration.
     - Text
     - 
   * - ``default_value``
     - Displays the default value of the configuration.
     - Text
     - 
   * - ``category``
     - Displays the category of the configuration.
     - Text
     - 
   * - ``flag_type``
     - Displays the flag_type of the configuration.
     - Text
     - 
   * - ``description``
     - Displays the description of the configuration.
     - Text
     - 
   * - ``data_type``
     - Displays the data type of the configuration.
     - Text
     - 
   * - ``range``
     - Displays the range of the configuration.
     - Text
     - 
	 
The following is an example of the generated output:

**Comment** - *Need generated output example.*

.. code-block:: postgres
   
   GENERATED OUTPUT EXAMPLE

Permissions
=============
No permissions are required for the ``DESCRIBE CONFIGURATION`` command.