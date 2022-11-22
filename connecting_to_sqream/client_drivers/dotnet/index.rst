.. _net:

*************************
.NET
*************************
The SqreamNet ADO.NET Data Provider lets you connect to SQream through your .NET environment.

The .NET page includes the following sections:

.. contents:: 
   :local:
   :depth: 1

Integrating SQreamNet
==================================
The **Integrating SQreamNet** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Prerequisites
----------------
The SqreamNet provider requires a .NET version 6 or newer.

Integrating SQreamNet
-------------------------
To integrate SQreamNet, unzip the archive file and save to a known location. Next, in your IDE, add a Sqreamnet.dll reference to your project.
If you wish to upgrade SQreamNet within an existing project, you may replace the existing .dll file with an updated one or change the project's reference location to a new one.


Known Driver Limitations
----------------------------
 * Unicode characters are not supported when using ``INSERT INTO AS SELECT``.

 * To avoid possible casting issues, use ``getDouble`` when using ``FLOAT``.

Connecting to SQream For the First Time
==============================================
An initial connection to SQream must be established by creating a **SqreamConnection** object using a connection string.

.. contents:: 
   :local:
   :depth: 1
   

Connection String
--------------------
To connect to SQream, instantiate a **SqreamConnection** object using this connection string.

The following is the syntax for SQream:

.. code-block:: text

   "Data Source=<hostname or ip>,<port>;User=<username>;Password=<password>;Initial Catalog=<database name>;Integrated Security=true";

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - State
     - Default
     - Description
   * - ``<data source>``
     - Mandatory
     - None
     - Hostname/IP/FQDN and port of the SQream DB worker. For example, ``127.0.0.1:5000``, ``sqream.mynetwork.co:3108``
   * - ``<initial catalog>``
     - Mandatory
     - None
     - Database name to connect to. For example, ``master``
   * - ``<username>``
     - Mandatory
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``<password>``
     - Mandatory
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
   * - ``<service>``
     - Optional
     - ``sqream``
     - Specifices service queue to use. For example, ``service=etl``
   * - ``<ssl>``
     - Optional
     - ``false``
     - Specifies SSL for this connection. For example, ``ssl=true``
   * - ``<cluster>``
     - Optional
     - ``true``
     - Connect via load balancer (use only if exists, and check port).

Connection String Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following is an example of a SQream cluster with load balancer and no service queues (with SSL):

.. code-block:: text

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;Integrated Security=true;ssl=true;cluster=true;
    

The following is a minimal example for a local standalone SQream database:

.. code-block:: text 

  
   Data Source=127.0.0.1,5000;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;

The following is an example of a SQream cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: text

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=raviga;Integrated Security=true;service=etl;cluster=true;

Sample C# Program
--------------------
You can download the :download:`.NET Application Sample File <sample.cs>` below by right-clicking and saving it to your computer.

.. literalinclude:: sample.cs
    :language: C#
    :caption: .NET Application Sample
    :linenos:
