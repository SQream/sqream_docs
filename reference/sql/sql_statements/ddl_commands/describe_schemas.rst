.. _describe_schemas:

*****************
DESCRIBE SCHEMAS
*****************
The ``DESCRIBE SCHEMAS`` command lets you list information about schemas in your cluster.

Syntax
==========
The following is the syntax for the ``DESCRIBE SCHEMAS`` command:

.. code-block:: postgres

   DESCRIBE SCHEMAS [DATABASE <database_name>]

Parameters
============
The following parameters can be used with the ``DESCRIBE SCHEMAS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Value
     - Description
     - Type
   * - ``DATABASE``
     - ``database_name``
     - The name of the database.
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
The following is an example of the generated output in Studio:

.. image:: /_static/images/describe_schemas.png

**Comment** - *Do we currently support rechunker_ignore? Compare screenshot with table above. Also, the "o" in "schema_id" and "rechunker_ignore" are lower case o's, not 0's.*

Permissions
=============
No permissions are required for the ``DESCRIBE_SCHEMAS`` command.