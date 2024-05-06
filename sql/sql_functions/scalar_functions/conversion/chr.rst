:orphan:

.. _chr:

***
CHR
***

The ``CHR`` function takes an integer parameter representing the ASCII code and returns the corresponding character.

Syntax
======

.. code-block:: postgres

   CHR(int)
   
Argument
========

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Description
   * - ``int``
     - Integer argument that represents the ASCII code of the character you want to retrieve


Returns
=======

Returns the ASCII character representation of the supplied integer.


Example
=======

Create the following table:

.. code-block:: postgres

	CREATE OR REPLACE TABLE t(x INT NOT NULL);

	INSERT INTO t (x)
	VALUES (72), (101), (108), (108), (111);
	
Execute the ``CHR`` function:

.. code-block:: postgres

	SELECT CHR(x) FROM t;
	
Output:

.. code-block:: postgres

	CHR   |
	------+
	H     |
	e     |
	l     |
	l     |
	o     |