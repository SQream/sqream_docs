.. _decode:

********************
DECODE
********************
The **DECODE** function is used for decoding or extracting binary data from a textual input string.

Syntax
==========
The following shows the correct syntax for the DECODE function:

.. code-block:: postgres

   DECODE(string input_text, format type_text)

Parameters
============
The following table shows the DECODE parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``input_text``
     - Defines the input text string.
   * - ``type_text``
     - Defines the format used for decoding the input text.

Returns
=========



Examples
===========

   
Permissions
=============

The role must have the ``SUPERUSER`` permissions.