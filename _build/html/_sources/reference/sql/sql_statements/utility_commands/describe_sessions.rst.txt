.. _describe_sessions:

*****************
DESCRIBE SESSIONS
*****************
The ``DESCRIBE SESSIONS`` command replaces the `SHOW_SERVER_STATUS <https://docs.sqream.com/en/latest/reference/sql/sql_functions/system_functions/show_server_status.html>`_ command.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
==========
The following is the syntax for the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSIONS [ USER <user_name> ][ TIMEFRAME FROM <start_date_time> TO <end_date_time> ]

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
   * - ``USER``
     - ``user_name``
     - Optional parameter for filtering by username.
     - Text
   * - ``TIMEFRAME FROM``  
     - ``<start_date_time>``
     - Optional parameter for filtering by time frame - must be used in combination with ``TO``.
     - DATETIME
   * - ``TIMEFRAME TO``  
     - ``<end_date_time>``
     - Optional parameter for filtering by time frame - must be used in combination with ``FROM``.
     - DATETIME
	 
	 
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
	 
Examples
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSIONS;
   	 
	 
+---------------------+----------------------+-----------+-------+----------------+----------------------+---------+-------------------+---------------------------------------+------------+
| start_time          | end_time             | database  | role  | source_ip      | client               | status  | rejection_reason  | session_id                            | username   |
+=====================+======================+===========+=======+================+======================+=========+===================+=======================================+============+
| 2022-09-20 6:46:47  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | e77075e0-51cc-4956-b192-b68ce17a4bc5  | sqream     |
| 2022-09-20 6:46:46  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | 6f2c3ee3-4f4b-48f2-90d3-458a26c2788c  | sqream     |
| 2022-09-20 6:46:46  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | e1e4ca64-5079-4e3d-bc47-c1216960ae0f  | sqream     |
| 2022-09-20 5:23:27  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 4bad606f-696f-42a2-9df1-c9f3eb1cf801  | sqream     |
| 2022-09-20 5:22:28  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | c5d86508-86e1-490f-8421-d2bfbc3f062c  | sqream     |
| 2022-09-20 5:19:39  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | a6485840-1191-4154-a303-7872a466ac70  | sqream     |
| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 2aaf1e33-3b55-4b2b-8fe9-c837d700665d  | sqream     |
| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 8f3c91b7-816e-4e36-b999-e4853e4fe255  | sqream     |
| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | ca5b1c86-a696-49f9-bc72-6fff76691799  | sqream     |
+---------------------+----------------------+-----------+-------+----------------+----------------------+---------+-------------------+---------------------------------------+------------+

The following is an example of the ``DESCRIBE SESSIONS`` command filtering a specific time frame:

.. code-block:: postgres

   DESCRIBE SESSIONS TIMEFRAME FROM '2022-09-19 10:00:00' TO '2022-09-19 16:00:00';
   
+----------------------+----------------------+-----------+-------+---------------+----------------------+---------+-------------------+---------------------------------------+------------+
| start_time           | end_time             | database  | role  | source_ip     | client               | status  | rejection_reason  | session_id                            | username   |
+======================+======================+===========+=======+===============+======================+=========+===================+=======================================+============+
| 2022-09-19 15:32:49  | 2022-09-19 15:32:55  | master    | N/A   | 192.168.4.69  | SQream JDBC v0.1.33  | Closed  | N/A               | dd40f403-ba34-460c-835b-2161a59f52a3  | sqream     |
| 2022-09-19 15:27:04  | 2022-09-19 15:27:04  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | 914869f7-d4f4-45ea-9563-68eeb2ea3189  | sqream     |
| 2022-09-19 14:08:50  | 2022-09-19 14:08:59  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | a4dfa69a-a73e-4731-81e5-b7c87dd8dc7b  | sqream     |
| 2022-09-19 14:08:38  | 2022-09-19 14:08:48  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | c3339342-02fa-49e8-b7f1-1172d577c5b7  | sqream     |
|                      |                      |           |       |               |                      |         |                   |                                       |            |
|                      |                      |           |       |               |                      |         |                   |                                       |            |
|                      |                      |           |       |               |                      |         |                   |                                       |            |
|                      |                      |           |       |               |                      |         |                   |                                       |            |
|                      |                      |           |       |               |                      |         |                   |                                       |            |
+----------------------+----------------------+-----------+-------+---------------+----------------------+---------+-------------------+---------------------------------------+------------+


Permissions
=============
A user may execute ``DESCRIBE SESSIONS`` to list his sessions.

``SUPERUSER`` may execute ``DESCRIBE SESSIONS`` to list any session by any user.