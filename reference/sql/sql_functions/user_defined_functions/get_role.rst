.. _get_role:

GET_ROLE
-----------------------
The ``GET_ROLE`` user-defined function shows the following role-related information:

.. list-table::
   :widths: 15 50 45
   :header-rows: 1   
   
   * - Function
     - Description
     - Default
   * - ``select get_role_permissions``
     - Returns all permissions granted to a role in table form.
     - Yes/No **Comment** - *Verify.*
   * - ``select get_role_global_ddl``
     - Return the definition of a role in a DDL format. **Comment** - *Need description.*
     - Yes/No **Comment** - *Verify.*
   * - ``select get_role_database_ddl``
     - Return the definition of a role in a DDL format. **Comment** - *Need description.*
     - Yes/No **Comment** - *Verify.*

The following is an example output of the ``select get_role_permissions`` function:

.. code-block:: console
   
   $ 
	  
The following is an example output of the ``select get_role_global_ddl`` function:

.. code-block:: console
   
   $ 
	  
The following is an example output of the ``get_role_database_ddl`` function:

.. code-block:: console
   
   $ 
	  