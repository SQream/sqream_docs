.. _describe_session_queries:

*****************
DESCRIBE SESSION QUERIES
*****************
The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries.

Syntax
==========
The following is the syntax for the ``DESCRIBE SESSION QUERIES`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES  [SESSION ID <session-id>] 

Parameters
============
The following parameters can be used with the ``DESCRIBE SESSION QUERIES`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``SESSION ID``
     - ``session_id``
     - The session ID of the query.
     - Text
	 
.. note:: The ``SESSION_ID`` parameter is optional. If you do not specify a session ID, SQream uses the session ID of the current session.
	 
Example
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES SESSION ID  'b6173e04-6e2a-4266-bef0-6fc9b8ffc097';
   	 
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
   * - ``query_id``
     - Displays the query ID.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097:3
   * - ``query_status``
     - Displays the query status.
     - Text
     - EXECUTION_SUCCEED,SELECT
   * - ``query_type``
     - Displays the query type.
     - Text
     - SELECT
   * - ``sql_text``
     - Selects the defined SQL text from the specified table.
     - Text
     - select * from t1
   * - ``session_id``
     - Selects the session ID.
     - Text
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097
   * - ``start_time``
     - Displays the start date and time.
     - Type
     - 2022-05-02T15:32:49
   * - ``client_info``
     - Displays information about the client.
     - Type
     - SQream JDBC v0.1.33 

The following is an example of the generated output in Studio:
  
.. image:: /_static/images/describe_session_queries.png

**Comment** - *Need higher quality image. Please speak with me and I'll show you how to get one.*

Permissions
=============
No permissions are required for the ``DESCRIBE SESSION QUERIES`` command.