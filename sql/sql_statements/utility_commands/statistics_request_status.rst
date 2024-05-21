:orphan:

.. _statistics_request_status:

*************************
STATISTICS REQUEST STATUS
*************************

This command returns information about your statistics collection request, including whether or not the collection is completed.

Syntax
======

.. code-block:: postgres

	STATISTICS REQUEST STATUS [sessionId '<session_id>'] queryId '<query_id>'

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1

   * - Parameter
     - Description
     - Parameter Type
   * - ``session_id``
     - :ref:`String literal<literals>`
     - Specifies the session ID
   * - ``query_id``
     - :ref:`String literal<literals>`
     - Specifies the query ID

Examples
========

.. code-block:: postgres

	STATISTICS REQUEST STATUS queryId '1';

Output:

.. code-block:: none

	session_id                          |query_id|submission_time        |start_execution_time   |termination_time|status   |current_column|total_num_columns|error_message|
	------------------------------------+--------+-----------------------+-----------------------+----------------+---------+--------------+-----------------+-------------+
	1ebafa4a-c843-4133-8335-54d295bdfdd0|1       |2024-05-21 10:02:30.249|2024-05-21 10:02:30.249|                |EXECUTING|3             |4                |             |

Permissions
===========

The role must have the ``SUPERUSER`` permissions.