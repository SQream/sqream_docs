.. _march_2024:

******************
March 2024
******************

Monitoring Loads
================

The **Dashboard** serves as a tool for you to monitor and promptly respond to any changes within your system. It enables you to track the health of your system and ensures that your workloads are operating as expected in near real-time.

Jobs monitoring example:

|jobs_dashboard_monitor|

See :ref:`monitoring_dashboard`

``DESCRIBE SESSION QUERIES`` Enhancement
========================================

The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries. You can now list queries in multiple sessions.

Example:

.. code-block:: postgres

	DESCRIBE SESSION QUERIES STATUS IN FETCHING_RESULTS, COMPILING;

See :ref:`describe_session_queries`

Support Access
==============

Facilitating a seamless and effortless support experience by authorizing the BLUE Support Team with Temporary Access. This proactive action will be undertaken by a cluster admin for a predetermined duration.

See :ref:`support_team_access`


.. |jobs_dashboard_monitor| image:: /_static/images/jobs_dashboard_monitor.png
   :align: middle    
   
