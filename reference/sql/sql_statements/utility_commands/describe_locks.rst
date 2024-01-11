.. _describe_locks:

**************
DESCRIBE LOCKS
**************

Returns a list of locks from across your cluster.

.. note:: ``DESCRIBE`` commands use CPU to increase usability.

Syntax
======

The following is the syntax for the ``DESCRIBE LOCKS`` command:

.. code-block:: postgres

   DESCRIBE LOCKS
   DESC LOCKS
   
Parameters
==========

``DESCRIBE LOCKS`` command has no input parameters.
 
    
Output
======

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Column
     - Type
     - Comments
   * - ``statement_id``
     - ``TEXT``
     - Displays the statement ID that caused the lock 
   * - ``username``
     - ``TEXT``
     - Displays the the user that executed the statement
   * - ``server``
     - ``TEXT``
     - Displays the the server name 
   * - ``port``
     - ``TEXT``
     - Displays the the port number  
   * - ``locked_object``
     - ``TEXT``
     - Displays the the full qualified name of the object being locked, separated with ``$``, e.g. ``table$t$public$nba2`` for table nba2 in schema public, in database t
   * - ``lockmode``
     - ``TEXT``
     - Displays the the locking mode (inclusive or exclusive) 
   * - ``statement_start_time``
     - ``DATETIME``
     - Displays the timestamp the statement started 
   * - ``lock_start_time``
     - ``DATETIME``
     - Displays the timestamp the lock was obtained
   * - ``statement_string``
     - ``TEXT``
     - The SQL syntax that triggered this lock

Permissions
===========

This command requires a ``SUPERUSER`` permission.
