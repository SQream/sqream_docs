.. _delete:

**********************
DELETE
**********************

``DELETE`` removes specific rows from a table.

.. tip:: 
   * To delete all rows from a table, see :ref:`TRUNCATE<truncate>`
   * To delete columns, see :ref:`DROP COLUMN<drop_column>`

Permissions
=============

The role must have the ``DELETE`` and ``SELECT`` permissions at the table level.

Syntax
==========

.. code-block:: postgres

   delete_table_statement ::=
       DELETE FROM [schema_name.]table_name [ WHERE value_expr ]
       ;

   chunk_cleanup_statement ::= 
       SELECT CLEANUP_CHUNKS ( 'schema_name', 'table_name' )
       ;

   extent_cleanup_statement ::= 
       SELECT CLEANUP_EXTENTS ( 'schema_name', 'table_name' )
       ;

   table_name ::= identifier
   
   schema_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema for the table.
   * - ``table_name``
     - The name of the table to delete rows from.
   * - ``value_expr``
     - An expression that returns Boolean values using columns, such as ``<column> = <value>``. Rows that match the expression will be deleted.

How SQream DB deletes data
====================================

Deleting data in SQream DB is a two-step process. First, SQream DB marks rows as deleted, but they remain on-disk until a cleanup process is initiated.

The cleanup process is not automatic, as it can take some time for very large tables which some customers prefer to perform during off-peak hours.

Phase 1: Logical Delete
---------------------------

The result set for ``SELECT`` queries will not contain the deleted data. Data is marked for deletion, but not physically deleted from disk.

Phase 2: Clean-up
--------------------

Files marked for deletion during the logical deletion stage are removed from disk. This is achieved by calling both utility function commands: ``CLEANUP_CHUNKS`` and ``CLEANUP_EXTENTS`` sequentially.

.. note::
   * :ref:`ALTER TABLE<alter_table>` and other DDL operations are blocked on tables that require clean-up.
   * The value expression for deletion can't be the result of a subquery or a join.
   * SQream DB may prevent a very long delete process. If the estimated time is beyond the threshold, the error message will explain how to override this limitation and continue the process.

Additional notes
-------------------

Disk space usage after delete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the exception of a full table delete (:ref:`TRUNCATE<truncate>`), deleting data does not free up disk space. To free up disk space, trigger the cleanup process.

Select performance on deleted rows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Queries on tables that have deleted rows may have to scan data that hasn't been cleaned up.
In some cases, this can cause queries to take longer than expected. To solve this issue, trigger the cleanup process.


Examples
===========

Deleting values from a table
------------------------------

.. code-block:: psql

   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
   farm=> DELETE FROM cool_animals WHERE weight > 1000;
   executed
   
   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   6,\N,\N
   
   4 rows

Deleting values based on more complex predicates
---------------------------------------------------

.. code-block:: psql

   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
   farm=> DELETE FROM cool_animals WHERE weight > 1000;
   executed
   
   farm=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   6,\N,\N
   
   4 rows


Identifying and cleaning up tables
---------------------------------------

List tables that haven't been cleaned up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql
   
   farm=> SELECT t.table_name FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      GROUP BY 1;
   cool_animals
   
   1 row

Identify predicates for clean-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   weight > 1000
   
   1 row

Triggering a cleanup
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: psql

   -- Chunk reorganization (SWEEP)
   farm=> SELECT CLEANUP_CHUNKS('public','cool_animals');
   executed

   -- Delete leftover files (VACUUM)
   farm=> SELECT CLEANUP_EXTENTS('public','cool_animals');
   executed
   
   
   farm=> SELECT delete_predicate FROM sqream_catalog.delete_predicates dp
      JOIN sqream_catalog.tables t
      ON dp.table_id = t.table_id
      WHERE t.table_name = 'cool_animals';
   
   0 rows