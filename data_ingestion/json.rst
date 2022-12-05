.. _json:

**************************
Ingesting Data from JSON
**************************

.. contents:: 
   :local:
   :depth: 1
   
Overview
========

JSON (Java Script Object Notation) is used both as a file format and as a serialization method. The JSON file format is flexible and is commonly used for dynamic, nested, and semi-structured data representations. 

The SQream DB JSON parser handles `RFC 8259 <https://datatracker.ietf.org/doc/html/rfc8259>`_.
SQream DB supports:

* JSON files either as a continuous batch of JSON objects, or as an array of JSON objects
* The `JSON Lines <https://jsonlines.org/>`_  standard, in which every newline (ASCII 10) character always marks the end of a JSON object; therefore, if a value string contains a newline character, it must be escaped as \\n
When exporting data, SQream will always use objects.


Making JSON Files Accessible to Workers
=======================================
To give workers access to files, every node in your system must have access to the storage being used.

The following are required for JSON files to be accessible to workers:

* For files hosted on NFS, ensure that the mount is accessible from all servers.

* For HDFS, ensure that SQream servers have access to the HDFS NameNode with the correct **user-id**. For more information, see :ref:`hdfs`.

* For S3, ensure network access to the S3 endpoint. For more information, see :ref:`s3`.

For more information about restricted worker access, see :ref:`workload_manager`.



Creating a Foreign Table
=========================
When creating a foreign table statement, make sure that the table schema corresponds with the JSON file structure.

The example in this section is based on the source ``nba.json`` table shown below:

.. csv-table:: nba.json
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

The following example shows the correct file structure used to build the ``CREATE FOREIGN TABLE`` statement based on the **nba.json** table:

.. code-block:: postgres
   
   CREATE FOREIGN TABLE ext_nba
   (

        Name       TEXT,
        Team       TEXT,
        Number     BIGINT,
        Position   TEXT,
        Age        BIGINT,
        Height     TEXT,
        Weight     BIGINT,
        College    TEXT,
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
A JSON field consists of a key name and a value. JSON values may be one of the following reserved words (lower-case) ``false``, ``true``, and ``null``, or any of the following data types:


.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - JSON Data Type
     - Representation in SQream
     - Notes
   * - Number
     - ``tinyint``, ``smallint``, ``int``, ``bigint``, ``float``, ``double``, ``numeric``
     - 
   * - String
     - ``TEXT``, ``VARCHAR``, ``NVARCHAR``
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
 
JSON key names, which are case sensitive, are mapped to SQream columns. By default, key names which do not have corresponding SQream table columns are treated as errors, though this behavior can be changed so that they are ignored instead.

An empty JSON field is automatically mapped to SQream with ``null`` as a value.


Ingesting Data into SQream
===========================

.. contents:: In this topic:
   :local:

Syntax
-------
To access JSON files, use the ``json_fdw`` with a ``COPY FROM``, ``COPY TO``, or ``CREATE FOREIG TABLE`` statement.
The FDW syntax is:

.. code-block:: 

	json_fdw [OPTIONS(option=value[,...])]

.. note:: Reading and writing JSON files is enabled only by using the ``json-fdw`` file format specifier.

Parameters
------------

The following parameters are supported by ``json_fdw``:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``datetime_format``
     - Default value is ``default``. Supported date formats can be found in the :ref:`COPY FROM <copy_from>` page.  
   * - ``ignore_extra_fields``
     - Default value is ``false``. When value is ``true``, key names which do not have corresponding SQream table columns will be ignored. Parameter may be used with the ``COPY TO`` and ``IGNORE FOREIGN TABLE`` statements. 
   * - ``compression``
     - Supported values are ``auto``, ``gzip``, and ``none``. ``auto`` means that the compression type is automatically detected upon import. Parameter is not supported for exporting. ``gzip`` means that a ``gzip`` compression is applied. ``none`` means that no compression or an attempt to decompress will take place. 
   * - ``location``
     - A path on the local filesystem, S3, or HDFS URI. The local path must be an absolute path that SQream DB can access.
   * - ``offset``
     - The row number to start with.
   * - ``limit``
     - When specified, tells SQream DB to stop loading after the specified number of rows. Unlimited if unset.
   * - ``error_log``
     - 
   * - ``continue_on_error``
     - Specifies if errors should be ignored or skipped. When set to true, the transaction will continue despite rejected data. This parameter should be set together with ``error_count``. When reading multiple files, if an entire file can’t be opened it will be skipped.
   * - ``error_count``
     - Specifies the threshold for the maximum number of faulty records that will be ignored. This setting must be used in conjunction with ``continue_on_error``.
   * - ``enforce_single_file``
     - Enforces the maximum file size (bytes). Permitted values: ``true`` - creates one file of unlimited size, ``false`` - permits creating several files together limited by the ``MAX_FILE_SIZE``. When set to ``true``, the single file size is not limited by the ``MAX_FILE_SIZE`` setting. When set to ``false``, the combined file sizes cannot exceed the ``MAX_FILE_SIZE``. Default value: ``false``.
   * - ``max_file_size``
     - Sets the maximum file size (bytes).
   * - ``aws_id``, ``aws_secret``
     - Specifies the authentication details for secured S3 buckets
 

Automatic Schema Inference
---------------------------

You may let SQream DB automatically infer the schema of a foreign table when using ``json_fdw``. For more information, follow the :ref:`Automatic Foreign Table DDL Resolution<automatic_foreign_table_ddl_resolution>` page.

Examples
------------

The following is an example of creating a table using the ``COPY FROM``, ``COPY TO``, and ``CREATE FOREIGN TABLE`` statements:

.. code-block:: postgres
   
   COPY t
     FROM WRAPPER json_fdw
     OPTIONS
     (
       location = 'somefile.json'
     )
   ;

.. code-block:: postgres
   
   COPY t
     TO WRAPPER json_fdw
     OPTIONS
     (
       location = 'somefile.json'
     )
   ;

.. code-block:: postgres
   
   CREATE FOREIGN TABLE t
	 (
	   id int not null
	 )
     WRAPPER json_fdw
     OPTIONS
     (
       location = 'somefile.json'
     )
   ;

The following is an example of loading data from a JSON file into SQream:

.. code-block:: postgres

    WRAPPER json_fdw
    OPTIONS
    (
      LOCATION =  's3://sqream-demo-data/nba.json'
    );
	  
