.. _pentaho_data_integration:


*************************
Connecting to SQream Using Pentaho Data Integration
*************************

Overview
=========
This document is a viability report on **Pentaho Data Integration (PDI)** as an ETL tool for Big Data and its compatibility with SQreamDB. It provides documentation for stakeholders using SQreamDB. PDI is part of Hitachi's Lumada portfolio.

It includes the following:

* :ref:`A Quick Start guide <quickstart_guide>`
* :ref:`Information about supported SQream drivers <supported_sqream_drivers>`
* :ref:`Information about supported data sources <supported_data_sources>`
* :ref:`Information about supported tools and operating system versions <supported_tool_os_versions>`
* :ref:`A description of known issues <known_issues>`
* :ref:`Related links <related_links>`
* :ref:`Download links <download_links>`

.. _quickstart_guide:

Quick Start Guide
-----------------
This Quick Start Guide describes how to start using PDI.

In this tutorial, we cover the steps to install Pentaho Data Integration, part of Hitachi’s Lumada portfolio, on your Microsoft Windows computer  and to start the app

1. Download PDI according to `Pentaho Community Edition (CE) Installation Guide <https://www.hitachivantara.com/en-us/pdf/white-paper/pentaho-community-edition-installation-guide-for-windows-whitepaper.pdf>`_.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_01.png

2. Do one of the following:

   * Use the CLI to open the PDI client for your operating system:

     * Windows:
   
       .. code-block:: console
     
          $ spoon.bat
   
     * Linux:
   
       .. code-block:: console
     
          $ ./spoon.sh &>/dev/null &
    
   * Open the spoon.bat file from its folder location.
		  
.. image:: /_static/images/third_party_connectors/pentaho/spoon_bat_file.png

3. In the **View** tab, right-click **Transformations** and click **New**.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_1.png

A new transformation tab is created.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_2.png

3. In the **Design** tab, click **Input** to show its file contents.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_3.png

4. Drag and drop **CSV file input** file to the new transformation tab that you created.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_4.png

5. Double-click **CSV file input**. The **CSV file input** panel is displayed.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_5.png

6. In the **Step name** field, type a name.

.. image:: /_static/images/third_party_connectors/pentaho/pentaho_6.png

7. To the right of the **Filename** field, click **Browse** and select the file that you want to read from and click **OK**.

.. image:: /_static/images/third_party_connectors/pentaho/add_csv_file.png

8. In the CSV file input window, click **Get Fields**.

.. image:: /_static/images/third_party_connectors/pentaho/get_fields.png

9. In the **Sample data** window, enter the number of lines you want to sample and click **OK**. The default setting is **100**.

.. image:: /_static/images/third_party_connectors/pentaho/number_of_lines_to_sample.png

The tool reads the file and suggests the field name and type. **Comment - is this reflected on the GUI?**

10. In the CSV file input window, click **Preview**.

.. image:: /_static/images/third_party_connectors/pentaho/preview.png

10. In the **Preview size** window, enter the number of rows you want to preview and click **OK**. The default setting is **1000**.

.. image:: /_static/images/third_party_connectors/pentaho/number_of_rows_to_preview.png






