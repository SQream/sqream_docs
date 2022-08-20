.. _inserting_rows:

****************************
Inserting Rows
****************************
The **Inserting Rows** section describes the following:

* :ref:`Inserting basic rows<inserting_basic_rows>`
* :ref:`Changing value order<changing_value_order>`
* :ref:`Inserting multiple rows<inserting_multiple_rows>`
* :ref:`Omitting columns<omitting_columns>`


.. _inserting_basic_rows:

**Inserting Basic Rows**

You can insert basic rows into a table using the ``INSERT`` statement. The inserted statement includes the table name, an optional list of column names, and column values listed in the same order as the column names, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals VALUES (1, 'Dog', 7);
   
   executed

.. _changing_value_order:

**Changing Value Order**

You can change the order of values by specifying the column order, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals(weight, id, name) VALUES (3, 2, 'Possum');
   
   executed

.. _inserting_multiple_rows:

**Inserting Multiple Rows**

You can insert multiple rows using the ``INSERT`` statement by using sets of parentheses separated by commas, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals VALUES
         (3, 'Cat', 5) ,
         (4, 'Elephant', 6500) ,
         (5, 'Rhinoceros', 2100);
   
   executed

.. note:: You can load large data sets using bulk loading methods instead. For more information, see :ref:`inserting_data`.

.. _omitting_columns:

**Omitting Columns**

Omitting columns that have a default values (including default ``NULL`` values) uses the default value, as shown in the following example:

.. code-block:: psql

   test=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed

.. code-block:: psql

   test=> INSERT INTO cool_animals (id) VALUES (6);
   
   executed
   test=> SELECT * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100
   6,\N,\N
   
   6 rows

.. note:: Null row values are represented as ``\N``

For more information on inserting rows, see :ref:`insert`.

For more information on default values, see :ref:`default value<default_values>`.