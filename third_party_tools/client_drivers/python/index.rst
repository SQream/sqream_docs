.. _pysqream:

*************************
Python (pysqream)
*************************

The SQream Python connector is a set of packages that allows Python programs to connect to SQream DB.

* ``pysqream`` is a pure Python connector. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

* ``pysqream-sqlalchemy`` is a SQLAlchemy dialect for ``pysqream``

The connector supports Python 3.6.5 and newer.

The base ``pysqream`` package conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_.

.. contents:: In this topic:
   :local:

Installing the Python connector
==================================

Prerequisites
----------------

1. Python
^^^^^^^^^^^^

The connector requires Python 3.6.5 or newer. To verify your version of Python:

.. code-block:: console

   $ python --version
   Python 3.7.3
   

.. note:: If both Python 2.x and 3.x are installed, you can run ``python3`` and ``pip3`` instead of ``python`` and ``pip`` respectively for the rest of this guide

.. warning:: If you're running on an older version, ``pip`` will fetch an older version of ``pysqream``, with version <3.0.0. This version is currently not supported.

2. PIP
^^^^^^^^^^^^
The Python connector is installed via ``pip``, the Python package manager and installer.

We recommend upgrading to the latest version of ``pip`` before installing. To verify that you are on the latest version, run the following command:

.. code-block:: console

   $ python -m pip install --upgrade pip
   Collecting pip
      Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
        |████████████████████████████████| 1.4MB 1.6MB/s
   Installing collected packages: pip
     Found existing installation: pip 19.1.1
       Uninstalling pip-19.1.1:
         Successfully uninstalled pip-19.1.1
   Successfully installed pip-19.3.1

.. note:: 
   * On macOS, you may want to use virtualenv to install Python and the connector, to ensure compatibility with the built-in Python environment
   *  If you encounter an error including ``SSLError`` or ``WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.`` - please be sure to reinstall Python with SSL enabled, or use virtualenv or Anaconda.

3. OpenSSL for Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^

Some distributions of Python do not include OpenSSL. The Python connector relies on OpenSSL for secure connections to SQream DB.

* To install OpenSSL on RHEL/CentOS

   .. code-block:: console
   
      $ sudo yum install -y libffi-devel openssl-devel

* To install OpenSSL on Ubuntu

   .. code-block:: console
   
      $ sudo apt-get install libssl-dev libffi-dev -y

4. Cython (optional)
^^^^^^^^^^^^^^^^^^^^^^^^

Optional but highly recommended is Cython, which improves performance of Python applications.

   .. code-block:: console
   
      $ pip install cython

Install via pip
-----------------

The Python connector is available via `PyPi <https://pypi.org/project/pysqream/>`_.

Install the connector with ``pip``:

.. code-block:: console
   
   $ pip install pysqream pysqream-sqlalchemy

``pip`` will automatically install all necessary libraries and modules.

Upgrading an existing installation
--------------------------------------

The Python drivers are updated periodically.
To upgrade an existing pysqream installation, use pip's ``-U`` flag.

.. code-block:: console
   
   $ pip install pysqream pysqream-sqlalchemy -U


Validate the installation
-----------------------------

Create a file called ``test.py``, containing the following:

.. literalinclude:: test.py
    :language: python
    :caption: pysqream Validation Script
    :linenos:

Make sure to replace the parameters in the connection with the respective parameters for your SQream DB installation.

Run the test file to verify that you can connect to SQream DB:

.. code-block:: console
   
   $ python test.py
   Version: v2020.1

If all went well, you are now ready to build an application using the SQream DB Python connector!

If any connection error appears, verify that you have access to a running SQream DB and that the connection parameters are correct.

SQLAlchemy examples
========================

SQLAlchemy is an ORM for Python.

When you install the SQream DB dialect (``pysqream-sqlalchemy``) you can use frameworks like Pandas, TensorFlow, and Alembic to query SQream DB directly.

A simple connection example
---------------------------------

.. code-block:: python

   import sqlalchemy as sa
   from sqlalchemy.engine.url import URL

   engine_url = URL('sqream'
                 , username='rhendricks'
                 , password='secret_passwor"
                 , host='localhost'
                 , port=5000
                 , database='raviga'
                 , query={'use_ssl': False})

   engine = sa.create_engine(engine_url)

   res = engine.execute('create table test (ints int)')
   res = engine.execute('insert into test values (5), (6)')
   res = engine.execute('select * from test')

Pulling a table into Pandas
---------------------------------

In this example, we use the URL method to create the connection string.

.. code-block:: python

   import sqlalchemy as sa
   import pandas as pd
   from sqlalchemy.engine.url import URL


   engine_url = URL('sqream'
                 , username='rhendricks'
                 , password='secret_passwor"
                 , host='localhost'
                 , port=5000
                 , database='raviga'
                 , query={'use_ssl': False})

   engine = sa.create_engine(engine_url)
   
   table_df = pd.read_sql("select * from nba", con=engine)


API Examples
===============

Explaining the connection example
---------------------------------------

First, import the package and create a connection

.. code-block:: python
   
   # Import pysqream package
   
   import pysqream

   """
   Connection parameters include:
   * IP/Hostname
   * Port
   * database name
   * username
   * password 
   * Connect through load balancer, or direct to worker (Default: false - direct to worker)
   * use SSL connection (default: false)
   * Optional service queue (default: 'sqream')
   """
   
   # Create a connection object
   
   con = pysqream.connect(host='127.0.0.1', port=3108, database='raviga'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)

Then, run a query and fetch the results

.. code-block:: python

   cur = con.cursor()  # Create a new cursor
   # Prepare and execute a query
   cur.execute('select show_version()')
   
   result = cur.fetchall() # `fetchall` gets the entire data set
   
   print (f"Version: {result[0][0]}")

This should print the SQream DB version. For example ``v2020.1``.

Finally, we will close the connection

.. code-block:: python
   
   con.close()

Using the cursor
--------------------------------------------

The DB-API specification includes several methods for fetching results from the cursor.

We will use the ``nba`` example. Here's a peek at the table contents:

.. csv-table:: nba
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

Like before, we will import the library and create a :py:meth:`~Connection`, followed by :py:meth:`~Connection.execute` on a simple ``SELECT *`` query.

.. code-block:: python
   
   import pysqream
   con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)

   cur = con.cursor() # Create a new cursor
   # The select statement:
   statement = 'SELECT * FROM nba'
   cur.execute(statement)

After executing the statement, we have a :py:meth:`Connection<cursor>` cursor object waiting. A cursor is iterable, meaning that everytime we fetch, it advances the cursor to the next row.

Use :py:meth:`~Connection.fetchone` to get one record at a time:

.. code-block:: python
   
   first_row = cur.fetchone() # Fetch one row at a time (first row)
   
   second_row = cur.fetchone() # Fetch one row at a time (second row)

To get several rows at a time, use :py:meth:`~Connection.fetchmany`:

.. code-block:: python
   
   # executing `fetchone` twice is equivalent to this form:
   third_and_fourth_rows = cur.fetchmany(2)

To get all rows at once, use :py:meth:`~Connection.fetchall`:

.. code-block:: python
   
   # To get all rows at once, use `fetchall`
   remaining_rows = cur.fetchall()

   # Close the connection when done
   con.close()

Here are the contents of the row variables we used:

.. code-block:: pycon
   
   >>> print(first_row)
   ('Avery Bradley', 'Boston Celtics', 0, 'PG', 25, '6-2', 180, 'Texas', 7730337)
   >>> print(second_row)
   ('Jae Crowder', 'Boston Celtics', 99, 'SF', 25, '6-6', 235, 'Marquette', 6796117)
   >>> print(third_and_fourth_rows)
   [('John Holland', 'Boston Celtics', 30, 'SG', 27, '6-5', 205, 'Boston University', None), ('R.J. Hunter', 'Boston Celtics', 28, 'SG', 22, '6-5', 185, 'Georgia State', 1148640)]
   >>> print(remaining_rows)
   [('Jonas Jerebko', 'Boston Celtics', 8, 'PF', 29, '6-10', 231, None, 5000000), ('Amir Johnson', 'Boston Celtics', 90, 'PF', 29, '6-9', 240, None, 12000000), ('Jordan Mickey', 'Boston Celtics', 55, 'PF', 21, '6-8', 235, 'LSU', 1170960), ('Kelly Olynyk', 'Boston Celtics', 41, 'C', 25, '7-0', 238, 'Gonzaga', 2165160),
   [...]

.. note:: Calling a fetch command after all rows have been fetched will return an empty array (``[]``).

Reading result metadata
----------------------------

When executing a statement, the connection object also contains metadata about the result set (e.g.column names, types, etc).

The metadata is stored in the :py:attr:`Connection.description` object of the cursor.

.. code-block:: pycon
   
   >>> import pysqream
   >>> con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
   ...                , username='rhendricks', password='Tr0ub4dor&3'
   ...                , clustered=True)
   >>> cur = con.cursor()
   >>> statement = 'SELECT * FROM nba'
   >>> cur.execute(statement)
   <pysqream.dbapi.Connection object at 0x000002EA952139B0>
   >>> print(cur.description)
   [('Name', 'STRING', 24, 24, None, None, True), ('Team', 'STRING', 22, 22, None, None, True), ('Number', 'NUMBER', 1, 1, None, None, True), ('Position', 'STRING', 2, 2, None, None, True), ('Age (as of 2018)', 'NUMBER', 1, 1, None, None, True), ('Height', 'STRING', 4, 4, None, None, True), ('Weight', 'NUMBER', 2, 2, None, None, True), ('College', 'STRING', 21, 21, None, None, True), ('Salary', 'NUMBER', 4, 4, None, None, True)]

To get a list of column names, iterate over the ``description`` list:
   
.. code-block:: pycon
   
   >>> [ i[0] for i in cur.description ]
   ['Name', 'Team', 'Number', 'Position', 'Age (as of 2018)', 'Height', 'Weight', 'College', 'Salary']

Loading data into a table
---------------------------

This example loads 10,000 rows of dummy data to a SQream DB instance

.. code-block:: python
   
   import pysqream
   from datetime import date, datetime
   from time import time

   con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)
   
   # Create a table for loading
   create = 'create or replace table perf (b bool, t tinyint, sm smallint, i int, bi bigint, f real, d double, s varchar(12), ss text, dt date, dtt datetime)'
   con.execute(create)

   # After creating the table, we can load data into it with the INSERT command

   # Create dummy data which matches the table we created
   data = (False, 2, 12, 145, 84124234, 3.141, -4.3, "Marty McFly" , u"キウイは楽しい鳥です" , date(2019, 12, 17), datetime(1955, 11, 4, 1, 23, 0, 0))
   
   
   row_count = 10**4

   # Get a new cursor
   cur = con.cursor()
   insert = 'insert into perf values (?,?,?,?,?,?,?,?,?,?,?)'
   start = time()
   cur.executemany(insert, [data] * row_count)
   print (f"Total insert time for {row_count} rows: {time() - start} seconds")

   # Close this cursor
   cur.close()
   
   # Verify that the data was inserted correctly
   # Get a new cursor
   cur = con.cursor()
   cur.execute('select count(*) from perf')
   result = cur.fetchall() # `fetchall` collects the entire data set
   print (f"Count of inserted rows: {result[0][0]}")

   # When done, close the cursor
   cur.close()
   
   # Close the connection
   con.close()

Reading data from a CSV file for load into a table
----------------------------------------------------------

We will write a helper function to create an :ref:`insert` statement, by reading an existing table's metadata.

.. code-block:: python
   
   import pysqream
   import datetime

   def insert_from_csv(cur, table_name, csv_filename, field_delimiter = ',', null_markers = []):
      """
      We will first ask SQream DB for some table information.
      This is important for understanding the number of columns, and will help
      to create a matching INSERT statement
      """

      column_info = cur.execute(f"SELECT * FROM {table_name} LIMIT 0").description


      def parse_datetime(v):
         try:
               return datetime.datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S.%f')
         except ValueError:
               try:
                  return datetime.datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S')
               except ValueError:
                  return datetime.datetime.strptime(row[i], '%Y-%m-%d')

      # Create enough placeholders (`?`) for the INSERT query string
      qstring = ','.join(['?'] * len(column_info))
      insert_statement = f"insert into {table_name} values ({qstring})"

      # Open the CSV file
      with open(csv_filename, mode='r') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=field_delimiter)

      # Execute the INSERT statement with the CSV data
      cur.executemany(insert_statement, [row for row in csv_reader])


   con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)
   
   cur = con.cursor()
   insert_from_csv(cur, 'nba', 'nba.csv', field_delimiter = ',', null_markers = [])
   
   con.close()


Using SQLAlchemy ORM to create tables and fill them with data
-----------------------------------------------------------------------

You can also use the ORM to create tables and insert data to them from Python objects.

For example:

.. code-block:: python
   
   import sqlalchemy as sa
   import pandas as pd
   from sqlalchemy.engine.url import URL


   engine_url = URL('sqream'
                 , username='rhendricks'
                 , password='secret_passwor"
                 , host='localhost'
                 , port=5000
                 , database='raviga'
                 , query={'use_ssl': False})

   engine = sa.create_engine(engine_url)
   
   # Build a metadata object and bind it
   
   metadata = sa.MetaData()
   metadata.bind = engine
   
   # Create a table in the local metadata
   
   employees = sa.Table(
   'employees'
   , metadata 
   , sa.Column('id', sa.Integer)
   , sa.Column('name', sa.VARCHAR(32))
   , sa.Column('lastname', sa.VARCHAR(32))
   , sa.Column('salary', sa.Float)
   )

   # The create_all() function uses the SQream DB engine object
   # to create all the defined table objects.

   metadata.create_all(engine)
   
   # Now that the table exists, we can insert data into it.
   
   # Build the data rows
   insert_data = [ {'id': 1, 'name': 'Richard','lastname': 'Hendricks',   'salary': 12000.75}
                  ,{'id': 3,  'name': 'Bertram', 'lastname': 'Gilfoyle', 'salary': 8400.0}
                  ,{'id': 8,  'name': 'Donald', 'lastname': 'Dunn', 'salary': 6500.40}
                 ]

   # Build the insert command
   ins = employees.insert(insert_data)
   
   # Execute the command
   result = engine.execute(ins)

.. toctree::
   :maxdepth: 8
   :caption: Further information
   
   api-reference
