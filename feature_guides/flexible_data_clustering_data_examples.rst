.. _flexible_data_clustering_data_examples:

***********************
Examples
***********************
The **Examples** includes the following examples:

.. contents:: 
   :local:
   :depth: 1
   
Creating a Clustered Table
-----------------------------
The following is an example of syntax for creating a clustered table on a table naturally ordered by ``start_date``. An alternative cluster key can be defined on such a table to improve performance on queries already ordered by ``country``:

.. code-block:: postgres

   CREATE TABLE users (
      name VARCHAR(30) NOT NULL,
      start_date datetime not null,
      country VARCHAR(30) DEFAULT 'Unknown' NOT NULL
   ) CLUSTER BY country;