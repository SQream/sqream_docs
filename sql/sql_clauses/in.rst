:orphan:

.. _in:

**
IN
**

The ``IN`` clause tests if an expression is contained in a list of values.

Syntax
======

.. code-block:: postgres

	expr [ NOT ] IN  ( value_expr [, ...] )
   
Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - A general value expression or a literal to test.
   * - ``value_expr [, ...]``
     - A comma separated list of literal values of the same data type as ``expr``

Returns
=======

Returns ``TRUE`` when ``expr`` is contained in the set, or ``FALSE`` otherwise.

Usage Notes
===========

* ``NULL`` is never equal to ``NULL``, so to check if a value is ``NULL`` use :ref:`IS NULL<is_null>` instead.

* Using ``IN`` with more than 100 literal values can slow down query compilation. If your query relies on more than 100 values, consider using a lookup table and an inner join.

Examples
========

``IN``
------

.. code-block:: psql

	SELECT
	  name,
	  num_eyes
	FROM
	  cool_animals
	WHERE
	  num_eyes IN (8, 10);
	
.. code-block:: none	

	name           | num_eyes
	---------------+---------
	Spider         |        8
	Horseshoe crab |       10


``NOT IN``
----------

.. code-block:: psql

	SELECT
	  name,
	  num_eyes
	FROM
	  cool_animals
	WHERE
	  num_eyes NOT IN (8, 10);
	
.. code-block:: none	

	name           | num_eyes
	---------------+---------
	Box Jellyfish  |       24
	Human          |        2
	Fox            |        2
	Possum         |        2
