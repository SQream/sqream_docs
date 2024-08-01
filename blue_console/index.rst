.. _blue_console:

************
BLUE Console
************

BLUE has a native client program that provides a command-line interface (CLI) for interacting with your cloud stored data. It allows you to connect to database servers, execute SQL queries and commands, and receive the results in a text-based format.

Before You Begin
================

It is essential that you have the following installed:

* `SQream Blue Java CLI <https://storage.cloud.google.com/cicd-storage/jdbc-console/release/jdbc-console-1.0.5-blue.zip>`_
* Java 17

Running BLUE Console
=====================

BLUE console is Java-based and may run on any Java-supported platform.

#. Use the BLUE web interface to generate an access token and copy it.
   
   For instructions on how to generate and copy access tokens, go to :ref:`connecting_to_blue`.

#. To start the client, run the following command:

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar --host=<BLUE cluster FQDN> --access-token=cHczWjlIWHk2****

Output:
	
.. code-block:: none

	Welcome to JDBC console version jdbc-console-0.1.3-69
	To quit use ^d or exit; to abort ^c
	Connection URL: jdbc:Sqream://<BLUE cluster FQDN>:443/master;accesstoken=cHczWjlIWHk2****;pool=Default;source=CLI
	master=>
	
#. To view a full list of arguments before starting the client, run the following command:

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar --host=<BLUE cluster FQDN> --access-token=cHczWjlIWHk2**** --help


First Steps 
============

After entering your access token, you are presented with the BLUE console. The database name shown means you are now ready to run statements and queries. 

Statements and queries are standard SQL, followed by a semicolon ``;``.

.. code-block:: none
 
	master=> CREATE OR REPLACE FOREIGN TABLE "public"."nba"
	(
	  Name TEXT,
	  Team TEXT,
	  Number INT,
	  Position TEXT,
	  Age INT,
	  Height TEXT,
	  Weight INT,
	  College TEXT,
	  Salary INT
	)
	WRAPPER
	  json_fdw
	OPTIONS
	  (
	LOCATION = 'gs://product_sqream/Documentation/nba.json'
	  );
	Done
	time: 5.284 s


Statement results are usually formatted as a valid CSV, followed by the number of rows and the statement elapsed time. 

``NULL`` values are represented as ``\N``.

.. code-block:: none

	master=> SELECT TOP 5 * FROM nba;
	| Name            | Team              | Number | Position | Age | Birthday | Weight | College            | Salary   |
	|-----------------|-------------------|--------|----------|-----|----------|--------|--------------------|----------|
	| Avery Bradley   | Boston Celtics    | 0      | PG       | 25  | 2-Jun    | 180    | Texas              | 7730337  |
	| Jae Crowder     | Boston Celtics    | 99     | SF       | 25  | 6-Jun    | 235    | Marquette          | 6796117  |
	| John Holland    | Boston Celtics    | 30     | SG       | 27  | 5-Jun    | 205    | Boston University  | \N       |
	| R.J. Hunter     | Boston Celtics    | 28     | SG       | 22  | 5-Jun    | 185    | Georgia State      | 1148640  |
	| Jonas Jerebko   | Boston Celtics    | 8      | PF       | 29  | 10-Jun   | 231    | \N                 | 5000000  |
	5 rows
	time: 3.579 s

Operator References
==============================

Arguments
------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Default
     - Description
   * - ``-c`` or ``--command``
     - None
     - Changes the mode of operation to single-command, non-interactive. Use this argument to run a statement and immediately exit the database.
   * - ``-f`` or ``--file``
     - None
     - Changes the mode of operation to multi-command, non-interactive. Use this argument to run a sequence of statements from an external file and immediately exit.
   * - ``-h`` or ``--host``
     - 
     - Fully Qualified Domain Name (FQDN) address of the Blue server to connect to
   * - ``-d``, ``--database``, or ``--databasename``
     - None
     - Specifies the database name for queries and statements in this session.
   * - ``--results-only``
     - False
     - Outputs results only, without timing information and row counts
   * - ``--no-history``
     - False
     - When set, prevents command history from being saved in ``~/.sqream/clientcmdhist``
   * - ``--delimiter``
     - ``,``
     - Specifies the field separator. By default, ``blue sql`` outputs valid CSVs. Change the delimiter to modify the output to another delimited format (e.g. TSV, PSV).
   * - ``--access-token``
     - None
     - Provide a security token that grants access to protected resources or operations.
   * - ``--table-view``
     - ``true``
     - Displays query results in a table view format with column headers. The display limit is set to 10,000 rows. 
   * - ``--internal``
     - False
     - Shows query id
   * - ``--log`` or ``log-file``
     - False
     - A log file will be created
   * - ``-p`` or ``--port``
     - ``5000``
     - Sets the connection port.
   * - ``pool``
     - Pool defined as default
     - The resource pool you wish to use
   * - ``--query-timeout``
     - None
     - Query timeout in seconds
   * - ``--show-results``
     - True
     - Determines whether or not results are shown

	
Record Delimiters
---------------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Supported Record Delimiters
     - Non-Supported Delimiters 
     - Recommended Delimiters
   * - Printable ASCII values (32-126)
     - ``\``, ``N``, ``-``, ``:``, ``"``, ``\n``, ``\r``, ``.``, lower-case Latin letters, digits (0-9)
     - ``,``, ``|``, ``tab`` character

Meta-Commands
-------------

Meta-commands in BLUE SQL start with a backslash (\\) and do not require ``;`` at the end for execution.
	
.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Command
     - Description
     - Example
   * - ``^c``
     - Abort the currently running statement 
     - ``\^c``
   * - ``^d`` or ``exit``
     - Quit the client. (Same as ``Ctrl-d``)
     - ``master=> \exit;``
   * - ``\c <database>`` or ``\connect <database>``
     - Changes the current connection to an alternate database
     - ``master=> \c basketball`` 
       ``basketball=>``
	 
Keyboard Shortcuts
==============================

Keyboard shortcuts provide efficient ways to navigate and manipulate text on the command line, improving productivity and ease of use.

Navigating
------------

The below shortcuts are only supported for Linux environments. 

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
     - Deletes from the cursor to the beginning of the command line.
   * - ``Ctrl-k``
     - Deletes from the cursor to the end of the command line.
   * - ``Ctrl-w``
     - Delete from cursor to beginning of a word.
   * - ``Ctrl-y``
     - Pastes a word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor. 
   * - ``Alt-b``
     - Moves back one word (or goes to the beginning of the word where the cursor is).
   * - ``Alt-f``
     - Moves forward one word (or goes to the end of the word the cursor is).
   * - ``Alt-d``
     - Deletes to the end of a word starting at the cursor. Deletes the whole word if the cursor is at the beginning of that word.
   * - ``Alt-c``
     - Capitalizes letters in a word starting at the cursor. Capitalize the whole word if the cursor is at the beginning of that word.
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
	 
Searching Command Line History
--------------------------------

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

Examples
========

Executing "On-The-Go" Commands
--------------------------------------------

Use the ``--c`` or ``--command`` option to execute a statement and exit the database. This can be useful when you need to run scheduled queries or create a local file out of query results.

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar --host=product1-sqream.isqream.com --access-token=############# -d master -c "SELECT TOP 5 * FROM nba;"
	Welcome to JDBC console version jdbc-console-0.1.3-69
	To quit use ^d or exit; to abort ^c
	Connection URL: jdbc:Sqream://<BLUE cluster FQDN>:443/master;accesstoken=cHczWjlIWHk2****;pool=Default;source=CLI
	SELECT TOP 5* FROM nba;
	| Name            | Team              | Number | Position | Age | Birthday | Weight | College            | Salary   |
	|-----------------|-------------------|--------|----------|-----|----------|--------|--------------------|----------|
	| Avery Bradley   | Boston Celtics    | 0      | PG       | 25  | 2-Jun    | 180    | Texas              | 7730337  |
	| Jae Crowder     | Boston Celtics    | 99     | SF       | 25  | 6-Jun    | 235    | Marquette          | 6796117  |
	| John Holland    | Boston Celtics    | 30     | SG       | 27  | 5-Jun    | 205    | Boston University  | \N       |
	| R.J. Hunter     | Boston Celtics    | 28     | SG       | 22  | 5-Jun    | 185    | Georgia State      | 1148640  |
	| Jonas Jerebko   | Boston Celtics    | 8      | PF       | 29  | 10-Jun   | 231    | \N                 | 5000000  |
	5 rows
	time: 2.976 s
	closing session...

Remove the timing and row count by passing the ``--results-only`` parameter.

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar --host=product1-sqream.isqream.com --access-token=############# --results-only -d master -c "SELECT TOP 5* FROM nba;"
	| Name            | Team              | Number | Position | Age | Birthday | Weight | College            | Salary   |
	|-----------------|-------------------|--------|----------|-----|----------|--------|--------------------|----------|
	| Avery Bradley   | Boston Celtics    | 0      | PG       | 25  | 2-Jun    | 180    | Texas              | 7730337  |
	| Jae Crowder     | Boston Celtics    | 99     | SF       | 25  | 6-Jun    | 235    | Marquette          | 6796117  |
	| John Holland    | Boston Celtics    | 30     | SG       | 27  | 5-Jun    | 205    | Boston University  | \N       |
	| R.J. Hunter     | Boston Celtics    | 28     | SG       | 22  | 5-Jun    | 185    | Georgia State      | 1148640  |
	| Jonas Jerebko   | Boston Celtics    | 8      | PF       | 29  | 10-Jun   | 231    | \N                 | 5000000  |


Executing Batch SQL Scripts
---------------------------	

Use the ``-f <filename>`` argument:

.. code-block:: none

	$ java -jar jdbc-console-1.0.5-blue.jar --host=product.isqream.com --access-token=########## -f=example_script.sql
	 
.. tip::

	Output can be saved to a file by using the ``>`` redirection operator.

Navigating Between Databases
-----------------------------

Creating a new database and using the ``\c`` option to switch over to it:

.. code-block:: none

	master=> CREATE DATABASE basketball;
	Done
	time: 0.59 s

	master=> \c basketball

Exporting SQL Query Results to CSV
----------------------------------

Use the ``--results-only`` flag to remove the row counts and timing.

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar --host=product.isqream.com --access-token=########## -d master -c "SELECT * FROM aba" --results-only > file.csv
	cat file.csv
	
Changing a CSV to a TSV
-----------------------

The ``--delimiter`` parameter accepts any printable character.

.. tip::

	To insert a tab, use ``Ctrl-V`` followed by ``Tab`` in Bash.

.. code-block:: none

	java -jar jdbc-console-1.0.5-blue.jar.jar --host=product.isqream.com --access-token=########## -d farm -c "SELECT * FROM animals" --delimiter '  ' > file.tsv
	cat file.tsv

Executing a Series of Statements From a File
-------------------------------------------- 

Assuming a file containing SQL statements (separated by semicolons):

.. code-block:: none

	cat some_queries.sql
	 CREATE TABLE calm_farm_animals
	( id INT IDENTITY(0, 1), name TEXT
	);

	INSERT INTO calm_farm_animals (name)
	  SELECT name FROM   animals WHERE  is_angry = false;


	java -jar jdbc-console-1.0.5-blue.jar --host=product.isqream.com --access-token=########## -d farm -f some_queries.sql
	executed
	time: 0.018289s
	executed
	time: 0.090697s

Connecting Using Variables in Linux Environments
------------------------------------------------------------

You can save connection parameters as environment variables:

.. code-block:: none

	export SQREAM_USER=sqream;
	export SQREAM_DATABASE=farm;
	java -jar jdbc-console-1.0.5-blue.jar --0.1.3-69.jar --host=product.isqream.com --access-token=########## --username=$SQREAM_USER -d $SQREAM_DATABASE
