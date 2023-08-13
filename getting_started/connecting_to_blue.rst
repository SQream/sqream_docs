.. _connecting_to_blue:

===========
Integration
===========

Users who wish to connect to BLUE from their own applications or tools may need to use connectors. BLUE supports the most common database tools and interfaces, giving you direct access through a variety of connectors, visualization tools, and utilities. 

To use any of the following connectors, applications, and tools, it is essential that you create dedicated BLUE **Clients** and generate client connection access tokens.

Access Token Management
-----------------------

Access tokens are used to establish secure connections with connectors and third-party platforms by providing a means of authentication and authorization. They enhance security by ensuring only authorized entities can access the BLUE cluster. Access tokens help manage machine-to-machine communication, enable auditing and logging, and promote compatibility with modern integration practices. 

Creating Access Tokens
^^^^^^^^^^^^^^^^^^^^^^

Using connectors and third-party tools requires BLUE clients to be associated with access tokens. Once an access token is generated, you may use it to secure the connection between your BLUE client and the respective BLUE cluster or platform, ensuring authenticated access, controlled data interaction, and enhanced security measures in place.

:ref:`Creating roles<create_role>` before generating access tokens is a best practice.

#. Log in to your BLUE interface and navigate to **Settings** > **Access Token Management**.

#. Select **Create New Client** and fill in a **Client Name** and a **Client Role**.

   Consider providing a **Client Name** that can be widely understood, such as **BI**, **JDBC**, or **Analysis**.
	
   Your newly created BLUE client inherits permissions from the associated **Client Role**.

#. Select **Generate Token**.	

   A Client creation pop-up window with your new access token appears.
	
#. Copy the access token  or select **Done**.

Managing Access Tokens
^^^^^^^^^^^^^^^^^^^^^^

You may manage each of your BLUE clients' access tokens separately. 

#. Log in to your BLUE interface and navigate to **Settings** > **Access Token Management**.

#. For each BLUE client, you may select any of the following options:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Option
     - Description
   * - **Show**
     - Shows your access token in case you need to copy it
   * - **Disable** / **Enable**
     - Correspondingly disables BLUE client connection or enables it. May be used for system maintenance or in the event of a compromised token
   * - **Delete**
     - Deletes BLUE client. May be used when a client is no longer needed
   * - **Regenerate Access Token**
     - Regenerates access token. May be used when your access token expires

----------------------

Connectors, Drivers, and Third-Parties
--------------------------------------

Connectors and Drivers
^^^^^^^^^^^^^^^^^^^^^^

:ref:`JDBC<java_jdbc>`

:ref:`ODBC<odbc>`

:ref:`Python<pysqream>`

Data Management, Analysis, and Business Intelligence Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data Integration Tools
""""""""""""""""""""""

:ref:`Denodo<denodo>`

:ref:`Informatica Cloud Services<informatica>`

:ref:`Pentaho Data Integration<pentaho_data_integration>`

:ref:`Talend<talend>`

:ref:`SQL Workbench<connect_to_sql_workbench>`

Business Intelligence (BI) Tools
""""""""""""""""""""""""""""""""

:ref:`MicroStrategy<micro_strategy>`

:ref:`Power BI Desktop<power_bi>`

:ref:`SAP BusinessObjects<sap_businessobjects>`

:ref:`SAS Viya<connect_to_sas_viya>`

:ref:`Tableau<tableau>`

:ref:`TIBCO Spotfire<tibco_spotfire>`

Data Analysis and Programming Languages
"""""""""""""""""""""""""""""""""""""""

:ref:`PHP<php>`

:ref:`R<r>`

.. topic:: Additional Connection Methods and Tools

   If you wish to use any other connection method or tool which is not currently supported, you may contact our `support team <https://sqream.atlassian.net/servicedesk/>`_, and they'll look into it.
