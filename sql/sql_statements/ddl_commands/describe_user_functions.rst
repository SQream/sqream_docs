.. _describe_user_functions:

***********************
DESCRIBE USER FUNCTIONS
***********************

The ``DESCRIBE USER FUNCTIONS`` command lets you list all user-defined functions in your database.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] USER FUNCTIONS [DATABASE <database_name>] [LIKE 'pattern']

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Parameter Value
     - Description
   * - ``DATABASE``
     - :ref:`Identifier<keywords_and_identifiers>` 
     - The name of the database containing user-defined functions
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
   * - ``function_id``
     - ``INTEGER`` 
     - Displays the ID of the function
   * - ``function_name``
     - ``TEXT``
     - Displays the name of the function
   * - ``function_body``
     - ``TEXT``
     - Displays the syntax of the function

	 
Examples
========

.. code-block:: sql

	DESCRIBE USER FUNCTIONS DATABASE master;	
	
	database_name|function_id|function_name|function_body                                                                                                |
	-------------+-----------+-------------+-------------------------------------------------------------------------------------------------------------+
	master       |0          |str_to_date  |SELECT CAST((substring(f,1,4) || '-' || substring(f,5,2) || '-' || substring(f,7,2)) AS date);               |
	master       |1          |least_sq     |SELECT CASE WHEN a <= b THEN a WHEN b < a THEN b WHEN a IS NULL THEN b WHEN b IS NULL THEN a ELSE NULL END;  |
	master       |2          |add_months   |SELECT dateadd(month,n,dt);                                                                                  |

.. code-block:: sql	
		
	DESCRIBE USER FUNCTIONS DATABASE master like '%date%';

	database_name|function_id|function_name|function_body                                                                                   |
	-------------+-----------+-------------+------------------------------------------------------------------------------------------------+
	master       |0          |str_to_date  |SELECT CAST((substring(f,1,4) || '-' || substring(f,5,2) || '-' || substring(f,7,2)) AS date);  |
   
Permissions
===========

This command requires ``USAGE`` permission on the schema level.
