.. _describe_user_functions:

***********************
DESCRIBE USER FUNCTIONS
***********************

The ``DESCRIBE USER FUNCTIONS`` command lets you list all user-defined functions in your database.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE USER FUNCTIONS`` command:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS [DATABASE <database_name>] [LIKE 'function_name']
   DESC USER FUNCTIONS [DATABASE <database_name>] [LIKE 'function_name']

Parameters
==========

The following parameters can be used with the ``DESCRIBE USER FUNCTIONS`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``DATABASE``
     - ``database_name``
     - The name of the database containing user-defined functions
   * - ``LIKE``
     - ``function_name``
     - The ``LIKE`` operator is used to perform pattern matching within strings. It supports the ``%`` wild card, which is used to match any sequence of characters (including none) within a string.
  
Output
======

Using the ``DESCRIBE USER FUNCTIONS`` command generates the following output:

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
   * - ``function_id``
     - Displays the ID of the function.
     - INTEGER
     - 0	 
   * - ``function_name``
     - Displays the name of the function.
     - TEXT
     - add_months
   * - ``function_body``
     - Displays the syntax of the function.
     - TEXT
     - select dateadd(month,n,dt);

	 
Examples
========

.. code-block:: sql

	DESCRIBE USER FUNCTIONS DATABASE master;
	
.. code-block:: none
	
	database_name|function_id|function_name|function_body                                                                                                                                                    |
	-------------+-----------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
	master       |0          |str_to_date  |select cast((substring(f,1,4) || '-' || substring(f,5,2) || '-' || substring(f,7,2)) as date);                                                                   |
	master       |1          |least_sq     |select case          when a <= b then a          when b < a then b          when a is null then b          when b is null then a          else null        end;  |
	master       |2          |add_months   |select dateadd(month,n,dt);                                                                                                                                      |

.. code-block:: sql	
		
		DESCRIBE USER FUNCTIONS DATABASE master like '%date%';
	   
.. code-block:: none

		database_name|function_id|function_name|function_body                                                                                   |
		-------------+-----------+-------------+------------------------------------------------------------------------------------------------+
		master       |0          |str_to_date  |select cast((substring(f,1,4) || '-' || substring(f,5,2) || '-' || substring(f,7,2)) as date);  |
   
Permissions
===========

This command requires ``USAGE`` permission on the schema level.
