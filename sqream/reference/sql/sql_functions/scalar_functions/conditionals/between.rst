.. _between:

**************************
BETWEEN
**************************

``BETWEEN`` is used to simplify range tests, by returning ``TRUE`` when the input is within two boundaries.

Syntax
==========

.. code-block:: postgres

   expr [ NOT ] BETWEEN lower_bound AND upper_bound


Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - A general value expression or a literal.
   * - ``lower_bound``, ``upper_bound``
     - Lower and upper bounds, of the same data type as ``expr``

Returns
============

Returns ``TRUE`` when ``expr`` is within the bounds, or ``FALSE`` otherwise.

Notes
=======

* ``expr BETWEEN X AND Y`` is equivalent to ``expr >=X AND expr <=Y``.

* The upper boundary must be greater than the lower boundary

Examples
===========

BETWEEN
-----------

.. code-block:: psql

   farm=> SELECT name, num_eyes FROM cool_animals WHERE num_eyes BETWEEN 5 and 8
   name           | num_eyes
   ---------------+---------
   Spider         |        8
   Starfish       |        5
   Praying mantis |        5

NOT BETWEEN
--------------

.. code-block:: psql

   farm=> SELECT name, num_eyes FROM cool_animals WHERE num_eyes NOT BETWEEN 5 and 8
   name           | num_eyes
   ---------------+---------
   Human          |        2
   Horseshoe crab |       10
   Box Jellyfish  |       24
   Fox            |        2
   Possum         |        2
