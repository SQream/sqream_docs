{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _python_modules:\
\
\
\
Python Modules (Python Scalar Functions)\
========================================\
\
SQream's Python Module functionality enables users to integrate custom Python code and functions directly into the database engine.\
\
This allows advanced data manipulation and custom machine learning operations, all GPU-accelerated.\
\
Syntax\
------\
\
.. code-block:: sql\
\
   CREATE OR REPLACE MODULE module_name\
   OPTIONS (\
       path = '/path/to/python_script.py',\
       entry_points = [\
           [\
               name = 'handler_name',\
               param_types = [sql_data_type, ...],\
               return_type = sql_data_type,\
               gpu_acceleration = \{TRUE | FALSE\}\
           ],\
           ...\
       ]\
   );\
\
Where:\
\
- `module_name`: Unique identifier\
- `path`: Absolute path to the `.py` file\
- `entry_points`: List of callable functions with input/output types\
\
Supported `sql_data_type`:\
\
- INT, BIGINT, SMALLINT\
- FLOAT, REAL, DOUBLE\
- TEXT, DATE, DATETIME, BOOLEAN\
- DECIMAL(p,s), NUMERIC(p,s)\
\
Examples\
--------\
\
**Example 1: Module with text functions**\
\
.. code-block:: sql\
\
   CREATE OR REPLACE MODULE my_module OPTIONS (\
       path = '/home/sagib/py_module.py',\
       entry_points = [\
           [ name = 'upper',\
             param_types = [text],\
             return_type = text,\
             gpu_acceleration = TRUE ],\
           [ name = 'lower',\
             param_types = [text],\
             return_type = text,\
             gpu_acceleration = FALSE ]\
       ]\
   );\
\
**Example 2: Module with arithmetic logic**\
\
Python file `/tmp/myArithmetic.py`:\
\
.. code-block:: python\
\
   import pandas as pd\
\
   def myAdd(df):\
       df['sum'] = df.iloc[:, 0] + df.iloc[:, 1]\
       return df['sum']\
\
   def mySub(df):\
       df['sub'] = df.iloc[:, 0] - df.iloc[:, 1]\
       return df['sub']\
\
Create module and run:\
\
.. code-block:: sql\
\
   CREATE OR REPLACE MODULE arith_module OPTIONS (\
       path = '/tmp/myArithmetic.py',\
       entry_points = [\
           [ name = 'myAdd', param_types = [INT, INT], return_type = INT, gpu_acceleration = TRUE ],\
           [ name = 'mySub', param_types = [INT, INT], return_type = INT, gpu_acceleration = FALSE ]\
       ]\
   );\
\
   CREATE OR REPLACE TABLE t (x INT, y INT);\
   INSERT INTO t VALUES (1,1), (2,2), (3,3), (4,2);\
\
   SELECT arith_module.myAdd(x, y) FROM t;\
   SELECT arith_module.mySub(x, y) FROM t;\
\
Configurations\
--------------\
\
**In `sqream.conf`:**\
\
.. list-table::\
   :widths: 40 20 40\
   :header-rows: 1\
\
   * - Flag\
     - Scope\
     - Default\
   * - pythonModulesGrpcPort\
     - Worker\
     - 50051\
   * - grpcGpuAllocatorPort\
     - Worker\
     - 50052\
\
**In `etc/python_service_config.json`:**\
\
.. code-block:: json\
\
   \{\
     "port": 50051,\
     "gpu_alloc_port": 50052\
   \}\
\
Logs\
----\
\
Python module logs are defined in `etc/python_service_log_properties`:\
\
.. code-block:: ini\
\
   [loggers]\
   keys=root\
\
   [handlers]\
   keys=consoleHandler,fileHandler\
\
   [formatters]\
   keys=standardFormatter\
\
   [logger_root]\
   level=DEBUG\
   handlers=consoleHandler,fileHandler\
\
   [handler_consoleHandler]\
   class=StreamHandler\
   level=INFO\
   formatter=standardFormatter\
   args=(sys.stdout,)\
\
   [handler_fileHandler]\
   class=logging.handlers.RotatingFileHandler\
   level=DEBUG\
   formatter=standardFormatter\
   args=('py_module_service.log', 'a', 1048576, 10)\
\
   [formatter_standardFormatter]\
   format=%(asctime)s.%(msecs)03d|%(levelname)s|%(message)s\
   datefmt=%Y-%m-%d %H:%M:%S\
\
Example output:\
\
.. code-block:: text\
\
   2025-04-20 20:08:49.124|INFO|ConnectionID=3|StatementID=1|Executing Python function: myAdd\
\
Usage Notes\
-----------\
\
- Python version: 3.11\
- Each Python module service runs per-worker\
- Only scalar return values (1 column) supported\
- Chunk-by-chunk execution (batch processing)\
- No control over memory within module 
\f1 \uc0\u8594 
\f0  possible OOM\
- Local paths only (no remote)\
- Cannot nest Python module calls\
- No support for array types\
\
Security\
--------\
\
- Only SUPERUSERs can create modules\
- SUPERUSER can delegate permissions:\
\
.. code-block:: sql\
\
   GRANT EXECUTE ON MODULE module_name TO role;\
}