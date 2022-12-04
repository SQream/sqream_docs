.. _json:

**************************
Inserting Data from JSON
**************************


.. contents:: In this topic:
   :local:


Overview
========
JSON (Java Script Object Notation) is a popular textual format. It’s flexibility makes it a common choice for representing dynamic, nested and semi-structured data. It’s used both as a file format and as a way for serializing messages.

SQream DB's JSON parser handles `RFC 8259 <https://datatracker.ietf.org/doc/html/rfc8259>`_. SQream supports JSON files consisting of either as a continuous batch of JSON objects, or as an array of JSON objects.

SQream supports the `JSON Lines <https://jsonlines.org/>`_ standard, in which each lines in the input file contains exactly one JSON value (either an array or an object). When exporting data, SQream will always use objects.
Note that in JSONLines files every newlines (ASCII 10) character always marked the end of a JSON object. Therefore, value strings containing newline must escape it as \n.


Making JSON Files Accessible to Workers
================
To give workers access to files every node must have the same view of the storage being used.

The following apply for JSON files to be accessible to workers:

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS name node with the correct **user-id**. For more information, see :ref:`hdfs`.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3`.

For more information about restricted worker access, see :ref:`workload_manager`.

Preparing Your Table
===============
You can build your table structure on both local and foreign tables:

   
Creating a Table
---------------------   
Before loading data, you must build the ``CREATE TABLE`` to correspond with the file structure of the inserted table.

The example in this section is based on the source ``nba.json`` table shown below:

.. csv-table:: nba.json
   :file: nba-t10.json
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE TABLE`` statement based on the **nba.json** table:

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
    WRAPPER json_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.json'
    );

.. tip:: 

   An exact match must exist between the SQream and JSON types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.json** file is stored on S3 at ``s3://sqream-demo-data/nba.json``.

Creating a Foreign Table
---------------------
Before loading data, you must build the ``CREATE FOREIGN TABLE`` to correspond with the file structure of the inserted table.

The example in this section is based on the source ``nba.json`` table shown below:

.. csv-table:: nba.json
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to create the ``CREATE FOREIGN TABLE`` statement based on the **nba.json** table:

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
    WRAPPER json_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.json'
    );

.. tip:: 

   An exact match must exist between the SQream and JSON types. For unsupported column types, you can set the type to any type and exclude it from subsequent queries.

.. note:: The **nba.json** file is stored on S3 at ``s3://sqream-demo-data/nba.json``.

.. note:: The examples in the sections above are identical except for the syntax used to create the tables.


Mapping JSON to SQream
=======================
A JSON field consists of a key name and a value. JSON values may be the lower-case ``false``, ``true``, and ``null``, or any of the following data types:


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - JSON Data Type
     - Representation in SQream
     - Notes
   * - Number
     - 
     - 
   * - String
     - ``TEXT``, ``VARCHAR``, NVARCHAR
     - Support in ``VARCHAR`` and ``NVARCHAR`` data types is about to end.
   * - JSON Literal
     - ``null``, ``true``, ``false``
     - 
   * - JSON Array
     - ``TEXT``
     - 
   * - JSON Object
     - ``TEXT``
     - 
 
JSON key names are mapped to SQream columns. Key names are case sensitive.
Note that using the jsonpath_location option overrides this mapping. - Verify meaning with Ben or Eyal.
A JSON row containing more than one field is registered as an error unless the fdw is configured to ignore. 
An JSON row which is missing a field, automatically receives ``null`` as the value.


Ingesting Data into SQream
==========================


Syntax
-------
Before ingesting data into SQream from a JSON file, you must create a table using the following syntax:

.. code-block:: 

   COPY [schema name.]table_name
  FROM WRAPPER fdw_name
  ;

After creating a table you can ingest data from an Avro file into SQream using the following syntax:

.. code-block:: 

   json_fdw

To access JSON files, use the ``json_fdw`` with a ``copy_from``, ``copy_to``, or ``create_foreign_table`` statement.
The FDW syntax is:

.. code-block:: 

   json_fdw [OPTIONS(option=value[,...])]

.. note:: Accessing JSON files is possible only by using the FDW syntax. 

Parameters
----------
The following parameters are supported by json_fdw:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``datetime_format``
     - Default value is ``DEFAULT``. Supported date formats can be found in :ref:```COPY_TO``<copy_from>`.  
   * - ``ignore_extra_fields``
     - Default is ``false``. 
   * - ``location``
     - A path on the local filesystem, S3, or HDFS URI. The local path must be an absolute path that SQream DB can access.
   * - ``offset``
     - The row number to start with.
   * - ``limit``
     - When specified, tells SQream DB to stop loading after the specified number of rows. Unlimited if unset.
   * - ``error_log``
     - 
   * - ``continue_on_error
     - Specifies if errors should be ignored or skipped. When set to true, the transaction will continue despite rejected data. This parameter should be set together with ``ERROR_COUNT`` When reading multiple files, if an entire file can’t be opened it will be skipped.
   * - ``error_count``
     - Specifies the threshold for the maximum number of faulty records that will be ignored. This setting must be used in conjunction with ``CONTINUE_ON_ERROR``.
   * - ``enforce_single_file``
     - Enforces the maximum file size (bytes). Permitted values: ``true`` - creates one file of unlimited size, ``false`` - permits creating several files together limited by the ``MAX_FILE_SIZE``. When set to ``true``, the single file size is not limited by the ``MAX_FILE_SIZE`` setting. When set to ``false``, the combined file sizes cannot exceed the ``MAX_FILE_SIZE``. Default value: ``FALSE``.
   * - ``max_file_size``
     - Sets the maximum file size (bytes).
   * - ``aws_id``, ``aws_secret``
     - Specifies the authentication details for secured S3 buckets
 

Automatic Schema Inference
---------------------------
You may let SQream DB automatically infer the schema of a foreign table when using ``json_fdw``. For more information, follow the :ref:`Automatic Foreign Table DDL Resolution<automatic_foreign_table_ddl_resolution>` page.



Examples
--------



Limitations
===========
Currently SQream does not support compressed JSON files. 