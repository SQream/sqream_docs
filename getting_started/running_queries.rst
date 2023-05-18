.. _running_queries:

****************************
Running Queries
****************************

Running Basic Queries
---------------------

You can run a basic query using the ``SELECT`` keyword, followed by a list of columns and values to be returned, and the table to get the data from, as shown in the following example:

.. code-block:: psql

   test=> SELECT id, name, weight FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows
   
For more information on the ``SELECT`` keyword, see :ref:`select`.


To Output All Columns
---------------------

You can output all columns without specifying them using the star operator ``*``, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows


Outputting Shorthand Table Values
---------------------------------

You can output the number of values in a table without getting the full result set by using the ``COUNT`` statement:

.. code-block:: psql

   test=> SELECT COUNT(*) FROM cool_animals;
   6
   
   1 row


Filtering Results
-----------------

You can filter results by adding a ``WHERE`` clause and specifying the filter condition, as shown in the following example:

.. code-block:: psql

   test=> SELECT id, name, weight FROM cool_animals WHERE weight > 1000;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   
   2 rows

Sorting Results
---------------

You can sort results by adding an ``ORDER BY`` clause and specifying ascending (``ASC``) or descending (``DESC``) order, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3
   6,\N,\N

   6 rows


Filtering Null Rows
--------------------

You can filter null rows by adding an ``IS NOT NULL`` filter, as shown in the following example:

.. code-block:: psql

   test=> SELECT * FROM cool_animals WHERE weight IS NOT NULL ORDER BY weight DESC;
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   1,Dog                 ,7
   3,Cat                 ,5
   2,Possum              ,3

   5 rows
   
For more information, see the following:

* Outputting the number of values in a table without getting the full result set - :ref:`COUNT(*)<count>`.
* Filtering results - :ref:`WHERE<where>`
* Sorting results - :ref:`ORDER BY<order_by>`
* Filtering rows - :ref:`IS NOT NULL<is_null>`