.. _first_steps:

****************************
Getting Started
****************************

The **Getting Started** page describes the following:

.. contents::
   :local:
   :depth: 1

Before Installing SQream
============================
Before installing SQream, you must set up your local machine according to SQream's recommended pre-installation configurations.

For more information, see the following:

* `Hardware Guide <https://docs.sqream.com/en/v2021.2/guides/operations/hardware_guide.html>`_.
* `Recommended Pre-Installation Configuration <https://docs.sqream.com/en/latest/guides/operations/setup/recommended_pre-installation_configurations.html>`_.





Installing SQream
============================
The **Installing SQream** section includes the following SQream installation methods:

* `Installing SQream natively <https://docs.sqream.com/en/latest/guides/operations/installing_sqream_with_binary.html>`_ - Describes installing SQream using binary packages provided by SQream.
* `Installing SQream with Kubernetes <https://docs.sqream.com/en/latest/guides/operations/installing_sqream_with_kubernetes.html>`_ - Describes installing SQream using the Kubernetes open source platform.
* `Installing and running SQream in a Docker container <https://docs.sqream.com/en/v2021.2/guides/operations/running_sqream_in_a_docker_container.html>`_ - Describes how to run SQream in a Docker container.

Using the SQream SQL Command Line Interface
============================================
SQream includes a built-in client for executing SQL statements either interactively or using the Command Line Interface (CLI). The **SQream SQL CLI Reference** page provides a reference for the options and parameters.

For more information, see `SQream SQL CLI Reference <https://docs.sqream.com/en/latest/reference/cli/sqream_sql.html>`_.

Performing Basic SQream Operations
====================================
After installing SQream you can perform the operations described in the **Performing Basic SQream Operations** section:

.. contents::
   :local:
   :depth: 1


Running the SQream SQL Client
---------------------------------
The following example shows how to run the SQream SQL client:

.. code-block:: psql

   $ sqream sql --port=5000 --username=rhendricks -d master
   Password:
   
   Interactive client mode
   To quit, use ^D or \q.
   
   master=> _

Running the SQream SQL client prompts you to provide your password. Use the username and password that you have set up, or your DBA has provided.
  
.. tip::
   * You can exit the shell by typing ``\q``  or :kbd:`Ctrl-d`. 
   * A new SQream cluster contains a database named `master,` which is the database used in the examples on this page.

Creating a New Database
--------------------------
**To create a new database:**

1. Write a :ref:`create_database` statement.

   The following is an example of creating a new database:

   .. code-block:: psql

      master=> CREATE DATABASE test;
      executed

2. Reconnect to the newly created database.

   1. Exit the client by typing ``\q`` and pressing **Enter**.
   2. From the Linux shell, restart the client with the new database name:

      .. code-block:: psql

         $ sqream sql --port=5000 --username=rhendricks -d test
         Password:
   
         Interactive client mode
         To quit, use ^D or \q.
   
         test=> _

    The name of the new database that you are connected to is displayed in the prompt.

Creating Your First Table
------------------------------
The **Creating Your First Table** section describes the following:

* :ref:`Creating a table<creating_a_table>`
* :ref:`Replacing a table<replacing_a_table>`
* :ref:`Listing a CREATE TABLE statement<listing_a_create_table_statement>`
* :ref:`Dropping a table<dropping_a_table>`


.. _creating_a_table:

**Creating a Table**

The ``CREATE TABLE`` syntax is used to create your first table. This table includes a table name and column specifications, as shown in the following example:

.. code-block:: postgres

   CREATE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );

For more information on creating a table, see :ref:`create_table`.

.. _replacing_a_table:

**Replacing a Table**

You can drop an existing table and create a new one by adding the ``OR REPLACE`` parameter after the ``CREATE`` keyword, as shown in the following example:

.. code-block:: postgres

   CREATE OR REPLACE TABLE cool_animals (
      id INT NOT NULL,
      name VARCHAR(20),
      weight INT
   );

.. TODO: cool_animals? I think we need to decide if the customer for this documenation is 12 years old, or an IT professional.

.. _listing_a_create_table_statement:

**Listing a CREATE TABLE Statement**
   
You can list the full, verbose ``CREATE TABLE`` statement for a table by using the **GET DDL** function with the table name as shown in the following example:

.. code-block:: psql

   test=> SELECT GET_DDL('cool_animals');
   create table "public"."cool_animals" (
   "id" int not null,
   "name" varchar(20),
   "weight" int
   );

.. note:: 

   * SQream DB identifier names such as table names and column names are not case sensitive. SQream DB lowercases all identifiers bu default. If you want to maintain case, enclose the identifiers with double-quotes.
   * SQream DB places all tables in the `public` schema, unless another schema is created and specified as part of the table name.
   
For information on listing a ``CREATE TABLE`` statement, see :ref:`get_ddl`.

.. _dropping_a_table:

**Dropping a Table**

When you have finished working with your table, you can drop the table to remove it table and its content, as shown in the following example:

.. code-block:: psql

   test=> DROP TABLE cool_animals;
   
   executed
   
For more information on dropping tables, see :ref:`drop_table`.

Listing Tables
------------------
To see the tables in the current database you can query the catalog, as shown in the following example:

.. code-block:: psql

   test=> SELECT table_name FROM sqream_catalog.tables;
   cool_animals
   
   1 rows

Inserting Rows
-------------------
The **Inserting Rows** section describes the following:

* :ref:`Inserting basic rows<inserting_basic_rows>`
* :ref:`Changing value order<changing_value_order>`
* :ref:`Inserting multiple rows<inserting_multiple_rows>`
* :ref:`Omitting columns<omitting_columns>`


.. _inserting_basic_rows:

**Inserting Basic Rows**

You can insert basic rows into a table using the ``INSERT`` statement. The inserted statement includes the table name, an optional list of column names, and column values listed in the same order as the column names, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals VALUES (1, 'Dog', 7);
   
   executed

.. _changing_value_order:

**Changing Value Order**

You can change the order of values by specifying the column order, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals(weight, id, name) VALUES (3, 2, 'Possum');
   
   executed

.. _inserting_multiple_rows:

**Inserting Multiple Rows**

You can insert multiple rows using the ``INSERT`` statement by using sets of parentheses separated by commas, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals VALUES
         (3, 'Cat', 5) ,
         (4, 'Elephant', 6500) ,
         (5, 'Rhinoceros', 2100);
   
   executed

.. note:: You can load large data sets using bulk loading methods instead. For more information, see :ref:`inserting_data`.

.. _omitting_columns:

**Omitting Columns**

Omitting columns that have a default values (including default ``NULL`` values) uses the default value, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed

.. code-block:: psql

   test=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed
   test=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

.. note:: Null row values are represented as ``\N``

For more information on inserting rows, see :ref:`insert`.

For more information on default values, see :ref:`default value<default_values>`.


Running Queries
------------------
The **Running Queries** section describes the following:

* :ref:`Running basic queries<running_basic_queries>`
* :ref:`Outputting all columns<outputting_all_columns>`
* :ref:`Outputting shorthand table values<outputting_shorthand_table_values>`
* :ref:`Filtering results<filtering_results>`
* :ref:`Sorting results<sorting_results>`
* :ref:`Filtering null rows<filtering_null_rows>`


.. _running_basic_queries:

**Running Basic Queries**

You can run a basic query using the ``SELECT`` keyword, followed by a list of columns and values to be returned, and the table to get the data from, as shown in the following example:

.. code-block:: psql

   test=> SELECT id, name, weight FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
For more information on the ``SELECT`` keyword, see :ref:`select`.

.. _outputting_all_columns:

**To Output All Columns**

You can output all columns without specifying them using the star operator ``*``, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

.. _outputting_shorthand_table_values:

**Outputting Shorthand Table Values**

You can output the number of values in a table without getting the full result set by using the ``COUNT`` statement:

.. code-block:: psql

   test=> SELECT COUNT(*) FROM cool_animals;
   6
   
   1 row

.. _filtering_results:

**Filtering Results**

You can filter results by adding a ``WHERE`` clause and specifying the filter condition, as shown in the following example:

.. code-block:: psql

   test=> SELECT id, name, weight FROM cool_animals WHERE weight > 1000;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   
   2 rows

.. _sorting_results:

**Sorting Results**

You can sort results by adding an ``ORDER BY`` clause and specifying ascending (``ASC``) or descending (``DESC``) order, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3
   6,\N,\N

   6 rows

.. _filtering_null_rows:

**Filtering Null Rows**

You can filter null rows by adding an ``IS NOT NULL`` filter, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals WHERE weight IS NOT NULL ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3

   5 rows
   
For more information, see the following:

* Outputting the number of values in a table without getting the full result set - :ref:`COUNT(*)<count>`.
* Filtering results - :ref:`WHERE<where>`
* Sorting results - :ref:`ORDER BY<order_by>`
* Filtering rows - :ref:`IS NOT NULL<is_null>`



Deleting Rows
-----------------
The **Deleting Rows** section describes the following:

* :ref:`Deleting selected rows<deleting_selected_rows>`
* :ref:`Deleting all rows<deleting_all_rows>`

.. _deleting_selected_rows:

**Deleting Selected Rows**

You can delete rows in a table selectively using the ``DELETE`` command. You must include a table name and `WHERE` clause to specify the rows to delete, as shown in the following example:

.. code-block:: psql

   test=> DELETE FROM cool_animals WHERE weight is null;
   
   executed
   master=> SELECT  * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100

   5 rows

.. _deleting_all_rows:

**Deleting All Rows**

You can delete all rows in a table using the ``TRUNCATE`` command followed by the table name, as shown in the following example:

.. code-block:: psql

   test=> TRUNCATE TABLE cool_animals;
   
   executed

.. note:: While :ref:`truncate` deletes data from disk immediately, :ref:`delete` does not physically remove the deleted rows.

For more information, see the following:

* Deleting selected rows - :ref:`DELETE<delete>`
* Deleting all rows - :ref:`TRUNCATE<truncate>`

Saving Query Results to a CSV or PSV File
--------------------------------------------


You can save query results to a CSV or PSV file using the ``sqream sql`` command from a CLI client. This saves your query results to the selected delimited file format, as shown in the following example:

.. code-block:: console

   $ sqream sql --username=mjordan --database=nba --host=localhost --port=5000 -c "SELECT * FROM nba LIMIT 5" --results-only --delimiter='|' > nba.psv
   $ cat nba.psv
   Avery Bradley           |Boston Celtics        |0|PG|25|6-2 |180|Texas                |7730337
   Jae Crowder             |Boston Celtics        |99|SF|25|6-6 |235|Marquette            |6796117
   John Holland            |Boston Celtics        |30|SG|27|6-5 |205|Boston University    |\N
   R.J. Hunter             |Boston Celtics        |28|SG|22|6-5 |185|Georgia State        |1148640
   Jonas Jerebko           |Boston Celtics        |8|PF|29|6-10|231|\N|5000000

For more output options, see :ref:`Controlling the Client Output<controlling_output>`.

.. rubric:: What's next?

* Explore all of SQream DB's :ref:`SQL Syntax <sql_syntax>`.
* See the full :ref:`SQream SQL CLI reference <sqream_sql_cli_reference>`.
* Connect a :ref:`third party tool <third_party_tools>` to start analyzing data.
