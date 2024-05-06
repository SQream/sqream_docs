:orphan:

.. _substring:

*********
SUBSTRING
*********

the ``SUBSTRING`` function is used to extract a portion of a string based on specified starting position and length.

.. note:: Some systems call this function ``SUBSTR``.

See also :ref:`regexp_substr`.

Syntax
======

.. code-block:: postgres

   SUBSTRING( expr, start_pos, length )

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr``
     - Original string expression from which you want to extract the substring
   * - ``start_pos``
     - Accepts an integer or bigint expression that specifies the position within the string where the extraction should begin. If start exceeds the number of characters in the expression, an empty string is returned.  If start is less than 1, the expression starts from the first character
   * - ``length``
     - Accepts an integer or bigint expression that specifies the number of characters to be returned from the expression. If the sum of start and length exceeds the total number of characters in the expression, the entire value starting from the position specified by start is returned. If length is negative or zero, the function returns an empty string

Returns
=======

* Returns the same type as the argument supplied

* If any of the arguments is NULL, the return is NULL

Notes
=====

* Character count starts at 1.


Examples
========

For these examples, assume a table named ``nba``, with the following structure:

.. code-block:: postgres
   
   CREATE TABLE nba
   (
      Name text(40),
      Team text(40),
      Number tinyint,
      Position text(2),
      Age tinyint,
      Height text(4),
      Weight real,
      College text(40),
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

