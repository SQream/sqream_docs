.. _explain:

*****************
EXPLAIN
*****************

``EXPLAIN`` returns a static query plan, which can be used to debug.

Permissions
=============

The role must have the ``SELECT`` privileges for any tables referenced by the query.

Syntax
==========

.. code-block:: postgres

   explain_statement ::=
       SELECT EXPLAIN(query_stmt)
       ;

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``query_stmt``
     - The select query to generate the plan for.

Notes
===========

Use dollar-quoting to escape the query text

Examples
===========

Generating a static query plan
----------------------------------

.. code-block:: psql

   t=> SELECT EXPLAIN($$SELECT DATEADD(hour,1,dt) FROM cool_dates$$);
      Select
         Specific (TTNative Gpu) (dateadd@null := dt@null,
                                  dateadd@val := (pure_if dt@null "0" (addHoursdt2dt dt@val "1")))
       Table Scan
           public.cool_dates ("dt@null", "dt@val") []

