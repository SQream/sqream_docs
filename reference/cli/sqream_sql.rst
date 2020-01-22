.. _sqream_sql_cli_reference:

*********************************
sqream sql CLI reference
*********************************

SQream DB comes with a built-in client for executing SQL statements either interactively or from the command-line.

This page serves as a reference for the options and parameters. Learn more about using SQream DB SQL with the CLI by visiting the :ref:`first_steps` tutorial.

.. contents:: In this topic:
   :local:

Running sqream sql
======================

``sqream sql`` can be found in the ``bin`` directory of your SQream DB installation, under the name ``sqream``.

.. versionchanged:: 2020.1
   Starting from version 2020.1, ``ClientCmd`` has been renamed to ``sqream sql``.

Using sqream sql
=================

By default, sqream sql runs in interactive mode. You can issue commands or SQL statements.

Running commands interactively (SQL shell)
--------------------------------------------

When starting sqream sql, after entering your password, you are presented with the SQL shell.

To exit the shell, type ``\q``  or :kbd:`Ctrl-d`. 

.. code-block:: psql

   $ sqream sql --port=5000 --username=jdoe --databasename=master
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

   $ sqream sql --port=5000 --username=mjordan -d master
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

   $ sqream sql --port=5000 --username=jdoe -d master -f sql_script.sql --results-only

.. tip:: Output can be saved to a file by using redirection (``>``).

Executing commands immediately (``-c``)
-------------------------------------------

To run a statement from the console, use the ``-c <statement>`` argument.

For example,

.. code-block:: console

   $ sqream sql --port=5000 --username=jdoe -d nba -c "SELECT TOP 5 * FROM nba"
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

   $ sqream sql --port=5000 --username=mjordan -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_

Connect to local server 127.0.0.1 via the built-in load balancer on port 3108, to the default built-in database, `master`:

.. code-block:: psql

   $ sqream sql --port=3105 --clustered --username=mjordan -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_

Execute statements in the interactive shell
-----------------------------------------------

Note that all SQL commands end with a semicolon.

Creating a new database and switching over to it without reconnecting:

.. code-block:: psql

   $ sqream sql --port=3105 --clustered --username=oldmcd -d master
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

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals WHERE is_angry = true"
   4,bull                          ,1
   1 row
   time: 0.095941s

.. _controlling_output:

Controlling the output of the client
----------------------------------------

Two parameters control the dispay of results from the client:

* ``--results-only`` - removes row counts and timing information
* ``--delimiter`` - changes the record delimiter

Export SQL query result to CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the ``--results-only`` flag removes the row counts and timing.

.. code-block:: console

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --results-only > file.csv
   $ cat file.csv
   1,goat                          ,0
   2,sow                           ,0
   3,chicken                       ,0
   4,bull                          ,1

Change a CSV to a TSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``--delimiter`` parameter accepts any printable character.

.. tip:: To insert a tab, use :kbd:`Ctrl-V` followed by :kbd:`Tab ↹` in Bash.

.. code-block:: console

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --delimiter '  ' > file.tsv
   $ cat file.tsv
   1  goat                             0
   2  sow                              0
   3  chicken                          0
   4  bull                             1


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

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -f some_queries.sql
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
   $ sqream sql --port=3105 --clustered --username=$SQREAM_USER -d $SQREAM_DATABASE

Connecting to a specific queue
-----------------------------------

When using the :ref:`dynamic workload manager<workload_manager>` - connect to ``etl`` queue instead of using the default ``sqream`` queue

.. code-block:: psql

   $ sqream sql --port=3105 --clustered --username=mjordan -d master --service=etl
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_


Operations and flag reference
===============================

Command line arguments
-----------------------

**SQream SQL** supports the following command line arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``-c`` or ``--command``
     - None
     - Changes the mode of operation to single-command, non-interactive. Use this argument to run a statement and immediately exit.
   * - ``-f`` or ``--file``
     - None
     - Changes the mode of operation to multi-command, non-interactive. Use this argument to run a sequence of statements from an external file and immediately exit.
   * - ``--host``
     - ``127.0.0.1``
     - Address of the SQream DB worker.
   * - ``--port``
     - ``5000``
     - Sets the connection port.
   * - ``--databasename`` or ``-d``
     - None
     - Specifies the database name for queries and statements in this session.
   * - ``--username``
     - None
     -  Username to connect to the specified database.
   * - ``--password``
     - None
     - Specify the password using the command line argument. If not specified, the client will prompt the user for the password.
   * - ``--clustered``
     - False
     - When used, the client connects to the load balancer, usually on port ``3108``. If not set, the client assumes the connection is to a standalone SQream DB worker.
   * - ``--service``
     - ``sqream``
     - :ref:`Service name (queue)<workload_manager>` that statements will file into.
   * - ``--results-only``
     - False
     - Outputs results only, without timing information and row counts
   * - ``--no-history``
     - False
     - When set, prevents command history from being saved in ``~/.sqream/clientcmdhist``
   * - ``--delimiter``
     - ``,``
     - Specifies the field separator. By default, ``sqream sql`` outputs valid CSVs. Change the delimiter to modify the output to another delimited format (e.g. TSV, PSV). See the section :ref:`supported record delimiters<supported_record_delimiters>` below for more information.

.. tip:: Run ``$  sqream sql --help`` to see a full list of arguments

.. _supported_record_delimiters: 

Supported record delimiters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The supported record delimiters are printable ASCII values (32-126).

* Recommended delimiters for use are: ``,``, ``|``, tab character.

* The following characters are **not supported**: ``\``, ``N``, ``-``, ``:``, ``"``, ``\n``, ``\r``, lower-case latin letters, digits (0-9)

Meta-commands
----------------

* Meta-commands in SQream SQL start with a backslash (``\``)

.. note:: Meta commands do not end with a semicolon

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Example
     - Description
   * - ``\q`` or ``\quit``
     - .. code-block:: psql
          
            master=> \q
     - Quit the client. (Same as :kbd:`Ctrl-d`)
   * - ``\c <database>`` or ``\connect <database>``
     - .. code-block:: psql
          
            master=> \c fox
            fox=>
     - Changes the current connection to an alternate database

Basic Commands
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-l`
     - Clear the screen.
   * - :kbd:`Ctrl-c`
     - Terminate the current command.
   * - :kbd:`Ctrl-z`
     - Suspend/stop the command.
   * - :kbd:`Ctrl-d`
     - Quit SQream SQL



Moving about the command line
---------------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-a`
     - go to the start of the command line 
   * - :kbd:`Ctrl-e`
     - go to the end of the command line 
   * - :kbd:`Ctrl-k`
     - delete from cursor to the end of the command line 
   * - :kbd:`Ctrl-u`
     - delete from cursor to the start of the command line 
   * - :kbd:`Ctrl-w`
     - delete from cursor to start of word (i.e. delete backwards one word) 
   * - :kbd:`Ctrl-y`
     - paste word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor 
   * - :kbd:`Alt-b`
     - move backward one word (or go to start of word the cursor is currently on)
   * - :kbd:`Alt-f`
     - move forward one word (or go to end of word the cursor is currently on) 
   * - :kbd:`Alt-d`
     - delete to end of word starting at cursor (whole word if cursor is at the beginning of word) 
   * - :kbd:`Alt-c`
     - capitalize to end of word starting at cursor (whole word if cursor is at the beginning of word) 
   * - :kbd:`Alt-u`
     - make uppercase from cursor to end of word 
   * - :kbd:`Alt-l`
     - make lowercase from cursor to end of word 
   * - :kbd:`Ctrl-f`
     - move forward one character 
   * - :kbd:`Ctrl-b`
     - move backward one character 
   * - :kbd:`Ctrl-h`
     - delete character before the cursor 
   * - :kbd:`Ctrl-t`
     - swap character under cursor with the previous one

Searching
------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-r`
     - search the history backwards
   * - :kbd:`Ctrl-g`
     - escape from history searching mode
   * - :kbd:`Ctrl-p`
     - previous command in history (i.e. walk back through the command history)
   * - :kbd:`Ctrl-n`
     - next command in history (i.e. walk forward through the command history)
