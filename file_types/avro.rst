.. _avro:

**************************
Avro
**************************

**Avro** is a well-known data serialization system that relies on schemas. Due to its flexibility as an efficient data storage method, BLUE supports the Avro binary data format as an alternative to JSON. Avro files are represented using the **Object Container File** format, in which the Avro schema is encoded alongside binary data. Multiple files loaded in the same transaction are serialized using the same schema. If they are not serialized using the same schema, an error message is displayed. BLUE uses the **.avro** extension for ingested Avro files.


Preparing Your Foreign Table
===============

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

   An exact match must exist between the BLUE and Avro types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.avro** file is stored on S3 at ``s3://sqream-demo-data/nba.avro``.

Mapping Between BLUE and Avro Data Types
=================

Mapping between BLUE and Avro data types depends on the Avro data type:

Primitive Data Types
--------------
The following table shows the supported **Primitive** data types:

+-------------+------------------------------------------------------+
| Avro Type   | BLUE Type                                            |
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
|            | BLUE Type                                             |
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
| Avro Type                  | BLUE Type                                       |
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
When mapping objects to rows, each Avro object or message must contain one ``record`` type object corresponding to a single row in BLUE. The ``record`` fields are associated by name to their target table columns. Additional unmapped fields will be ignored. Note that using the JSONPath option overrides this.

Parameters
==========
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
Because external tables do not automatically verify the file integrity or structure, BLUE recommends manually verifying your table output when ingesting Avro files into BLUE. This lets you determine if your table output is identical to your originally inserted table.

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

