.. _current_method_command_examples:

**************************
Command Examples
**************************
This section includes the following command examples:

.. contents:: 
   :local:
   :depth: 1
   
Running a Regular Flag Type Command
---------------------
The following is an example of running a **Regular** flag type command:

.. code-block:: console
   
   SET spoolMemoryGB= 11;
   executed
   
Running a Worker Flag Type Command
---------------------
The following is an example of running a **Worker** flag type command:

.. code-block:: console
   
   SHOW spoolMemoryGB;

Running a Cluster Flag Type Command
---------------------
The following is an example of running a **Cluster** flag type command:

.. code-block:: console
   
   ALTER SYSTEM RESET useMetadataServer;
   executed
   

SQream uses the **sqream_catalog.parameters** catalog table for showing all flags, providing the scope (default, cluster and session), description, default value and actual value.

The following is the correct syntax for a catalog table query:

.. code-block:: console
   
   SELECT * FROM sqream_catalog.settings

The following is an example of a catalog table query:

.. code-block:: console
   
   externalTableBlobEstimate, 100, 100, default,
   varcharEncoding, ascii, ascii, default, Changes the expected encoding for Varchar columns
   useCrcForTextJoinKeys, true, true, default,
   hiveStyleImplicitStringCasts, false, false, default,