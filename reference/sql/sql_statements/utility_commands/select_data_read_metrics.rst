.. _select_data_read_metrics:

*************************
SELECT DATA READ METRICS
*************************

The ``SELECT data_read_metrics`` utility function enables you to examine your cluster's data read during a specified time period, ensuring adherence to license limits.

The data read result is presented in this format: Year-Month-Day, showcasing data read on each specified date, along with the total data read according to your license plan. 

Syntax
==========

.. code-block:: sql

	SELECT data_read_metrics(['monthly'] | ['daily'], <'start-date'>, <'end-date'>)

Parameters
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - State
     - Description
   * - ``monthly`` or ``daily``
     - Mandatory
     - Specifies the time frame within which data was read 
   * - ``start-date``
     - Mandatory
     -  The starting date for the data retrieval period
   * - ``end-date``
     - Mandatory
     -  The ending date for the data retrieval period

Output
============

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``date``
     - Date of data read
   * - ``actual_data_read``
     - Total data read within the specified date
   * - ``data_read_limit_license_value``
     - Data read quota limit as per license plan
	 
	 
Examples
===========

Daily data reads are cumulative. For a comprehensive view of your data read usage, execute a monthly data read.
   
.. code-block:: postgres

	SELECT data_read_metrics('daily','2023-05-01', '2023-05-05');
	
Output:

.. code-block:: console

	date        | actual_data_read   | data_read_limit_license_value
	------------+--------------------+------------------------------
	2023-May-01 | 20GB               | 5000GB
	2023-May-02 | 50GB               | 5000GB
	2023-May-03 | 10GB               | 5000GB
	2023-May-04 | 5GB                | 5000GB
	2023-May-05 | 4GB                | 5000GB
	
	
Monthly data reads:

.. code-block:: postgres

	SELECT data_read_metrics('monthly','2023-05-15', '2023-06-05');
	
Output:

.. code-block:: console
	
	date        | actual_data_read   | data_read_limit_license_value
	------------+--------------------+------------------------------
	2023 May,   | 20GB               | 5000GB
	2023 June   | 50GB               | 5000GB
	
Permissions
=============

Using the ``SELECT data_read_metrics`` command requires ``SUPERUSER`` permissions.