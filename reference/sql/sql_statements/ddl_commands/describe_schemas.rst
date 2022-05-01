.. _describe_schemas:

*****************
DESCRIBE SCHEMAS
*****************
The ``DESCRIBE SCHEMAS`` command lets you show all schemas in your cluster.

**Comment** - *See the Output table for this command. The outputs there are not schemas, but rather INFORMATION about the schemas. Please confirm.*

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE SCHEMAS [DATABASE <db_name>]

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE SCHEMAS** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``db_name``
     - Outputs the schema name.	 
	 
Examples
==============
The following is an example of the **DESCRIBE SCHEMAS** command:

.. code-block:: postgres

   DESCRIBE SCHEMAS DATABASE master;
   	 
Output
=============
Using the **DESCRIBE SCHEMAS** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
     - Type
   * - ``schema_id``
     - Displays the schema ID.
     - Integer
   * - ``name``
     - Displays the schema name.
     - Text
   * - ``owner``
     - Displays the schema owner.
     - Text
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*