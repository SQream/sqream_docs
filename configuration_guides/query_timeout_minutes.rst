:orphan:

.. _query_timeout_minutes:

**************************************************
Query Timeout Minutes
**************************************************

The ``QueryTimeoutMinutes`` session flag is designed to identify queries that have exceeded a specified time limit. Once the flag value is reached, the query automatically stops.

* **Data type** - integer
* **Default value** - ``0`` (no query timeout)
* **Allowed values** - 1—4320 (1 minute up to 72 hours)