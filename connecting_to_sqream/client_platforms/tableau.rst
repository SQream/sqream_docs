.. _tableau:

*******
Tableau
*******

SQream's Tableau connector, based on standard JDBC, enables storing and fast querying large volumes of data. This connector is useful for users who want to integrate and analyze data from various sources within the Tableau platform. With the Tableau connector, users can easily connect to databases and cloud applications and perform high-speed queries on large datasets. Additionally, the connector allows for seamless integration with Tableau, enabling users to visualize their data.

SQream supports both Tableau Desktop and Tableau Server on Windows, MacOS, and Linux distributions.

For more information on SQream's integration with Tableau, see `Tableau Connectors <https://extensiongallery.tableau.com/connectors?version=2019.4>`_.

.. contents::
   :local:
   :depth: 1

Prerequisites
-------------

It is essential that you have the following installed:

* Tableau version 9.2 or newer 

Setting Up JDBC
----------------

#. Download the SQream JDBC Connector :ref:`.jar file <client_drivers>`.
#. Place the JDBC .jar file in the Tableau driver directory.

   Based on your operating system, you may find the Tableau driver directory in one of the following locations:
   
   * Tableau Desktop on MacOS: ``~/Library/Tableau/Drivers``
   * Tableau Desktop on Windows: ``C:\Program Files\Tableau\Drivers``
   * Tableau on Linux: ``/opt/tableau/tableau_driver/jdbc``

Installing the Tableau Connector
--------------------------------

#. Download the :ref:`Tableau Connector <client_drivers>` ``SQreamDB.taco`` file.
   
#. Based on the installation method that you used for installing Tableau, place the Tableau Connector ``SQreamDB.taco`` file in the Tableau connector directory:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Product / Platform
     - Path
   * - Tableau Desktop for Windows
     - ``C:\Users[user]\Documents\My Tableau Repository\Connectors``
   * - Tableau Desktop for Mac
     - ``/Users/[user]/Documents/My Tableau Repository/Connectors``
   * - Tableau Prep for Windows
     - ``C:\Users[user]\Documents\My Tableau Prep Repository\Connectors``
   * - Tableau Prep for Mac
     - ``/Users/[user]/Documents/My Tableau Prep Repository/Connectors``
   * - Flow web authoring on Tableau Server
     - ``/data/tabsvc/flowqueryservice/Connectors``
   * - Tableau Prep Conductor on Tableau Server
     - ``/data/tabsvc/flowprocessor/Connectors``
   * - Tableau Server
     - ``C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Connectors``

3. Restart Tableau Desktop or Tableau server.

Connecting to SQream
--------------------


#. Start Tableau Desktop.

    ::
	
#. In the **Connect** menu, under the **To a Server** option , click **More**.

   Additional connection options are displayed.

    ::
	
#. Select **SQream DB by SQream Technologies**.

   The connection dialog box is displayed.

    ::
	
#. In the connection dialog box, fill in the fields and click **Sign In**.

   The connection is established, and the data source page is displayed.

Information about step 4 fields:
   
  .. list-table:: 
     :widths: 15 38 38
     :header-rows: 1
   
     * - Field name
       - Description
       - Example
     * - Server
       - Defines the server of the SQream worker.
       - ``127.0.0.1`` or ``sqream.mynetwork.co``
     * - Port
       - Defines the TCP port of the SQream worker.
       - ``3108`` when using a load balancer, or ``5100`` when connecting directly to a worker with SSL.
     * - Database
       - Defines the database to establish a connection with.
       - ``master``
     * - Cluster
       - Enables (``true``) or disables (``false``) the load balancer. After enabling or disabling the load balance, verify the connection.
       - 
     * - Username
       - Specifies the username of a role to use when connecting.
       - ``rhendricks``	 
     * - Password
       - Specifies the password of the selected role.
       - ``Tr0ub4dor&3``
     * - Require SSL 
       - Sets SSL as a requirement for establishing this connection.
       - 



