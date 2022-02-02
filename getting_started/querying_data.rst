.. _querying_data:

****************************
Querying Data
****************************
One of the most basic operations when using SQream is querying data.

To begin familiarizing yourself with querying data, you can create the following table using the ``CREATE TABLE`` statement:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name varchar(40),
      Team varchar(40),
      Number tinyint,
      Position varchar(2),
      Age tinyint,
      Height varchar(4),
      Weight real,
      College varchar(40),
      Salary float
    );


You can down download the above (:download:`nba.csv table </_static/samples/nba.csv>`) if needed, shown below:

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

The above query gets the following from the table above, limited to showing the first ten results:

* Name
* Team name
* Age

.. code-block:: psql
   
   nba=> SELECT Name, Team, Age FROM nba LIMIT 10;
   Avery Bradley,Boston Celtics,25
   Jae Crowder,Boston Celtics,25
   John Holland,Boston Celtics,27
   R.J. Hunter,Boston Celtics,22
   Jonas Jerebko,Boston Celtics,29
   Amir Johnson,Boston Celtics,29
   Jordan Mickey,Boston Celtics,21
   Kelly Olynyk,Boston Celtics,25
   Terry Rozier,Boston Celtics,22
   Marcus Smart,Boston Celtics,22