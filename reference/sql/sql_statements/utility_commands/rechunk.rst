:orphan:

.. _rechunk:

*******
RECHUNK
*******

SQreamDB is the most efficient for processing large data chunks. The ``rechunk`` function improves performance when handling tables with small data chunks by allowing you to consolidate these small chunks into larger ones. This function also handles mixed chunks, which include one or more deleted records and/or records marked for deletion but not yet purged (i.e., awaiting the removal of deleted data). When applied to mixed chunks, the function performs a :ref:`cleanup operation<delete_guide>`, resulting in clean, large data chunks.

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


Rechunk Encrypted Columns
=========================

For tables with encrypted columns, the utility function is RECHUNK_ENCRYPTED requires also the database name and the encryption keys for each encrypted column.

Syntax
==========

.. code-block:: postgres

   SELECT RECHUNK_ENCRYPTED('<db_name>','<schema>', '<table>', '<col1>', '<key1>', '<col2>', '<key2>', ...);

Example
==========

.. code-block:: postgres

   CREATE TABLE sc.tbl (
       x TEXT ENCRYPT,
       y TEXT,
       z TEXT ENCRYPT
   );

   SELECT RECHUNK_ENCRYPTED('master','sc', 'tbl', 'x', '[key-for-x]', 'z', '[key-for-z]');


Permissions
=============

Using the ``rechunk`` command requires no special permissions.
