.. _mcp:

***************
MCP | Integrating SQream DB and Anthropic Claude
***************

The MCP server will establish a robust framework for integrating third-party services and AI models directly with the SQream database.

Features
================

* **Direct SQL Execution**: Run queries against SQreamDB from Claude

* **Documentation Access**: Built-in access to SQreamDB syntax and functions

* **Query Optimization**: Get help with performance tuning

* **Schema Exploration**: Browse tables, columns, and database structure

* **Data Type Support**: Full support for SQreamDB data types and functions


Setting Up a Connection to SQreamDB
===================================

#. In the Design Studio, click the menu File > New > Data Source > JDBC and select SqreamDB.

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
     * - Database URI
       - The URI that specifies the location and details of the database or data source to be connected
       - ``jdbc:Sqream://<host_and_port>/<database_name>;[<optional_parameters>; ...]`` 
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

Notes
==========

* Denodo 9.1 and Denodo 8.0u20240926 already include an adapter for SQreamDB and its driver so they no longer have to download the driver. They do not have to fill in Database adapter, nor Driver class path, nor Driver class.

* With the SQreamDB adapter, the user does not have to restart.

* With the SQreamDB adapter, the Limitation mentioned above does not occur.