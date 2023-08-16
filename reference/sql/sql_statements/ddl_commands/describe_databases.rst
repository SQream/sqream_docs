.. _describe_databases:

******************
DESCRIBE DATABASES
******************

The ``DESCRIBE DATABASES`` command lets you list information about the databases in your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE DATABASES`` command:

.. code-block:: postgres

   DESCRIBE DATABASES [LIKE 'pattern']
   DESC DATABASES [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``LIKE``
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings.
   * - ``%``
     -
     - The ``%`` wildcard is used in conjunction with the ``LIKE`` operator to match any sequence of characters (including none) within a string.

Output
======

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
     - TEXT
     - master
   * - ``created_on``
     - Displays the date and time when the database was created.
     - DATE
     - 2022-04-12 15:10:38
   * - ``is_current``
     - Displays the database that you are currently connected to.
     - BOOLEAN
     - 1
	     
Examples
========

.. code-block:: sql   
	   
	DESCRIBE DATABASES;

Output:

.. code-block:: none

	database_name|created_on         |is_current|
	-------------+-------------------+----------+
	master       |2023-06-29 19:48:43|true      |
	student      |2023-08-16 08:57:56|false     |
	teacher      |2023-08-16 08:58:25|false     |
	teacher1     |2023-08-16 08:58:45|false     |
	teacher2     |2023-08-16 08:58:52|false     |
	
.. code-block:: sql   
	   
	DESCRIBE DATABASES LIKE '%teacher%';
	
.. code-block:: none
	
	database_name|created_on         |is_current|
	-------------+-------------------+----------+
	teacher      |2023-08-16 08:58:25|false     |
	teacher1     |2023-08-16 08:58:45|false     |
	teacher2     |2023-08-16 08:58:52|false     |

Permissions
===========

Using the ``DESCRIBE DATABASES`` command requires ``SUPERUSER`` permissions.
