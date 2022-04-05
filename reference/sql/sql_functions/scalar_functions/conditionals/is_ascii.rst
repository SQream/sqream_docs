.. _is_ascii:

**************************
IS_ASCII
**************************

``IS_ASCII`` is used to test if a string contains only ASCII characters.

Syntax
==========

.. code-block:: postgres

   IS_ASCII( expr ) --> BOOL
   


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
   
   CREATE TABLE dictionary (id INT NOT NULL, text TEXT);
   INSERT INTO dictionary VALUES (1, '行こう'), (2, '乾杯'), (3, 'L''chaim');
   SELECT id, text, IS_ASCII(text) FROM dictionary;

IS NULL
-----------

.. code-block:: psql

   id | text     | is_ascii
   ---+----------+----------+---------
    1 | 行こう    | false
    2 | 乾杯      | false
    3 | L'chaim   | true	


