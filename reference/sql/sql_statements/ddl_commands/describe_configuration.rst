.. _describe_configuration:

*****************
DESCRIBE CONFIGURATION
*****************
The ``DESCRIBE CONFIGURATION`` command is used for showing all RTC configurations set on the session level using the ``SET`` command. Closing a session restores all RTC configurations to their default settings.

**Comment** - *According to the* `current configuration page <https://docs.sqream.com/en/latest/configuration_guides/current_configuration_method.html#regular-flag-types>`_, *the full name of the command is* ``show_conf_UF``. *Is this the command that DESCRIBE CONFIGURATION is replacing in V2?*

.. note:: The ``DESCRIBE CONFIGURATION`` command replaces the ``SHOW_CONF`` command. 

For more information, see :ref:`current_configuration_method`.

Syntax
==========
The following is the syntax for the ``DESCRIBE QUERY`` command:

**Comment** - *The syntax example below is unclear.*

.. code-block:: postgres

   DESCRIBE CONFIG[URATION] (PARAM[ETER] <parameter>)* [LIKE 'pattern'] [DEV_MODE];
   
Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE CONFIGURATION** command:

**Comment** - *I will update this table based on the response to the above comment.* 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSION ID``
     - ``session_id``
     - (Optional) The session ID of the query.
     - Type
   * - ``QUERY ID``
     - ``query-id``
     - The query ID of the user.
     - Required
 
Example
==============
The following is an example of the ``DESCRIBE QUERY`` command:

**Comment** - *Need example*

.. code-block:: postgres

   DESCRIBE QUERY SESSION ID '3d5b9e46-4ef8-46d7-bfc3-5c19505494b5' QUERY ID '5';
	 
Output
=============
Using the ``DESCRIBE CONFIGURATION`` command generates the following output:

**Comment** - *Each row needs an example*

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
	 
The following is an example of the generated output in Studio:

**Comment** - *Need generated output example.*

.. code-block:: postgres
   
   GENERATED OUTPUT EXAMPLE

Permissions
=============
No permissions are required for the ``DESCRIBE CONFIGURATION`` command.