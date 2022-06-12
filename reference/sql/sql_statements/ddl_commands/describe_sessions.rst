.. _describe_sessions:

*****************
DESCRIBE SESSIONS
*****************
The ``DESCRIBE SESSIONS`` command replaces the `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_server_status.html>`_ command.

Syntax
==========
The following is the syntax for the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSIONS [<user_name>]

Parameters
============
The following parameters can be used with the ``DESCRIBE SESSIONS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSIONS``
     - *(Optional)* ``user_name``
     - The name of the user on the session.
     - Text
	 
Example
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSIONS
   	 
Output
=============
Using the ``DESCRIBE SESSIONS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``start_time``
     - Displays the start time of the session.
     - Date
     - 12-06-2022 06:16:56
   * - ``database``
     - Displays the name of the database.
     - Text
     - master
   * - ``source_ip``
     - Displays the IP address of the client connected to SQream.
     - Integer
     - 10.212.134.4	 
   * - ``client``
     - Displays the name and version of the client.
     - Text
     - SQream JDBC v0.1.33
   * - ``status``
     - Displays the status of the client.
     - Text
     - Active
   * - ``session_id``
     - Displays the session ID.
     - Text
     - efd226bb-cc57-4d41-8ff9-c9300830c571
	 
The following is an example of the generated output in Studio:

.. image:: /_static/images/describe_sessions.png

Permissions
=============
No permissions are required for the ``DESCRIBE SESSIONS`` command.