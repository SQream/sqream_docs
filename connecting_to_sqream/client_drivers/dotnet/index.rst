.. _net:

*************************
.NET
*************************
The SqreamNet ADO.NET Data Provider allows you to connect to a SQream database server through .NET environments. This page describes how to establish such connection.

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
The SqreamNet provider requires a .NET Framework 6 or newer.

Verifying the Correct .NET Framework Version is Installed 
---------------------
To verify the correct version of .NET Framework is installed, go to your Framework directory, under Microsoft.NET and look for a v6.x.x directory. In case an older version of .NET Framework exists, you may follow Microsoft guidelines: ____

Integrating SQreamNet
-------------------------
To integrate SQreamNet, unzip the archive file and save to a known location. Next, in your Visual Studio, add a reference to the Sqreamnet.dll file to your project.
If you wish to upgrade SQreamNet within an existing project, you may replace the .dll file with an updated one or add a reference to the updated .dll file within its new location.

Using SQreamNet in your Visual Studio project
----------------------------


Connecting to SQream For the First Time
==============================================
An initial connection to SQream must be established by creating a **SqreamConnection** object by using a connection string.

.. contents:: 
   :local:
   :depth: 1
   
Connection string
--------------
Use ``com.sqream.jdbc.SQDriver`` as the driver class in the JDBC application.

Connection String
--------------------
SQreamNet Data Provider relies on a connection string.

The following is the syntax for SQream:

.. code-block:: text

   "Data Source=<hostname or ip>,<port>;User=<username>;Password=<password>;Initial \ Catalog=master;Integrated Security=true";

Connection Parameters
^^^^^^^^^^^^^^^^^^^^^^^^
The following table shows the connection string parameters:

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
   * - ``username=<username>``
     - Mandatory
     - None
     - Username of a role to use for connection. For example, ``username=rhendricks``
   * - ``password=<password>``
     - Mandatory
     - None
     - Specifies the password of the selected role. For example, ``password=Tr0ub4dor&3``
   * - ``service=<service>``
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

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial \ Catalog=master;Integrated Security=true;ssl=true;cluster=true;


The following is a minimal example for a local standalone SQream database:

.. code-block:: text 

  
   Data Source=127.0.0.1,5000;User=rhendricks;Password=Tr0ub4dor&3;Initial \ Catalog=master;

The following is an example of a SQream cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: text

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial \ Catalog=raviga;Integrated Security=true;service=etl;cluster=true;

Sample C# Program
--------------------
You can download the :download:`JDBC Application Sample File <sample.java>` below by right-clicking and saving it to your computer.

.. literalinclude:: sample.java
    :language: java
    :caption: JDBC Application Sample
    :linenos:
