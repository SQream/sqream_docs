.. _get_total_chunks_size:

********************
GET TOTAL CHUNKS SIZE
********************
The ``get_total_chunks_size`` function returns the total size of all data chunks saved in the system in both compressed and uncompressed formats.

.. contents:: 
   :local:
   :depth: 1   

Syntax
==========

.. code-block:: postgres

   SELECT get_total_chunks_size(<OUTPUT_UNITS>, [DATABASE_NAME], [SCHEMA_NAME, [TABLE_NAME]])

Parameters
============
The following table shows the ``SELECT get_total_chunks_size`` parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - State
     - Description
   * - ``OUTPUT_UNITS``
     - Mandatory
     - Specifies the desired unit of measurement for the output size, with valid values of ``BYTE``, ``MB``, ``GB``, ``TB``, or ``PB``
   * - ``DATABASE_NAME``
     - Optional
     - Specifies the name of the database to analyze. If not specified, the function will analyze all databases in the cluster.
   * - ``SCHEMA_NAME``
     - Optional
     - Specifies the name of the schema to analyze. If not specified, the function will analyze all schemas in the specified database.
   * - ``TABLE_NAME``
     - Optional
     - Specifies the name of a specific table to analyze. If not specified, the function will analyze all tables in the specified schema.

Example
===========

.. code-block:: psql

   SELECT get_total_chunks_size('MB');
   
Output
==========


.. code-block:: postgres

   compression-type         | value                          | size  | 
   -------------------------+--------------------------------+-------+
   Compressed               | 0.00036144256591796875         |   MB  |
   Uncompressed             | 0.00036144256591796875         |   MB  |

Permissions
=============

Using the ``get_total_chunks_size`` command requires no special permissions.