.. _denodo:

***************
Denodo Platform
***************

Denodo Platform is a data virtualization solution that enables integration, access, and real-time data delivery from disparate on-premises and cloud-based sources.

Prerequisites
=============

It is essential that you have the following installed:

* Denodo 8.0

Setting Up a Connection to SQreamDB
===================================

#. Under ``Denodo\DenodoPlatform8.0\lib\extensions\jdbc-drivers``, create a directory named ``sqream``.

#. Download the SQreamDB JDBC Connector :ref:`.jar file <client_drivers>` and save it under the newly created ``sqream`` directory.

#. In the Denodo Platform menu, go to **File** > **New** > **Data Source** > **JDBC**.

   A connection dialog box is displayed.

#. Under the **Configuration** tab, select the **Connection** tab and fill in the data source information:

  .. list-table:: 
     :widths: auto
     :header-rows: 1
   
     * - Field name
       - Description
       - Value
       - Example
     * - Name
       - The name of the data source
       - ``sqream``
       -
     * - Database adapter
       - The database adapter allows Denodo Platform to communicate and interact with SQreamDB 
       - ``Generic``
       -
     * - Driver class path
       - The path to the location of the JDBC driver required for the connection to the data source
       - 
       - ``path/to/jdbcdriver/sqream-jdbc-x.x.x``
     * - Driver class
       - The class name of the JDBC driver used to connect to the data source
       - ``com.sqream.jdbc.SQDriver``
       -
     * - Database URI
       - The URI that specifies the location and details of the database or data source to be connected
       - ``jdbc:Sream://192.168.4.93:3108/master;cluster=true`` 
       -
     * - Transaction isolation
       - The level of isolation used to manage concurrent transactions in the database connection, ensuring data consistency and integrity
       - ``Database default``
       -
     * - Authentication
       - Authentication method
       - ``Use login and password``
       -
     * - Login
       - The SQreamDB role 
       - 
       - ``SqreamRole``
     * - Password
       - The SQreamDB role password
       - 
       - ``SqreamRolePassword2023``
	   
5. To verify your newly created connection, select the **Test connection** button.

