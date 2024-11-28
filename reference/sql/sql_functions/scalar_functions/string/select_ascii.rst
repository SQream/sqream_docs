.. _select_ascii:

*****
ASCII
*****
The **ASCII** function is commonly used in combination with other SQL functions for operations such as data transformation, validation, and storing based on ASCII values.

Syntax
======
The following shows the syntax for the SELECT ASCII function:

.. code-block:: postgres

	ASCII()

Return
======

The function returns an 'INT' value representing the ASCII code of the leftmost character in a string.

Example
===========
.. code-block:: postgres

   SELECT ASCII('hello');
