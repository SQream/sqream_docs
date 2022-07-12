.. _pentaho_data_integration:

*************************
Connecting to SQream Using Pentaho Data Integration
*************************
.. _pentaho_top:

Overview
=========
This document is a Quick Start Guide that describes how to install Pentaho, create a transformation, and define your output. 

The Connecting to SQream Using Pentaho page describes the following:

* :ref:`Installing Pentaho <install_pentaho>`
* :ref:`Installing and setting up the JDBC driver <install_set_up_jdbc_driver>`
* :ref:`Creating a transformation <create_transformation>`
* :ref:`Defining your output <define_output>`
* :ref:`Importing your data <import_data>`

.. _install_pentaho:

Installing Pentaho
~~~~~~~~~~~~~~~~~
To install PDI, see the `Pentaho Community Edition (CE) Installation Guide <https://www.hitachivantara.com/en-us/pdf/white-paper/pentaho-community-edition-installation-guide-for-windows-whitepaper.pdf>`_.

The **Pentaho Community Edition (CE) Installation Guide** describes how to do the following:

* Downloading the PDI software.
* Installing the **JRE (Java Runtime Environment)** and **JDK (Java Development Kit)**.
* Setting up the JRE and JDK environment variables for PDI.

:ref:`Back to Overview <pentaho_top>`

.. _install_set_up_jdbc_driver:

Installing and Setting Up the JDBC Driver
~~~~~~~~~~~~~~~~~
After installing Pentaho you must install and set up the JDBC driver. This section explains how to set up the JDBC driver using Pentaho. These instructions use Spoon, the graphical transformation and job designer associated with the PDI suite.

You can install the driver by copying and pasting the SQream JDBC .jar file into your **<directory>/design-tools/data-integration/lib** directory. 

**NOTE:** Contact your SQream license account manager for the JDBC .jar file.

:ref:`Back to Overview <pentaho_top>`

.. _create_transformation:

Creating a Transformation
~~~~~~~~~~~~~~~~~~
After installing Pentaho you can create a transformation.

**To create a transformation:**

1. Use the CLI to open the PDI client for your operating system (Windows):
   
     .. code-block:: console
     
        $ spoon.bat

2. Open the spoon.bat file from its folder location.

::
		  
3. In the **View** tab, right-click **Transformations** and click **New**.

A new transformation tab is created.

4. In the **Design** tab, click **Input** to show its file contents.

::

5. Drag and drop the **CSV file input** item to the new transformation tab that you created.

::

6. Double-click **CSV file input**. The **CSV file input** panel is displayed.

::

7. In the **Step name** field, type a name.

::

8. To the right of the **Filename** field, click **Browse**.

::

9. Select the file that you want to read from and click **OK**.

::

10. In the CSV file input window, click **Get Fields**.

::

11. In the **Sample data** window, enter the number of lines you want to sample and click **OK**. The default setting is **100**.

    The tool reads the file and suggests the field name and type.

12. In the CSV file input window, click **Preview**.

::

13. In the **Preview size** window, enter the number of rows you want to preview and click **OK**. The default setting is **1000**.

::

14. Verify that the preview data is correct and click **Close**.

::

15. Click **OK** in the **CSV file input** window.

:ref:`Back to Overview <pentaho_top>`

.. _define_output:

Defining Your Output
-----------------
After creating your transformation you must define your output.

**To define your output:**

1. In the **Design** tab, click **Output**.

   The Output folder is opened.
   
2. Drag and drop **Table output** item to the Transformation window.

::

3. Double-click **Table output** to open the **Table output** dialog box.

::

4. From the **Table output** dialog box, type a **Step name** and click **New** to create a new connection. Your **steps** are the building blocks of a transformation, such as file input or a table output.

The **Database Connection** window is displayed with the **General** tab selected by default.

5. Enter or select the following information in the Database Connection window and click **Test**.

The following table shows and describes the information that you need to fill out in the Database Connection window:

.. list-table:: 
   :widths: 6 31 73
   :header-rows: 1
   
   * - No.
     - Element Name
     - Description
   * - 1
     - Connection name
     - Enter a name that uniquely describes your connection, such as **sampledata**.
   * - 2
     - Connection type
     - Select **Generic database**.
   * - 3
     - Access
     - Select **Native (JDBC)**.
   * - 4
     - Custom connection URL
     - Insert **jdbc:Sqream://<host:port>/<database name>;user=<username>;password=<password>;[<optional parameters>; ...];**. The IP is a node in your SQream cluster and is the name or schema of the database you want to connect to. Verify that you have not used any leading or trailing spaces.
   * - 5
     - Custom driver class name
     - Insert **com.sqream.jdbc.SQDriver**. Verify that you have not used any leading or trailing spaces.
   * - 6
     - Username
     - Your SQreamdb username. If you leave this blank, you will be prompted to provide it when you connect.	 
   * - 7
     - Password
     - Your password. If you leave this blank, you will be prompted to provide it when you connect.

The following message is displayed:	 
	 
.. image:: /_static/images/third_party_connectors/pentaho/connection_tested_successfully_2.png	 
	 
6. Click **OK** in the window above, in the Database Connection window, and Table Output window.

:ref:`Back to Overview <pentaho_top>`

.. _import_data:

Importing Data
-----------------
After defining your output you can begin importing your data.

For more information about backing up users, permissions, or schedules, see `Backup and Restore Pentaho Repositories <https://help.pentaho.com/Documentation/7.0/0P0/Managing_the_Pentaho_Repository/Backup_and_Restore_Pentaho_Repositories>`_

**To import data:**

1. Double-click the **Table output** connection that you just created.

::

2. To the right of the **Target schema** field, click **Browse** and select a schema name.

::

3. Click **OK**. The selected schema name is displayed in the **Target schema** field.

::

4. Create a new hop connection between the **CSV file input** and **Table output** steps:

   1. On the CSV file input step item, click the **new hop connection** icon.
   
      .. image:: /_static/images/third_party_connectors/pentaho/csv_file_input_options.png
   
   2. Drag an arrow from the **CSV file input** step item to the **Table output** step item.
   
      .. image:: /_static/images/third_party_connectors/pentaho/csv_file_input_options_2.png   

   3. Release the mouse button. The following options are displayed.
   
   4. Select **Main output of step**.
   
      .. image:: /_static/images/third_party_connectors/pentaho/main_output_of_step.png
   
::

5. Double-click **Table output** to open the **Table output** dialog box.

::

6. In the **Target table** field, define a target table name.

::

7. Click **SQL** to open the **Simple SQL editor.**
   
::
   
8. In the **Simple SQL editor**, click **Execute**.

   The system processes and displays the results of the SQL statements.
   
9. Close all open dialog boxes.

::

10. Click the play button to execute the transformation.

   .. image:: /_static/images/third_party_connectors/pentaho/execute_transformation.png

    The **Run Options** dialog box is displayed.

11. Click **Run**. The **Execution Results** are displayed.
 
:ref:`Back to Overview <pentaho_top>`
