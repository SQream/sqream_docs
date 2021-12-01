.. _tibco_spotfire:


*************************
Connecting to SQream Using TIBCO Spotfire
*************************
Overview
=========
The **TIBCO Spotfire** software is an analytics solution that enables visualizing and exploring data through dashboards and advanced analytics.

This document is a Quick Start Guide that describes the following:
   
.. contents::
   :local: 
   :depth: 1
   
Establishing a Connection between TIBCO Spotfire and SQream
-----------------
TIBCO Spotfire supports the following versions:

* **JDBC driver** - Version 4.5.2 
* **ODBC driver** - Version 4.1.1

SQream supports TIBCO Spotfire version 7.12.0.

The **Establishing a JDBC Connection between TIBCO Spotfire and SQream** section describes the following:

.. contents::
   :local: 
   :depth: 1   
   
Creating a JDBC Connection
~~~~~~~~~~~
For TIBCO Spotfire to recognize SQream, you must add the correct JDBC jar file to Spotfire's loaded binary folder. The following is an example of a path to the Spotfire loaded binaries folder: ``C:\tibco\tss\7.12.0\tomcat\bin``.

For the complete TIBCO Spotfire documentation, see `TIBCO Spotfire® JDBC Data Access Connectivity Details <https://community.tibco.com/wiki/tibco-spotfire-jdbc-data-access-connectivity-details>`_. 

Creating an ODBC Connection
~~~~~~~~~~~
**To create an ODBC connection**

1. Install and configure ODBC on Windows.

   For more information, see :ref:`Install and Configure ODBC on Windows<install_odbc_windows>`.
   
#. Launch the TIBCO Spotfire application.

    ::

#. From the **File** menu click **Add Data Tables**.

   The **Add Database Tables** window is displayed.

#. Click **Add** and select **Database**.

   The **Open Database** window is displayed.

#. In the **Data source type** area, select **ODBC SQream** (Odbc Data Provider) and click **Configure**.

   The **Configure Data Source and Connection** window is displayed.
   
#. Select **System or user data source** and from the drop-down menu select the DSN of your data source (SQreamDB).

    ::

#. Provide your database username and password and click **OK**.

    ::

#. In the **Open Database** window, click **OK**.

   The **Specify Tables and Columns** window is displayed.

#. In the **Specify Tables and Columns** window, select the checkboxes corresponding to the tables and columns that you want to include in your SQL statement.

    ::

#. In the **Data source name** field, set your data source name and click **OK**.

   Your data source is displayed in the **Data tables** area.

#. In the **Add Data Tables** dialog, click **OK** to load the data from your ODBC data source into Spotfire.

**Comment** - *I didn't do the above step. Do I need to document the result?*

.. note:: Verify that you have checked the SQL statement. 

Creating the SQream Data Source Template
~~~~~~~~~~~
After creating a connection, you can create your SQream data source template.

**To create your SQream data source template:**

1. Log in to the TIBCO Spotfire Server Configuration Tool.

    ::
	
#. From the **Configuration** tab, in the **Configuration Start** menu, click **Data Source Templates**.

   The **Data Source Templates** list is displayed.
   
#. From the Data Source Templates list do one of the following:

  * Override an existing template:
   
    1. In the template text field, select an existing template.
	
	    ::
		
    2. Copy and paste your data source template text.
	 
	     ::
	 
  * Create a new template:
   
    1. Click **New**.
        
       The **Add Data Source Template** window is displayed.
	   
       .. _creating_sqream_data_source_template:
		
    2. In the **Name** field, define your template name.
	
	    ::
		
    3. In the **Data Source Template** text field, copy and paste your data source template text.
	
       The following is an example of a data source template:		

       .. code-block:: console
	
          <jdbc-type-settings>
            <type-name>SQream   </type-name>
            <driver>com.sqream.jdbc.SQDriver   </driver>
            <connection-url-pattern>jdbc:Sqream://&lt;host&gt;:&lt;port&gt;/database;user=sqream;password=sqream;cluster=true   </connection-url-pattern>
            <supports-catalogs>true   </supports-catalogs>
            <supports-schemas>true   </supports-schemas>
            <supports-procedures>false   </supports-procedures>
            <table-types>TABLE,EXTERNAL_TABLE   </table-types>
            <java-to-sql-type-conversions>
             <type-mapping>
                <from>Bool   </from>
                <to>Integer   </to>
              </type-mapping>
              <type-mapping>
                <from>VARCHAR(2048)   </from>
                <to>String   </to>
              </type-mapping>
              <type-mapping>
                <from>INT   </from>
                <to>Integer   </to>
              </type-mapping>
              <type-mapping>
                <from>BIGINT   </from>
                <to>LongInteger   </to>
              </type-mapping>
              <type-mapping>
                <from>Real   </from>
                <to>Real   </to>
              </type-mapping>
	           <type-mapping>
                <from>Decimal   </from>
                <to>Float   </to>
              </type-mapping>
               <type-mapping>
                <from>Numeric   </from>
                <to>Float   </to>
              </type-mapping>
              <type-mapping>
                <from>Date   </from>
                <to>DATE   </to>
              </type-mapping>
              <type-mapping>
                <from>DateTime   </from>
                <to>DateTime   </to>
              </type-mapping>
             </java-to-sql-type-conversions>
            <ping-command>   </ping-command>
          </jdbc-type-settings>			
	
4. Click **Save configuration**.

    ::
	
5. Close and restart your Spotfire server.

Creating a Data Source
~~~~~~~~~~~
After creating the SQream data source template, you can create a data source.

**To create a data source:**

1. Launch the TIBCO Spotfire application.

    ::

#. From the **Tools** menu, select **Information Designer**.

   The **Information Designer** window is displayed.

    ::
	
#. From the **New** menu, click **Data Source**.

   The **Data Source** tab is displayed.

    ::
	
#. Provide the following information:

   * **Name** - define a unique name.
   
      ::
	  
   * **Type** - use the same type template name you used while configuring your template. See **Step 3** in :ref:`Creating the SQream Data Source Template<creating_sqream_data_source_template>`.
   
      ::
	  
   * **Connection URL** - use the standard JDBC connection string, ``<ip>:<port>/database``.
   
      ::
	  
   * **No of connections** - define a number between **1** and **100**. SQream recommends setting your number of connections to **100**.
   
      ::
	  
   * **Username and Password** - define your SQream username and password.   

Creating an Information Link
~~~~~~~~~~~
After creating a data source, you can create an information link.

**To create an information link**:

1. From the **Tools** menu, select **Information Designer**.

   The **Information Designer** window is displayed.

    ::

#. From the **New** menu, click **Information Link**.

   The **Information link** tab is displayed.
   
#. From the **Elements** tab, select an element and click **Add**. **Comment** - *The original doc specifically mentioned "column or filter elements". Do these need to be specifically mentioned?*

   The element you selected is displayed in the **Elements** region.
   
   Note the following:
   
   * You can select procedures from the Elements region.
   
      ::
	  
   * You can remove an element by selecting an element and clicking **Remove**.   

   .. tip:: If the Elements menu is not displayed, you can display it by clicking the **Elements** tab. You can simultaneously select multiple elements by pressing **Ctrl** and making additional selections, and select a range of elements by holding **Shift** and clicking two elements.
   
#. If the elements you select originate from more than one data source table, specify a **Join path**.

5. *Optional* - In the **Description** region, type the description of the information link.

    ::

#. *Optional* - To filter your data, expand the **Filters** section and do the following:

    1. From the **Information Link** region, select the element you added in Step 3 above.
	
	    ::
		
    2. Click **Add**.
	
       The **Add Column** window is displayed. **Comment** - *Please demonstrate.*
	   
    3. From the drop-down list, select a column to add a hard filter to and click **OK**.
	
       The selected column is added to the Filters list.
	   
    4. Repeat steps 2 and 3 to add filters to additional columns.
	
	    ::
		
    5. For each column, from the **Filter Type** drop-down list, select **range** or **values**.
	
       .. note:: Filtering by range means entering the upper and lower limits of the desired range. Filtering by values means entering the exact values that you want to include in the returned data, separated by semicolon.

    6. In the **Values** field type the desired values separated with semicolons, or set the upper and lower limits in the **Min Value** and **Max Value** fields. Alternatively, you can type ``?param_name`` in the Values field to use a parameter as the filter for the selected column, where ``param_name`` is the name used to identify the parameter. 

       .. note:: Because limits are inclusive, setting the lower limit to **1000** includes the value **1000** in the data table.
	   
       .. note:: When setting upper and lower limits on **String** type columns, ``A`` precedes ``AA``, and a lone letter precedes words beginning with that latter. For example, ``S** precedes **Smith**, indicating that the name ``Smith`` will not be present when you select names from ``D`` to ``S``. The order of characters is standard ASCII.
	   
   For more information on adding filters, see `Adding Hard Filters <https://docs.tibco.com/pub/spotfire/7.0.1/doc/html/id/id_adding_hard_filters.htm>`_.

7. *Optional* - To add runtime filtering prompts, expand the **Prompts** section and do the following:

    1. Click **Add**.
	
       The **Add Column** window is displayed.
	   
    #. From the **Select column** list, select a column to add a prompt to and click **OK**.
	
       The selected column is added to the Prompts list.
	   
    #. Repeat **Step 1** to add prompts to additional columns.
	
	    ::
		
    #. Do the following for each column:
	
       * Make a selection from the **Prompt Type** drop-down list.
       * Select or clear **Mandatory**.
       * *Optional* - Set your **Max Selections**.
	
   For more information on adding prompts, see `Adding Prompts <https://docs.tibco.com/pub/spotfire/7.0.1/doc/html/id/id_adding_prompts.htm>`_.

8. *Optional* - Expand the **Conditioning** section and specify one of the following conditions:

   * None
   * Distinct
   * Pivot

   Note that you can edit the Pivot conditioning by selecting **Pivot** and clicking **Edit**.
   
9. *Optional* - Expand the **Parameters** section and define your parameters.

     ::

10. *Optional* - Expand the **Properties** section and define your properties.

     ::

11. *Optional* - Expand the **Caching** section and enable or disable whether your information link can be cached.

     ::

12. Click **Save**.

    The **Save As** window is displayed.

13. In the tree, select where you want to save the information link.

     ::

14. In the **Name** field, type a name and description for the information link.

     ::


15. Click **Save**.

    The new information link is added to the library and can be accessed by other users.

.. tip:: You can test the information link directly by clicking **Open Data**. You can also view and edit the SQL belonging to the information link by clicking **SQL**.

For more information on the Information Link attributes, see `Information Link Tab <https://docs.tibco.com/pub/spotfire/7.0.1/doc/html/id/id_information_link_tab.htm>`_.

Troubleshooting
-------------
The **Troubleshooting** section describes the following scenarios:

.. contents::
   :local: 
   :depth: 1 

The JDBC Driver does not Support Boolean, Decimal, or Numeric Types
~~~~~~~~~~~
Attempting to establish a connection between SQream and TIBCO Spotfire using a JDBC driver is not supported, and Boolean, Decimal, or Numeric columns generate the following error:

.. code-block:: console

   Failed to execute query: Unsupported JDBC data type in query result: Bool (HRESULT: 80131500)

The error above is resolved by casting the columns as follows:

* ``Bool`` columns to ``INT``.
* ``Decimal`` and ``Numeric`` columns to ``REAL``.

For more information, see the following:

* **Resolving this error** - `Details on Change Data Types <https://docs.tibco.com/pub/sfire-analyst/10.3.2/doc/html/en-US/TIB_sfire-analyst_UsersGuide/data/data_details_on_change_data_type.htm>`_.

* **Supported data types** - :ref:`Data Types<data_types>`.

Information Services do not Support Live Queries
~~~~~~~~~~~
TIBCO Spotfire data connectors support live queries, but no APIs currently exist for creating custom data connectors. This is resolved by creating a customized SQream adapater using TIBCO's **Data Virtualization (TDV)** or the **Spotfire Advanced Services (ADS)**. These can be used from the built-in TDV connector to enable live queries.

This resolution applies to JDBC and ODBC drivers.