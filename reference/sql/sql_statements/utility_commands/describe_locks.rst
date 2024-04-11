.. _describe_locks:

**************
DESCRIBE LOCKS
**************

Returns a list of locks from across your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

.. code-block:: sql

   DESC[RIBE] LOCKS
    
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Data Type
     - Description
   * - ``statement_id``
     - Displays the statement ID that caused the lock 
     - ``TEXT``
   * - ``username``
     - Displays the the user that executed the statement
     - ``TEXT``
   * - ``server``
     - Displays the the server name 
     - ``TEXT``
   * - ``port``
     - Displays the the port number  
     - ``TEXT``
   * - ``locked_object``
     - Displays the the full qualified name of the object being locked, separated with ``$``
     - ``TEXT``
   * - ``lockmode``
     - Displays the the locking mode (``Inclusive`` or ``Exclusive``) 
     - ``TEXT``
   * - ``statement_start_time``
     - Displays the timestamp the statement started 
     - ``DATETIME``
   * - ``lock_start_time``
     - Displays the timestamp the lock was obtained
     - ``DATETIME``
   * - ``statement_string``
     - The SQL syntax that triggered this lock
     - ``TEXT``

Example
=======

.. code-block:: postgres

	DESCRIBE LOCKS;

Output:

.. code-block:: none

	statement_id|username|server      |port|locked_object|lock_mode|statement_start_time|lock_start_time     |statement_string                                                                               |
	------------+--------+------------+----+-------------+---------+--------------------+--------------------+-----------------------------------------------------------------------------------------------+
	287         |sqream  |192.168.1.91|5000|database$t   |Inclusive| 2019-12-26 00:03:30| 2019-12-26 00:03:30|CREATE OR REPLACE TABLE nba2 AS SELECT "Name" FROM nba WHERE REGEXP_COUNT("Name", '( )+', 8)>1;|



Permissions
===========

This command requires a ``SUPERUSER`` permission.
