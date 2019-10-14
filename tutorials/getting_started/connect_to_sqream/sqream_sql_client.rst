.. _sqream_sql_client:

*************************
SQream SQL Client (CLI)
*************************

SQream DB comes with a built-in client for executing SQL statements either interactively or from the command-line.

.. contents:: In this topic:
   :local:

Running SQream SQL
======================

**SQream SQL** can be found in the ``bin`` directory of your SQream DB installation, under the name ``ClientCmd``.

.. versionchanged:: 2019.3
   Starting from version 2019.3, ``ClientCmd`` has been renamed to ``sqream sql``.

Using SQream SQL
=================

By default, SQream SQL runs in interactive mode. You can issue commands or SQL statements.

Running commands interactively (SQL shell)
--------------------------------------------

When starting SQream SQL, after entering your password, you are presented with the SQL shell.

To exit the shell, type ``\q``  or :kbd:`Ctrl-d`. 

.. code-block:: psql

   $ ClientCmd --port=5000 --username=jdoe -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

The database name shown means you are now ready to run statements and queries.

Statements and queries are standard SQL, followed by a semicolon (``;``). Statement results are usually formatted as a valid CSV, 
followed by the number of rows and the elapsed time for that statement.

.. code-block:: psql

   master=> SELECT TOP 5 * FROM nba;
   Avery Bradley           ,Boston Celtics        ,0,PG,25,6-2 ,180,Texas                ,7730337
   Jae Crowder             ,Boston Celtics        ,99,SF,25,6-6 ,235,Marquette            ,6796117
   John Holland            ,Boston Celtics        ,30,SG,27,6-5 ,205,Boston University    ,\N
   R.J. Hunter             ,Boston Celtics        ,28,SG,22,6-5 ,185,Georgia State        ,1148640
   Jonas Jerebko           ,Boston Celtics        ,8,PF,29,6-10,231,\N,5000000
   5 rows
   time: 0.001185s

.. note:: Null values are represented as \\N.

When writing long statements and queries, it may be beneficial to use line-breaks.
The prompt for a multi-line statement will change from ``=>`` to ``.``, to alert users to the change. The statement will not execute until a semicolon is used.


.. code-block:: psql
   :emphasize-lines: 13

   $ ClientCmd --port=5000 --username=mjordan -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> SELECT "Age",
   . AVG("Salary")
   . FROM NBA
   . GROUP BY 1
   . ORDER BY 2 ASC
   . LIMIT 5
   . ;
   38,1840041
   19,1930440
   23,2034746
   21,2067379
   36,2238119
   5 rows
   time: 0.009320s


Executing batch scripts (``-f``)
---------------------------------

To run an SQL script, use the ``-f <filename>`` argument.

For example,

.. code-block:: console

   $ ClientCmd --port=5000 --username=jdoe -d master -f sql_script.sql --results-only

.. tip:: Output can be saved to a file by using redirection (``>``).

Executing commands immediately (``-c``)
-------------------------------------------

To run a statement from the console, use the ``-c <statement>`` argument.

For example,

.. code-block:: console

   $ ClientCmd --port=5000 --username=jdoe -d nba -c "SELECT TOP 5 * FROM nba"
   Avery Bradley           ,Boston Celtics        ,0,PG,25,6-2 ,180,Texas                ,7730337
   Jae Crowder             ,Boston Celtics        ,99,SF,25,6-6 ,235,Marquette            ,6796117
   John Holland            ,Boston Celtics        ,30,SG,27,6-5 ,205,Boston University    ,\N
   R.J. Hunter             ,Boston Celtics        ,28,SG,22,6-5 ,185,Georgia State        ,1148640
   Jonas Jerebko           ,Boston Celtics        ,8,PF,29,6-10,231,\N,5000000
   5 rows
   time: 0.202618s

.. tip:: Remove the timing and row count by passing the ``--results-only`` parameter

Examples
===========

Start a regular interactive shell
-----------------------------------

Connect to local server 127.0.0.1 on port 5000, to the default built-in database, `master`:

.. code-block:: psql

   $ ClientCmd --port=5000 --username=mjordan -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_

Connect to local server 127.0.0.1 via the built-in load balancer on port 3108, to the default built-in database, `master`:

.. code-block:: psql

   $ ClientCmd --port=3105 --clustered --username=mjordan -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_

Execute statements in the interactive shell
-----------------------------------------------

Note that all SQL commands end with a semicolon.

Creating a new database and switching over to it without reconnecting:

.. code-block:: psql

   $ ClientCmd --port=3105 --clustered --username=oldmcd -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> create database farm;
   executed
   time: 0.003811s
   master=> \c farm
   farm=>

.. code-block:: psql

   farm=> create table animals(id int not null, name varchar(30) not null, is_angry bool not null);
   executed
   time: 0.011940s

   farm=> insert into animals values(1,'goat',false);
   executed
   time: 0.000405s

   farm=> insert into animals values(4,'bull',true) ;
   executed
   time: 0.049338s

   farm=> select * from animals;
   1,goat                          ,0
   4,bull                          ,1
   2 rows
   time: 0.029299s

Execute SQL statements from the command line
----------------------------------------------

.. code-block:: console

   $ ClientCmd --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals WHERE is_angry = true"
   4,bull                          ,1
   1 row
   time: 0.095941s

Export SQL query result to CSV
--------------------------------

Using the ``--results-only`` flag removes the row counts and timing.

.. code-block:: console

   $ ClientCmd --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --results-only
   1,goat                          ,0
   2,sow                           ,0
   3,chicken                       ,0
   4,bull                          ,1


Execute a series of statements from a file
--------------------------------------------

Assuming a file containing SQL statements (separated by semicolons):

.. code-block:: console

   $ cat some_queries.sql
      CREATE TABLE calm_farm_animals 
     ( id INT IDENTITY(0, 1), name VARCHAR(30) 
     ); 

   INSERT INTO calm_farm_animals (name) 
     SELECT name FROM   animals WHERE  is_angry = false; 

.. code-block:: console

   $ ClientCmd --port=3105 --clustered --username=oldmcd -d farm -f some_queries.sql
   executed
   time: 0.018289s
   executed
   time: 0.090697s

Connect using environment variables
-------------------------------------

You can save connection parameters as environment variables:

.. code-block:: console

   $ export SQREAM_USER=sqream;
   $ export SQREAM_DATABASE=farm;
   $ ClientCmd --port=3105 --clustered --username=$SQREAM_USER -d $SQREAM_DATABASE


Operations and flag reference
===============================

For the full operations reference, see :ref:`the SQream SQL (CLI) Reference <sqream_sql_cli_reference>`.

.. include:: /reference/cli/sqream_sql.rst
   :start-line: 11
   :end-line: 105