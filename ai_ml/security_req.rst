.. _security_requirements:

Security Requirements
---------------------

This section outlines the necessary user privileges for creating and managing Python modules within AISQream, ensuring controlled access and security for custom code execution.

* Python module creation is allowed to SUPERUSERs only.
* SUPERUSERs can grant EXECUTE permission to other non-SUPERUSERs: ``GRANT EXECUTE ON MODULE module_name TO role;``