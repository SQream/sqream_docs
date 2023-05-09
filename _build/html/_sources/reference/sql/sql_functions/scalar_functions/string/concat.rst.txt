.. _concat:

**************************
``||`` (Concatenate)
**************************

Concatenate two strings to create a longer string

Syntax
==========


.. code-block:: postgres

   expr1 || expr2

Arguments
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``expr1``, ``expr2``
     - String expressions

Returns
============

Returns the same type as the argument supplied.

Notes
=======

* Both values must be strings, and can't be ``NULL``. If ``NULLS`` are expected, use :ref:`coalesce`.

* SQream DB removes the trailing spaces from strings by default, which may lead to unexpected results. See the examples for more information.

Examples
===========


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


Concatenate two values
--------------------------------------

Convert values to string types before concatenation

.. code-block:: psql

   
   nba=> SELECT ("Age" :: TEXT) || "Name" FROM nba ORDER BY 1 DESC LIMIT 5;
   ?column?        
   ----------------
   40Tim Duncan    
   40Kevin Garnett 
   40Andre Miller  
   39Vince Carter  
   39Pablo Prigioni


Concatenate two strings
-------------------------------

.. code-block:: psql

   t=> SELECT 'Hello, this is' || ' nice';
   ?column?           
   -------------------
   Hello, this is nice

.. warning::
   Trailing spaces are trimmed by default. For example,
   
   .. code-block:: psql

      t=> SELECT 'Hello, this is ' || 'nice';
      ?column?           
      -------------------
      Hello, this isnice
      
   This may sometimes lead to an unexpected result. See the example below for a remedy.


Adding spaces
-----------------

Add a space and concatenate it first to bypass the space trimming issue

.. code-block:: psql

   nba=> SELECT ("Age" :: TEXT || (' ' || "Name")) FROM nba ORDER BY 1 DESC LIMIT 5;
   ?column?         
   -----------------
   40 Tim Duncan    
   40 Kevin Garnett 
   40 Andre Miller  
   39 Vince Carter  
   39 Pablo Prigioni

