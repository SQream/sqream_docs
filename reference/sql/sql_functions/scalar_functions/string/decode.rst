.. _decode:

********************
DECODE
********************
The **DECODE** function is used to translate a code value into a corresponding value that is meaningful to humans. This function is typically used in situations where a code needs to be presented to a user in a more understandable format, such as when displaying data in a report or on a user interface.

Syntax
==========
The following shows the correct syntax for the DECODE function:

.. code-block:: postgres

   DECODE(string input_text, format type_text);

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

Return
======

Returns the same type as the argument supplied.

	
