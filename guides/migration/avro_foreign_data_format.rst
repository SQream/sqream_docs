.. _avro_foreign_data_format:

**************************
Inserting Data from Avro
**************************
The **Inserting Data from Avro** page describes inserting data from Avro into SQream and includes the following:

.. contents:: 
   :local:
   :depth: 2
   
Overview
===========
**Avro** is a well-known data serialization system that relies on schemas. Due to its flexibility and nesting as an efficient data storage method, SQream supports the Avro binary data format as an alternative to JSON.

Avro Data Types
===========

Avro includes the following data types:

.. contents:: 
   :local:
   :depth: 1

Primitive Data Types
--------------
The following table shows the supported **Primitive** data types:

+-------------+-------------------------------------------+
| Avro Type   | SQream Type                               |
|             +--------+---------------+--------+---------+
|             | Number | Date/Datetime | String | Boolean |
+=============+========+===============+========+=========+
| ``null``    | ✓      | ✓             | ✓      | ✓       |
+-------------+--------+---------------+--------+---------+
| ``boolean`` |        |               | ✓      | ✓       |
+-------------+--------+---------------+--------+---------+
| ``int``     | ✓      |               | ✓      |         |
+-------------+--------+---------------+--------+---------+
| ``long``    | ✓      |               | ✓      |         |
+-------------+--------+---------------+--------+---------+
| ``float``   | ✓      |               | ✓      |         |
+-------------+--------+---------------+--------+---------+
| ``double``  | ✓      |               | ✓      |         |
+-------------+--------+---------------+--------+---------+
| ``bytes``   |        |               |        |         |
+-------------+--------+---------------+--------+---------+
| ``string``  |        | ✓             | ✓      |         |
+-------------+--------+---------------+--------+---------+






Complex Data Types
--------------
The following table shows the supported **Complex** data types:

+------------+-------------------------------------------+
|            | SQream Type                               |
|            +--------+---------------+--------+---------+
|Avro Type   | Number | Date/Datetime | String | Boolean |
+============+========+===============+========+=========+
| ``record`` |        |               |        |         |
+------------+--------+---------------+--------+---------+
| ``enum``   |        |               | ✓      |         |
+------------+--------+---------------+--------+---------+
| ``array``  |        |               |        |         |
+------------+--------+---------------+--------+---------+
| ``map``    |        |               |        |         |
+------------+--------+---------------+--------+---------+
| ``union``  | ✓      | ✓             | ✓      | ✓       |
+------------+--------+---------------+--------+---------+
| ``fixed``  |        |               |        |         |
+------------+--------+---------------+--------+---------+


Logical Data Types
--------------
The following table shows the supported **Logical** data types:

+----------------------------+-------------------------------------------+
| Avro Type                  | SQream Type                               |
|                            +--------+---------------+--------+---------+
|                            | Number | Date/Datetime | String | Boolean |
+============================+========+===============+========+=========+
| ``decimal``                | ✓      |               | ✓      |         |
+----------------------------+--------+---------------+--------+---------+
| ``uuid``                   |        |               | ✓      |         |
+----------------------------+--------+---------------+--------+---------+
| ``date``                   |        | ✓             | ✓      |         |
+----------------------------+--------+---------------+--------+---------+
| ``time-millis``            |        |               |        |         |
+----------------------------+--------+---------------+--------+---------+
| ``time-micros``            |        |               |        |         |
+----------------------------+--------+---------------+--------+---------+
| ``timestamp-millis``       |        | ✓             | ✓      |         |
+----------------------------+--------+---------------+--------+---------+
| ``timestamp-micros``       |        | ✓             | ✓      |         |
+----------------------------+--------+---------------+--------+---------+
| ``local-timestamp-millis`` |        |               |        |         |
+----------------------------+--------+---------------+--------+---------+
| ``local-timestamp-micros`` |        |               |        |         |
+----------------------------+--------+---------------+--------+---------+
| ``duration``               |        |               |        |         |
+----------------------------+--------+---------------+--------+---------+

	 
Mapping Objects to Rows
===============
When mapping objects to rows, each Avro object or message must contain one ``record`` type object corresponding to a single row in SQream. The ``record`` fields are **Comment - Must be associated?** associated by name to their target table columns. 

Additional unmapped fields will be ignored. Note that using the JSONPath option overrides this.

Ingesting Avro Files
====================
This section describes how to ingest Avro files into SQream and covers the following:


.. contents:: 
   :local:
   :depth: 1


Preparing Your Avro Source File
----------
Prepare your Avro source files according to the following requirements:

* RFC 4180 standard CSV files, but can also be modified to support non-standard CSVs (with multi-character delimiters, unquoted fields, etc).

   ::

* Files are encoded with UTF-8 or ASCII.

   ::

* Field delimiter is an ASCII character or characters.

   ::

* Record delimiter, also known as a new line separator, is a Unix-style newline (``\n``), DOS-style newline (``\r\n``), or Mac style newline (``\r``).

   ::

* If a field is quoted, any double quote that appears must be double-quoted (similar to the :ref:`string literals quoting rules<string_literals>`. For example, to encode ``What are "birds"?``, the field should appear as ``"What are ""birds""?"``.

   ::

* Fields can be enclosed by double-quotes (optional), or mandatory quotes if they contain one of the following characters:

   * The record delimiter or field delimiter.

      ::

   * A double quote character.

      ::

   * A newline.
   
SQream does not support other modes of escaping, such as ``1,"What are \"birds\"?"``.

``NULL`` values can be marked in the following ways in Avro files:
   
   * An explicit null marker. For example, ``col1,\N,col3``.
   
      ::

   * An empty field delimited by the field delimiter. For example, ``col1,,col3``.
   
   .. note:: If a text field is quoted but contains no content (``""``) it is considered an empty text field and not ``NULL``.
   
For more information about standard CSV files, see `RFC 4180 standard CSVs <https://tools.ietf.org/html/rfc4180>`_.
   
Making Avro Files Accessible to Workers
---------------------
To give workers access to files every node must have the same view of the storage being used.

The following apply for Avro files to be accessible to workers:

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS name node with the correct **user-id**. For more information, see :ref:`hdfs`.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3`.

For more information about restricted worker access, see :ref:`workload_manager`.

Basing Your Table Structure on Inserted Tables
---------------------
Before loading data, you must build the ``CREATE EXTERNAL TABLE`` to correspond with the file structure of the inserted table.

The example in this section is based on the source ``nba.parquet`` table shown below:

.. csv-table:: nba.parquet
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE EXTERNAL TABLE`` statement based on the **nba.parquet** table:

.. code-block:: postgres
   
   CREATE FOREIGN TABLE ext_nba
   (
        Name       VARCHAR(40),
        Team       VARCHAR(40),
        Number     BIGINT,
        Position   VARCHAR(2),
        Age        BIGINT,
        Height     VARCHAR(4),
        Weight     BIGINT,
        College    VARCHAR(40),
        Salary     FLOAT
    )
    WRAPPER parquet_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.parquet'
    );

.. tip:: 

   An exact match must exist between the SQream and Avro types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.parquet** file is stored on S3 at ``s3://sqream-demo-data/nba.parquet``.

Verifying Your Table Output
---------------------
Because external tables do not automatically verify the file integrity or structure, you must manually verify that the table output is identical to the original inserted table.

The following is an example of the output based on the **nba.parquet** table:

.. code-block:: psql
   
   t=> SELECT * FROM ext_nba LIMIT 10;
   Name          | Team           | Number | Position | Age | Height | Weight | College           | Salary  
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

.. note:: If your table output has errors, verify that the structure of the Avro files correctly corresponds to the external table structure that you created.

Loading Data into SQream
---------------------

Syntax
~~~~~~~~~~~~~~~~~~~~~
The following is the correct syntax for loading data into SQream:

.. code-block:: postgres
   
   CREATE TABLE <table name> AS
      SELECT * FROM <external table>;
	  
The following is an example of loading data into SQream:

.. code-block:: postgres
   
   CREATE TABLE nba AS
      SELECT * FROM ext_nba;
	  
For more information about the **CREATE TABLE AS** statement, see :ref:`create_table_as`.

Examples
~~~~~~~~~~~~~~~~~~~~~

This section includes the following examples of loading data into SQream:

.. contents:: 
   :local:
   :depth: 1

Omitting Unsupported Column Types
**********************
When loading data, you can omit columns using the ``NULL as`` argument. You can use this argument to omit unsupported columns from queries that access external tables. By omitting them, these columns will not be called and will avoid generating a "type mismatch" error.

**Comment - Is "type mismatch" the official name of this error, do the words "type mismatch" appear anywhere, or is this just a description of the error?**

In the example below, the ``Position`` column is not supported due its type.

.. code-block:: postgres
   
   CREATE TABLE nba AS
      SELECT Name, Team, Number, NULL as Position, Age, Height, Weight, College, Salary FROM ext_nba;
   

Modifying Data Before Loading
**********************
One of the main reasons for staging data using the ``EXTERNAL TABLE`` argument is to examine and modify table contents before loading it into SQream.

For example, we can replace **Comment - Convert?** pounds with kilograms using the :ref:`create_table_as` statement

In the example below, the ``Position`` column is set to the default ``NULL``.

.. code-block:: postgres
   
   CREATE TABLE nba AS 
      SELECT name, team, number, NULL as Position, age, height, (weight / 2.205) as weight, college, salary 
              FROM ext_nba
              ORDER BY weight;


Loading a Table from a Directory of Avro Files on HDFS
**********************
The following is an example of loading a table from a directory of Avro files on HDFS:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.parquet'
     );
   
   CREATE TABLE users AS SELECT * FROM ext_users;

For more configuration option examples, see the `CREATE FOREIGN TABLE parameters <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/create_foreign_table.html#cft-parameters>`_.

Loading a Table from a Directory of Avro Files on S3
**********************
The following is an example of loading a table from a directory of Avro files on S3:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL)  
   WRAPPER parquet_fdw
   OPTIONS
     ( LOCATION = 's3://pp-secret-bucket/users/*.parquet',
       AWS_ID = 'our_aws_id',
       AWS_SECRET = 'our_aws_secret'
      );
   
   CREATE TABLE users AS SELECT * FROM ext_users;






