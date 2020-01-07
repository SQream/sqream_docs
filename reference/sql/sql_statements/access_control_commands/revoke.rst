.. _revoke:

*****************
REVOKE
*****************

The ``REVOKE`` statement removes permissions from a role. It allows for removing permissions to specific objects.

See also :ref:`grant`, :ref:`drop_role`.

Permissions
=============

To revoke permissions, the current role must have the ``SUPERUSER`` permission, or have the ``ADMIN OPTION``.

Syntax
==========

.. code-block:: postgres

   grant_statement ::=
      { 
      -- revoke permissions at the cluster level:
      REVOKE 
         { SUPERUSER
         | LOGIN 
         | PASSWORD 'password' 
         } 
         FROM role_name [, ...] 
      
      -- Revoke permissions at the database level:
      | REVOKE
         {
            { CREATE
            | CONNECT
            | DDL
            | SUPERUSER
            | CREATE FUNCTION
            } [, ...] 
         | ALL [PERMISSIONS]
         }  
         ON DATABASE database_name [, ...]
         FROM role_name [, ...] 
      
      -- Revoke permissions at the schema level: 
      | REVOKE 
         {
            { CREATE 
            | DDL 
            | USAGE 
            | SUPERUSER 
            } [, ...]
         | ALL [PERMISSIONS ]
         } 
         ON SCHEMA schema_name [, ...] 
         FROM role_name [, ...]
      
      -- Revoke permissions at the object level: 
      | REVOKE 
         {
            { SELECT 
            | INSERT 
            | DELETE 
            | DDL 
            } [, ...]
         | ALL [PERMISSIONS]
         }
         ON { TABLE table_name [, ...] | ALL TABLES IN SCHEMA schema_name [, ...]} 
         FROM role_name [, ...]
      
                  
      -- Revoke execute function permission: 
      | REVOKE 
         { ALL 
         | EXECUTE 
         | DDL
         } 
         ON FUNCTION function_name 
         FROM role_name [, ...]
       
                  
      -- Remove permissions between roles by revoking role membership: 
      | REVOKE role_name [, ...] 
         FROM role_name_2
         [ WITH ADMIN OPTION ]

      ;

   role_name ::= identifier  
   
   role_name2 ::= identifier  
   
   database_name ::= identifier
   
   table_name ::= identifier
   
   schema_name ::= identifier

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``role_name``
     - The name of the role to revoke permissions from
   * - ``table_name``, ``database_name``, ``schema_name``, ``function_name``
     - Object to revoke permissions on.
   * - ``WITH ADMIN OPTION``
     - 
         If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.
         
         Specifying ``WITH ADMIN OPTION`` for revocation will return the role to an ordinary role. An ordinary role cannot grant or revoke membership.
         
         

.. include:: grant.rst
   :start-line: 123
   :end-line: 174


Examples
===========

Prevent a role from modifying table contents
----------------------------------------------

If you don't trust user ``shifty``, reokve DDL and INSERT permissions.

.. code-block:: postgres

   REVOKE INSERT ON TABLE important_table FROM shifty;
   REVOKE DDL ON TABLE important_table FROM shifty;

Demoting a user from superuser
-------------------------------------

.. code-block:: postgres
   
   -- On the entire cluster
   REVOKE SUPERUSER FROM new_role;

Revoking admin option
------------------------------

If ``WITH ADMIN OPTION`` is specified, the role that has the admin option can in turn grant membership in the role to others, and revoke membership in the role as well.


.. code-block:: postgres
   
   -- dba_user1 has been demoted from team lead, so he should not be able to grant
   -- permissions to other users.
   
   REVOKE r_database_architect FROM dba_user1 WITH ADMIN OPTION;

