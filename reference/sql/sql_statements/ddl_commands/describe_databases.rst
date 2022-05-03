.. _describe_databases:

*****************
DESCRIBE DATABASES
*****************
The ``DESCRIBE DATABASES`` command lets you show all databases in your cluster.

**Comment** - *See the Output table for this command. The outputs there are not databases, but rather INFORMATION about the database. Please confirm.*

Syntax
==========
The following is the correct syntax for the ``DESCRIBE DATABASES`` command:

.. code-block:: postgres

   DESCRIBE DATABASES

Parameters
============
The ``DESCRIBE DATABASES`` command has no parameters.

Examples
==============
The following is an example of the ``DESCRIBE DATABASES`` command:

.. code-block:: postgres

   DESCRIBE DATABASES
 
Output
=============
Using the ``DESCRIBE DATABASES`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``database_name``
     - Displays the name of the database.
     - Text
     - master
   * - ``created_on``
     - Displays the date and time when the database was created.
     - Date
     - 2022-04-27 19:04:53
     
Example
===========
The following is an example of the generated output:

.. code-block:: postgres

   master,2022-04-27 19:04:53

Permissions
=============
**Comment** - *What are the permissions?*