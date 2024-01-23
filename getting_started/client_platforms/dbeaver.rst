.. _dbeaver:

*******
DBeaver
*******

This page provides the necessary information for establishing a connection to BLUE from DBeaver.

Before You Begin
================

* The BLUE JDBC driver requires Java 1.8 or newer
* Download the BLUE JDBC driver `here <http://nexus.sq.l:18081/repository/maven-releases/com/sqream/sqream-jdbc/0.1.65/sqream-jdbc-0.1.65.jar>`_

Connection String 
=================

This section provides the database server location, authentication details, and other connection string parameters and values.

URL Template
------------

.. code-block:: java

	jdbc:Sqream://{host}:{port}/{database};accessToken={xxxxxxx}

Connection Parameters
---------------------
   
.. list-table:: 
   :widths: 3 10 4
   :header-rows: 1
   
   * - Parameter
     - Description
     - Example
   * - ``host``
     - Your BLUE host name 
     - ``sqream.isqream.com``
   * - ``port``
     - Your BLUE port number
     - ``443``
   * - ``database``
     - The BLUE database you wish to establish a connection to 
     - ``master``
   * - ``accessToken``
     - A BLUE access token
     - ``RFlFblB2WVpIQmVBalpNRE9JU2dTUFN4MHZvcFZwb1Z5Q21YaD``
	 
Establishing a Connection
=========================

1. Open your DBeaver application.

2. Under **Database**, select **New Database Connection**.

   The **Connect to a database** window opens.
   
3. Select **All**, search for **SQreamDB**, and select **Next**.

4. In the **Main** tab, select **Driver Settings**.

   The **Edit Driver 'SQreamDB'** window opens.

5. Go to the **Libraries** tab and select **Add File**.

6. Navigate to the location of your BLUE JDBC driver, select it and select **Open**.

7. Click on the file path you had added and select **Find Class**.

8. In the **Driver class** box, select ``jdbc.BlueDriver`` and select **OK**.
 
9. Under the **Main** tab, set **Connected by** to **URL** and enter your connection string parameters and values. 

   Example:

   .. code-block:: java

		jdbc:Sqream://sqream.isqream.com:443/master;accessToken=RFlFblB2WVpIQmVBalpNRE9JU2dTUFN4MHZvcFZwb1Z5Q21YaD
	
10. Select **Finish**.

11. Under **Database**, select **Connect**.




