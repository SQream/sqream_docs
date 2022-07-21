.. _sap_businessobjects:

*************************
Connecting to SQream Using SAP BusinessObjects
*************************
The **Connecting to SQream Using SAP BusinessObjects** guide includes the following sections:

.. contents::
   :local:
   :depth: 1
   
Overview
==========
The **Connecting to SQream Using SAP BusinessObjects** guide describes the best practices for configuring a connection between SQream and the SAP BusinessObjects BI platform. SAP BO's multi-tier architecture includes both client and server components, and this guide describes integrating SQream with SAP BO's object client tools using a generic JDBC connector. The instructions in this guide are relevant to both the **Universe Design Tool (UDT)** and the **Information Design Tool (IDT)**. This document only covers how to establish a connection using the generic out-of-the-box JDBC connectors, and does not cover related business object products, such as the **Business Objects Data Integrator**.

The **Define a new connection** window below shows the generic JDBC driver, which you can use to establish a new connection to a database.

.. image:: /_static/images/SAP_BO_2.png

SAP BO also lets you customize the interface to include a SQream data source.

Establising a New Connection Using a Generic JDCB Connector
==========
This section shows an example of using a generic JDBC connector to establish a new connection.

**To establish a new connection using a generic JDBC connector:**

1. In the fields, provide a user name, password, database URL, and JDBC class.

   The following is the correct format for the database URL:
   
   .. code-block:: console

      <pre>jdbc:Sqream://<ipaddress>:3108/<nameofdatabase>
	  
   SQream recommends quickly testing your connection to SQream by selecting the Generic JDBC data source in the **Define a new connection** window. When you connect using a generic JDBC data source you do not need to modify your configuration files, but are limited to the out-of-the-box settings defined in the default **jdbc.prm** file.
   
   .. note:: Modifying the jdbc.prm file for the generic driver impacts all other databases using the same driver.

   For more information, see `Connection String Examples <https://docs.sqream.com/en/v2020-1/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string-examples>`_.

2. (Optonal)If you are using the generic JDBC driver specific to SQream, modify the jdbc.sbo file to include the SQream JDBC driver location by adding the following lines under the Database section of the file:

   .. code-block:: console

      Database Active="Yes" Name="SQream JDBC data source">
      <JDBCDriver>
      <ClassPath>
      <Path>C:\Program Files\SQream Technologies\JDBC Driver\2021.2.0-4.5.3\sqream-jdbc-4.5.3.jar</Path>
      </ClassPath>
      </Parameter>
      <Parameter Name="JDBC Class">
      com.sqream.jdbc.SQDriver

      </JDBCDriver>
      </DataBase>

3. Restart the BusinessObjects server.

   When the connection is established, **SQream** is listed as a driver selection.