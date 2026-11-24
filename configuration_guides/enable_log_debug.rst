:orphan:

.. _enable_log_debug:

************************************************
Enabling Modification of ClientLogger Debug File
************************************************

.. note:: The ``enableLogDebug`` flag is deprecated and has no effect. Setting it does not change what is logged. The debug log level is set by :ref:`logDebugLevel<log_debug_level>`. The ``enableLogDebug`` flag will be removed in a future version, so remove it from your configuration files.

The ``enableLogDebug`` flag used to enable creating and logging in the **clientLogger_debug** file.

The following describes the ``enableLogDebug`` flag:

* **Data type** - boolean
* **Default value** - ``TRUE``