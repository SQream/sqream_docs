:orphan:

.. _to_hex:

**************************
TO_HEX
**************************

Converts an integer to a hexadecimal representation.

Syntax
======

.. code-block:: postgres

   TO_HEX( expr ) --> TEXT

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - This function accepts ``INT`` and ``BIGINT`` expressions

Returns
=======

If the input number is of type ``INT``, the return string will be 10 characters long (8 characters for the digits and 2 characters for the "0x" prefix). If the input number is of type ``BIGINT``, the return string will be 18 characters long (16 characters for the digits and 2 characters for the "0x" prefix).

Examples
========

``BIGINT`` data type
--------------------

.. code-block:: postgres

   CREATE TABLE cool_numbers(number BIGINT NOT NULL);
   
.. code-block:: postgres

   INSERT INTO cool_numbers VALUES (-42), (3735928559), (666), (3135097598), (3221229823);

.. code-block:: postgres

   SELECT TO_HEX(number) FROM cool_numbers;
   
Output:

.. code-block:: none

	to_hex            
	------------------
	0xffffffffffffffd6
	0x00000000deadbeef
	0x000000000000029a
	0x00000000baddcafe
	0x00000000c00010ff


``INT`` data type
-----------------

.. code-block:: postgres

	CREATE TABLE cool_numbers(number INT NOT NULL);
	
.. code-block:: postgres

	INSERT INTO cool_numbers VALUES (-42), (373592855), (666), (313509759), (322122982);
	
.. code-block:: postgres

	SELECT TO_HEX(number) FROM cool_numbers;
	
Output:

.. code-block:: none

	to_hex            
	----------
	0xffffffd6
	0x16449317
	0x0000029a
	0x12afc77f
	0x133334e6