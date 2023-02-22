.. _select_ascii:

********************
SELECT ASCII
********************
The **SELECT ASCII** function is commonly used in combination with other SQL functions for operations such as data transformation, validation, and storing based on ASCII values.

Syntax
==========
The following shows the syntax for the SELECT ASCII function:

.. code-block:: postgres

   SELECT ASCII('');

Returns
=========

The SELECT ASCII function returns the ASCII code value of the leftmost character of a string.

Example
===========
.. code-block:: postgres

   SELECT ASCII('hello');
