.. _loading_data_using_sqload:

***********************
Loading Data to SQream Using Sqload
***********************
This page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
==============================
**SQload** is a tool designed to transfer data between SQream and relational databases. You can use SQload to import data from a relational database management system (RDBMS) such as MSSQL, Oracle, or Teradata into the SQream.

Prerequisites
==============================
The following are the prerequisites:

* Linux or CentOS operating system.

   ::

* Java SDK 1.8.x version.

   ::

* All necessary ports open on the firewall.

Installing SQload
==============================
This section describes how to install SQload.

**To install SQload:**

1. Download the most current Sqload installer sqload-<version>.tar.gz from `Client Drivers <https://docs.sqream.com/en/latest/connecting_to_sqream/client_drivers/index.html>`_.
    
    ::

2. Extract the package into the folder you want to locate, such as **/usr/local/sqload-<version>**.

    ::

3. Run the following command:

   .. code-block:: console

      tar -xvf sqload-<version>.tar.gz

Configuring SQload
==============================
When configuring SQload, you only have the option of using the **sqload.config** file, which contains the connection details for SQream and source databases.

**To configure SQload:**

1. Modify the option **sqload.config** file:

   * **For Oracle:** #Source database properties:

   .. code-block:: console

      source.db.type=oracle

      source.db.name=orcl

      source.db.user=ferdio

      source.db.password=*****

      source.db.url=192.168.1.105

      source.db.port=1521

  * **For SQream**: #Target database properties:

  .. code-block:: console

     target.db.type=sqream

     target.db.name=tidemodb

     target.db.user=sqream

     target.db.password=*****

     target.db.url=192.168.0.102

     target.db.port=3108

     target.db.cluster=true

2. Check the connectivity:

   .. code-block:: console

      "sqload --test"

   This command checks the connectivity for both the source and SQream database.


Operating SQload
==============================
You can operate SQload by running the following command:

.. code-block:: console

   $ SQload -help

     usage: SQload [ARGS]

The following table describes the available commands:

+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| Commands                          | Description                                                                          | Default               |
+===================================+======================================================================================+=======================+
| -drop <true/false>                | Drops and recreates the target table before performing the load operation.           | FALSE                 |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -fetchsize <fetch size>           | Displays the number of entries to read from the database at once.                    | 1000                  |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -filter <select criteria>         | Displays the custom filter for the SQL ``SELECT`` statement, such as ``year=2022``.  | 1=1                   |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -h,--help                         | Displays the Help menu.                                                              | NA                    |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -limit <Number of rows>           | Displays several limited rows.                                                       | 0                     |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -splitby <Column Name>            | Displays the column name for split. This is required for multi-thread loads.         | NA                    |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -table <schema.table_name>        | Displays the source table name.                                                      | NA                    |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -tabletarget <schema.table_name>  | Displays the target table name.                                                      | Same as source table  |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -thread <number of threads>       | Displays the number of parallel worker threads.                                      | 1                     |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| -truncate <true/false>            | Truncates the target table.                                                          | FALSE                 |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| --columnlist  <file-name>         | Displays the file containing column names to be loaded.                              | NA - not implemented  |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+
| --ignorecolumns                   | Displays the columns to be ignored during the load operation.                        | NA                    |
+-----------------------------------+--------------------------------------------------------------------------------------+-----------------------+

See 'SQload --help' for information on a specific command.

The following is an example of a command:

.. code-block:: console

   $ sqload --table SMSDW.LINEITEM --fetch-size 100000 -drop true
