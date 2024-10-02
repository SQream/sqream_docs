.. _foreign_tables:

**************
Foreign Tables
**************

Foreign tables can be used to run queries directly on data without inserting it into BLUE first.
BLUE supports read only foreign tables, so you can query from foreign tables, but you cannot insert to them, or run deletes or updates on them.

Although foreign tables can be used without inserting data into BLUE, one of their main use cases is to help with the insertion process. An insert select statement on a foreign table can be used to insert data into SQream using the full power of the query engine to perform ETL.


   
Supported Data Formats
======================

BLUE supports foreign tables over:

* Text files (e.g. CSV, PSV, TSV)
* ORC
* Parquet
* JSON
* Avro

Supported Data Staging
======================

SQream can stage data from:

* :ref:`gcp`
* :ref:`s3`

Using Foreign Tables
=====================

Use a foreign table to stage data before loading from CSV, Parquet or ORC files.

Planning for Data Staging
-------------------------

For the following examples, we will interact with a CSV file.

The file is stored on :ref:`s3`, at ``s3://sqream-demo-data/nba_players.csv``.
We will make note of the file structure, to create a matching ``CREATE_EXTERNAL_TABLE`` statement.

Creating a Foreign Table
------------------------

Based on the source file structure, we :ref:`create a foreign table<create_foreign_table>` with the appropriate structure, and point it to the file.

.. code-block:: postgres
   
	CREATE FOREIGN TABLE nba
	(
	 Name TEXT,
	 Team TEXT,
	 Number tinyint,
	 Position TEXT,
	 Age tinyint,
	 Height TEXT,
	 Weight real,
	 College TEXT,
	 Salary float
	)
	WRAPPER csv_fdw -- Text file
	OPTIONS
	(
	 LOCATION =  's3://sqream-demo-data/nba_players.csv', 
	 RECORD DELIMITER = '\r\n'; -- DOS delimited file
	);

The file format in this case is CSV, and it is stored as an :ref:`s3` object. 

We also took note that the record delimiter was a DOS newline (``\r\n``).

Querying Foreign Tables
------------------------

Let's peek at the data from the foreign table:

.. code-block:: postgres
   
	SELECT * 
	FROM 
	  nba 
	LIMIT 10;
	
Output:

.. code-block:: none
	
	name          | team           | number | position | age | height | weight | college           | salary  
	--------------+----------------+--------+----------+-----+--------+--------+-------------------+---------
	Avery Bradley | Boston Celtics |      0 | PG       |  25 | 6-2    |    180 | Texas             |  7730337
	Jae Crowder   | Boston Celtics |     99 | SF       |  25 | 6-6    |    235 | Marquette         |  6796117
	John Holland  | Boston Celtics |     30 | SG       |  27 | 6-5    |    205 | Boston University |         
	R.J. Hunter   | Boston Celtics |     28 | SG       |  22 | 6-5    |    185 | Georgia State     |  1148640
	Jonas Jerebko | Boston Celtics |      8 | PF       |  29 | 6-10   |    231 |                   |  5000000
	Amir Johnson  | Boston Celtics |     90 | PF       |  29 | 6-9    |    240 |                   | 12000000
	Jordan Mickey | Boston Celtics |     55 | PF       |  21 | 6-8    |    235 | LSU               |  1170960
	Kelly Olynyk  | Boston Celtics |     41 | C        |  25 | 7-0    |    238 | Gonzaga           |  2165160
	Terry Rozier  | Boston Celtics |     12 | PG       |  22 | 6-2    |    190 | Louisville        |  1824360
	Marcus Smart  | Boston Celtics |     36 | PG       |  22 | 6-4    |    220 | Oklahoma State    |  3431040

Modifying Data from Staging
---------------------------

One of the main reasons for staging data is to examine the content and modify it before loading.
Assume we are unhappy with weight being in pounds because we want to use kilograms instead. We can apply the transformation as part of a query:

.. code-block:: postgres
   
	SELECT 
	 name, 
	 team, 
	 number,
	 position, 
	 age, 
	 height, (weight / 2.205) as weight, 
	 college, salary 
	FROM nba
	ORDER BY weight;

Output:

.. code-block:: none

	name                     | team                   | number | position | age | height | weight   | college               | salary  
	-------------------------+------------------------+--------+----------+-----+--------+----------+-----------------------+---------
	Nikola Pekovic           | Minnesota Timberwolves |     14 | C        |  30 | 6-11   |  139.229 |                       | 12100000
	Boban Marjanovic         | San Antonio Spurs      |     40 | C        |  27 | 7-3    | 131.5193 |                       |  1200000
	Al Jefferson             | Charlotte Hornets      |     25 | C        |  31 | 6-10   | 131.0658 |                       | 13500000
	Jusuf Nurkic             | Denver Nuggets         |     23 | C        |  21 | 7-0    | 126.9841 |                       |  1842000
	Andre Drummond           | Detroit Pistons        |      0 | C        |  22 | 6-11   | 126.5306 | Connecticut           |  3272091
	Kevin Seraphin           | New York Knicks        |      1 | C        |  26 | 6-10   | 126.0771 |                       |  2814000
	Brook Lopez              | Brooklyn Nets          |     11 | C        |  28 | 7-0    | 124.7166 | Stanford              | 19689000
	Jahlil Okafor            | Philadelphia 76ers     |      8 | C        |  20 | 6-11   | 124.7166 | Duke                  |  4582680
	Cristiano Felicio        | Chicago Bulls          |      6 | PF       |  23 | 6-10   | 124.7166 |                       |   525093
	[...]

Now, if we're happy with the results, we can convert the staged foreign table to a standard table

Converting a Foreign Table to a Standard Database Table
-------------------------------------------------------

:ref:`create_table_as` can be used to materialize a foreign table into a regular table.

.. tip:: If you intend to use the table multiple times, convert the foreign table to a standard table.

.. code-block:: postgres
   
	CREATE TABLE real_nba AS 
	SELECT 
	 name, 
	 team, 
	 number, 
	 position, 
	 age, 
	 height, 
	(weight / 2.205) AS weight, 
	 college, salary 
	FROM nba
	ORDER BY weight;

	SELECT * FROM real_nba LIMIT 5;

Output:

.. code-block:: none

	name             | team                   | number | position | age | height | weight   | college     | salary  
	-----------------+------------------------+--------+----------+-----+--------+----------+-------------+---------
	Nikola Pekovic   | Minnesota Timberwolves |     14 | C        |  30 | 6-11   |  139.229 |             | 12100000
	Boban Marjanovic | San Antonio Spurs      |     40 | C        |  27 | 7-3    | 131.5193 |             |  1200000
	Al Jefferson     | Charlotte Hornets      |     25 | C        |  31 | 6-10   | 131.0658 |             | 13500000
	Jusuf Nurkic     | Denver Nuggets         |     23 | C        |  21 | 7-0    | 126.9841 |             |  1842000
	Andre Drummond   | Detroit Pistons        |      0 | C        |  22 | 6-11   | 126.5306 | Connecticut |  3272091

Error Handling and Limitations
==============================

* Error handling in foreign tables is limited. Any error that occurs during source data parsing will result in the statement aborting.

* Foreign tables are logical and do not contain any data, their structure is not verified or enforced until a query uses the table.
   
For example, a CSV with the wrong delimiter may cause a query to fail, even though the table has been created successfully:
   
.. code-block:: postgres
      
	SELECT * FROM nba;
	select * from nba;
	-- Record delimiter mismatch during CSV parsing. User defined line delimiter \n does not match the first delimiter \r\n found in s3://sqream-demo-data/nba.csv

* Since the data for a foreign table is not stored in BLUE, it can be changed or removed at any time by a foreign process. As a result, the same query can return different results each time it runs against a foreign table. Similarly, a query might fail if the foreign data is moved, removed, or has changed structure.