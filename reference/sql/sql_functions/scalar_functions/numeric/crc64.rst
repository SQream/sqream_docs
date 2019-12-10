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
     - Text expression (``VARCHAR``, ``NVARCHAR``)

Returns
============

Always returns a 64-bit ``BIGINT`` value

Notes
=======

* If the input value is NULL, the result is NULL.

Examples
===========

Natural log values
--------------------------

.. code-block:: psql

   numbers=> SELECT CRC64(x) FROM 
   .>   (VALUES ('This is a relatively long text string, that can be converted to a shorter hash' :: varchar(80)))
   .>   as t(x);
   crc64               
   --------------------
   -9085161068710498500

