:orphan:

.. _values:

******
VALUES
******

``VALUES`` is a table constructor used to define tabular data. It's utilized with :ref:`INSERT<insert>` statements to insert one or more rows.

Syntax
======

.. code-block:: postgres

   VALUES ( <value_expr> [, ... ] ) [, ... ]

Usage Notes
===========

.. glossary::

   ``value_expr``

      Each set of comma-separated ``value_expr`` in parentheses represents a single row in the result set.

   **Column names**

      Column names of the result table are auto-generated. To rename the column, add an ``AS`` clause.
	  
	**Aggregations**
		Aggregations (e.g., ``SUM``, ``COUNT``) cannot be directly used in the ``VALUES`` clause.

Examples
========

Tabular Data with VALUES
------------------------

.. code-block:: postgres

	VALUES (1,2,3,4), (5,6,7,8), (9,10,11,12);

	clmn1 |clmn2 |clmn3 |clmn4  
	------+------+------+-----
	1     | 2    | 3    | 4       
	5     | 6    | 7    | 8  
	9     | 10   | 11   | 12  

Using VALUES in a ``SELECT`` Query
----------------------------------

To use VALUES in a select query, assign a :ref:`name<identifiers>` to the ``VALUES`` clause with an ``AS`` clause.

.. code-block:: postgres

	SELECT
	 t.*
	FROM
	(
	 VALUES
	  (1, 2, 3, 'a'),
	  (5, 6, 7, 'b'),
	  (9, 10, 11, 'c')
	) AS t;

	clmn1 |clmn2 |clmn3 |clmn4  
	------+------+------+-----
	1     | 2    | 3    | a       
	5     | 6    | 7    | b  
	9     | 10   | 11   | c  

You can also use this to rename the columns

.. code-block:: postgres

	SELECT
	  t.*
	FROM
	 (
	  VALUES
	   (1, 2, 3, 'a'),
	   (5, 6, 7, 'b'),
	   (9, 10, 11, 'c')
	 ) AS t(a, b, c, d);


Creating a Table Using ``VALUES``
---------------------------------

Use ``AS`` to assign names to columns

.. code-block:: postgres

	CREATE TABLE
	  cool_animals AS (
	   SELECTt.*
	   FROM
	(
	  VALUES
	  (1, 'dog'),
	  (2, 'cat'),
	  (3, 'horse'),
	  (4, 'hippopotamus')
	)  
	  AS t(id, name)
	  );

Permissions
===========

This clause requires no special permissions.
