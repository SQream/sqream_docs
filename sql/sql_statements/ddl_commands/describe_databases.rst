:orphan:

.. _describe_databases:

******************
DESCRIBE DATABASES
******************

The ``DESCRIBE DATABASES`` command lets you list information about the databases in your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] DATABASES [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Type
     - Description
   * - ``LIKE``
     - :ref:`STRING literal<literals>`	
     - String pattern to match

Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``database_name``
     - ``TEXT``
     - Displays the name of the database
   * - ``created_on``
     - ``DATE``
     - Displays the date and time when the database was created
   * - ``is_current``
     - ``BOOLEAN``
     - Displays the database that you are currently connected to
	     
Examples
========

.. code-block:: sql   
	   
	DESCRIBE DATABASES;

	database_name|created_on         |is_current|
	-------------+-------------------+----------+
	master       |2023-06-29 19:48:43|true      |
	student      |2023-08-16 08:57:56|false     |
	teacher      |2023-08-16 08:58:25|false     |
	teacher1     |2023-08-16 08:58:45|false     |
	teacher2     |2023-08-16 08:58:52|false     |
	
.. code-block:: sql   
	   
	DESCRIBE DATABASES LIKE '%teacher%';
	
	database_name|created_on         |is_current|
	-------------+-------------------+----------+
	teacher      |2023-08-16 08:58:25|false     |
	teacher1     |2023-08-16 08:58:45|false     |
	teacher2     |2023-08-16 08:58:52|false     |

Permissions
===========

This command requires ``CONNECT`` permission on the database level.
