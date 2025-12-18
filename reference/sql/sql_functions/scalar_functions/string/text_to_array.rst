.. _text_to_array:

*********
TEXT_TO_ARRAY
*********

The ``TEXT_TO_ARRAY`` function converts a delimited text value into an array of strings using the specified delimiter.

.. note:: Some systems call this function ``SUBSTR``.

See also :ref:`regexp_substr`.

Syntax
======

.. code-block:: postgres

   cast_utils.text_to_array(text_column,delimiter)

Arguments
=========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``text_column``
     - The input string to be split into array elements.
   * - ``delimiter``
     - The string used as a separator between elements in text_column.

Returns
=======

* One array value per input row

* Each element in the returned array corresponds to a substring of text_column separated by delimiter.

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

