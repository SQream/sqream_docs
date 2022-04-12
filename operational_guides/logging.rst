.. _logging:

***********************
Logging
***********************

Locating the Log Files
==========================

The :ref:`storage cluster<storage_cluster>` contains a ``logs`` directory. Each worker produces a log file in its own directory, which can be identified by the worker's hostname and port.

.. TODO: expand this by giving some use caes for working with log files directly in sqream (troubleshooting, performance analysis, monitoring, that kind of thing. Stick to things customers actually use and/or we instruct them to do with the logs, not theoretical things they could do with the logs

.. note:: Additional internal debug logs may reside in the main ``logs`` directory.

The worker logs contain information messages, warnings, and errors pertaining to SQream DB's operation, including:

* Server start-up and shutdown
* Configuration changes
* Exceptions and errors
* User login events
* Session events
* Statement execution success / failure 
* Statement execution statistics

Log Structure and Contents
---------------------------------

The log is a CSV, with several fields.

.. list-table:: Log fields
   :widths: auto
   :header-rows: 1
   
   * - Field
     - Description
   * - ``#SQ#``
     - Start delimiter. When used with the end of line delimiter can be used to parse multi-line statements correctly
   * - Row Id
     - Unique identifier for the row
   * - Timestamp
     - Timestamp for the message (ISO 8601 date format)
   * - Information Level
     - Information level of the message. See :ref:`information level table<information_level>` below
   * - Thread Id
     - System thread identifier (internal use)
   * - Worker hostname
     - Hostname of the worker that generated the message
   * - Worker port
     - Port of the worker that generated the message
   * - Connection Id
     - Connection Id for the message. Defaults to ``-1`` if no connection
   * - Database name
     - Database name that generated the message. Can be empty for no database
   * - User Id
     - User role that was connected during the message. Can be empty if no user caused the message
   * - Statement Id
     - Statement Id for the message. Defaults to ``-1`` if no statement
   * - Service name
     - Service name for the connection. Can be empty.
   * - Message type Id
     - Message type Id. See :ref:`message type table<message_type>` below)
   * - Message
     - Content for the message
   * - ``#EOM#``
     - End of line delimiter 


.. _information_level:

.. list-table:: Information Level
   :widths: auto
   :header-rows: 1
   
   * - Level
     - Description
   * - ``SYSTEM``
     - System information like start up, shutdown, configuration change
   * - ``FATAL``
     - Fatal errors that may cause outage
   * - ``ERROR``
     - Errors encountered during statement execution
   * - ``WARNING``
     - Warnings
   * - ``INFO``
     - Information and statistics

.. _message_type:

.. list-table:: Message Type
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Level
     - Description
     - Example message content
   * - ``1``
     - ``INFO``
     - Statement start information
     - 
         * ``"Query before parsing`` (statement handle opened)
         * ``"SELECT * FROM nba WHERE ""Team"" NOT LIKE ""Portland%%"""`` (statement preparing)
   * - ``2``
     - ``INFO``
     - Statement passed to another worker for execution
     - 
         * ``""Reconstruct query before parsing"``
         * ``"SELECT * FROM nba WHERE ""Team"" NOT LIKE ""Portland%%"""`` (statement preparing on node)
   * - ``4``
     - ``INFO``
     - Statement has entered execution
     - ``"Statement execution"``
   * - ``10``
     - ``INFO``
     - Statement execution completed
     - ``"Success"`` / ``"Failed"``
   * - ``20``
     - ``INFO``
     - Compilation error, with accompanying error message
     - ``"Could not find function dateplart in catalog."``
   * - ``21``
     - ``INFO``
     - Execution error, with accompanying error message
     - ``Error text``
   * - ``30``
     - ``INFO``
     - Size of data read from disk in megabytes
     - ``18``
   * - ``31``
     - ``INFO``
     - Row count of result set
     - ``45``
   * - ``32``
     - ``INFO``
     - Processed Rows
     - ``450134749978``
   * - ``100``
     - ``INFO``
     - Session start - Client IP address
     - ``"192.168.5.5"``
   * - ``101``
     - ``INFO``
     - Login
     - ``"Login Success"`` / ``"Login Failed"``
   * - ``110``
     - ``INFO``
     - Session end
     - ``"Session ended"``
   * - ``200``
     - ``INFO``
     - :ref:`show_node_info` periodic output
     - 
   * - ``500``
     - ``ERROR``
     - Exception occured in a statement
     - ``"Cannot return the inverse cosine of a number not in [-1,1] range"``
   * - ``1000``
     - ``SYSTEM``
     - Worker startup message
     - ``"Server Start Time - 2019-12-30 21:18:31, SQream ver{v2020.2}"``
   * - ``1002``
     - ``SYSTEM``
     - ``Metadata``
     - ``Metadata server location``
   * - ``1003``
     - ``SYSTEM``
     - Show all configuration values
     - .. code-block:: none
          
          "Flags configuration:
             compileFlags, extendedAssertions, false, true;
             compileFlags, useSortMergeJoin, false, false;
             compileFlags, distinctAggregatesOnHost, true, false;
             [...]"

   * - ``1004``
     - ``SYSTEM``
     - SQream DB metadata version
     - ``"23"``
   * - ``1010``
     - ``FATAL``
     - Fatal server error
     - ``"Mismatch in storage version, upgrade is needed,Storage version: 22, Server version is: 23"``
   * - ``1090``
     - ``INFO``
     - Configuration change
     - ``Successful set config useSortMergeJoin to value: true``
   * - ``1100``
     - ``SYSTEM``
     - Worker shutdown
     - ``"Server shutdown"``

Log-Naming
---------------------------

Log file name syntax

``sqream_<date>_<sequence>.log``

* 
   ``date`` is formatted ``%y%m%d``, for example ``20191231`` for December 31st 2019.
   
   By default, each worker will create a new log file every time it is restarted.

* ``sequence`` is the log's sequence. When a log is rotated, the sequence number increases. This starts at ``000``.

For example, ``/home/rhendricks/sqream_storage/192.168.1.91_5000``.

See the :ref:`log_rotation` below for information about controlling this setting.


Log Control and Maintenance
======================================

Changing Log Verbosity
--------------------------

A few configuration settings alter the verbosity of the logs:

.. list-table:: Log verbosity configuration
   :widths: auto
   :header-rows: 1
   
   * - Flag
     - Description
     - Default
     - Values
   * - ``logClientLevel``
     - Used to control which log level should appear in the logs
     - ``4`` (``INFO``)
     - ``0`` SYSTEM (lowest) - ``4`` INFO (highest).  See :ref:`information level table<information_level>` above.
   * - ``nodeInfoLoggingSec``
     -   
         Sets an interval for automatically logging long-running statements' :ref:`show_node_info` output.
         Output is written as a message type ``200``.
     - ``60`` (every minute)  
     - Positive whole number >=1.

.. _log_rotation:

Changing Log Rotation
-----------------------

A few configuration settings alter the log rotation policy:

.. list-table:: Log rotation configuration
   :widths: auto
   :header-rows: 1
   
   * - Flag
     - Description
     - Default
     - Values
   * - ``useLogMaxFileSize``
     - Rotate log files once they reach a certain file size. When ``true``, set the ``logMaxFileSizeMB`` accordingly.
     - ``false``
     - ``false`` or ``true``.
   * - ``logMaxFileSizeMB``
     - Sets the size threshold in megabytes after which a new log file will be opened.
     - ``20``
     - ``1`` to ``1024`` (1MB to 1GB)
   * - ``logFileRotateTimeFrequency``
     - Frequency of log rotation
     - ``never``
     - ``daily``, ``weekly``, ``monthly``, ``never``

.. _collecting_logs2:

Collecting Logs from Your Cluster
====================================

Collecting logs from your cluster can be as simple as creating an archive from the ``logs`` subdirectory: ``tar -czvf logs.tgz *.log``.

However, SQream DB comes bundled with a data collection utility and an SQL utility intended for collecting logs and additional information that can help SQream support drill down into possible issues.

SQL Syntax
----------

.. code-block:: postgres
   
   SELECT REPORT_COLLECTION(output_path, mode)
   ;
   
   output_path ::= 
      filepath
   
   mode ::= 
      log | db | db_and_log
   

Command Line Utility
--------------------------

If you cannot access SQream DB for any reason, you can also use a command line toolto collect the same information:

.. code-block:: console
   
   $ ./bin/report_collection <path to storage> <path for output> <mode>


Parameters
---------------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``output_path``
     - Path for the output archive. The output file will be named ``report_<date>_<time>.tar``.
   * - ``mode``
     - 
         One of three modes:
         * ``'log'`` - Collects all log files
         * ``'db'`` - Collects the metadata database (includes DDL, but no data)
         * ``'db_and_log'`` - Collect both log files and metadata database

Example
-----------------

Write an archive to ``/home/rhendricks``, containing log files:

.. code-block:: postgres
   
   SELECT REPORT_COLLECTION('/home/rhendricks', 'log')
   ;

Write an archive to ``/home/rhendricks``, containing log files and metadata database:

.. code-block:: postgres
   
   SELECT REPORT_COLLECTION('/home/rhendricks', 'db_and_log')
   ;
   

Using the command line utility:

.. code-block:: console
   
   $ ./bin/report_collection /home/rhendricks/sqream_storage /home/rhendricks db_and_log


Troubleshooting with Logs
===============================

Loading Logs with Foreign Tables
---------------------------------------

Assuming logs are stored at ``/home/rhendricks/sqream_storage/logs/``, a database administrator can access the logs using the :ref:`external_tables` concept through SQream DB.

.. code-block:: postgres

   CREATE FOREIGN TABLE logs 
   (
     start_marker      VARCHAR(4),
     row_id            BIGINT,
     timestamp         DATETIME,
     message_level     TEXT,
     thread_id         TEXT,
     worker_hostname   TEXT,
     worker_port       INT,
     connection_id     INT,
     database_name     TEXT,
     user_name         TEXT,
     statement_id      INT,
     service_name      TEXT,
     message_type_id   INT,
     message           TEXT,
     end_message       VARCHAR(5)
   )
   WRAPPER csv_fdw
   OPTIONS
     (
        LOCATION = '/home/rhendricks/sqream_storage/logs/**/sqream*.log',
        DELIMITER = '|',
        CONTINUE_ON_ERROR = true
     )
   ;
   
For more information, see `Loading Logs with Foreign Tables <https://docs.sqream.com/en/latest/reference/sql/sql_statements/dml_commands/copy_from.html>`_.




Counting Message Types
------------------------------

.. code-block:: psql

   t=> SELECT message_type_id, COUNT(*) FROM logs GROUP BY 1;
   message_type_id | count
   ----------------+----------
                 0 |         9
                 1 |      5578
                 4 |      2319
                10 |      2788
                20 |       549
                30 |       411
                31 |      1720
                32 |      1720
               100 |      2592
               101 |      2598
               110 |      2571
               200 |        11
               500 |       136
              1000 |        19
              1003 |        19
              1004 |        19
              1010 |         5

Finding Fatal Errors
----------------------

.. code-block:: psql

   t=> SELECT message FROM logs WHERE message_type_id=1010;
   Internal Runtime Error,open cluster metadata database:IO error: lock /home/rhendricks/sqream_storage/leveldb/LOCK: Resource temporarily unavailable
   Internal Runtime Error,open cluster metadata database:IO error: lock /home/rhendricks/sqream_storage/leveldb/LOCK: Resource temporarily unavailable
   Mismatch in storage version, upgrade is needed,Storage version: 25, Server version is: 26
   Mismatch in storage version, upgrade is needed,Storage version: 25, Server version is: 26
   Internal Runtime Error,open cluster metadata database:IO error: lock /home/rhendricks/sqream_storage/LOCK: Resource temporarily unavailable

Countng Error Events Within a Certain Timeframe
---------------------------------------------------

.. code-block:: psql

   t=> SELECT message_type_id,
   .          COUNT(*)
   .   FROM logs
   .   WHERE message_type_id IN (1010,500)
   .   AND timestamp BETWEEN '2019-12-20' AND '2020-01-01'
   .   GROUP BY 1;
   message_type_id | count
   ----------------+------
               500 |    18
              1010 |     3


.. _tracing_errors:

Tracing Errors to Find Offending Statements
-------------------------------------------------

If we know an error occured, but don't know which statement caused it, we can find it using the connection ID and statement ID.

.. code-block:: psql

   t=> SELECT connection_id, statement_id, message
   .     FROM logs
   .     WHERE message_level = 'ERROR'
   .     AND timestamp BETWEEN '2020-01-01' AND '2020-01-06';
   connection_id | statement_id | message                                                                                                                                                          
   --------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------
              79 |           67 | Column type mismatch, expected UByte, got INT64 on column Number, file name: /home/sqream/nba.parquet                                                            

Use the ``connection_id`` and ``statement_id`` to narrow down the results.

.. code-block:: psql
   
   t=>   SELECT database_name, message FROM logs
   .       WHERE connection_id=79 AND statement_id=67 AND message_type_id=1;
   database_name | message                  
   --------------+--------------------------
   master        | Query before parsing     
   master        | SELECT * FROM nba_parquet



.. how logs are read with csvkit, find a better working solution
