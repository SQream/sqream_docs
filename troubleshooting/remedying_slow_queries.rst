.. _remedying_slow_queries:

***********************
Remedying Slow Queries
***********************

This page describes how to troubleshoot the causes of slow queries.

Slow queries may be the result of various factors, including inefficient query practices, suboptimal table designs, or issues with system resources. If you're experiencing sluggish query performance, it's essential to diagnose and address the underlying causes promptly.

.. glossary::

	**Step 1: A single query is slow**
	
		If a query isn't performing as you expect, follow the :ref:`Query best practices<query_best_practices>` section of the :ref:`sql_best_practices` guide.
		
		If all queries are slow, continue to step 2.

	**Step 3: Check that all workers are up (web interface)**
	
		#. Check the BLUE web interface upper ribbon for inactive Workers. 
         
		#. If not all Workers are up, ask a ``clusteradmin`` to :ref:`resume suspended Workers<suspending_and_resuming_pools>`.
         
		If all workers are up, continue to step 4.

	**Step 5: Check if the session workload is balanced across all workers**

		#. Run the same query several times and check that it appears across multiple workers (use ``SELECT show_server_status()`` to monitor)
		#. If some workers have a heavier workload, check the service queue usage. Refer to the :ref:`workload_manager` guide.
         
		If the workload is balanced, continue to step 6.

	**Step 6: Check if there are long running statements**

		#. Identify any currently running statements using the :ref:`describe_session_queries` utility command. 
		#. If there are more statements than available resources, some statements may be in an ``In queue`` mode.
		#. If there is a statement that has been running for too long and is blocking the queue, consider stopping it using the :ref:`abort` utility command.
				 
		If the statement does not stop correctly, contact BLUE support at `blue_support@sqreamtech.com <blue_support@sqreamtech.com>`_.
				 
		If there are no long running statements or this does not help, continue to step 7.

	**Step 7: Check if there are active locks**

		#. Use :ref:`describe_locks` utility command to list any outstanding locks.
		#. If a statement is locking some objects, consider waiting for that statement to end or stopping it.
		#. If after a statement is completed the locks don't free up, refer to the :ref:`concurrency_and_locks` guide.
				 
		If performance does not improve after the locks are released, continue to step 8.
				 
If performance does not improve, contact BLUE support at `blue_support@sqreamtech.com <blue_support@sqreamtech.com>`_.