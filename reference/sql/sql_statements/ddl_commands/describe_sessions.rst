.. _describe_sessions:

*****************
DESCRIBE SESSIONS
*****************
The ``DESCRIBE SESSIONS`` command replaces the `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_server_status.html>`_ command, and lets you display a list of sessions:

* Actively connected sessions with no running statements
 
   ::

* Sessions with queued queries

   ::
  
* Closed sessions

Syntax
==========
The following is the correct syntax for the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSIONS

Parameters
============
The following parameters can be used with the ``DESCRIBE SESSIONS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``DESCRIBE SESSIONS``
     - Displays the name of the database.
	 
Examples
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
     - Displays the name of the database.
     - Date
     - 02-05-2022 15:23:48
   * - ``database``
     - Displays the name of the database.
     - Text
     - master
   * - ``client``
     - Displays the name of the client.
     - Text
     - SQream JDBC v0.1.33
   * - ``status``
     - Displays the status of the client.
     - Text
     - Active
   * - ``session_id``
     - Displays the session ID.
     - Text
     - 64935a0b-7e9d-40b0-828c-6d4f196d4830	 

Permissions
=============
**Comment** - *What are the permissions?*