.. _is_ascii:

**************************
IS_ASCII
**************************

``IS_ASCII`` is used to test if a string contains only ASCII characters.

Syntax
==========

.. code-block:: postgres

   IS_ASCII( expr ) --> Boolean
   


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - A general value expression or a literal to test.


Returns
============

Returns ``TRUE`` when ``expr`` contains only ASCII characters (0-127) or ``FALSE`` otherwise.

Notes
========

* If the expression to test is ``NULL``, ``IS_ASCII`` returns ``NULL``.

Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE dictionary (id INT NOT NULL, fw NVARCHAR(30), en VARCHAR(30));
   
   INSERT INTO dictionary VALUES (1, '行こう', 'Let''s go'), (2, '乾杯', 'Cheers'), (3, 'L''chaim', 'Cheers');

IS NULL
-----------

.. code-block:: psql

   m=> SELECT id, en, fw, IS_ASCII(fw) FROM dictionary;
   id | en       | fw       | is_ascii
   ---+----------+----------+---------
    1 | Let's go | 行こう     | false   
    2 | Cheers   | 乾杯      | false   
    3 | Cheers   | L'chaim  | true    


