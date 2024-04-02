.. _april_2024:

******************
April 2024
******************

``DESCRIBE SESSION QUERIES`` Enhancement
========================================

The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries. You can now list queries in multiple sessions.

Example:

.. code-block:: postgres

	DESCRIBE SESSION QUERIES STATUS IN FETCHING_RESULTS, COMPILING;

See :ref:`describe_session_queries`

