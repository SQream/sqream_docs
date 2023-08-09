.. _charindex:

*********
CHARINDEX
*********

``CHARINDEX`` is a 1-based indexing function that returns the starting position of a specified substring within a given string. 


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

Examples
========

For these examples, consider the following table and contents:

.. code-block:: sql

      CREATE TABLE users (
          id INT,
          username TEXT,
          email TEXT,
          password TEXT
      );

      INSERT INTO users (id, username, email, password)
      VALUES (1, 'john_doe', 'john.doe@example.com', 'password1'),
             (2, 'jane_doe', 'jane.doe@example.com', 'password2'),
             (3, 'bob_smith', 'bob.smith@example.com', 'password3'),
             (4, 'susan_jones', 'susan.jones@example.com', 'password4');


Using ``CHARINDEX``
-------------------

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


