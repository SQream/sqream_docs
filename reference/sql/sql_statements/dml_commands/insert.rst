.. _insert:

**********************
INSERT
**********************

``INSERT`` inserts one or more rows into a table.

.. tip:: 
   * To bulk load data into existing tables, the :ref:`COPY FROM<copy_from>` command performs better than ``INSERT``.
   * To load Parquet or ORC files, see :ref:`CREATE EXTERNAL TABLE<create_external_table>`

Permissions
=============

The role must have the ``INSERT`` permission to the destination table.

Synopsis
==========

.. code-block:: postgres

   insert_statement ::=

    INSERT INTO [schema_name.]table_name
        [ ( column_name [, ... ] ) ]
    query ;
    

   schema_name ::= identifier
   
   table_name ::= identifier

   column_name ::= identifier


Elements
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``[schema_name.]table_name``
     - Table to insert data into
   * - ``( column_name [, ...] )``
     - A comma separated list of column names that specifies the destination columns of the insert.
   * - ``query``
     - A :ref:`SELECT<select>` or :ref:`VALUES<values>` statement. Each value must match the data type of its destination column. The values must also match the order of the table or columns if specified with ` (column_name, ...)`.



Examples
===========

Inserting a single row
------------------------------

.. code-block:: postgres
   
   INSERT INTO cool_animals VALUES (5, 'fox', 15);

Changing column order
------------------------------

.. code-block:: postgres
   
   INSERT INTO cool_animals(name, weight, id) VALUES ('possum', '7', 6);

