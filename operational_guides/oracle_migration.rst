.. _oracle_migration:

**********************
Oracle Migration Guide
**********************



Before You Begin
================



Using SQream Commands, Statements, and UDFs
===========================================

.. list-table:: Operation Functions
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``+ (unary)``
     - ``+ (unary)``
     - +a
   * - ``+``
     - ``+``
     - a+ b
   * - ``- (unary)``
     - ``- (unary)``
     - -a
   * - ``-``
     - ``-``
     - a - b
   * - ``*``
     - ``*``
     - a * b
   * - ``/``
     - ``/``
     - a / b
   * - ``%``
     - ``%``
     - a % b
   * - ``&``
     - ``&``
     - AND
   * - ``~``
     - ``~``
     - NOT
   * - ``|``
     - ``|``
     - OR
   * - ``<<``
     - ``<<``
     - Shift left
   * - ``>>``
     - ``>>``
     - Shift right
   * - ``XOR``
     - ``XOR``
     - XOR

.. list-table:: Conditional Functions
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ``BETWEEN``
     - ``BETWEEN``
     - Value is in [ or not within ] the range
   * - ``CASE``
     - ``CASE``
     - Tests a conditional expression, depending on the result
   * - ``COALESCE``
     - ``COALESCE``
     - Evaluate first non-NULL expression
   * - ``IN``
     - ``IN``
     - Value is in [ or not within ] a set of values
   * - ``ISNULL``
     - ``ISNULL``
     - Alias for COALESCE with two expressions
   * - ``IS_ASCII``
     - ``IS_ASCII``
     - Test a TEXT for ASCII-only characters
   * - ``IS_NULL``
     - ``IS NULL``
     - Check for NULL [ or non-NULL ] values
   * - ``DECODE``
     - ``DECODE``
     - Decodes or extracts binary data from a textual input string
   

.. list-table:: Numeric Functions
   :widths: auto
   :header-rows: 1
   
   * - Oracle
     - SQream
     - Description
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
   * - ````
     - ````
     - 
