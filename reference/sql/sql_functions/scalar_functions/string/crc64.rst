.. _crc64:

**************************
CRC64
**************************

Calculates the CRC-64 hash of a text expression

Syntax
==========

.. code-block:: postgres

   CRC64( expr ) --> BIGINT

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Text expression (``TEXT``)

Returns
============

Returns a CRC-64 hash of the text input, of type ``BIGINT``.

.. note:: If the input value is NULL, the result is NULL.

Examples
===========

Calculate a CRC-64 hash of a string
---------------------------------------

.. code-block:: psql

   SELECT CRC64(x) FROM (VALUES ('This is a relatively long text string, that can be converted to a shorter hash' :: text)) as t(x);
   -8397827068206190216