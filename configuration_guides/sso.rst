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

Setting SQreamDB Acceleration Studio
====================================
 
1. Set :ref:`ldap` to be your authentication management service.

   The ``authenticationMethod`` flag value should be ``ldap``

  .. code-block:: json
	
	"authenticationMethod": "ldap"   
 
2. In your ``sqream_legacy.json`` file, add the following flags:

   * ``SSOValidateUrl`` flag with the IdP URL
   * ``mfaLogoutUrl`` flag with the logout URL
   
   Example:
 
  .. code-block:: json
   
	"SSOValidateUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/userinfo"
	"mfaLogoutUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/signoff"
 
3. Set Acceleration Studio to use SSO by manually pasting your IdP URL to your ``sqream_admin_config.json`` file.

   Alternatively, you can set the IdP URL during an Acceleration Studio installation process by pasting it to the questionnaire prompted following the ``npm run setup`` command, but this approach is less recommended.


	
4. Restart SQreamDB.
5. Restart SQreamDB Acceleration Studio.

