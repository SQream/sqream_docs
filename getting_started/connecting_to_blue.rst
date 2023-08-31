.. _connecting_to_blue:

===========
Integration
===========

Users who wish to use the BLUE :ref:`Jobs<performing_basic_blue_operations>` workflow management tool or establish connections to BLUE from their personal applications or tools are required to employ connectors and obtain authentication access tokens, thereby necessitating the creation of dedicated BLUE **Clients** and the generation of these access tokens to enable the use of Jobs, connectors, applications, and tools in question.

Access tokens, managed via Airflow for authentication and security, are essential for establishing secure links to connectors and external platforms. These tokens serve to authenticate and authorize, enhancing security by permitting only authorized entities to access the BLUE cluster. Their importance lies in facilitating smooth machine-to-machine communication, enabling thorough auditing and logging, and aligning with modern integration practices.

Creating Clients and Generating Access Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using connectors and third-party tools requires BLUE clients to be associated with access tokens. Once an access token is generated, you may use it to secure the connection between your BLUE client and the respective BLUE cluster or platform, ensuring authenticated access, controlled data interaction, and enhanced security measures in place.

:ref:`Creating roles<create_role>` before generating access tokens is a best practice.

#. Log in to your BLUE interface and navigate to **Settings** > **Access Token Management**.

#. Select **Create New Client** and fill in a **Client Name** and a **Client Role**.

   Consider providing a **Client Name** that can be widely understood, such as *BI*, *JDBC*, or *Analysis*.
	
   Your newly created BLUE client inherits permissions from the associated **Client Role**.

#. Select **Generate Token**.	

   A Client creation pop-up window with your new access token appears.
	
#. Copy the access token or select **Done**.

#. Use the access token within your connector or third-party application or tool configuration.

#. To enable **Jobs**, designate a recently created client or one of your existing clients as a connection for Jobs by choosing it from the Jobs column on under the **Access Token Management** tab.

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
     - Regenerates access token. May be used in the event of a compromised token

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

:ref:`Apache Airflow<apache_airflow>`

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
