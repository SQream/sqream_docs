.. _before_you_begin:

***********************
Before you begin
***********************

Before you install or deploy SQream DB, please verify you have the following:

* An NVIDIA-capable server, either on-premise or on supported cloud platforms

   * Supported operating systems: Red Hat Enterprise Linux v7.x / CentOS v7.x / Ubuntu 18.04 / Amazon Linux
   * NVIDIA GPU. A Tesla GPU is highly recommended
   * A privileged SSH connection to the server (sudo)

* A SQream DB license (contact support@sqream.com or your SQream account manager for your license key)

* A 3rd party tool that can connect to SQream DB via JDBC, ODBC, or Python

If you do not have a SQream DB license, visit our website and `sign up for SQream DB`_ today!

What does the installation process look like?
----------------------------------------------

To install SQream DB, we will go through the following steps:

#. Prepare the host OS for NVIDIA driver installation

#. Install the NVIDIA driver

#. Install Docker CE

#. Install nvidia-docker2

#. Prepare disk space for SQream DB

#. Install SQream DB

#. Additional system configuration for performance and stability


.. rubric:: What's next?

* When ready, start :ref:`installing SQream DB <installing_sqream_db_docker>`

.. _`sign up for SQream DB`: https://sqream.com/try-sqream-db

.. TODO Links for if the user has already installed SQream DB but wants to configure, upgrade, or scale out the system further