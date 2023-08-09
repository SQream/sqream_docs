.. _getting_started:

***************
Getting Started
***************

The Getting Started guide provides an overview of the key steps to begin using BLUE, a comprehensive platform that offers advanced security features and seamless integration with various data analysis tools. This guide covers the login process, third-party tool integration, managing resources effectively, and utilizing Jobs, a powerful SQL workflow tool.

Login
-----

By leveraging Auth0, BLUE enables not only IDP authentication, but also multi-factor authentication, encryption, and anomaly detection to protect user data and prevent unauthorized access. 

Logging In Using Identity Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Follow the BLUE URL provided by your admin. 

#. Once you're in, select **Log In**. 

#. You will then be redirected to your IDP page, where you will need to verify your credentials. 
   This is a one-time process, after which you will be redirected back to the BLUE interface. 

From your second login onward, you will be automatically redirected to the BLUE interface.

Logging In Using Auth0
^^^^^^^^^^^^^^^^^^^^^^

#. Check your email for an Auth0 invite from your administrator to join BLUE and select **ACCEPT INVITATION**.

   An invitation window opens.
   
#. Select **Continue** and you will be logged in to BLUE.

------------------

Third-Party Tools
-----------------

Use the data analysis platform you're used to work with by :ref:`connecting to BLUE<connecting_to_blue>` using Python, JDBC, or ODBC.

------------------

Managing Your Resources
-----------------------

The :ref:`Resource Pool <managing_your_resources>` panel optimizes resource utilization in your BLUE environment. Reduce runtime during idle periods to manage costs and allocate workers based on department-specific needs for improved cluster utilization. Fine-tune worker allocation to maximize the benefits of your BLUE environment.

------------------

SQL Workflows
-------------

**Jobs** is a SQL :ref:`workflow tool <performing_basic_blue_operations>` for creating complex workflows. It automates sequences of SQL scripts, triggering them to deliver insights or prepare data for advanced tasks like modeling and training. Execute jobs manually or schedule them for automatic execution.


.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   managing_your_resources 
   performing_basic_blue_operations
   connecting_to_blue
   
   
