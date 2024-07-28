:orphan:

.. _charindex:

*********
CHARINDEX
*********

``CHARINDEX`` is a 1-based indexing function (both input and output) that returns the starting position of a specified substring within a given string. 


See also :ref:`patindex`, :ref:`regexp_instr`.

Syntax
======

.. code-block:: sql

	CHARINDEX ( needle_string_expr , haystack_string_expr [ , start_location ] )

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``needle_string_expr``
     - String to find
   * - ``haystack_string_expr``
     - String to search within
   * - ``start_location``
     - An integer at which the search starts. This value is optional and when not supplied, the search starts at the beggining of ``needle_string_expr``

Returns
=======

Integer start position of a match, or 0 if no match was found.

If one of the parameters is NULL, then the return value is NULL.

Empty string search returns 0.

Examples
========

For these examples, consider the following table:

.. code-block:: none

	id  | username	  | email                   |
	----+-------------+-------------------------+
	1   | john_doe    | john.doe@example.com    |
	----+-------------+-------------------------+
	2   | jane_doe    | jane.doe@example.com    |
	----+-------------+-------------------------+
	3   | bob_smith   | bob.smith@example.com   | 
	----+-------------+-------------------------+
	4   | susan_jones | susan.jones@example.com |


.. code-block:: sql

   SELECT CHARINDEX('doe', username) FROM users;

Output:

.. code-block:: none

   charindex|
   ---------+
   6        |
   6        |
   0        |
   0        |
   
.. code-block:: sql

	SELECT CHARINDEX('doe', username, 10) FROM users;

Output:

.. code-block:: none

   charindex|
   ---------+
   0        |
   0        |
   0        |
   0        |

.. code-block:: sql

	SELECT CHARINDEX('jane_doe', username, -10) FROM users;
	
.. code-block:: none

   charindex|
   ---------+
   0        |
   1        |
   0        |
   0        |
