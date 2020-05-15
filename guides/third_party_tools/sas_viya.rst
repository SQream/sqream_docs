.. _connect_to_sas_viya:

*************************
Connecting to SAS Viya
*************************

You can use SAS Viya to connect to a SQream DB cluster. This tutorial is a guide that will show you how to connect to SAS Viya.

.. contents:: In this topic:
   :local:

Installing SAS Viya
============================

SQream DB has been tested with SAS Viya v.03.05 and newer.

If you do not already have SAS Viya installed, refer to SAS's website https://www.sas.com/en_us/software/viya.html .


Installing the JDBC driver
=================================================

#. Download the JDBC driver :ref:`from the client drivers page<client_drivers>`.

#. Unzip the JDBC driver into a location on the SAS Viya server.
   
   SQream recommends creating the directory ``/opt/sqream`` on the SAS Viya server.


Configuring the JDBC driver in SAS Viya
====================================================

#. Sign into SAS Studio

#. 
   Create a new SAS program
   
   .. figure:: /_static/images/sas_viya_new_program.png
      :scale: 80 %
      
   
#. Create a sample program to explore data


   .. literalinclude:: connect.sas
      :language: sas
      :caption: Sample SAS program
      :linenos:
      :emphasize-lines: 11

   This sample program does several things:
      
      * Line 10: Start a JDBC session named ``sqlib``, associated with the SQream DB driver. This statement extends the SAS global LIBNAME statement so that you can assign a libref to your data source. This feature lets you reference a table in SQream DB directly in a DATA Step or SAS procedure. 
      
      * Line 11: Instruct SAS Viya where to find the SQream DB JDBC driver. This step is required because SAS Viya will not honor the SAS_ACCESS_CLASSPATH environment variable for this connection.
      
      * 
         Lines 12-15: Associate the libref to be able to use it in the program as ``sqlib.tablename``. The libref will be ``sqlib`` and it will use the JDBC engine and connect to the ``sqream-cluster.piedpiper.com`` SQream DB cluster. 
         
         The database name is ``raviga`` and the schema is ``public``.
         
         See our JDBC guide for `connection string documentation <connection_string>`.
         
      * Lines 19-23: Data preparation step. We load data from the customers table into the in-memory space in SAS Viya.
      
      * Lines 25-27: DATA step. This step should be familiar to SAS v9 users. We use standard SAS naming conventions to reference the data, with ``sqlib`` as the libref and ``customers`` as the table.


#. Run the program by clicking the Run button
   
   .. figure:: /_static/images/sas_viya_run_program.png
      :scale: 80 %
      
      The Run button runs the current SAS program

   If the sample ran correctly, three new tabs will appear: **Log**, **Results**, and **Output Data**.
   
#. The query results can be seen in the **Results** tab.

   .. figure:: /_static/images/sas_viya_results_tab.png
      :scale: 80 %
      
      The results tab contains query results
   
   

Browsing data and workbooks
========================================

#. From the panel on the left, navigate to **Libraries** to open the navigation tree.

#. Our previously created library named ``SQLIB`` will populate, and show the table ``customers``. Double clicking on the table name will expand it and show the columns.

#. Find the workbook you created in the DATA step. It should appear under ``WORK``.

   The workbook will be named ``sqlib.customers``. Double click it to expand the table tree.



SAS Viya best practices and troubleshooting
=================================================

Cut out what you don't need
-----------------------------

* Bring only the data sources you need into SAS Viya. As a best practice, do not bring in tables that you don't intend to explore.

* Add filters before the DATA step to reduce in-memory size. Add filters to the datasource before exploring, so that the queries sent to SQream DB run faster.


Create a separate service for SAS Viya
---------------------------------------

SQream recommends that SAS Viya get a separate service with the DWLM. This will reduce the impact of SAS Viya on other applications and processes, such as ETL.

This works in conjunction with the load balancer to ensure good performance.


Troubleshooting ``java.lang.ClassNotFoundException: com.sqream.jdbc.SQDriver`` exceptions
--------------------------------------------------------------------------------------------------------

In some cases, SAS Viya may have trouble finding the SQream DB JDBC driver. This message explains that the driver can't be found.

To solve this issue, try two things:

1. Verify that the JDBC driver was placed in a directory that SAS Viya can access

2. Verify the classpath in your SAS program. Make sure that the classpath is correct, and the file it references can be accessed by SAS Viya.

If you're still experiencing issues after restarting SAS Viya, we're always happy to help. Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.
