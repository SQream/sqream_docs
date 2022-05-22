.. _pysqream_api_reference:

*************************
Python API Reference
*************************
The **Python API Reference** page describes the following:

.. contents::
   :local:
   :depth: 1

Overview
===================
The SQream Python connector allows Python programs to connect to SQream, and conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_. The main Python connector module is pysqream, which contains the ``connection`` class.

**Comment** - *"Connect" or "connection"?*

The following is the syntax for the ``connect`` class:

.. code-block:: postgres
   
   $ connect(host, port, database, username, password, clustered = False, use_ssl = False, service='sqream', reconnect_attempts=3, reconnect_interval=10)
 
The ``Connection`` class creates a new ``Connection`` object and connects to SQream.

The following table describes the ``connect`` object parameters:

.. list-table::
   :widths: 15 75
   :header-rows: 1   
   
   * - Parameter
     - Description
   * - host
     - Sets the SQream hostname or IP.
   * - port
     - Sets the SQream port.
   * - database
     - Sets the database name.
   * - username
     - Sets the username for establishing a connection.
   * - password
     - Sets the password used with your ``username``.
   * - clustered
     - Connects using either the load balancer or direct to worker (Default: false - direct to worker).
   * - use_ssl
     - Uses an SSL connection (default: false).
   * - service
     - (Optional) Sets the service queue (default: 'sqream').
   * - reconnect_attempts
     - Sets the number of failed reconnection attempts to attempt before closing the connection.
   * - reconnect_interval
     - Sets the time in seconds between reconnection attempts.
	
.. _connection_object_parameters:
	
Connection Object Parameters
===================
The following table describes the ``Connection`` class parameters:

.. list-table::
   :widths: 15 117
   :header-rows: 1   
   
   * - Parameter
     - Description
   * - arraysize
     - Specifies the number of rows to fetch at a time using ``fetchmany()``. Default - ``1``.
   * - rowcount
     - Not used. Return ``-1``.
   * - description
     - Displays read-only attributes containing the following result set metadata:

       * ``name`` - Displays the column name.
       * ``type_code`` - Displays the internal type code.
       * ``display_size`` - Not used, identical to ``internal_size`` below.
       * ``internal_size`` - Displays the Data size (bytes).
       * ``precision`` - Not used. Displays the precision of numeric data.
       * ``scale`` - Not used. Displays the scale for numeric data.
       * ``null_ok`` - Specifices whether ``NULL`` values are allowed for the column.
   * - execute
     - Executes statements (self, query, params=None). Parameters are not supported.
	 
       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
       * ``query`` - Displays a statment or query text.
       * ``params`` - Not used.	 
   * - executemany
     - Prepares a statement and executes it against all parameter sequences found in ``rows_or_cols`` (self, query, rows_or_cols=None, data_as='rows', amount=None).

       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
       * ``query`` - INSERT statement.
       * ``rows_or_cols`` - Data buffer to insert. This should be a sequence of lists or tuples..
       * ``data_as`` - (Optional) Read data as rows or columns.
       * ``amount`` - (Optional) count of rows to insert.
   * - close
     - Closes a statement and connection (self). Closed statements must be reopened by creating a new cursor.

       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
   * - cursor
     - Creates a new :ref:`Connection Object Parameters<connection_object_parameters>` cursor (self). Recommended - create a new cursor for every statement.

       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
   * - fetchall
     - Fetches all remaining records from the result set (self, data_as='rows'). Returns an empty sequence if no more rows are available.
	 
       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
       * ``data_as`` - (Optional) Reads data as rows or columns.
   * - fetchone
     - Fetches one record from the result set. Returns an empty sequence if no more rows are available.

       * ``self`` - :ref:`Connection Object Parameters<connection_object_parameters>`.
       * ``size`` - Sets the number of records to fetch. If not set, fetches ``Connection.arraysize`` records (default = 1).
       * ``data_as`` - (Optional) Reads data as rows or columns.
   * - __iter__()
     - Makes the cursor iterable.
	 
API Level Object Parameters
===================
apilevel = '2.0'

**Comment** - *On the original page, the above was part of the heading. Is it redundant given the following line?*

The API Level object parameter is a string constant stating the supported API level. The Python connector supports API 2.0.

Thread Safety Object Parameters
===================
The **Thread Safety** object parameter displays the thread safety level the interface supports. The Python connector currently supports level 1, which states that threads can share the module, but not connections.
	 
Parameter Style Object Parameters
===================	 
The **paramstyle** object parameter sets the placeholder marker and is set to to ``qmark``, which is a **question mark** (``?``).