.. _substring:

**************************
SUBSTRING
**************************
 
Returns a substring of the input starting at ``start_pos``.

.. note:: Some systems call this function ``SUBSTR``.

See also :ref:`regexp_substr`.

Syntax
==========

.. code-block:: postgres

   SUBSTRING( expr, start_pos, length )

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - String expression
   * - ``start_pos``
     - Starting position (starts at 1)
   * - ``length``
     - Number of characters to extract

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* Character count starts at 1.

* If the value is NULL, the result is NULL.

Examples
===========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name text,
      Team text,
      Number tinyint,
      Position text,
      Age tinyint,
      Height text,
      Weight real,
      College text,
      Salary float
    );


Here's a peek at the table contents (:download:`Download nba.csv </_static/samples/nba.csv>`):

.. csv-table:: nba.csv
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1

Substring using fixed offsets
-------------------------------

Get 4 characters, starting from the 4th character

.. code-block:: psql

   nba=> SELECT SUBSTRING("Name", 4, 4) FROM nba LIMIT 5;
   substring
   ---------
   ry B     
   Cro      
   n Ho     
   . Hu     
   as J     

Truncating strings
--------------------

Trim a string to 10 characters

.. code-block:: psql

   nba=> SELECT SUBSTRING("Name", 1, 10) FROM nba LIMIT 5;
   substring 
   ----------
   Avery Brad
   Jae Crowde
   John Holla
   R.J. Hunte
   Jonas Jere

