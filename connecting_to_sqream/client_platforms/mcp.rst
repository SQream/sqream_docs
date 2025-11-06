.. _mcp:

***************
MCP | Integrating SQream DB and Anthropic Claude
***************

Model Context Protocol (MCP), is an open standard introduced by Anthropic in November 2024. It standardizes how AI systems (like LLMs and agents) interact with external tools and data sources.
This intrface allows you to query your data using natural language, using Claude as LLM.
The installation is done on the client machine.

Features
================

* **Direct SQL Execution**: Run queries against SQreamDB from Claude

* **Documentation Access**: Built-in access to SQreamDB syntax and functions

* **Query Optimization**: Get help with performance tuning

* **Schema Exploration**: Browse tables, columns, and database structure

* **Data Type Support**: Full support for SQreamDB data types and functions


Prerequisites - client side
===================================

* Python 3.11.X or 3.12.X installed

* Access to a SQreamDB instance

* Claude Desktop application installed


Client installation steps
===================================

#. Download Claude for Windows / Mac - `Claude download <https://claude.ai/download>`_. 

#. Download Sqream MCP server package - `download <https://sq-ftp-public.s3.us-east-1.amazonaws.com/sqreamdb-mcp-server-release/sqreamdb-mcp-server-v1.0.2.zip>`_. 

#. Unzip the sqreamdb-mcp-server-v1.0.2.zip package.

   .. note::
      During this installation guide:

      - <EXTRACTED_PACKAGE_PATH> will represent where the ZIP will be extracted to  
      - <SQREAM_MCP_DIR> will represent location:  
        <EXTRACTED_PACKAGE_PATH>\sqreamdb_mcp_server_<VERSION>\sqreamdb-mcp-server

   Run in command line:

   .. code-block:: console

      python -m zipfile -e "C:\Users\<USER>\Downloads\sqreamdb_mcp_server_<version>.zip" "<EXTRACTED_PACKAGE_PATH>"

#. MCP-server setup

   There are two ways to setup Sqream MCP server - automated and manual.
   
   Each of those steps requires to configure Sqream worker connection details Claude will communicate with connection Parameters:

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

   
.. note:: **clustered** is optional and should be used if server picker port is used as your port

**Automated Setup**:

Go to your SQREAM_MCP_DIR directory on your Windows/Mac machine and run the setup script with your SQreamDB connection parameters:

``python setup_sqreamdb_mcp.py host=<hostname> port=<port> database=<database> username=<username> password=<password>``

Example:

``python setup_sqreamdb_mcp.py host=1.2.3.4 port=5000 database=master username=sqream password=sqream``


The script will:

* Create a Python virtual environment

* Install all required dependencies

* Configure Claude Desktop to use the SQreamDB MCP server

* Set up the connection parameters



**In case you could not use the anutomated setup**, perform the following manual setup procedure:

#. Create virtual environment:

   .. code-block:: console

      cd "<SQREAM_MCP_DIR>"
      python -m venv sqreamdb_mcp_env
      sqreamdb_mcp_env\Scripts\activate

#. Install dependencies:

   .. code-block:: console

      pip install -r requirements.txt

#. Configure Claude Desktop:

   Add the MCP server configuration to your Claude Desktop settings:

   a. Find Python.exe location:
      ``where python``

   b. Find sqreamdb_mcp_server location (should be at <SQREAM_MCP_DIR>/sqreamdb_mcp_server.py)

   c. Change Claude config file from this similar path:

   ``C:\\Users\\<USER>\\AppData\\Roaming\\Claude\\claude_desktop_config.json``

   to:

   .. code-block:: console

      {
        "mcpServers": {
          "sqreamdb": {
            "command": "<PYTHON_LOCATION>",
            "args": [
              "<SQREAM_MCP_DIR>\\sqreamdb_mcp_server.py",
              "host=<IP> port=<PORT> database=<DATABASE> username=<USER> password=<PASSWORD>"
            ]
          }
        }
      }

   .. note:: Path shall be with escaping characters. Example:

      .. code-block:: console

         C:\\Users\\sqream\\Desktop\\sqream1\\sqreamdb_mcp_server_1.0.0_20251020\\
         sqreamdb_mcp_server_1.0.0\\sqreamdb_mcp_server.py

#. Save configuration file.


Usage
===================================

#. **Restart Claude Desktop** after setup completion.


#. **Start using SQreamDB queries** directly in Claude conversations


#. Claude can:

* Execute SQL queries against your SQreamDB

* Access SQreamDB documentation and syntax

* Help with database operations and optimization



Troubleshooting
===================

Common Issues:

#. **Python Version**: Ensure you're using Python 3.11 or higher


#. **Connection Issues**: Verify your SQreamDB server is accessible and credentials are correct


#. **Claude Desktop**: Make sure to restart Claude Desktop after setup


Verification:

#. Open Claude Desktop


#. Ask Claude: "Can you connect to SQreamDB?"


#. Claude should be able to access SQreamDB documentation and execute queries