.. _describe_cluster_status:

*****************
DESCRIBE CLUSTER STATUS
*****************
The ``DESCRIBE CLUSTER STATUS`` command lets you display the currently running cluster resources, state, and a total line where relevant, such as total CPU and RAM.

Syntax
==========
The following is the correct syntax:

.. code-block:: postgres

   DESCRIBE CLUSTER STATUS
   
**Comment** - *The source doc had no syntax example. Can you please provide one?*

Parameters
============
The following parameters can be used when switching databases with the **DESCRIBE CLUSTER STATUS** command:

**Comment** - *Parameter table must be based on the example when provided. The following table is just a space holder.*

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Element
     - Description
   * - ``schema_name``
     - Displays the name of the schema.
   * - ``database_name``
     - Displays the name of the database.
   * - ``table``
     - Displays the name of the table.
   * - ``table type``
     - Lets you select EXTERNAL, INTERNAL, or ALL tables.
   * - ``column_name_pattern``
     - Outputs pre-defined information related to the table.
   * - ``HISTORY``
     - **Comment** - *What does HISTORY output?*
	 
Examples
==============
The following is an example of the **DESCRIBE CLUSTER STATUS** command:

.. code-block:: postgres

   EXAMPLE
   
**Comment** - *The source doc had no example. Can you please provide one?*
	 
Output
=============
Using the **DESCRIBE CLUSTER STATUS** command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Field
     - Type
     - Comments
   * - K8s ID
     - Big integer
     - K8s pod guide
   * - K8s Name
     - Text
     - K8s pod name
   * - K8s Ready
     - Text
     - K8s pod ready
   * - K8s Status
     - Text
     - K8s pod status
   * - K8s Restarts
     - Integer
     - K8s pod restarts
   * - K8s Age
     - Text
     - K8s pod age
   * - Current CPU Utilization
     - Percentage
     - K8s pod CPU utilization
   * - Current GPU Utilization
     - Percentage
     - K8s pod GPU utilization
   * - K8s RAM utilization
     - Double (mb)
     - K8s RAM utilization
   * - Current Cached RAM
     - Double (mb)
     - K8s pod cached RAM
   * - Current Fetch Data
     - Integer (KB)
     - 
   * - Current Insert Data
     - Integer (KB)
     - 
   * - Current Update Data
     - Integer (KB)
     - 
   * - Storage Utilized Space
     - Integer (GB)
     - Total line only
   * - Storage Free Space 
     - Integer (GB)
     - Total line only
   * - Temp Storage Utilized Space
     - Integer (GB)
     - Total line only
   * - Temp Storage Free Space
     - Integer (GB)
     - Total line only
   * - Metadata Storage Utilized Space
     - Integer (GB)
     - Total line only
   * - Metadata Storage Free Space
     - Integer (GB)
     - Total line only
   * - Type
     - Text
     - Same as name for most pods, for RTCs list if Query / Catalog / Streaming / Background delete **Comment** - *Need clarification*
   * - Session ID
     - Big Integer
     - The pod served by the current session. May be ``null`` when idle.
     
Examples
===========
The following is an example of the generated output:

**Comment** - *Can you please provide an example?*

Permissions
=============
**Comment** - *What are the permissions?*