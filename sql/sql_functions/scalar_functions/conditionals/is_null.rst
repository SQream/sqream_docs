.. _is_null:

**************************
IS NULL
**************************

``IS NULL`` is used to test if an expression is null.

Syntax
==========

.. code-block:: postgres

   expr IS [ NOT ] NULL
   


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

Returns ``TRUE`` when ``expr`` is ``NULL`` or ``FALSE`` otherwise.


Examples
===========

For these examples, consider the following table and contents:

.. code-block:: postgres
   
   CREATE TABLE t (id INT NOT NULL, name TEXT, weight INT);
   
   INSERT INTO t VALUES (1, 'Kangaroo', 120), (2, 'Koala', 20), (3, 'Wombat', 60)
                       ,(4, 'Kappa', NULL),(5, 'Echidna', 8),(6, 'Chupacabra', NULL)
                       ,(7, 'Kraken', NULL);

IS NULL
-----------

.. code-block:: psql

   m=> SELECT * FROM t WHERE weight IS NULL;
   id | name       | weight
   ---+------------+-------
    4 | Kappa      |       
    6 | Chupacabra |       
    7 | Kraken     |       



Using IS NOT NULL to filter unwanted results
-----------------------------------------------

.. code-block:: psql

   m=> SELECT AVG(weight) FROM t WHERE weight IS NOT NULL;
   avg
   ---
   52

