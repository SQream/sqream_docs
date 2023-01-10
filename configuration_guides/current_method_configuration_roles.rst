.. _current_method_configuration_roles:

**************************
Configuration Roles
**************************
SQream divides flags into the following roles, each with their own set of permissions:

* :ref:`admin_flags` - can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command:
   
   * Regular
   * Worker
   * Cluster
   
* :ref:`generic_flags` - can be modified by standard users on a session basis:

   * Regular
   * Worker