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


Prerequisites
===================================

* Python 3.11 or higher (3.11 recommended)

* Access to a SQreamDB instance

* Claude Desktop application


Installation steps
===================================

#. Download Claude for Windows / Mac - `Claude download <https://claude.ai/download>`_. 


#. Download Sqream MCP server package - `download <http://artifactory.host-98.sq.l/artifactory/webapp/#/artifacts/browse/tree/General/mcp_server/releases>`_. 

**Note**:During this installation guide - <SQREAM_MCP_DIR> will represents location: <extracted package path>/sqreamdb_mcp_server_<VERSION>/sqreamdb-mcp-server

#. Server setup
There are 2 ways to setup Sqream MCP server - Automated and manual.  Each of those steps requires to configure Sqream worker connection details Claude will communicate with:

Connection Parameters:

  .. list-table:: 
     :widths: auto
     :header-rows: 1
   
     * - Parameter
       - Description
       - Example
     * - ``host``
       - SQreamDB server hostname or IP
       - ``192.168.4.68``
     * - ``port``
       - SQreamDB/Server_picker server port
       - ``5000`` 
     * - ``database``
       - Database name to connect to
       - ``master``
     * - ``username``
       - SQreamDB username
       - ``sqream``
     * - ``password``
       - SQreamDB password 
       - ``Sqream``
     * - ``clustered``
       - set to true if server picker is used
       - ``false``

**Note**:**clustered** is optional and should be used if server picker port is used as your port
   
Automated Setup:

Run the setup script with your SQreamDB connection parameters:

``python setup_sqreamdb_mcp.py host=<hostname> port=<port> database=<database> username=<username> password=<password>``



Example:

``python <SQREAM_MCP_DIR>/setup_sqreamdb_mcp.py host=1.2.3.4 port=5000 database=master username=sqream password=sqream``

.. list-table:: 
     :widths: auto
     :header-rows: 1
   
     * - Linux / Mac
       - Windows
     * - ::
            cd <SQREAM_MCP_DIR>
            python setup_sqreamdb_mcp.py host=<IP> port=<PORT> database=<DATABASE> username=<USER> password=<PASSWORD>
      - ::
            cd <SQREAM_MCP_DIR>
            py setup_sqreamdb_mcp.py host=<IP> port=<PORT> database=<DATABASE> username=<USER> password=<PASSWORD>

Example:

python <SQREAM_MCP_DIR>/setup_sqreamdb_mcp.py host=1.2.3.4 port=5000 database=master username=sqream password=sqream

The script will :

* Create a Python virtual environment

* Install all required dependencies

* Configure Claude Desktop to use the SQreamDB MCP server

* Set up the connection parameters



Notes
==========

* Denodo 9.1 and Denodo 8.0u20240926 already include an adapter for SQreamDB and its driver so they no longer have to download the driver. They do not have to fill in Database adapter, nor Driver class path, nor Driver class.

* With the SQreamDB adapter, the user does not have to restart.

* With the SQreamDB adapter, the Limitation mentioned above does not occur.