.. _mode:

**************************
MODE
**************************
The **MODE** function returns the most common value in the selected column. If there are no repeating values, or if there is the same frequency of multiple values, this function returns the top value based on the ``ORDER BY`` clause. 

The **MODE** function is commonly used with the following functions:

* `PERCENTILE_CONT <https://docs.sqream.com/en/v2020.3.1/reference/sql/sql_functions/aggregate_functions/percentile_cont.html>`_ function
* `PERCENTILE_DISC <https://docs.sqream.com/en/v2020.3.1/reference/sql/sql_functions/aggregate_functions/percentile_disc.html>`_ function

Syntax
========
The following is the correct syntax for the ``MODE`` function:

.. code-block:: postgres

   MODE() WITHIN GROUP (ORDER BY column)   
   
Example
========
The example in this section is based on the ``players`` table below:

.. list-table::
   :widths: 33 33 33
   :header-rows: 1

+-----------------+----------+-----------+
| **Player_Name** | **Team** | **Score** |
+-----------------+----------+-----------+
| T_Tock          | Blue     | 13        |
+-----------------+----------+-----------+
| N_Stein         | Blue     | 20        |
+-----------------+----------+-----------+
| F_Dirk          | Blue     | 20        |
+-----------------+----------+-----------+
| Y_Hyung         | Blue     | 10        |
+-----------------+----------+-----------+
| A_Rodrick       | Blue     | 13        |
+-----------------+----------+-----------+
| R_Evans         | Red      | 55        |
+-----------------+----------+-----------+
| C_Johnston      | Red      | 20        |
+-----------------+----------+-----------+
| K_Stoll         | Red      | 25        |
+-----------------+----------+-----------+
| J_Loftus        | Red      | 22        |
+-----------------+----------+-----------+
| L_Ellis         | Red      | 7         |
+-----------------+----------+-----------+
| G_Elroy         | Red      | 23        |
+-----------------+----------+-----------+

The following is an example of the ``MODE`` function:

.. code-block:: postgres

   SELECT 
   MODE() WITHIN GROUP (ORDER BY score) as Mode
   FROM players;
             
   Mode|
   ----+
   20
