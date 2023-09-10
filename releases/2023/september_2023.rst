.. _september_2023:

******************
September 2023
******************

New Features
-------------

Resource Availability Status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Easily follow the number of Workers available for new queries at a glance with the **Resource Availability Status** located at the top of the page. 

* The status shows the number of Workers that are currently working on executed queries, out of your total Worker sum
* A green dot at the left of the bar indicates that your cluster is active with one or more Workers up and running, while a red dot indicates that your cluster is suspended
* Hovering over the status bar reveals information about your cluster, including your current cluster size, the number of Workers allocated to each of your resource pools, and which of your pools are currently active

Cluster Resize
^^^^^^^^^^^^^^

You may now easily :ref:`resize<managing_your_resources>` your BLUE cluster to be either:

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Size
     - Number of Workers
     - Capability
   * - Small
     - 1
     - Useful for experimenting and getting to know BLUE
   * - Medium
     - 4
     - Gain basic parallelism capabilities
   * - Large
     - 10
     - Gain parallelism capabilities such as concurrency, shorter query times, and the ability to adjust resource pool sizes to suit various business needs

.. hidden::

Jobs Authentication
^^^^^^^^^^^^^^^^^^^^
The BLUE :ref:`Jobs<performing_basic_blue_operations>` workflow management tool has been added an authentication layer that requires you to generate an access token and define a **Blue Jobs** connection.

.. visible::

Resolved Issues
-----------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Issue
     - Fix
   * - Different Parquet table structures provide uneven query performance  
     - Query performance is stable throughout all Parquet table structures




