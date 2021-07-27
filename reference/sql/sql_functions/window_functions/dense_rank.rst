.. _dense_rank:

**************************
DENSE_RANK
**************************

The **DENSE_RANK** function returns data ranking information and is similar to the **RANK** function. Its main difference is related to the results of identical line values. While the RANK function proceeds with the next row after providing the same value for identical consecutive rows (for example, 1,1,3), the DENSE_RANK function proceeds with the next number in the sequence (1,1,2).

Syntax
-------
The following shows the correct syntax for the DENSE_RANK function.

.. code-block:: postgres

   DENSE_RANK ( ) OVER (...)  

Arguments
---------
None

Returns
---------
Returns data ranking information.