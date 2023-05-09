.. _charindex:

**************************
CHARINDEX
**************************

Returns the starting position of a string inside another string.

See also :ref:`patindex`, :ref:`regexp_instr`.

Syntax
==========

.. code-block:: postgres

   CHARINDEX ( needle_string_expr , haystack_string_expr [ , start_location ] )

Arguments
============

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
============

Integer start position of a match, or 0 if no match was found.

Notes
=======

* If the value is ``NULL``, the result is ``NULL``.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres

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
-----------------------------------------

.. code-block:: psql

   SELECT username, CHARINDEX('john', username) FROM users;

   username      | charindex
   --------------+----------
   john_doe      |         1
   jane_doe      |         0
   bob_smith     |         0
   susan_jones   |         0

