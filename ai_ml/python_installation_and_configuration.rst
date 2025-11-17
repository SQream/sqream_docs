.. _python_modules:

Python modules - Installation & Configuration
----------------------------------------

SQream's Python Module enables users to integrate custom Python code and functions directly. This allows for advanced data manipulation and custom machine learning operations, all accelerated by GPU.

* `Configurations`_
* `Logs`_
* :ref:`How to run Python module service<How_to>`
* :ref:`User notes & limitations<User_notes>`


.. _Configurations:

Configurations:
^^^^^^^^^^^^^^^

Sqream configuration:
In this version, Python module service is per Sqream worker only. It is required to set configuration change regarding communication details in Sqream config:

.. list-table::
   :header-rows: 1

   * - Config file
     - Flag name
     - Flag type
     - Default value
   * - Sqream config (not legacy)
     - pythonModulesGrpcPort
     - Worker
     - 50051
   * - Sqream config (not legacy)
     - grpcGpuAllocatorPort
     - Worker
     - 50052

Python module configuration:
Service’s configuration is located in etc/python_service_config.json:

.. code:: json

    {
         "port": 50051,
         "gpu_alloc_port": 50052
    }

.. note::
   Worker flag means it can’t be changed while the worker is up, the change will occur only after Sqream workers restart.
   Python module flags must match Sqream worker’s flags mentioned above.

.. _Logs:

Logs:
^^^^^

Python module service has a log configuration file. Logs can be either shown to screen, and also be exported to file (same as we have in Sqream’s log4cxx log configuration).
File path: ``etc/python_service_log_properties``.
File content:

.. list-table::
   :header-rows: 1

   * - Configuration file
     - Explanation
   * - ``[loggers]``
     - keys=root
   * - ``[handlers]``
     - keys=consoleHandler,fileHandler
   * - ``[formatters]``
     - keys=standardFormatter
   * - ``[logger_root]``
     - level=DEBUG, handlers=consoleHandler,fileHandler
   * - ``[handler_consoleHandler]``
     - class=StreamHandler, level=INFO, formatter=standardFormatter, args=(sys.stdout,)
   * - ``[handler_fileHandler]``
     - class=logging.handlers.RotatingFileHandler, level=DEBUG, formatter=standardFormatter, args=('py_module_service.log', 'a', 1048576, 10)
   * - ``[formatter_standardFormatter]``
     - format=%(asctime)s.%(msecs)03d|%(levelname)s|%(message)s, datefmt=%Y-%m-%d %H:%M:%S

.. note::
   ``consoleHandler`` - Responsible for logs that are been shown as console output, ``handler_consoleHandler``: Handler that supplies additional configuration for console output logs. For example:
   * Class: Handler category, in this case it will be StreamHandler.
   * Level: Required log level (Supported levels: ERROR / WARNING / INFO / DEBUG).
   * Formatter: In which format the logs will be shown.
   * args: Arguments which are required for the handler class (keep as it is in the example).

   ``fileHandler`` - Responsible for logs that are been shown as console output, ``handler_fileHandler``: Handler that supplies additional configuration for log files exportation:
   * Class: Handler category, in this case it will be RotatingFileHandler.
   * Level: Required log level (Supported levels: ERROR / WARNING / INFO / DEBUG).
   * Formatter: In which format the logs will be shown.
   * args: Arguments which are required for the handler class (keep as it is in the example). Based on the supplied example:
     * ``'py_module_service.log'`` - The location + file name of generated log file.
     * ``'a'`` - Means appending on the same file.
     * ``1048576`` - Max file size in bytes.
     * ``10`` - Keeping up to 10 log files, the rest will be deleted.

   ``formatter_standardFormatter``: Used for declaring formats for different uses:
   * ``format=%(asctime)s.%(msecs)03d|%(levelname)s|%(message)s`` - The log file that will be shown / exported.
   * ``datefmt=%Y-%m-%d %H:%M:%S`` - Used for internal usage.

Log format: ``<datetime>|<log_type>|<connection_id>|<statement_id>|<log_message>``

Log output example:
Python module logs also contain Connection & Session id information, in order to understand what was Sqream’s executed statement that triggered those logs.
Also, Python module’s logs are on Python module execution level. In case of multiple execution on the same statement it is possible to correlate between both sides.

In SQream:

.. image:: /_static/images/log_output_example.png
   :alt: SQream Console Output Example

Show node info: (Can see statement’s python execution on node id level):

.. image:: /_static/images/python_module_service_sni.png
   :alt: Python Module - Show Node Info Example


Python module logs:

.. image:: /_static/images/python_module_service_logs.png
   :alt: Python Module Logs Example

.. note::
   Logs mentioned in this example can be shown both on console / exported to log file.
   ``module_uid``: Python module execution unique identifier - contains:
   * Connection ID
   * Statement ID
   * Node ID (Execution tree identifier from show node info)

.. _How_to:

**How to install python module service**


**One-time installation**

1. Create Python3.11 virtual environment:

   .. code-block:: bash

      python3.11 -m venv my_venv
      source my_venv/bin/activate

2. Install required Python3.11 libraries and run requirements.txt installation
   (this may take a few minutes):

   .. code-block:: bash

      sudo yum install -y python3.11-devel
      pip3.11 install -r requirements.txt


**Run Python module service**

1. Activate virtual environment:

   .. code-block:: bash

      source my_venv/bin/activate

2. Run Python module service:

   .. code-block:: bash

      python3.11 py_modules.py


.. _User_notes:

User notes & limitations:
^^^^^^^^^^^^^^^^^^^^^^^

Environmental:
""""""""""""""

* Python version is limited to the SQream prerequisites compiled version, that means the user must align to the recent SQream version, and upgrading a python version, requires upgrading SQream package.
* Python code would run with default Linux privileges therefore could be potentially dangerous and need to be handled with caution.
* As mentioned above - In this version there can be a python module service per worker.

Python module syntax:
"""""""""""""""""""""

* ``Param_types`` field may be empty - for example a function that returns timestamp.
* By default, ``param_types`` and ``return_type`` are nullable, mirroring the behavior of DDL statements. To enforce non-null input or output parameters, users must explicitly specify this requirement.

Python module execution notes:
""""""""""""""""""""""""""""""

* Python module’s main purpose is for batch processing, which means, python functions will occur chunk by chunk separately. For example, for ‘max’ function (which is aggregational function), instead of getting one maximum value from all chunks, we will get the maximum per chunk.
* Chunk processing is limited to default chunk size (E.g. 1M), and cannot be customized when invoked.
* In addition to memory constraints, we have no control over RAM memory consumed within the Python module which may cause runtime errors of OOM.
* Python functions that would print to stdout would be visible only where Python module’s process is running.
* Error handling should work properly, Python errors would get raised in Sqream as runtime errors.
* Python module’s file path - Currently local paths are supported only.

Unsupported functionalities:
""""""""""""""""""""""""""""

* Nested Python module calls are not supported, functions that call other Python module functions, etc.
* Array data type - isn’t supported in this version.
* Currently will be supported only on current DB.
