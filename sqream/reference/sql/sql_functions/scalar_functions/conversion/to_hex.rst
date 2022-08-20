.. _to_hex:

**************************
TO_HEX
**************************

Converts an integer to a hexadecimal representation.

Syntax
==========

.. code-block:: postgres

   TO_HEX( expr ) --> VARCHAR

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - An integer expression

Returns
============

* Representation of the hexadecimal number of type ``VARCHAR``.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

   CREATE TABLE cool_numbers(number BIGINT NOT NULL);

   INSERT INTO cool_numbers VALUES (42), (3735928559), (666), (3135097598), (3221229823);


Convert numbers to hexadecimal
-------------------------------------

.. code-block:: psql

   master=> SELECT TO_HEX(number) FROM cool_numbers;
   to_hex            
   ------------------
   0x000000000000002a
   0x00000000deadbeef
   0x000000000000029a
   0x00000000baddcafe
   0x00000000c00010ff
