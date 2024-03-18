.. _rechunk:

*******
RECHUNK
*******

SQreamDB is most efficient processing large data chunks. The ``rechunk`` function improves performance when handling tables with small data chunks by allowing you to consolidate these small chunks into larger ones. Additionally, this function also addresses mixed chunks, which are those containing one or more deleted records. When applied to mixed chunks, the function performs a :ref:`cleanup operation<delete_guide>`, resulting in clean, large data chunks.

Syntax
==========

.. code-block:: postgres

   SELECT rechunk('<schema_name>', '<table_name>')

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``schema_name``
     - The name of the schema in which the table to rechunk is in 
   * - ``table_name``
     - The name of the table to rechunk

Example
=======

.. code-block:: postgres

   SELECT rechunk('public', 't');

Permissions
=============

Using the ``rechunk`` command requires no special permissions.