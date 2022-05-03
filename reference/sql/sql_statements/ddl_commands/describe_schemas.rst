.. _describe_schemas:

*****************
DESCRIBE SCHEMAS
*****************
The ``DESCRIBE SCHEMAS`` command lets you show all schemas in your cluster.

**Comment** - *See the Output table for this command. The outputs there are not schemas, but rather INFORMATION about the schemas. Please confirm.*

Syntax
==========
The following is the correct syntax for the ``DESCRIBE SCHEMAS`` command:

.. code-block:: postgres

   DESCRIBE SCHEMAS [DATABASE <database_name>]

Parameters
============
The following parameters can be used with the ``DESCRIBE SCHEMAS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
   * - ``database_name``
     - Displays the name of the database.
     - Text
	 
Examples
==============
The following is an example of the ``DESCRIBE SCHEMAS`` command:

.. code-block:: postgres

   DESCRIBE SCHEMAS DATABASE master;
   	 
Output
=============
Using the ``DESCRIBE SCHEMAS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``schema_id``
     - Displays the schema ID.
     - Integer
     - 0
   * - ``schema_name``
     - Displays the schema name.
     - Text
     - public
   * - ``schema_owner``
     - Displays the schema owner.
     - Text
     - sqream
     
Example
===========
The following is an example of the generated output:

.. code-block:: postgres

   0,public,sqream,false

Permissions
=============
**Comment** - *What are the permissions?*