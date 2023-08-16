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

   DESCRIBE USER FUNCTIONS [DATABASE <database_name>] [LIKE 'pattern']
   DESC USER FUNCTIONS [DATABASE <database_name>] [LIKE 'pattern']

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
     - ``pattern``
     - The ``LIKE`` operator is used to perform pattern matching within strings
   * - ``%``
     -
     - The ``%`` wildcard is used in conjunction with the ``LIKE`` operator to match any sequence of characters (including none) within a string
  
	 
Example
=======

The following is an example of the ``DESCRIBE USER FUNCTIONS`` command:

.. code-block:: postgres

   DESCRIBE USER FUNCTIONS DATABASE master;
	 
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
     - Text
     - master
   * - ``function_id``
     - Displays the ID of the function.
     - Integer
     - 0	 
   * - ``function_name``
     - Displays the name of the function.
     - Text
     - add_months
   * - ``function_body``
     - Displays the syntax of the function.
     - Text
     - select dateadd(month,n,dt);

The following is an example of the generated output:

.. code-block:: postgres

   master,0,november,november,4,1980
   
Permissions
===========

Using the ``DESCRIBE USER FUNCTINS`` command requires ``USAGE`` permissions.