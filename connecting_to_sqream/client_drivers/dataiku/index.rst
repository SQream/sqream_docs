.. _dataiku:

*******
Dataiku
*******

This Plugin accelerates data transfer from Amazon S3 to SqreamDB within Dataiku DSS. It enables direct loading of data from S3 to SqreamDB, ensuring rapid transfers without external steps.

The Plugin includes a code environment that automatically installs the SqreamDB Python Connector (pysqream) alongside the Plugin.

The following file formats are supported:

* Avro
* JSON
* CSV (requires manual data type mapping as the default for all columns is ``TEXT``) 

Before You Begin
=================

It is essential you have the follwoing:

* Sqreamdb :ref:`java_jdbc` connection set up in DSS

* Amazon S3 connection set up in DSS

* Python 3.9

Establishing a Dataiku Connection
=================================

In your Dataiku web interface:

#. Upload the plugin from the following SQreamDB Git repository:

   .. code-block:: console

	-- Repository URL:
	git@github.com:SQream/dataiku_plugin.git
	
	-- Path in repository:
	s3_bulk_load

#. Define a DSS S3 dataset. 

#. Add the plugin to your flow.

#. Set the S3 Dataset as Input of the Plugin (mandatory). 

#. Assign a name for the output dataset stored in your SQreamDB connection. 

#. Provide AWS Access Key and Secret Key by either:
 a. Filling in the values in the Plugin form

 b. Set the Project Variables or set the Global Variables when DSS Variables are used

