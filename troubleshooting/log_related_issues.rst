.. _log_related_issues:

***********************
Log Related Issues
***********************
The **Log Related Issues** page describes how to resolve the following common issues:

.. toctree::
   :maxdepth: 2
   :glob:
   :titlesonly:

Loading Logs with Foreign Tables
---------------------------------------
Assuming logs are stored at ``/home/rhendricks/sqream_storage/logs/``, a database administrator can access the logs using the :ref:`external_tables` concept through SQream DB.

.. code-block:: postgres

   CREATE FOREIGN TABLE logs 
   (
     start_marker      TEXT,
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
     end_message       TEXT
   )
   WRAPPER csv_fdw
   OPTIONS
     (
        LOCATION = '/home/rhendricks/sqream_storage/logs/**/sqream*.log',
        DELIMITER = '|',
        CONTINUE_ON_ERROR = true
     )
   ;
   
For more information, see `Loading Logs with Foreign Tables <https://docs.sqream.com/en/v2020.3.2/reference/sql/sql_statements/dml_commands/copy_from.html>`_.





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