.. _getting_started:

***************
Overview
***************

The Getting Started guide provides an overview of the key steps to begin using BLUE, a comprehensive platform that offers advanced security features and seamless integration with various data analysis tools. This guide covers the login process, third-party tool integration, managing resources effectively, and utilizing Jobs, a powerful SQL workflow tool.

Login
-----

By leveraging Auth0, BLUE enables:

* IDP authentication
* Multi-Factor Authentication
* Encryption
* Anomaly detection protecting data and preventing unauthorized access 

Auth0
^^^^^

#. Check your email for an Auth0 invite from your administrator to join BLUE and select **ACCEPT INVITATION**.

   An invitation window opens.
   
#. Select **Continue** and you will be logged in to BLUE.

Identity Providers
^^^^^^^^^^^^^^^^^^

#. Follow the BLUE URL provided by your admin. 

#. Once you're in, select **Log In**. 

#. You will then be redirected to your IDP page, where you will need to verify your credentials. 
   This is a one-time process, after which you will be redirected back to the BLUE interface. 

From your second login onward, you will be automatically redirected to the BLUE interface.


Third-Party Tools
-----------------

:ref:`Connect<connecting_to_blue>` your favorite data analysis platforms and BI tools using Python, JDBC, or ODBC.


Manage Your Resources
-----------------------

:ref:`Manage your resources <managing_your_resources>` and reduce runtime during idle periods for better costs. Allocate workers based on department-specific needs for improved cluster utilization.


SQL Workflows
-------------

**Jobs** is a SQL and Python :ref:`workflow tool <performing_basic_blue_operations>` for creating complex workflows. It automates sequences of SQL and Python scripts, triggering them to deliver insights or prepare data for advanced tasks such as data modeling and training.


.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   managing_your_resources 
   performing_basic_blue_operations
   connecting_to_blue
   
   
