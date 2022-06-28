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

   DESCRIBE CONFIGURATION (PARAMETER <parameter>)* [LIKE 'pattern'] [DEV_MODE];
   
**Comment** - *The PRD says, "Describe dev_mode config parameters (in additon to the non_dev parameters list) - hidden option for internal use only, not to be documented." Confirm.*
   
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
     - **Comment** - *Value needed*
     - Describe specific config parameters using LIKE pattern.
     - Required **Comment** - *True?*
   * - ``DEV_MODE``
     - **Comment** - *Does not need to be documented. Confirm.*
     - 
     - 
 
Example
==============
The following is an example of the ``DESCRIBE CONFIGURATION`` command:

**Comment** - *Waiting for access to doc.*

.. code-block:: postgres   
	 
Output
=============
Using the ``DESCRIBE CONFIGURATION`` command generates the following output:

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