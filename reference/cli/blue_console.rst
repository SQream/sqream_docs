.. _blue_console:

************************
BLUE Console
************************

BLUE has a native client program that provides a command-line interface (CLI) for interacting with your on-line stored data. It allows you to connect to database servers, execute SQL queries and commands, and receive the results in a text-based format.


Running BLUE CLI
================

BLUE CLI is Java based and may be run on any Java supported platform - use the following link to check supported platforms and download `Java 11 <https://www.oracle.com/java/technologies/downloads/#java11>`_.

#. Using the BLUE web interface, generate and copy an access token.
   
   For instruction on how to generate and copy access tokens, go to the :ref:access_tokens

#. Start the client by browsing your CLI for the location of the ``jdbc-console-*.*.**.jar`` file and execute it as follows:

.. code-block:: console

	$ sudo java -jar jdbc-console-*.*.**.jar --host=<BLUE cluster IP FQDN> --access-token=<#####################################>
	
	Output:
	
	Welcome to JDBC console, SQream DB version 2.0.0
	To quit exit; to abort ^c
	Connection URL jdbc:Sqream://<BLUE cluster IP FQDN>:<port>/<database name>;--access-token=<#####################################>;[<optional parameters>; ...]
	master=>


Running Commands Interactively (SQL shell)
------------------------------------------

After entering your access token, you are presented with the **SQL shell**. The database name shown means you are now ready to run statements and queries. 

**SQL shell** control commands:

+-----------------------+----------------------------+
| Command               | Description                |
+=======================+============================+
| ``Ctrl-d``, ``exit;`` | Exit the SQL Shell         |
+-----------------------+----------------------------+
| ``^c``                | Abort a statement or query |
+-----------------------+----------------------------+


Statements and queries are standard SQL, followed by a semicolon ``;``.

.. code-block:: console
 
	master=> CREATE TABLE nba (
	  player_name TEXT,
	  team_name TEXT,
	  jersey_number INT,
	  position TEXT,
	  age INT,
	  height TEXT,
	  weight INT,
	  college TEXT,
	  salary INT
	);
	
.. code-block:: console

	INSERT INTO nba VALUES
	  ('Avery Bradley', 'Boston Celtics', 0, 'PG', 25, '6-2', 180, 'Texas', 7730337),
	  ('Jae Crowder', 'Boston Celtics', 99, 'SF', 25, '6-6', 235, 'Marquette', 6796117),
	  ('John Holland', 'Boston Celtics', 30, 'SG', 27, '6-5', 205, 'Boston University', NULL),
	  ('R.J. Hunter', 'Boston Celtics', 28, 'SG', 22, '6-5', 185, 'Georgia State', 1148640),
	  ('Jonas Jerebko', 'Boston Celtics', 8, 'PF', 29, '6-10', 231, NULL, 5000000);

Statement results are usually formatted as a valid CSV, followed by the number of rows and the elapsed time for that statement. 

Null values are represented as ``\N``.

.. code-block:: console

	master=> SELECT TOP 5 * FROM nba;
	Avery Bradley           ,Boston Celtics        ,0,PG,25,6-2 ,180,Texas                ,7730337
	Jae Crowder             ,Boston Celtics        ,99,SF,25,6-6 ,235,Marquette            ,6796117
	John Holland            ,Boston Celtics        ,30,SG,27,6-5 ,205,Boston University    ,\N
	R.J. Hunter             ,Boston Celtics        ,28,SG,22,6-5 ,185,Georgia State        ,1148640
	Jonas Jerebko           ,Boston Celtics        ,8,PF,29,6-10,231,\N,5000000
	5 rows
	time: 0.001185s

	
	
When writing long statements and queries, it may be beneficial to use line-breaks. The prompt for a multi-line statement will change from => to ., to alert users to the change. The statement will not execute until a semicolon is used.

.. code-block:: console

	master=> SELECT Age, AVG(Salary)
	FROM nba
	GROUP BY 1
	ORDER BY 2 ASC
	LIMIT 5
	;


	27,\N
	22,1148640
	29,5000000
	25,7263227
	4 rows
	time: 0.604 s
	
Executing Batch Scripts (-f)
----------------------------	

To run an SQL script, use the ``-f <filename>`` argument.
For example,

.. code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=5000 --username=jdoe -d master -f sql_script.sql --results-only
	 
.. tip::

	Output can be saved to a file by using redirection (>).
	
Executing Commands Immediately (-c)
-----------------------------------

To run a statement from the console, use the ``-c <statement>`` argument.

For example,

.. code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=5000 --username=jdoe -d nba -c "SELECT TOP 5 * FROM nba"
	Avery Bradley           ,Boston Celtics        ,0,PG,25,6-2 ,180,Texas                ,7730337
	Jae Crowder             ,Boston Celtics        ,99,SF,25,6-6 ,235,Marquette            ,6796117
	John Holland            ,Boston Celtics        ,30,SG,27,6-5 ,205,Boston University    ,\N
	R.J. Hunter             ,Boston Celtics        ,28,SG,22,6-5 ,185,Georgia State        ,1148640
	Jonas Jerebko           ,Boston Celtics        ,8,PF,29,6-10,231,\N,5000000
	5 rows
	time: 0.202618s

.. tip::

	Remove the timing and row count by passing the ``--results-only`` parameter.

Examples
========

Executing Statements in an Interactive Shell
--------------------------------------------

Note that all SQL commands end with a semicolon.

Creating a new database and switching over to it without reconnecting:

.. code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=oldmcd -d master


	Interactive client mode
	To quit, use ^D or \q.

	master=> create database farm;
	executed
	time: 0.003811s
	master=> \c farm
	farm=>


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

.. code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals WHERE is_angry = true"
	4,bull                          ,1
	1 row
	time: 0.095941s
	
Controlling the Client Output
-----------------------------

Two parameters control the client result display:

+-----------------------+---------------------------------------------------+
| Parameter             | Description                                       |
+=======================+===================================================+
| ``--results-only``    | Removes row counts and timing information         |
+-----------------------+---------------------------------------------------+
| ``--delimiter``       | Changes the record delimiter                      |
+-----------------------+---------------------------------------------------+

Exporting SQL Query Results to CSV
----------------------------------

Using the ``--results-only`` flag removes the row counts and timing.

..code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --results-only > file.csv
	$ cat file.csv
	1,goat                          ,0
	2,sow                           ,0
	3,chicken                       ,0
	4,bull                          ,1
	
Changing a CSV to a TSV
-----------------------

The ``--delimiter`` parameter accepts any printable character.

.. tip::

	To insert a tab, use ``Ctrl-V`` followed by ``Tab`` in Bash.

.. code-block::

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=oldmcd -d farm -c "SELECT * FROM animals" --delimiter '  ' > file.tsv
	$ cat file.tsv
	1  goat                             0
	2  sow                              0
	3  chicken                          0
	4  bull                             1

Executing a Series of Statements From a File
-------------------------------------------- 

Assuming a file containing SQL statements (separated by semicolons):

.. code-block::

	$ cat some_queries.sql
	   CREATE TABLE calm_farm_animals
	  ( id INT IDENTITY(0, 1), name VARCHAR(30)
	  );

	INSERT INTO calm_farm_animals (name)
	  SELECT name FROM   animals WHERE  is_angry = false;


	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=oldmcd -d farm -f some_queries.sql
	executed
	time: 0.018289s
	executed
	time: 0.090697s

Connecting Using Environment Variables in Linux environments
------------------------------------------------------------

.. code-block::

	You can save connection parameters as environment variables:
	$ export SQREAM_USER=sqream;
	$ export SQREAM_DATABASE=farm;
	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=3105 --clustered --username=$SQREAM_USER -d $SQREAM_DATABASE

Operations and Flag References
==============================

Command Line Arguments
----------------------

Sqream SQL supports the following command line arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``-c`` or ``command``
     - None
     - Changes the mode of operation to single-command, non-interactive. Use this argument to run a statement and immediately exit.
   * - ``-f`` or ``--file``
     - None
     - Changes the mode of operation to multi-command, non-interactive. Use this argument to run a sequence of statements from an external file and immediately exit.
   * - ``--host``
     - 
     - Fully Qualified Domain Name (FQDN) address of the Blue server to connect to
   * - ``--databasename`` or ``-d``
     - None
     - Specifies the database name for queries and statements in this session.
   * - ``results-only``
     - False
     - Outputs results only, without timing information and row counts
   * - ``no-history``
     - False
     - When set, prevents command history from being saved in ``~/.sqream/clientcmdhist``
   * - ``delimiter``
     - ``,``
     - Specifies the field separator. By default, ``sqream sql`` outputs valid CSVs. Change the delimiter to modify the output to another delimited format (e.g. TSV, PSV). See the section supported record delimiters below for more information.
   * - ``access-token``
     - None
     - Provide a security token that grants access to protected resources or operations.

.. tip::

	Run ``$  java -jar jdbc-console-*.*.**.jar  --help`` to see a full list of arguments.
	
Supported Record Delimiters
---------------------------

The supported record delimiters are printable ASCII values (32-126).

* Recommended delimiters for use are: ``,``, ``|``, tab character.
* The following characters are **not supported**: ``\, N, -, :, ", \n, \r, .,`` lower-case latin letters, digits (0-9)

Meta-Commands
-------------

* Meta-commands in Sqream SQL start with a backslash (\)

.. note::

	Meta commands do not end with a semicolon.
	
.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Example
     - Description
   * - ``^c``
     - 
     - Abort the currently running statement 
   * - ``^d`` or ``exit``
     - ``master=> exit;``
     - Quit the client. (Same as ``Ctrl-d``)
   * - ``\c <database> or \connect <database>``
     - ``master=> \c fox`` 
       ``fox=>``
     - Changes the current connection to an alternate database
	 
Moving Around the Command Line
==============================

Note: below shortcuts are only supported for Linux environments 

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
   * - ``Ctrl-a``
     - Goes to the beginning of the command line.
   * - ``Ctrl-e``
     - Goes to the end of the command line.
   * - ``Ctrl-u``
     - Deletes from cursor to the beginning of the command line.
   * - ``Ctrl-k``
     - Deletes from the cursor to the end of the command line.
   * - ``Ctrl-w``
     - Delete from cursor to beginning of a word.
   * - ``Ctrl-y``
     - Pastes a word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor. 
   * - ``Alt-b``
     - Moves back one word (or goes to the beginning of the word where the cursor is).
   * - ``Alt-f``
     - Moves forward one word (or goes to the end of word the cursor is).
   * - ``Alt-d``
     - Deletes to the end of a word starting at the cursor. Deletes the whole word if the cursor is at the beginning of that word.
   * - ``Alt-c``
     - Capitalizes letters in a word starting at the cursor. Capitalizes the whole word if the cursor is at the beginning of that word.
   * - ``Alt-u``
     - Capitalizes from the cursor to the end of the word.
   * - ``Alt-l``
     - Makes lowercase from the cursor to the end of the word.
   * - ``Ctrl-f``
     - Moves forward one character.
   * - ``Ctrl-b``
     - Moves backward one character.
   * - ``Ctrl-h``
     - Deletes characters located before the cursor.
   * - ``Ctrl-t``
     - Swaps a character at the cursor with the previous character.

	 
Searching
---------

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Command
     - Description
   * - ``Ctrl-r``
     - Searches the history backward.
   * - ``Ctrl-g``
     - Escapes from history-searching mode.
   * - ``Ctrl-p``
     - Searches the previous command in history.
   * - ``Ctrl-n``
     - Searches the next command in history.

