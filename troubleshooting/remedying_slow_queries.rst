.. _remedying_slow_queries:

***********************
Remedying Slow Queries
***********************

The **Remedying Slow Queries** page describes how to troubleshoot the causes of slow queries.

The following table is a checklist you can use to identify the cause of your slow queries:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Step
     - Description
     - Results
   * - 1
     - A single query is slow
     - 
         If a query isn't performing as you expect, follow the :ref:`Query best practices<query_best_practices>` part of the :ref:`sql_best_practices` guide.
         
         If all queries are slow, continue to step 2.
   * - 2
     - All queries on a specific table are slow
     - 
         #. If all queries on a specific table aren't performing as you expect, follow the :ref:`Table design best practices<table_design_best_practices>` part of the :ref:`sql_best_practices` guide.
         #. Check for active delete predicates in the table. Consult the :ref:`delete_guide` guide for more information.
         
         If the problem spans all tables, continue to step 3.
   * - 3
     - Check that all workers are up
     - 
         Use ``SELECT show_cluster_nodes();`` to list the active cluster workers.
         
         If the worker list is incomplete, locate and start the missing worker(s).
         
         If all workers are up, continue to step 4.
   * - 4
     - Check that all workers are performing well
     - 
         #. Identify if a specific worker is slower than others by running the same query on different workers. (e.g. by connecting directly to the worker or through a service queue)
         #. If a specific worker is slower than others, investigate performance issues on the host using standard monitoring tools (e.g. ``top``).
         #. Restart SQream DB workers on the problematic host.
         
         If all workers are performing well, continue to step 5.
   * - 5 
     - Check if the workload is balanced across all workers
     - 
         #. Run the same query several times and check that it appears across multiple workers (use ``SELECT show_server_status()`` to monitor)
         #. If some workers have a heavier workload, check the service queue usage. Refer to the :ref:`workload_manager` guide.
         
         If the workload is balanced, continue to step 6.
   * - 6
     - Check if there are long running statements
     - 
         #. Identify any currently running statements (use ``SELECT show_server_status()`` to monitor)
         #. If there are more statements than available resources, some statements may be in an ``In queue`` mode.
         #. If there is a statement that has been running for too long and is blocking the queue, consider stopping it (use ``SELECT stop_statement(<statement id>)``).
         
         If the statement does not stop correctly, contact `SQream Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.
         
         If there are no long running statements or this does not help, continue to step 7.
   * - 7
     - Check if there are active locks
     - 
         #. Use ``SELECT show_locks()`` to list any outstanding locks.
         #. If a statement is locking some objects, consider waiting for that statement to end or stop it.
         #. If after a statement is completed the locks don't free up, refer to the :ref:`concurrency_and_locks` guide.
         
         If performance does not improve after the locks are released, continue to step 8.
   * - 8
     - Check free memory across hosts
     - 
         #. Check free memory across the hosts by running ``$ free -th`` from the terminal.
         #. If the machine has less than 5% free memory, consider **lowering** the ``limitQueryMemoryGB`` and ``spoolMemoryGB`` settings. Refer to the :ref:`spooling` guide.
         #. If the machine has a lot of free memory, consider **increasing** the ``limitQueryMemoryGB`` and ``spoolMemoryGB`` settings.
         
         If performance does not improve, contact `SQream Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.