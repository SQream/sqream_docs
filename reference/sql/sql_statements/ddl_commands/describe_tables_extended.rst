.. _describe_tables_extended:

*****************
DESCRIBE TABLES EXTENDED
*****************
The ``DESCRIBE TABLES EXTENDED`` command lets you list all the tables in your database, including information about storage and deleted data.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE TABLES EXTENDED [DATABASE <database_name>] [SCHEMA <schema_name>] EXTERNAL | INTERNAL | VIEW | ALL (default)

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE TABLES EXTENDED** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``schema_name``
     - Displays the schema name.
   * - ``database_name``
     - Displays the name of the database.
   * - ``table type``
     - Lets you select EXTERNAL, INTERNAL, or ALL tables.
	 
Examples
==============
The following is an example of the **DESCRIBE TABLES EXTENDED** command:

.. code-block:: postgres

   DESCRIBE TABLES EXTENDED DATABASE <public> SCHEMA <customers> INTERNAL
   
Output
=============
Using the **DESCRIBE SCHEMAS** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
	 - Type
   * - ``created_on``
     - Displays the date and time when the table was created.
     - Date
   * - ``name``
     - Displays the name of the table.
     - Text
   * - ``type``
     - Displays the type of table (internal/external/all).
     - Text	 
   * - ``database``
     - Displays the name of the database.
     - Text	    
   * - ``schema``
     - Displays the name of the schema.
     - Text
   * - ``owner``
     - Displays the owner of the schema.
     - Text
   * - ``rows``
     - Displays the number of rows in the table, returning ``NULL`` for external table.
     - Big Integer
   * - ``bytes``
     - Displays the compressed number of bytes scanned if the whole table is scanned during a query. This number may differ from the number of bytes stored on-disk for a table.
     - 
   * - ``dropped_on``
     - Returned if the HISTORY variable is used, returning ``NULL`` when no tables are dropped.
     - Date
   * - ``number_of_chunks``
     - Displays the number of chunks.
     - Integer	 
   * - ``bytes``
     - Displays the uncompressed number of bytes scanned if the whole table is scanned during a query. This number may differ from the number of bytes stored on-disk for a table.	 
     - Big Integer	 
   * - ``number_of_chunks_with_deleted_rows``
     - Displays the number of chunks that rows were deleted from.
     - Integer
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*