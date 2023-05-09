.. _sql_data_types_boolean:

*************************
Boolean
*************************
The following table describes the Boolean data type.

.. list-table::
   :widths: 30 30 30
   :header-rows: 1
   
   * - Values
     - Syntax
     - Data Size (Not Null, Uncompressed)	 
   * - ``true``, ``false`` (case sensitive)
     - When loading from CSV, ``BOOL`` columns can accept ``0`` as ``false`` and ``1`` as ``true``.
     - 1 byte, but resulting average data sizes may be lower after compression.
	 
Boolean Examples
^^^^^^^^^^
The following is an example of the Boolean syntax:

.. code-block:: postgres
   
   CREATE TABLE animals (name TEXT, is_angry BOOL);
   
   INSERT INTO animals VALUES ('fox',true), ('cat',true), ('kiwi',false);
   
   SELECT name, CASE WHEN is_angry THEN 'Is really angry!' else 'Is not angry' END FROM animals;
   
The following is an example of the correct output:

.. code-block:: text

   "fox","Is really angry!"
   "cat","Is really angry!"
   "kiwi","Is not angry"

Boolean Casts and Conversions
^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the possible Boolean value conversions:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Type
     - Details
   * - ``TINYINT``, ``SMALLINT``, ``INT``, ``BIGINT``
     - ``true`` → ``1``, ``false`` → ``0``
   * - ``REAL``, ``DOUBLE``
     - ``true`` → ``1.0``, ``false`` → ``0.0``