.. _catalog_reference_examples:

*************************************
Examples
*************************************
The **Examples** page includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Listing All Tables in a Database
----------------------------------

.. code-block:: psql

   master=> SELECT * FROM sqream_catalog.tables;
   database_name | table_id | schema_name | table_name     | row_count_valid | row_count | rechunker_ignore
   --------------+----------+-------------+----------------+-----------------+-----------+-----------------
   master        |        1 | public      | nba            | true            |       457 |                0
   master        |       12 | public      | cool_dates     | true            |         5 |                0
   master        |       13 | public      | cool_numbers   | true            |         9 |                0
   master        |       27 | public      | jabberwocky    | true            |         8 |                0

Listing All Schemas in a Database
------------------------------------

.. code-block:: psql
   
   master=> SELECT * FROM sqream_catalog.schemas;
   schema_id | schema_name   | rechunker_ignore
   ----------+---------------+-----------------
           0 | public        | false           
           1 | secret_schema | false           


Listing Columns and Their Types for a Specific Table
---------------------------------------------------

.. code-block:: postgres

   SELECT column_name, type_name 
   FROM sqream_catalog.columns
   WHERE table_name='cool_animals';

Listing Delete Predicates
------------------------

.. code-block:: postgres

   SELECT  t.table_name, d.*  FROM 
   sqream_catalog.delete_predicates AS d  
   INNER JOIN sqream_catalog.tables AS t  
   ON d.table_id=t.table_id;


Listing Saved Queries
-----------------------------

.. code-block:: postgres

   SELECT * FROM sqream_catalog.savedqueries;
   
For more information, see  :ref:`saved_queries`.