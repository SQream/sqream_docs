.. _describe_databases:

*****************
DESCRIBE DATABASES
*****************
The ``DESCRIBE DATABASES`` command lets you show all databases in your cluster.

**Comment** - *See the Output table for this command. The outputs there are not databases, but rather INFORMATION about the database. Please confirm.*

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE DATABASES

Parameters
============
The following parameter can be used when switching databases with the **DESCRIBE DATABASES** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``DATABASES``
     - Displays the name of the database.
	 
Examples
==============
The following is an example of the **DESCRIBE DATABASES** command:

.. code-block:: postgres

   DESCRIBE DATABASES

**Comment** - *Need example*   
 
Output
=============
Using the **DESCRIBE DATABASES** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
     - Type
   * - ``created_on``
     - Displays the date and time when the database was created.
     - Date
   * - ``name``
     - Displays the name of the database.
     - Text
   * - ``is_current``
     - Displays whether the database is currently being used.
     - Boolean
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*