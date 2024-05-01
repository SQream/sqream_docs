.. _last_value:

**************************
LAST_VALUE
**************************
The **LAST_VALUE** function returns the value located in the selected column of the last row of a segment. If the table is not segmented, the LAST_VALUE function returns the value from the last row of the whole table.

This function returns the same type of variable that you input for your requested value. For example, requesting the value for the last employee in a list using an ``int`` type output returns an ``int`` type ID column.

Syntax
-------
The following shows the correct syntax for the LAST_VALUE function.

.. code-block:: postgres

   LAST_VALUE(Selected_Column) OVER (...)

Arguments
---------
None

Returns
---------
Returns the value located in the selected column of the last row of a segment.
