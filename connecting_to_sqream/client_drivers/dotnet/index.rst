.. _net:

**********
SQreamNET
**********

The SQreamNET ADO.NET Data Provider lets you connect to SQream through your .NET environment.

.. contents:: 
   :local:
   :depth: 1

Before You Begin
=================

* The SQreamNET provider requires a .NET version 6 or newer

* Download the SQreamNET driver from the :ref:`client drivers page<client_drivers>`

Integrating SQreamNET
======================

#. After downloading the .NET driver, save the archived file to a known location. 
#. In your IDE, add a SQreamNET.dll reference to your project.
#. If you wish to upgrade SQreamNET within an existing project, replace your existing .dll file with an updated one or change the project's reference location to a new one.

Connecting to SQream For the First Time
========================================

An initial connection to SQream must be established by creating a **SqreamConnection** object using a connection string.

Connection String Syntax
-------------------------

.. code-block:: console

   Data Source=<hostname or ip>,<port>;User=<username>;Password=<password>;Initial Catalog=<database name>;Integrated Security=true;

Connection Parameters
-----------------------

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
---------------------------

The following is an example of a SQream cluster with load balancer and no service queues (with SSL):

.. code-block:: console

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;Integrated Security=true;ssl=true;cluster=true;
    

The following is a minimal example for a local standalone SQream database:

.. code-block:: console 

  
   Data Source=127.0.0.1,5000;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=master;

The following is an example of a SQream cluster with load balancer and a specific service queue named ``etl``, to the database named ``raviga``

.. code-block:: console

   Data Source=sqream.mynetwork.co,3108;User=rhendricks;Password=Tr0ub4dor&3;Initial Catalog=raviga;Integrated Security=true;service=etl;cluster=true;

Sample C# Program
-----------------

You can download the :download:`.NET Application Sample File <sample.cs>` below by right-clicking and saving it to your computer.

.. literalinclude:: sample.cs
    :language: C#
    :caption: .NET Application Sample
    :linenos:

Limitations
===============

* Unicode characters are not supported when using ``INSERT INTO AS SELECT``

* To avoid possible casting issues, use ``getDouble`` when using ``FLOAT``

* The ``ARRAY`` data types is not supported. If your database schema includes ``ARRAY`` columns, you may encounter compatibility issues when using SQreamNET to connect to the database.