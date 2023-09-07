.. _azure:

***********************
Azure
***********************


.. contents::
   :local:
   :depth: 1


Azure URI Format
=================

Specify a location for a file (or files) when using :ref:`copy_from` or :ref:`foreign_tables`.

The following is an example of the general Azure syntax:

.. code-block:: console
 
	azure://accountname.core.windows.net/path


Connection String
===================

Connection String Example:

.. code-block::

	"DefaultEndpointsProtocol=https;AccountName=myaccount101;AccountKey=#######################################==;EndpointSuffix=core.windows.net"

Use the following parameters within your SQreamDB legacy configuration file for authentication:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``DefaultEndpointsProtocol``
     - Specifies the protocol (e.g., https or http) used for accessing the storage service
   * - ``AccountName``
     - Represents the unique name of your Azure Storage account
   * - ``AccountKey``
     - Acts as the primary access key for securely authenticating and accessing resources within the storage account
   * - ``EndpointSuffix``
     - Denotes the Azure Storage service endpoint suffix for a specific region or deployment, such as ``.core.windows.net``


   
Example
============

.. code-block::

	COPY table_name FROM WRAPPER csv_fdw OPTIONS(location = 'azure://sqreamrole.core.windows.net/sqream-demo-data/file.csv');