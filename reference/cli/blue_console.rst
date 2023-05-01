.. _blue_console:

************
Sqream SQL CLI Reference
************

SQream DB has a native client for executing SQL statements either interactively or from the command-line.
This page serves as a reference for the options and parameters.




Installing Sqream SQL
=====================

SQream CLI is Java based and may be run on any Java supported platform - use the following link to check supported platforms and download Java 11 https://www.oracle.com/java/technologies/downloads/#java11

Start the client:
Browse to the location of the ``jdbc-console-*.*.**.jar`` file and execute it as follows:

.. code-block:: console

	$ sudo java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	$ 
	Welcome to JDBC console
	To quit, use ^C or exit
	Connection URLjdbc:Sqream://[SQream cluster IP address]:[SQream cluster port]/master;user=[username];password=[password];cluster=false
	master=> _

	master=> _


Using Sqream SQL
================

By default, sqream sql runs in interactive mode. You can issue commands or SQL statements.

Running Commands Interactively (SQL shell)
------------------------------------------

When starting sqream sql, after entering your password, you are presented with the SQL shell.
To exit the shell, type ``\q or Ctrl-d``.

.. code-block:: console

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=5000 --username=jdoe --databasename=master
	Password:

	Interactive client mode
	To quit, use ^D or \q.

	master=> _

The database name shown means you are now ready to run statements and queries.

Statements and queries are standard SQL, followed by a semicolon (;). Statement results are usually formatted as a valid CSV, followed by the number of rows and the elapsed time for that statement.

.. code-block:: console

	master=> SELECT TOP 5 * FROM nba;
	Avery Bradley           ,Boston Celtics        ,0,PG,25,6-2 ,180,Texas                ,7730337
	Jae Crowder             ,Boston Celtics        ,99,SF,25,6-6 ,235,Marquette            ,6796117
	John Holland            ,Boston Celtics        ,30,SG,27,6-5 ,205,Boston University    ,\N
	R.J. Hunter             ,Boston Celtics        ,28,SG,22,6-5 ,185,Georgia State        ,1148640
	Jonas Jerebko           ,Boston Celtics        ,8,PF,29,6-10,231,\N,5000000
	5 rows
	time: 0.001185s

.. Note::

	Null values are represented as \N.
	
When writing long statements and queries, it may be beneficial to use line-breaks. The prompt for a multi-line statement will change from => to ., to alert users to the change. The statement will not execute until a semicolon is used.

.. code-block:: posgres

	$ java -jar jdbc-console-*.*.**.jar --host=[SQream cluster IP address]
	 --port=5000 --username=mjordan -d master
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
	Password:

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

Two parameters control the dispay of results from the client:
* ``--results-only`` - removes row counts and timing information
* ``--delimiter`` - changes the record delimiter

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
     - Defaul
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
   * - 
     - 
     - 
   * - 
     - 
     - 
   * - 
     - 
     - 
	 