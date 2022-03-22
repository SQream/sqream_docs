.. _percent_rank:

**************************
PERCENT_RANK
**************************

The **PERCENT_RANK** function returns relative data ranking information and is similar to the **RANK** function.

It differs from the RANK function in the following ways:

* The output type is ``double`` instead of ``bigint``.
* Shows ranking as a *relative* rank number (for example, a number between and including ``0`` and ``1``), and not an *absolute* rank number (for example, ``1``, ``1``, ``3``).

Syntax
-------
The following shows the correct syntax for the PERCENT_RANK function.

.. code-block:: postgres

   PERCENT_RANK ( ) OVER (...)       

Arguments
---------
None

Returns
---------
Returns relative data ranking information in the form of a number between (and including) ``0`` and ``1``.
