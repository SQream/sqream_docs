.. _decode:

********************
DECODE
********************
The ``DECODE`` function takes an expression or column and compares it to a series of search values. It returns a result value that corresponds to the first matching search value, or the default value ``NULL`` if no matches are found. 

Syntax
==========
The following shows the correct syntax for the DECODE function:

.. code-block:: postgres

   DECODE( <expr> , <search1> , <result1> [ , <search2> , <result2> ... ] [ , <default> ] )

Parameters
============
The following table shows the DECODE parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - The expression to be evaluated.
   * - ``search``
     - A value that ``expr`` is compared against.
   * - ``result1``
     - A value that is returnd if ``expr`` matches ``search``.

Return
======

Returns the same type as the argument supplied.

Example
=======

.. code-block:: postgres

	CREATE TABLE test1 (european_size int not null);
	INSERT INTO test1 values (8),(9),(10),(11);
	
	SELECT european_size,DECODE(european_size,8,40,9,41,10,42,99) from test1;
	
		Output:
		+---------------+---------+
		|european_size	|decode   |
		+-------------------------+
		|8		|40	  |
		+---------------+---------+
		|9		|41	  |
		+-------------------------+
		|10		|42	  |
		+-------------------------+
		|11		|99	  |
		+-------------------------+
   

	
