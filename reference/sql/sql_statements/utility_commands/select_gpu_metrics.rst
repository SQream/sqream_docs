.. _select_gpu_metrics:

*************************
SELECT GPU METRICS
*************************

The ``SELECT gpu_metrics`` utility function allows you to check your cluster's GPU usage within a specific time frame. This is useful to ensure that GPU usage stays within the allowed license limits.

An empty result indicates no usage deviation during the specified time. If the GPU usage exceeds the quota, the result will show the highest deviation in this format: Year-Month-Day, GPU deviated usage, and GPU quota limit as per your license plan. 

Syntax
==========

.. code-block:: postgres

	SELECT gpu_metrics(['monthly'] | ['daily'], <'start-date'>, <'end-date'>)

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

Examples
===========

Daily GPU usage:
   
.. code-block:: console

	master=> SELECT gpu_metrics('daily','2023-05-01', '2023-05-05);
	2023-May-01, 2,1
	2023-May-02, 3,1
	2023-May-03, 3,1
	2 rows
	time: 0.103436s

Monthly GPU usage:

.. code-block:: console

	master=> SELECT gpu_metrics('monthly', '2023-04-01', '2023-06-05');
	2023 Apr, 2,1
	1 rows
	time: 0.155396s
   


Permissions
=============

Using the ``SELECT gpu_metrics`` command requires ``SUPERUSER`` permissions.