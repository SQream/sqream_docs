:orphan:

.. _async_log_buffer_events:

***********************
Async Log Buffer Events
***********************

The ``asyncLogBufferEvents`` flag sets the number of log events each asynchronous log appender buffers before a write to the log file is required.

Log files are written to cluster storage, so appending to them is a write to a network filesystem. Buffering more events lets a worker ride out a slow write without waiting for it. Because the appenders block rather than discard when the buffer is full, a buffer too small for the write latency delays log events instead of losing them.

The following describes the ``asyncLogBufferEvents`` flag:

* **Data type** - int
* **Default value** - ``8192``
* **Allowed values** - Any positive integer, in log events

The buffer is created when the appender is set up at worker startup, so a change to this flag applies to workers started afterwards.
