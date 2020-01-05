.. _pysqream_api_reference:

*************************
pysqream API reference
*************************

The SQream Python connector provides an interface for creating and running Python applications that can connect to a SQream DB database. It provides a lighter-weight alternative to working through native C++ or Java bindings, including JDBC and ODBC drivers.

pysqream conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_


The main module is pysqream, which contains the :py:meth:`Connection` class.

.. method:: connect(host, port, database, username, password, clustered = False, use_ssl = False, service='sqream', reconnect_attempts=3, reconnect_interval=10)
   
   Creates a new :py:meth:`Connection` object and connects to SQream DB.
   
   host
      SQream DB hostname or IP

   port
      SQream DB port 

   database
      database name

   username
      Username to use for connection

   password
      Password for ``username``

   clustered
      Connect through load balancer, or direct to worker (Default: false - direct to worker)

   use_ssl
      use SSL connection (default: false)

   service
      Optional service queue (default: 'sqream')

   reconnect_attempts
      Number of reconnection attempts to attempt before closing the connection

   reconnect_interval
      Time in seconds between each reconnection attempt

.. class:: Connection
   
   .. attribute:: arraysize
   
      Specifies the number of rows to fetch at a time with :py:meth:`~Connection.fetchmany`. Defaults to 1 - one row at a time.

   .. attribute:: rowcount
   
      Unused, always returns -1.
   
   .. attribute:: description
      
      Read-only attribute that contains result set metadata.
      
      This attribute is populated after a statement is executed.
      
      .. list-table:: 
         :widths: auto
         :header-rows: 1
         
         * - Value
           - Description
         * - ``name``
           - Column name
         * - ``type_code``
           - Internal type code
         * - ``display_size``
           - Not used - same as ``internal_size``
         * - ``internal_size``
           - Data size in bytes
         * - ``precision``
           - Precision of numeric data (not used)
         * - ``scale``
           - Scale for numeric data (not used)
         * - ``null_ok``
           - Specifies if ``NULL`` values are allowed for this column

   .. method:: execute(self, query, params=None)
      
      Execute a statement.
      
      Parameters are not supported
      
      self
         :py:meth:`Connection`

      query
         statement or query text
      
      params
         Unused
      
   .. method:: executemany(self, query, rows_or_cols=None, data_as='rows', amount=None)
      
      Prepares a statement and executes it against all parameter sequences found in ``rows_or_cols``.

      self
         :py:meth:`Connection`

      query
         INSERT statement
         
      rows_or_cols
         Data buffer to insert. This should be a sequence of lists or tuples.
      
      data_as
         (Optional) Read data as rows or columns
      
      amount
         (Optional) count of rows to insert
   
   .. method:: close(self)
      
      Close a statement and connection.
      After a statement is closed, it must be reopened by creating a new cursor.
            
      self
         :py:meth:`Connection`

   .. method:: cursor(self)
      
      Create a new :py:meth:`Connection` cursor.
      
      We recommend creating a new cursor for every statement.
      
      self
         :py:meth:`Connection`

   .. method:: fetchall(self, data_as='rows')
      
         Fetch all remaining records from the result set.
         
         An empty sequence is returned when no more rows are available.
      
      self
         :py:meth:`Connection`

      data_as
         (Optional) Read data as rows or columns

   .. method:: fetchone(self, data_as='rows')
      
      Fetch one record from the result set.
      
      An empty sequence is returned when no more rows are available.
      
      self
         :py:meth:`Connection`

      data_as
         (Optional) Read data as rows or columns


   .. method:: fetchmany(self, size=[Connection.arraysize], data_as='rows')
      
         Fetches the next several rows of a query result set.

         An empty sequence is returned when no more rows are available.

      self
         :py:meth:`Connection`

      size
         Number of records to fetch. If not set, fetches :py:obj:`Connection.arraysize` (1 by default) records

      data_as
         (Optional) Read data as rows or columns

   .. method:: __iter__()

         Makes the cursor iterable.


.. attribute:: apilevel = '2.0'
   
   String constant stating the supported API level. The connector supports API "2.0".

.. attribute:: threadsafety = 1
      
   Level of thread safety the interface supports. pysqream currently supports level 1, which states that threads can share the module, but not connections.

.. attribute:: paramstyle = 'qmark'
   
   The placeholder marker. Set to ``qmark``, which is a question mark (``?``).
