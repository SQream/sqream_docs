.. _execute_saved_query:

********************
EXECUTE_SAVED_QUERY
********************

``EXECUTE_SAVED_QUERY`` executes a :ref:`previously saved query<save_query>`.

Read more in the :ref:`saved_queries` guide.

See also: :ref:`save_query`, :ref:`drop_saved_query`, :ref:`show_saved_query`, :ref:`list_saved_queries`.

Permissions
=============

Executing a saved query requires ``SELECT`` permissions to access the tables referenced in the query.

Syntax
==========

.. code-block:: postgres

   execute_saved_query_statement ::=
       SELECT EXECUTE_SAVED_QUERY(saved_query_name, [ , argument [ , ... ] ] )
       ;

   saved_query_name ::= string_literal

   argument ::= string_literal | number_literal

Returns
==========

Query execution results, based on the query saved.

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``saved_query_name``
     - The name of the query to execute
   * - ``argument``
     - A comma separated list of argument literal values


Notes
=========

* Query parameters can be used as substitutes for literal expressions. Parameters cannot be used to substitute identifiers, column names, table names, or other parts of the query.

* Query parameters of a string datatype (like ``TEXT``) must be of a fixed length, and can be used in equality checks, but not patterns (e.g. :ref:`like`, :ref:`rlike`, etc)

* Query parameters' types are inferred at compile time.

Examples
===========

Assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name text,
      Team text,
      Number tinyint,
      Position text,
      Age tinyint,
      Height text,
      Weight real,
      College text,
      Salary float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1


Saving and executing a simple query
---------------------------------------

.. code-block:: psql

   t=> SELECT SAVE_QUERY('select_all','SELECT * FROM nba');
   executed
   t=> SELECT EXECUTE_SAVED_QUERY('select_all');
   Name                     | Team                   | Number | Position | Age | Height | Weight | College               | Salary  
   -------------------------+------------------------+--------+----------+-----+--------+--------+-----------------------+---------
   Avery Bradley            | Boston Celtics         |      0 | PG       |  25 | 6-2    |    180 | Texas                 |  7730337
   Jae Crowder              | Boston Celtics         |     99 | SF       |  25 | 6-6    |    235 | Marquette             |  6796117
   John Holland             | Boston Celtics         |     30 | SG       |  27 | 6-5    |    205 | Boston University     |         
   R.J. Hunter              | Boston Celtics         |     28 | SG       |  22 | 6-5    |    185 | Georgia State         |  1148640
   [...]

Saving and executing parametrized query
------------------------------------------

Use parameters to replace them later at execution time. 

.. tip:: Use dollar quoting (`$$`) to avoid escaping strings.

   .. code-block:: psql

      t=> SELECT SAVE_QUERY('select_by_weight_and_team',$$SELECT * FROM nba WHERE Weight > ? AND Team = ?$$);
      executed
      t=> SELECT EXECUTE_SAVED_QUERY('select_by_weight_and_team', 240, 'Toronto Raptors');
      Name              | Team            | Number | Position | Age | Height | Weight | College     | Salary 
      ------------------+-----------------+--------+----------+-----+--------+--------+-------------+--------
      Bismack Biyombo   | Toronto Raptors |      8 | C        |  23 | 6-9    |    245 |             | 2814000
      James Johnson     | Toronto Raptors |      3 | PF       |  29 | 6-9    |    250 | Wake Forest | 2500000
      Jason Thompson    | Toronto Raptors |      1 | PF       |  29 | 6-11   |    250 | Rider       |  245177
      Jonas Valanciunas | Toronto Raptors |     17 | C        |  24 | 7-0    |    255 |             | 4660482