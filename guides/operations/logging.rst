.. _logging:

***********************
Logging
***********************

Locating the log files
==========================

The :ref:`storage cluster<storage_cluster>` contains a ``logs`` directory. Each worker produces a log file in its own directory, which can be identified by the worker's hostname and port.

.. note:: Additional internal debug logs may reside in the main ``logs`` directory.

The worker logs contain information messages, warnings, and errors pertaining to SQream DB's operation, including:

* server start-up and shutdown
* configuration changes
* exceptions and errors
* user login events
* session events
* statement execution success / failure 
* statement execution statistics

Log structure and contents
---------------------------------

Logs contain five levels of information:

.. list-table:: Information level
   :widths: auto
   :header-rows: 1
   
   * - Level
     - Description
   * - ``SYSTEM``
     - System information like start up, shutdown, configuration change
   * - ``FATAL``
     - Fatal errors that may cause outage
   * - ``ERROR``
     - Errors encountered during statement execution
   * - ``WARNING``
     - Warnings
   * - ``INFO``
     - Information and statistics

0 SYSTEM |

1 FATAL    |

2 ERROR   |

3 WARNING |

4 INFO    
Log naming
---------------------------

Log file name syntax

``sqream_<date>_<sequence>.log``

* 
   ``date`` is formatted ``%y%m%d``, for example ``20191231`` for December 31st 2019.
   
   By default, each worker will create a new log file every day at midnight.

* ``sequence`` is the log's sequence. When a log is rotated, the sequence number increases. This starts at ``000``.

For example, ``/home/rhendricks/sqream_storage/192.168.1.91_5000``.


Logging control and maintenance
======================================

Change log destination
-------------------------

Change log verbosity
--------------------------

Change log rotation
-----------------------

Collect logs from your cluster
====================================

Troubleshooting with logs
===============================

Loading logs with external tables
---------------------------------------


some example use cases with logs


how logs are read with csvkit, find a better working solution



