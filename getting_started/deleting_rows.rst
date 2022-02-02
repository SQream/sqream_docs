.. _deleting_rows:

****************************
Deleting Rows
****************************
The **Deleting Rows** section describes the following:

* :ref:`Deleting selected rows<deleting_selected_rows>`
* :ref:`Deleting all rows<deleting_all_rows>`

.. _deleting_selected_rows:

**Deleting Selected Rows**

You can delete rows in a table selectively using the ``DELETE`` command. You must include a table name and `WHERE` clause to specify the rows to delete, as shown in the following example:

.. code-block:: psql

   test=> DELETE FROM cool_animals WHERE weight is null;
   
   executed
   master=> SELECT  * FROM cool_animals;
   1,Dog                 ,7
   2,Possum              ,3
   3,Cat                 ,5
   4,Elephant            ,6500
   5,Rhinoceros          ,2100

   5 rows

.. _deleting_all_rows:

**Deleting All Rows**

You can delete all rows in a table using the ``TRUNCATE`` command followed by the table name, as shown in the following example:

.. code-block:: psql

   test=> TRUNCATE TABLE cool_animals;
   
   executed

.. note:: While :ref:`truncate` deletes data from disk immediately, :ref:`delete` does not physically remove the deleted rows.

For more information, see the following:

* Deleting selected rows - :ref:`DELETE<delete>`
* Deleting all rows - :ref:`TRUNCATE<truncate>`