.. _repeat:
 
******
REPEAT
******

The ``REPEAT`` function repeats an input string expression as many times as specified.

Syntax
==========

.. code-block:: sql

   REPEAT('expr', n)

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``'expr'``
     - A ``TEXT`` expression
   * - ``n``
     - An ``INTEGER`` expression specifying the number of repetitions for the string expression
     

Return
======

* Returns a ``TEXT`` string.
* When ``n`` <= 0, and empty string is returned.

Examples
========

For these example, consider the following table:

.. code-block:: sql

	CREATE TABLE customer(customername TEXT);

	INSERT INTO customer VALUES 
	 ('Alfreds Futterkiste'), 
	 ('Ana Trujillo Emparedados y helados'),
	 ('Antonio Moreno Taquería'),
	 ('Around the Horn');

Repeating Content of a Table Column
-----------------------------------

.. code-block:: sql

	SELECT REPEAT(customername, 2) FROM customer;
   
	repeat                   
	--------------------------------------------------------------------
	Alfreds FutterkisteAlfreds Futterkiste
	Ana Trujillo Emparedados y heladosAna Trujillo Emparedados y helados
	Antonio Moreno TaqueríaAntonio Moreno Taquería
	Around the HornAround the Horn

Repeating a String
------------------

.. code-block:: sql

	SELECT REPEAT('abc', 3);
	   
	repeat                                        
	---------
	abcabcabc  


Repeating a String 0 Times
--------------------------

.. code-block:: sql

	SELECT REPEAT('abc', 0);
	   
	repeat                                        
	------      

Repeating an Empty String
-------------------------

.. code-block:: sql

	SELECT REPEAT('', 3);
	   
	repeat                                        
	------
           
