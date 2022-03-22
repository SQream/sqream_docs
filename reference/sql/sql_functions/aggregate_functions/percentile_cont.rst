.. _percentile_cont:

**************************
PERCENTILE_CONT
**************************
The **PERCENTILE_CONT** function returns the value located in the selected percentile of a specified column. The required input is a number between **0** and **1** that represents the wanted percentile and the column containing the wanted percentile. If the selected percentile does not have an exact value, the PERCENTILE_CONT function extrapolates a value estimated from the existing values. 

The **PERCENTILE_CONT** function returns an extrapolated value closest to the values in the requested percentile. If you want to see the closest value in your data to the requested percentile, use `PERCENTILE DISC <https://docs.sqream.com/en/v2020.3/reference/sql/sql_functions/aggregate_functions/percentile_disc.html>`_.

Syntax
========
The following is the correct syntax for the ``PERCENTILE_CONT`` function:

.. code-block:: postgres

   PERCENTILE_CONT(double) WITHIN GROUP (ORDER BY <column>)
   
Example
========
The example in this section is based on the ``players`` table below:

.. list-table::
   :widths: 33 33 33
   :header-rows: 1
   
+-----------------+----------+-----------+
| **Player_Name** | **Team** | **Score** |
+-----------------+----------+-----------+
| T_Tock          | Blue     | 12        |
+-----------------+----------+-----------+
| N_Stein         | Blue     | 23        |
+-----------------+----------+-----------+
| F_Dirk          | Blue     | 45        |
+-----------------+----------+-----------+
| Y_Hyung         | Blue     | 19        |
+-----------------+----------+-----------+
| A_Rodrick       | Blue     | 37        |
+-----------------+----------+-----------+
| R_Evans         | Red      | 52        |
+-----------------+----------+-----------+
| C_Johnston      | Red      | 43        |
+-----------------+----------+-----------+
| K_Stoll         | Red      | 27        |
+-----------------+----------+-----------+
| J_Loftus        | Red      | 8         |
+-----------------+----------+-----------+
| L_Ellis         | Red      | 13        |
+-----------------+----------+-----------+
| G_Elroy         | Red      | 31        |
+-----------------+----------+-----------+

The following is an example of the ``PERCENTILE_CONT`` function:

.. code-block:: postgres

   SELECT
   PERCENTILE_CONT(0.18) WITHIN GROUP (ORDER BY score) 
   FROM players;
             
   percentile_cont|
   ---------------+
   12.8
   
.. note:: The output value is an extrapolation of the halfway point between the values. 
