.. _percentile_disc:

**************************
PERCENTILE_DISC
**************************
The **PERCENTILE_DISC** function returns the value located in the selected percentile of a specified column. The required input is a number between **0** and **1** that represents the wanted percentile and the column that you want to rank. If the selected percentile does not have an exact value, this function returns the closest value beneath the requested percentile.

The **PERCENTILE_DISC** function returns an exact value based on the closest values in your data to the requested percentile. If you want to see an extrapolated value in your data closest to the requested percentile, use `PERCENTILE CONT <https://docs.sqream.com/en/latest/reference/sql/sql_functions/aggregate_functions/percentile_cont.html>`_.

Syntax
========
The following is the correct syntax for the ``PERCENTILE_DISC`` function:

.. code-block:: postgres

   PERCENTILE_DISC(double) WITHIN GROUP (ORDER BY <column>)   
   
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

The following is an example of the ``PERCENTILE_DISC`` function:

.. code-block:: postgres

   SELECT
   PERCENTILE_DISC(0.15) WITHIN GROUP (ORDER BY score)
   FROM players;

   percentile_disc|
   ---------------+
   12
