.. _concat_function:

**************************
CONCAT function
**************************

Concatenates one or more strings, or concatenates one or more binary values.

Syntax
==========


.. code-block:: postgres

   CONCAT( <expr> [ , <expr> ... ] )


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

The data type of the returned value is TEXT, If any input value is NULL, returns NULL.

Notes
=======

* The :ref:`concat` operator provides alternative syntax for CONCAT and requires at least two arguments.
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

   
   nba=> SELECT  CONCAT(Age ,Name) FROM nba ORDER BY 1 DESC LIMIT 5;
   ?column?        
   ----------------
   40Tim Duncan    
   40Kevin Garnett 
   40Andre Miller  
   39Vince Carter  
   39Pablo Prigioni
