.. _apache_airflow:

***************
Apache Airflow
***************

Apache Airflow is a popular open-source orchestration tool. It allows users to write complex workflows composed of multiple kinds of actions and services using Directed Acyclic Graphs (DAGs), and to schedule, debug and monitor workflow runs.

Different kinds of actions are represented with specialized Python classes, called “Operators”. BLUE can build one or more customized Operators for performing different operations.

Before You Begin
================

It is essential that you have the following installed:

* Linux OS
* Python 3.9 or later version
* :ref:`BLUE connection access token<connecting_to_blue>`

Installing Apache Airflow BLUE Connector
========================================

The Apache Airflow BLUE connector is installed via pip, the Python package manager and installer. It is available for download via `PyPi <https://pypi.org/project/airflow-provider-sqream-blue/>`_. The connector uses Airflow version 2.6.2 and will override any other version you have installed.

To install the Apache Airflow BLUE connector, run the following command:

.. code-block:: python

	pip3 install airflow-provider-sqream-blue
	
``pip3`` will automatically installs all necessary libraries and modules. 



Setting Up a BLUE Connection
============================

In Airflow, go to **Add Connection**, choose **sqream-blue** for **Connection Type**, and fill in the following connection fields:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Field name
     - Description
   * - Connection Id
     -  A unique identifier used within an Airflow DAG to reference this specific connection configuration
   * - Description
     - A brief explanation or label to help users understand the purpose or context of the connection
   * - Host
     - The hostname or IP address of the server or resource to which the connection will be established
   * - Database
     - The name or identifier of the database within the specified host
   * - Access token
     - A security token or credential used to authenticate and authorize access to BLUE

	  

