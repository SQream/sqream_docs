.. _access_tokens:

*************
Access Tokens
*************

Using connectors and third-party tools requires BLUE clients to be associated with access tokens. Once an access token is generated, you may use it to secure the connection between your BLUE client and the respective BLUE cluster or platform, ensuring authenticated access, controlled data interaction, and enhanced security measures in place.

.. topic:: ``clusteradmin``

   Only a ``clusteradmin`` can create and manage access tokens.

.. tip::

	:ref:`Creating roles<create_role>` before generating access tokens is a best practice.

Generating Access Tokens
========================

#. Log in to your BLUE interface and navigate to **Settings** > **Access Token Management**.

#. Select **Create New Client** and fill in a **Client Name** and a **Client Role**.

   Consider providing a **Client Name** that can be widely understood, such as *BI*, *JDBC*, or *Analysis*.
	
   Your newly created BLUE client inherits permissions from the associated **Client Role**.

#. Select **Generate Token**.	

   A Client creation pop-up window with your new access token appears.
	
#. Copy the access token or select **Done**.

#. Use the access token within your connector or third-party application or tool configuration.

#. To enable **Jobs**, designate a recently created client or one of your existing clients as a connection for Jobs by choosing it from the Jobs column, under the **Access Token Management** tab.

Managing Your Access Tokens
---------------------------

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