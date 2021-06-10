.. _sqream_sql_cli_reference:

*********************************
Sqream SQL CLI Reference
*********************************

SQream DB comes with a built-in client for executing SQL statements either interactively or from the command-line.

This page serves as a reference for the options and parameters. Learn more about using SQream DB SQL with the CLI by visiting the :ref:`first_steps` tutorial.

.. contents:: In this topic:
   :local:

Installing Sqream SQL
=========================

If you have a SQream DB installation on your server, ``sqream sql`` can be found in the ``bin`` directory of your SQream DB installation, under the name ``sqream``.

.. note:: If you installed SQream DB via Docker, the command is named ``sqream-client sql``, and can be found in the same location as the console.


.. versionchanged:: 2020.1
   As of version 2020.1, ``ClientCmd`` has been renamed to ``sqream sql``.
   

To run ``sqream sql`` on any other Linux host:

#. Download the ``sqream sql`` tarball package from the :ref:`client_drivers` page.
#. Untar the package: ``tar xf sqream-sql-v2020.1.1_stable.x86_64.tar.gz``
#. Start the client:
   
   .. code-block:: psql
      
      $ cd sqream-sql-v2020.1.1_stable.x86_64
      $ ./sqream sql --port=5000 --username=jdoe --databasename=master
      Password:
     
      Interactive client mode
      To quit, use ^D or \q.
      
      master=> _

Troubleshooting Sqream SQL Installation
-------------------------------------------

Upon running sqream sql for the first time, you may get an error ``error while loading shared libraries: libtinfo.so.5: cannot open shared object file: No such file or directory``.

Solving this error requires installing the ncruses or libtinfo libraries, depending on your operating system.

* Ubuntu:

   #. Install ``libtinfo``:
      
      ``$ sudo apt-get install -y libtinfo``
   #. Depending on your Ubuntu version, you may need to create a symbolic link to the newer libtinfo that was installed.
   
      For example, if ``libtinfo`` was installed as ``/lib/x86_64-linux-gnu/libtinfo.so.6.2``:
      
      ``$ sudo ln -s /lib/x86_64-linux-gnu/libtinfo.so.6.2 /lib/x86_64-linux-gnu/libtinfo.so.5``
      
* CentOS / RHEL:

   #. Install ``ncurses``:
   
      ``$ sudo yum install -y ncurses-libs``
   #. Depending on your RHEL version, you may need to create a symbolic link to the newer libtinfo that was installed.
   
      For example, if ``libtinfo`` was installed as ``/usr/lib64/libtinfo.so.6``:
      
      ``$ sudo ln -s /usr/lib64/libtinfo.so.6 /usr/lib64/libtinfo.so.5``

Using Sqream SQL
=================

By default, sqream sql runs in interactive mode. You can issue commands or SQL statements.

Running Commands Interactively (SQL shell)
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


Executing Batch Scripts (``-f``)
---------------------------------

To run an SQL script, use the ``-f <filename>`` argument.

For example,

.. code-block:: console

   $ sqream sql --port=5000 --username=jdoe -d master -f sql_script.sql --results-only

.. tip:: Output can be saved to a file by using redirection (``>``).

Executing Commands Immediately (``-c``)
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

Starting a Regular Interactive Shell
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

Executing Statements in an Interactive Shell
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

Executing SQL Statements from the Command Line
----------------------------------------------

.. code-block:: console

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals WHERE is_angry = true"
   4,bull                          ,1
   1 row
   time: 0.095941s

.. _controlling_output:

Controlling the Client Output
----------------------------------------

Two parameters control the dispay of results from the client:

* ``--results-only`` - removes row counts and timing information
* ``--delimiter`` - changes the record delimiter

Exporting SQL Query Results to CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the ``--results-only`` flag removes the row counts and timing.

.. code-block:: console

   $ sqream sql --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --results-only > file.csv
   $ cat file.csv
   1,goat                          ,0
   2,sow                           ,0
   3,chicken                       ,0
   4,bull                          ,1

Changing a CSV to a TSV
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


Executing a Series of Statements From a File
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

Connecting Using Environment Variables
-------------------------------------

You can save connection parameters as environment variables:

.. code-block:: console

   $ export SQREAM_USER=sqream;
   $ export SQREAM_DATABASE=farm;
   $ sqream sql --port=3105 --clustered --username=$SQREAM_USER -d $SQREAM_DATABASE

Connecting to a Specific Queue
-----------------------------------

When using the :ref:`dynamic workload manager<workload_manager>` - connect to ``etl`` queue instead of using the default ``sqream`` queue.

.. code-block:: psql

   $ sqream sql --port=3105 --clustered --username=mjordan -d master --service=etl
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=>_


Operations and Flag References
===============================

Command Line Arguments
-----------------------

**Sqream SQL** supports the following command line arguments:

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

Supported Record Delimiters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The supported record delimiters are printable ASCII values (32-126).

* Recommended delimiters for use are: ``,``, ``|``, tab character.

* The following characters are **not supported**: ``\``, ``N``, ``-``, ``:``, ``"``, ``\n``, ``\r``, ``.``, lower-case latin letters, digits (0-9)

Meta-Commands
----------------

* Meta-commands in Sqream SQL start with a backslash (``\``)

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
   :widths: 20 30 50
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



Moving Around the Command Line
---------------------------------

.. list-table:: 
   :widths: 17 83
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-a`
     - Goes to the beginning of the command line. 
   * - :kbd:`Ctrl-e`
     - Goes to the end of the command line. 
   * - :kbd:`Ctrl-u`
     - Deletes from cursor to the beginning of the command line. 
   * - :kbd:`Ctrl-k`
     - Deletes from the cursor to the end of the command line.
   * - :kbd:`Ctrl-w`
     - Delete from cursor to beginning of a word. 
   * - :kbd:`Ctrl-y`
     - Pastes a word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor. 
   * - :kbd:`Alt-b`
     - Moves back one word (or goes to the beginning of the word where the cursor is).
   * - :kbd:`Alt-f`
     - Moves forward one word (or goes to the end of word the cursor is). 
   * - :kbd:`Alt-d`
     - Deletes to the end of a word starting at the cursor. Deletes the whole word if the cursor is at the beginning of that word. 
   * - :kbd:`Alt-c`
     - Capitalizes letters in a word starting at the cursor. Capitalizes the whole word if the cursor is at the beginning of that word. 
   * - :kbd:`Alt-u`
     - Capitalizes from the cursor to the end of the word. 
   * - :kbd:`Alt-l`
     - Makes lowercase from the cursor to the end of the word. 
   * - :kbd:`Ctrl-f`
     - Moves forward one character. 
   * - :kbd:`Ctrl-b`
     - Moves backward one character. 
   * - :kbd:`Ctrl-h`
     - Deletes characters located before the cursor. 
   * - :kbd:`Ctrl-t`
     - Swaps a character at the cursor with the previous character.

Searching
------------

.. list-table:: 
   :widths: 17 83
   :header-rows: 1
   
   * - Command
     - Description
   * - :kbd:`Ctrl-r`
     - Searches the history backward.
   * - :kbd:`Ctrl-g`
     - Escapes from history-searching mode.
   * - :kbd:`Ctrl-p`
     - Searches the previous command in history.
   * - :kbd:`Ctrl-n`
     - Searches the next command in history.