.. _azure:

***********************
Azure Blob Storage
***********************

Azure Blob Storage (ABS) is a scalable object storage solution within Microsoft Azure, designed to store and manage vast amounts of unstructured data.

ABS Bucket File Location
=================================

ABS syntax to be used for specifying a single or multiple file location within an ABS bucket:

.. code-block:: sql
 
	azure://accountname.core.windows.net/path

Connection String
===================

Connection String Example:

.. code-block:: json

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


   
Examples
============

.. code-block::

	COPY table_name FROM WRAPPER csv_fdw OPTIONS(location = 'azure://sqreamrole.core.windows.net/sqream-demo-data/file.csv');