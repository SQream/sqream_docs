.. _sso:

**************
Single Sign-On
**************

Here you can learn how to configure a SSO login for SQreamDB Acceleration Studio by integrating with an identity provider (IdP). A SSO authentication allows users to authenticate once and then seamlessly access SQreamDB as one of multiple services. 

.. contents::
   :local:
   :depth: 1
   
Before You Begin
================

It is essential you have the following installed:

* SQreamDB Acceleration Studio v5.9.0 
* There should be an NGINX (or similar) service installed on your Acceleration Studio machine, which will serve as a reverse proxy. This service will accept HTTPS traffic from external sources and communicate with Studio via HTTP internally
* You have :ref:`ldap` set as your authentication management service.

Setting SQreamDB Acceleration Studio
====================================
 
#. In your ``sqream_legacy.json`` file, add the ``ssoValidateUrl`` flag with your IdP URL.

   Example:
 
   .. code-block:: json
	
	"ssoValidateUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/userinfo"
 
#. Set Acceleration Studio to use SSO by adding the following flag to your ``sqream_admin_config.json`` file:

   * ``mfaRedirectUrl`` flag with your redirect URL

   Example:
 
   .. code-block:: json
   
	"mfaRedirectUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/authorize?client_id=e5636823-fb99-4d38-bbd1-6a46175eddab&redirect_uri=https://ivans.sq.l/login&response_type=token&scope=openid profile p1:read:user",

  If Acceleration Studio is not yet installed, you can set both URLs during its installation process.
   

	   
#. Restart SQreamDB.

#. Restart SQreamDB Acceleration Studio.

