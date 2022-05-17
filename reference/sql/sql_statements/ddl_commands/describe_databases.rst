.. _describe_databases:

*****************
DESCRIBE DATABASES
*****************
The ``DESCRIBE DATABASES`` command lets you list information about the database in your cluster.

Syntax
==========
The following is the syntax for the ``DESCRIBE DATABASES`` command:

.. code-block:: postgres

   DESCRIBE DATABASES

Parameters
============
The ``DESCRIBE DATABASES`` command has no parameters.

Example
==============
The ``DESCRIBE_DATABASES`` command has no parameters.

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
     - 2022-04-12 15:10:38
   * - ``is_current``
     - Displays the database that you are currently connected to.
     - Boolean
     - 1
	     
The following is an example of the generated output in Studio:

.. image:: /_static/images/describe_databases.png

Permissions
=============
No permissions are required for the ``DESCRIBE DATABASES`` command.