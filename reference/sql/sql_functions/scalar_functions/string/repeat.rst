.. _repeat:

**************************
REPEAT
**************************
Repeats a string as many times as specified.

.. warning:: This function works ONLY with ``TEXT`` data type.


Syntax
==========

.. code-block:: postgres

   REPEAT(expr, character_count)

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - String expression
   * - ``character_count``
     

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* When ``character_count`` <= 0, and empty string is returned.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE customer(customername TEXT));

   INSERT INTO customer VALUES 
      ('Alfreds Futterkiste'), 
      ('Ana Trujillo Emparedados y helados'),
      ('Antonio Moreno Taquería'),
      ('Around the Horn');

Repeat the text in customername 2 times:
-----------------------------------------

.. code-block:: psql

   t=> SELECT REPEAT(customername, 2) FROM customers;
   
   repeat                   
   --------------------------
   Alfreds FutterkisteAlfreds Futterkiste
   Ana Trujillo Emparedados y heladosAna Trujillo Emparedados y helados
   Antonio Moreno TaqueríaAntonio Moreno Taquería
   Around the HornAround the Horn


Repeat the string 0 times:
----------------------------

.. code-block:: psql

   t=> SELECT REPEAT('abc', 0);
   
   repeat                                        
   -----------------------------------------------
   ''              

Repeat the string 1 times:
----------------------------

.. code-block:: psql

   t=> SELECT REPEAT('abc', 1);
   
   repeat                                        
   -----------------------------------------------
   'abc'         
   

Repeat the string 3 times:
----------------------------

.. code-block:: psql

   t=> SELECT REPEAT('a', 3);
   
   repeat                                        
   -----------------------------------------------
   'aaa'  


Repeat an empty string 10 times:
----------------------------

.. code-block:: psql

   t=> SELECT REPEAT('', 10);
   
   repeat                                        
   -----------------------------------------------
   ''        
   
   
Repeat a string -3 times:
----------------------------

.. code-block:: psql

   t=> SELECT REPEAT('abc', -3);
   
   repeat                                        
   -----------------------------------------------
   ''         