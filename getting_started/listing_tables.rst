.. _listing_tables:

****************************
Listing Tables
****************************
To see the tables in the current database you can query the catalog, as shown in the following example:

.. code-block:: psql

   test=> SELECT table_name FROM sqream_catalog.tables;
   cool_animals
   
   1 rows