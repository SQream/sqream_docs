.. _select_health_check_monitoring:

*******************************
SELECT HEALTH CHECK MONITORING
*******************************

The ``SELECT health_check_monitoring`` command allows system administrators to oversee the health of the database by monitoring the following categories:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Category
     - Description
   * - ``storage``
     - 
   * - ``metadata_stats``
     -	 
   * - ``license``
     - 
   * - ``self_healing``
     - 
	 
Syntax
==========

.. code-block:: sql

	SELECT health_check_monitoring('<category>', '<input_file>', '<export_path>')

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - State
     - Description
   * - ``category``
     - Mandatory
     - Specifies the system area for which to get health information about
   * - ``input_file``
     - Mandatory
     - The path to the specific configuration file of the *category* you wish to get information about
   * - ``export_path``
     - Mandatory
     - The path to the directory you wish to have your monitoring log file to extracted to

Storage
--------

Provides insights into cluster storage chunks and their fragmentation process. Offers an indication of irrelevant storage files in the cluster, preventing potential bottlenecks in chunk iteration during table readings in advance.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('storage', '', '')

License
--------

Provides details about the customer's license, including database storage capacity and licensing restrictions. Proactively alerts the customer before reaching license limitations, ensuring awareness and timely action.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('license', '', '')

self_healing
--------------


Supplies details on customer ETLs and loads, monitors the execution flow of queries over time, tracks the number of Workers per service, identifies idle Workers, and detects potential issues such as stuck snapshots. It is imperative to regularly monitor this data. During the Root Cause Analysis (RCA) process, it provides a clear understanding of executed operations at specific times, offering customers guidance on optimal resource allocation, particularly in terms of workers per service.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('self_healing', '', '')

Metadata Statistics
--------------------

Provides information on Worker and metadata reactivity. Regular monitoring allows for the identification of the system's performance during peak loads, indicating periods of heavy system load. This insight can be invaluable for uncovering potential concurrent issues.

Output
^^^^^^^^^

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * -
     -
   

	 
	 
Example
^^^^^^^^^

.. code-block:: sql

	SELECT health_check_monitoring('metadata_stats', '', '')

Permissions
=============

Using the ``SELECT health_check_monitoring`` command requires ``SUPERUSER`` permissions.