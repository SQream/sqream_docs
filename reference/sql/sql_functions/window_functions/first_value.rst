.. _first_value:

**************************
FIRST_VALUE
**************************
The **FIRST_VALUE** function returns the value located in the selected column of the first row of a segment. If the table is not segmented, the FIRST_VALUE function returns the value from the first row of the whole table.

This function returns the same type of variable that you input for your requested value. For example, requesting the value for the first employee in a list using an ``int`` type output returns an ``int`` type ID column. If you use a ``varchar`` type, the function returns a ``varchar`` type name column.

Syntax
-------
The following shows the correct syntax for the FIRST_VALUE function.

.. code-block:: postgres

   FIRST_VALUE(Selected_Column) OVER (...)

Arguments
---------
None

Returns
---------
Returns the value located in the selected column of the first row of a segment.
