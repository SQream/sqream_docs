.. _avro:

**************************
Inserting Data from Avro
**************************
The **Inserting Data from Avro** page describes inserting data from Avro into SQream and includes the following:

.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   :width: 110

.. contents:: 
   :local:
   :depth: 1
   
Overview
===========
**Avro** is a well-known data serialization system that relies on schemas. Due to its flexibility as an efficient data storage method, SQream supports the Avro binary data format as an alternative to JSON. Avro files are represented using the **Object Container File** format, in which the Avro schema is encoded alongside binary data. Multiple files loaded in the same transaction are serialized using the same schema. If they are not serialized using the same schema, an error message is displayed. SQream uses the **.avro** extension for ingested Avro files.

Making Avro Files Accessible to Workers
================
To give workers access to files every node must have the same view of the storage being used.

The following apply for Avro files to be accessible to workers:

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS name node with the correct **user-id**. For more information, see :ref:`hdfs`.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3`.

For more information about restricted worker access, see :ref:`workload_manager`.

Preparing Your Table
===============
You can build your table structure on both local and foreign tables:

.. contents:: 
   :local:
   :depth: 1
   
Creating a Table
---------------------   
Before loading data, you must build the ``CREATE TABLE`` to correspond with the file structure of the inserted table.

The example in this section is based on the source ``nba.avro`` table shown below:

.. csv-table:: nba.avro
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE TABLE`` statement based on the **nba.avro** table:

.. code-block:: postgres
   
   CREATE TABLE ext_nba
   (

        Name       TEXT(40),
        Team       TEXT(40),
        Number     BIGINT,
        Position   TEXT(2),
        Age        BIGINT,
        Height     TEXT(4),
        Weight     BIGINT,
        College    TEXT(40),
        Salary     FLOAT
    )
    WRAPPER avro_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.avro'
    );

.. tip:: 

   An exact match must exist between the SQream and Avro types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.avro** file is stored on S3 at ``s3://sqream-demo-data/nba.avro``.

Creating a Foreign Table
---------------------
Before loading data, you must build the ``CREATE FOREIGN TABLE`` to correspond with the file structure of the inserted table.

The example in this section is based on the source ``nba.avro`` table shown below:

.. csv-table:: nba.avro
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE FOREIGN TABLE`` statement based on the **nba.avro** table:

.. code-block:: postgres
   
   CREATE FOREIGN TABLE ext_nba
   (

        Name       TEXT(40),
        Team       TEXT(40),
        Number     BIGINT,
        Position   TEXT(2),
        Age        BIGINT,
        Height     TEXT(4),
        Weight     BIGINT,
        College    TEXT(40),
        Salary     FLOAT
    )
    WRAPPER avro_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.avro'
    );

.. tip:: 

   An exact match must exist between the SQream and Avro types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.avro** file is stored on S3 at ``s3://sqream-demo-data/nba.avro``.

.. note:: The examples in the sections above are identical except for the syntax used to create the tables.

Mapping Between SQream and Avro Data Types
=================
Mapping between SQream and Avro data types depends on the Avro data type:

.. contents:: 
   :local:
   :depth: 1

Primitive Data Types
--------------
The following table shows the supported **Primitive** data types:

+-------------+------------------------------------------------------+
| Avro Type   | SQream Type                                          |
|             +-----------+---------------+-----------+--------------+
|             | Number    | Date/Datetime | String    | Boolean      |
+=============+===========+===============+===========+==============+
| ``null``    | Supported | Supported     | Supported | Supported    |
+-------------+-----------+---------------+-----------+--------------+
| ``boolean`` |           |               | Supported | Supported    |
+-------------+-----------+---------------+-----------+--------------+
| ``int``     | Supported |               | Supported |              |
+-------------+-----------+---------------+-----------+--------------+
| ``long``    | Supported |               | Supported |              |
+-------------+-----------+---------------+-----------+--------------+
| ``float``   | Supported |               | Supported |              |
+-------------+-----------+---------------+-----------+--------------+
| ``double``  | Supported |               | Supported |              |
+-------------+-----------+---------------+-----------+--------------+
| ``bytes``   |           |               |           |              |
+-------------+-----------+---------------+-----------+--------------+
| ``string``  |           | Supported     | Supported |              |
+-------------+-----------+---------------+-----------+--------------+

Complex Data Types
--------------
The following table shows the supported **Complex** data types:

+------------+-------------------------------------------------------+
|            | SQream Type                                           |
|            +------------+----------------+-------------+-----------+
|Avro Type   | Number     |  Date/Datetime |   String    | Boolean   |
+============+============+================+=============+===========+
| ``record`` |            |                |             |           |
+------------+------------+----------------+-------------+-----------+
| ``enum``   |            |                | Supported   |           |
+------------+------------+----------------+-------------+-----------+
| ``array``  |            |                |             |           |
+------------+------------+----------------+-------------+-----------+
| ``map``    |            |                |             |           |
+------------+------------+----------------+-------------+-----------+
| ``union``  |  Supported | Supported      | Supported   | Supported |
+------------+------------+----------------+-------------+-----------+
| ``fixed``  |            |                |             |           |
+------------+------------+----------------+-------------+-----------+

Logical Data Types
--------------
The following table shows the supported **Logical** data types:

+----------------------------+-------------------------------------------------+
| Avro Type                  | SQream Type                                     |
|                            +-----------+---------------+-----------+---------+
|                            | Number    | Date/Datetime | String    | Boolean |
+============================+===========+===============+===========+=========+
| ``decimal``                | Supported |               | Supported |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``uuid``                   |           |               | Supported |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``date``                   |           | Supported     | Supported |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``time-millis``            |           |               |           |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``time-micros``            |           |               |           |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``timestamp-millis``       |           | Supported     | Supported |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``timestamp-micros``       |           | Supported     | Supported |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``local-timestamp-millis`` |           |               |           |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``local-timestamp-micros`` |           |               |           |         |
+----------------------------+-----------+---------------+-----------+---------+
| ``duration``               |           |               |           |         |
+----------------------------+-----------+---------------+-----------+---------+

.. note:: Number types include **tinyint**, **smallint**, **int**, **bigint**, **real** and **float**, and **numeric**. String types include **text**.

Mapping Objects to Rows
===============
When mapping objects to rows, each Avro object or message must contain one ``record`` type object corresponding to a single row in SQream. The ``record`` fields are associated by name to their target table columns. Additional unmapped fields will be ignored. Note that using the JSONPath option overrides this.

Ingesting Data into SQream
==============
This section includes the following:

.. contents:: 
   :local:
   :depth: 1
   
Syntax
-----------
Before ingesting data into SQream from an Avro file, you must create a table using the following syntax:

.. code-block:: postgres
   
   COPY [schema name.]table_name
     FROM WRAPPER fdw_name
   ;
	  
After creating a table you can ingest data from an Avro file into SQream using the following syntax:

.. code-block:: postgres

   avro_fdw
   
Example
-----------
The following is an example of creating a table:

.. code-block:: postgres
   
   COPY t
     FROM WRAPPER fdw_name
     OPTIONS
     (
       [ copy_from_option [, ...] ]
     )
   ;

The following is an example of loading data from an Avro file into SQream:

.. code-block:: postgres

    WRAPPER avro_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.avro'
    );
	  
For more examples, see :ref:`additional_examples`.

Parameters
===================
The following table shows the Avro parameter:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The schema name for the table. Defaults to ``public`` if not specified.

Best Practices
============
Because external tables do not automatically verify the file integrity or structure, SQream recommends manually verifying your table output when ingesting Avro files into SQream. This lets you determine if your table output is identical to your originally inserted table.

The following is an example of the output based on the **nba.avro** table:

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

.. _additional_examples:

Additional Examples
===============
This section includes the following additional examples of loading data into SQream:

.. contents:: 
   :local:
   :depth: 1

Omitting Unsupported Column Types
--------------
When loading data, you can omit columns using the ``NULL as`` argument. You can use this argument to omit unsupported columns from queries that access external tables. By omitting them, these columns will not be called and will avoid generating a "type mismatch" error.

In the example below, the ``Position`` column is not supported due its type.

.. code-block:: postgres
   
   CREATE TABLE nba AS
      SELECT Name, Team, Number, NULL as Position, Age, Height, Weight, College, Salary FROM ext_nba;   

Modifying Data Before Loading
--------------
One of the main reasons for staging data using the ``EXTERNAL TABLE`` argument is to examine and modify table contents before loading it into SQream.

For example, we can replace pounds with kilograms using the :ref:`create_table_as` statement

In the example below, the ``Position`` column is set to the default ``NULL``.

.. code-block:: postgres
   
   CREATE TABLE nba AS 
      SELECT name, team, number, NULL as Position, age, height, (weight / 2.205) as weight, college, salary 
              FROM ext_nba
              ORDER BY weight;

Loading a Table from a Directory of Avro Files on HDFS
--------------
The following is an example of loading a table from a directory of Avro files on HDFS:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name TEXT(30) NOT NULL, email TEXT(50) NOT NULL)  
   WRAPPER avro_fdw
   OPTIONS
     (
        LOCATION =  'hdfs://hadoop-nn.piedpiper.com/rhendricks/users/*.avro'
     );
   
   CREATE TABLE users AS SELECT * FROM ext_users;

For more configuration option examples, see the `CREATE FOREIGN TABLE parameters <https://docs.sqream.com/en/latest/reference/sql/sql_statements/ddl_commands/create_foreign_table.html#cft-parameters>`_.

Loading a Table from a Directory of Avro Files on S3
--------------
The following is an example of loading a table from a directory of Avro files on S3:

.. code-block:: postgres

   CREATE FOREIGN TABLE ext_users
     (id INT NOT NULL, name TEXT(30) NOT NULL, email TEXT(50) NOT NULL)  
   WRAPPER avro_fdw
   OPTIONS
     ( LOCATION = 's3://pp-secret-bucket/users/*.avro',
       AWS_ID = 'our_aws_id',
       AWS_SECRET = 'our_aws_secret'
      );
   
   CREATE TABLE users AS SELECT * FROM ext_users;