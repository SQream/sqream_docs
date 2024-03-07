.. _sso:

**************
Single Sign-On
**************

Configuring Single Sign-On (SSO) by integrating with an identity provider (IdP) to allow users to authenticate once and seamlessly access SQreamDB as one of multiple services. 

.. contents::
   :local:
   :depth: 1
   
Before You Begin
================

It is essential you have the following installed:

* SQreamDB Acceleration Studio v5.9.0 
* There should be an NGINX (or similar) service installed on your Acceleration Studio machine, which will serve as a reverse proxy. This service will accept HTTPS traffic from external sources and communicate with Studio via HTTP internally

Setting SQreamDB Acceleration Studio
==========================================================
 
1. Set :ref:`ldap` as your authentication management service.

   The ``authenticationMethod`` flag value should be ``ldap``

  .. code-block::
	
	"authenticationMethod": "ldap"   
 
2. Set Acceleration Studio to use SSO by choosing one of the following methods: 
 
   * Manually paste your IdP URL to your ``sqream_admin_config.json`` file (recommended method)

   * Set the IdP URL during an Acceleration Studio installation process by pasting it to the questionnaire prompted following the ``npm run setup`` command

3. In your ``sqream_legacy.json`` file, add the ``pingoneValidateUrl`` flag with the IdP URL.

   Example:
 
  .. code-block::
   
	"pingoneValidateUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/userinfo"
	
4. Restart SQreamDB.
5. Restart SQreamDB Acceleration Studio.

