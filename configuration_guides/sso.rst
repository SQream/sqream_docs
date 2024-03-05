.. _sso:

Ping Identity Single Sign-On
============================





.. contents::
   :local:
   :depth: 1
   
Before You Begin
================

It is essential you have the following installed:

* SQreamDB Acceleration Studio v5.9.0 
* There should be an NGINX (or similar) service installed on your Acceleration Studio machine, which will serve as a reverse proxy. This service will accept HTTPS traffic from external sources and communicate with Studio via HTTP internally
   
Setting Ping Identity
=============================
   
1. Log in to your Ping Identity account and create a **Single Page** application.

2. Under **Application** > **YourAccount**, set the following:

   * **Policies** > **DaVinci** > **PingOne**, set **Sign On and Registration**

   * **Resources**, set **openid**, **profile**, **P1:read:user**, **P1:verify:user**
	
3. Under **Application** > **YourAccount** > **Configuration**, create the following URLs:

   * **URLs** > Copy Authorization URL

   * Redirect URIs 

4. Under **Application** > **YourAccount**, copy Client ID and replace it in the following string: => This is 2nd part of the final URL.

``?client_id=e5636823-fb99-4d38-bbd1-6a46175eddab&redirect_uri=https://ivans.sq.l/login&response_type=token&scope=openid profile p1:read:user (Please note that the whole string must be copied)``

Connect both parts in a following manner:

``https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/authorize?client_id=e5636823-fb99-4d38-bbd1-6a46175eddab&redirect_uri=https://ivans.sq.l/login&response_type=token&scope=openid profile p1:read:user``

Logoff:

``https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/signoff``

Setting SQreamDB Acceleration Studio
==========================================================
 
1. Set PingOne SSO authentication using either of the following methods: 
 
   * The **recommended** method is to manually paste the authentication URL to your ``sqrea_admin_config.json`` file.

   * Alternatively, you may set the authentication URL during the SQreamDB Acceleration Studio installation process, after having ran the ``npm run setup`` command, by pasting the authentication URL in the questionnaire.

2. In your ``sqream_legacy.json``, change ``"authenticationMethod": "sqream"`` to ``"authenticationMethod": "ldap"`` and add the ``pingoneValidateUrl`` flag along with the ______ URL: ``"pingoneValidateUrl": "https://auth.pingone.eu/9db5d1c6-6dd6-4e40-b939-e0e4209e0ac5/as/userinfo"``

5. Restart SQreamDB.
6. Restart SQreamDB Acceleration Studio.

