.. _generating_access_tokens:

=======================
Access Token Management
=======================

Access tokens are used to establish secure connections with connectors and third-party platforms by providing a means of authentication and authorization. They enhance security by ensuring only authorized entities can access the database, offer granular control over permissions, and support token expiration and revocation. Access tokens help avoid sharing sensitive credentials, enable auditing and logging, and promote compatibility with modern integration practices. 

Creating Access Tokens
----------------------

Using connectors and third-party tools requires BLUE clients to be associated with access tokens. Once an access token is generated, you may use it to secure the connection between your BLUE client and the respective database or platform, ensuring authenticated access, controlled data interaction, and enhanced security measures in place.

#. Log in to your BLUE interface and navigate to **Settings** > **Access Token Management**.

#. Select **Create New Client** and fill in a **Client Name** and a **Client Role**.

	Consider providing a **Client Name** that can be widely understood, such as **BI**, **JDBC**, or **Analysis**.
	
	Your newly created BLUE client inherits permissions from the associated **Client Role**.

#. Select **Generate Token**.	

	A Client creation pop-up window with your new access token appears.
	
#. Copy the access token  or select **Done**.

------------------

Managing Access Tokens
----------------------

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
   * - **Disable** // **Enable**
     - Correspondingly disables BLUE client connection or enables it. May be used for system maintenance
   * - **Delete**
     - Deletes BLUE client. May be used when a client is no longer needed
   * - **Regenerate Access Token**
     - Regenerates access token. May be used when your access token expires



