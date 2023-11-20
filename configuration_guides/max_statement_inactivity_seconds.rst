.. _max_statement_inactivity_seconds:

********************************
MAX STATEMENT INACTIVITY SECONDS
********************************

The ``maxStatementInactivitySeconds`` parameter is optional and determines the maximum duration of statement inactivity before terminating the Worker. Its behavior is contingent on the configuration of ``healerActionGracefulShutdown``. If set to ``true``, it triggers a graceful Worker shutdown; if set to ``false``, the Worker continues without shutting down, accompanied by relevant log information regarding the stuck query. 

* **Data type** - size_t
* **Default value** - ``5*60*60 seconds (18000)``
* **Allowed values** - ``1-4000000000``

