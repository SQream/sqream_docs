.. _crc64:

**************************
CRC64
**************************

Calculates the CRC-64 hash of a text expression

Syntax
==========

.. code-block:: postgres

   CRC64( expr ) --> BIGINT
   
   CRC64_JOIN( expr ) --> BIGINT

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

Notes
=======

* If the input value is NULL, the result is NULL.

* The ``CRC64_JOIN`` can be used with ``VARCHAR`` only. It can not be used with ``TEXT``.

* The ``CRC64_JOIN`` variant ignores leading whitespace when used as a ``JOIN`` key.

Examples
===========

Calculate a CRC-64 hash of a string
---------------------------------------

.. code-block:: psql

   numbers=> SELECT CRC64(x) FROM 
   .    (VALUES ('This is a relatively long text string, that can be converted to a shorter hash' :: text))
   .    as t(x);
   crc64               
   --------------------
   -9085161068710498500

