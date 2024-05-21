:orphan:

.. _statistics_request_abort:

************************
STATISTICS REQUEST ABORT
************************

This command aborts an :ref:`analyze_table` execution. 

More about statistics under :ref:`cost_based_optimizer`

Syntax
======

.. code-block:: postgres

	STATISTICS REQUEST ABORT [sessionId '<session_id>'] queryId '<query_id>'

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

	STATISTICS REQUEST ABORT sessionId '1ebafa4a-c843-4133-8335-54d295bdfdd0' queryId '1';

Output:

.. code-block:: none

	Aborted

Permissions
===========

The role must have the ``SUPERUSER`` permissions.