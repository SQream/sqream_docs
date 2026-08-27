:orphan:

.. _spool_cleaner_backlog_warn:

**************************
Spool Cleaner Backlog Warn
**************************

The ``spoolCleanerBacklogWarn`` flag sets the number of temporary spool folders waiting for deletion above which the spool cleaner records a warning in the worker log.

One folder is queued per statement and the spool cleaner deletes them one at a time, so on cluster storage the queue can grow faster than it drains. The warning reports that state rather than letting the cleaner fall behind silently.

The following describes the ``spoolCleanerBacklogWarn`` flag:

* **Data type** - size_t
* **Default value** - ``1000``
* **Allowed values** - Any positive integer, in queued folders

The warning is recorded once when the backlog grows past the threshold, and a recovery message is recorded once the backlog falls below half of it. Lower the value to be told about a shorter backlog.
