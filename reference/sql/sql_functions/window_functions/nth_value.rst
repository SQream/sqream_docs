.. _nth_value:

**************************
NTH_VALUE
**************************

The **NTH_VALUE** function returns the value located in the selected column of a specified row of a segment. While the NTH_VALUE function is identical to the FIRST_VALUE and LAST_VALUE functions, it requires you to add a literal and whole ``int`` type ``n`` value representing the row number containing the value that you want. If you select an ``n`` value larger than the number of rows in the table, the NTH_VALUE function returns ``NULL``.

Syntax
-------
The following shows the correct syntax for the NTH_VALUE function.

.. code-block:: postgres

   NTH_VALUE(Selected_Column, n) OVER (...)

Examples
---------
The following example shows the syntax for a table named ``superstore`` used for tracking item sales in thousands:

.. code-block:: postgres

   CREATE TABLE superstore
   (

      "Section" text(40),
      "Product_Name" text(40),
      "Sales_In_K" int,
       );
	   
The following example shows the output of the syntax above:	 
	 
.. list-table::
   :widths: 24 26 50
   :header-rows: 1
   
   * - Section
     - Product_Name
     - Sales_In_K
   * - bed
     - pillow_case
     - 17
   * - bath
     - rubber_duck
     - 22 
   * - beyond
     - curtain
     - 15
   * - bed
     - side_table
     - 8
   * - bath
     - shampoo
     - 9 
   * - bed
     - blanket
     - 7
   * - bath
     - bath_bomb
     - 13
   * - bath
     - conditioner
     - 17 
   * - beyond
     - lamp
     - 7
   * - bath
     - soap
     - 13
   * - beyond
     - rug
     - 12 
   * - bed
     - pillow
     - 17