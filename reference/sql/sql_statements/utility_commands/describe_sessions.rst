.. _describe_sessions:

*****************
DESCRIBE SESSIONS
*****************

The ``DESCRIBE SESSIONS`` command returns information about a user's current session.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

	DESC[RIBE] SESSIONS 
	[ USER '<user_name>' ] 
	[ TIMEFRAME FROM '<start_date_time>' TO '<end_date_time>' ] 
	[ INITIATED BY ( ALL | { External | Blue_UI_User | Blue_UI_System | CLI | Jobs | Statistics } ) ]


Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``USER``
     - :ref:`STRING literal<literals>`	
     - Optional parameter for filtering by username
   * - ``TIMEFRAME FROM``  
     - :ref:`STRING literal<literals>`	
     - Optional parameter for filtering based on time frame (must be used in combination with ``TO``)
   * - ``TIMEFRAME TO``  
     - :ref:`DATETIME<supported_data_types>`
     - Optional parameter for filtering by time frame (must be used in combination with ``FROM``)
   * - ``INITIATED BY``
     - :ref:`STRING literal<literals>`	
     - Optional parameter for filtering based on the source that triggered the query 
	 
	 
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``start_time``
     - ``DATE``
     - Displays the start time of the session
   * - ``database``
     - ``TEXT``
     - Displays the name of the database
   * - ``source_ip``
     - ``INTEGER``
     - Displays the IP address of the client connected to BLUE
   * - ``client``
     - ``TEXT``
     - Displays the name and version of the client
   * - ``status``
     - ``TEXT``
     - Displays the status of the client
   * - ``session_id``
     - ``TEXT``
     - Displays the session ID
   * - ``InitiatedBy``
     - ``TEXT``
     - Displays the source that triggered the query
	 
Examples
========

.. code-block:: postgres

	DESCRIBE SESSIONS;
	 
	+---------------------+----------------------+-----------+-------+----------------+----------------------+---------+-------------------+---------------------------------------+------------+------------+
	| start_time          | end_time             | database  | role  | source_ip      | client               | status  | rejection_reason  | session_id                            | username   |InitiatedBy |
	+=====================+======================+===========+=======+================+======================+=========+===================+=======================================+============+============+
	| 2022-09-20 6:46:47  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | e77075e0-51cc-4956-b192-b68ce17a4bc5  | sqream     |CLI         |
	| 2022-09-20 6:46:46  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | 6f2c3ee3-4f4b-48f2-90d3-458a26c2788c  | sqream     |CLI         |
	| 2022-09-20 6:46:46  | 0000-00-00 00:00:00  | master    | N/A   | 192.168.0.209  | SQream JDBC v0.1.54  | Active  | N/A               | e1e4ca64-5079-4e3d-bc47-c1216960ae0f  | sqream     |Jobs        |
	| 2022-09-20 5:23:27  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 4bad606f-696f-42a2-9df1-c9f3eb1cf801  | sqream     |Blue_UI_User|
	| 2022-09-20 5:22:28  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | c5d86508-86e1-490f-8421-d2bfbc3f062c  | sqream     |Blue_UI_User|
	| 2022-09-20 5:19:39  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | a6485840-1191-4154-a303-7872a466ac70  | sqream     |Blue_UI_User|
	| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 2aaf1e33-3b55-4b2b-8fe9-c837d700665d  | sqream     |Blue_UI_User|
	| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | 8f3c91b7-816e-4e36-b999-e4853e4fe255  | sqream     |Blue_UI_User|
	| 2022-09-20 5:19:25  | 0000-00-00 00:00:00  | master    | N/A   | 10.233.84.4    | SQream Node.js       | Active  | N/A               | ca5b1c86-a696-49f9-bc72-6fff76691799  | sqream     |Blue_UI_User|
	+---------------------+----------------------+-----------+-------+----------------+----------------------+---------+-------------------+---------------------------------------+------------+------------+

.. code-block:: postgres

	DESCRIBE SESSIONS TIMEFRAME FROM '2022-09-19 10:00:00' TO '2022-09-19 16:00:00';

	+----------------------+----------------------+-----------+-------+---------------+----------------------+---------+-------------------+---------------------------------------+------------+------------+
	| start_time           | end_time             | database  | role  | source_ip     | client               | status  | rejection_reason  | session_id                            | username   |InitiatedBy |
	+======================+======================+===========+=======+===============+======================+=========+===================+=======================================+============+============+
	| 2022-09-19 15:32:49  | 2022-09-19 15:32:55  | master    | N/A   | 192.168.4.69  | SQream JDBC v0.1.33  | Closed  | N/A               | dd40f403-ba34-460c-835b-2161a59f52a3  | sqream     |CLI         |
	| 2022-09-19 15:27:04  | 2022-09-19 15:27:04  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | 914869f7-d4f4-45ea-9563-68eeb2ea3189  | sqream     |CLI         |
	| 2022-09-19 14:08:50  | 2022-09-19 14:08:59  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | a4dfa69a-a73e-4731-81e5-b7c87dd8dc7b  | sqream     |Blue_UI_User|
	| 2022-09-19 14:08:38  | 2022-09-19 14:08:48  | master    | N/A   | 192.168.2.31  | SQream JDBC v0.1.33  | Closed  | N/A               | c3339342-02fa-49e8-b7f1-1172d577c5b7  | sqream     |Jobs        |
	+----------------------+----------------------+-----------+-------+---------------+----------------------+---------+-------------------+---------------------------------------+------------+------------+


Permissions
===========

A user may execute ``DESCRIBE SESSIONS`` to list his sessions.

``SUPERUSER`` may execute ``DESCRIBE SESSIONS`` to list any session by any user.
