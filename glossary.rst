.. glossary:

Glossary
=====================================

.. glossary::

   Cluster
      A SQream DB deployment containing several :term:`workers<Worker>` running on one or more :term:`nodes<Node>`.

   Node
      A machine running SQream DB :term:`workers<Worker>`.

   Worker
      A SQream DB application that can respond to statements. Several workers can run on one or more :term:`nodes<Node>` to form a cluster.

   Metadata
      SQream DB's internal storage which contains details about database objects.

   Authentication
      Authentication is the process that identifies a user or :term:`role<Role>` to verify an identity - to make sure the user is who they say they are. This is done with a username and password. 

   Authorization
      Authorization defines the set of actions that an authenticaed :term:`role` can perform after gaining access to the system, protecting from threats that :term:`authentication` controls alone are not enough against.
   
   Role
      A role is a group or a user, depending on the permissions granted. A role groups together a set of permissions.

   Catalog
      A set of views that contains information (metadata) about the objects in a database (e.g. tables, columns, chunks, etc...).
   
   Storage cluster
      The storage cluster is the directory in which SQream DB stores data, including database objects, metadata database, and logs.
   
   UDF
   User-defined function
      A feature that extends SQream DB's built in SQL functionality with user-written Python code.
   
   