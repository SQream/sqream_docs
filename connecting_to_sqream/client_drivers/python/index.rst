.. _pysqream:

*************************
Python (pysqream)
*************************
The **Python** connector page describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
=============
The SQream Python connector is a set of packages that allows Python programs to connect to SQream DB.

* ``pysqream`` is a pure Python connector. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

* ``pysqream-sqlalchemy`` is a SQLAlchemy dialect for ``pysqream``

The connector supports Python 3.6.5 and newer. The base ``pysqream`` package conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_.

Installing the Python Connector
==================================

Prerequisites
----------------
Installing the Python connector includes the following prerequisites:

.. contents:: 
   :local:
   :depth: 1

Python
^^^^^^^^^^^^

The connector requires Python 3.6.5 or newer. To verify your version of Python:

.. code-block:: console

   $ python --version
   Python 3.7.3
   

.. note:: If both Python 2.x and 3.x are installed, you can run ``python3`` and ``pip3`` instead of ``python`` and ``pip`` respectively for the rest of this guide

.. warning:: If you're running on an older version, ``pip`` will fetch an older version of ``pysqream``, with version <3.0.0. This version is currently not supported.

PIP
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

OpenSSL for Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^
Some distributions of Python do not include OpenSSL. The Python connector relies on OpenSSL for secure connections to SQream DB.

* To install OpenSSL on RHEL/CentOS

  .. code-block:: console
   
     $ sudo yum install -y libffi-devel openssl-devel

* To install OpenSSL on Ubuntu

  .. code-block:: console
   
     $ sudo apt-get install libssl-dev libffi-dev -y

Installing via PIP
-----------------
The Python connector is available via `PyPi <https://pypi.org/project/pysqream/>`_.

Install the connector with ``pip``:

.. code-block:: console
   
   $ pip install pysqream pysqream-sqlalchemy

``pip`` will automatically install all necessary libraries and modules.

Upgrading an Existing Installation
--------------------------------------
The Python drivers are updated periodically. To upgrade an existing pysqream installation, use pip's ``-U`` flag:

.. code-block:: console
   
   $ pip install pysqream pysqream-sqlalchemy -U

Validating Your Installation
-----------------------------
This section describes how to validate your installation.

**To validate your installation**:

1. Create a file called ``test.py``, containing the following:

.. literalinclude:: test.py
    :language: python
    :caption: pysqream Validation Script
    :linenos:

2. Verify that the parameters in the connection have been replaced with your respective SQream installation parameters.

    ::

3. Run the test file to verify that you can connect to SQream:

   .. code-block:: console
   
      $ python test.py
      Version: v2020.1

   If the validation was successful, you can build an application using the SQream Python connector. If you receive a connection error, verify the following:

   * You have access to a running SQream database.

      ::

   * The connection parameters are correct.

SQLAlchemy Examples
========================
SQLAlchemy is an **Object-Relational Mapper (ORM) for Python. When you install the SQream dialect (``pysqream-sqlalchemy``) you can use frameworks such as Pandas, TensorFlow, and Alembic to query SQream directly.

This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Standard Connection Example
---------------------------------
The following is a standard connection example:

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

Pulling a Table into Pandas
---------------------------------
The following example shows how to pull a table in Pandas. This examples uses the URL method to create the connection string:

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
This section includes the following examples:

.. contents:: 
   :local:
   :depth: 1

Describing Your Connection
---------------------------------------
This example shows how to describe the connection.

**Describing your connection**:

1. Import the package and create a connection:

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

2. Run a query and fetch the results:

   .. code-block:: python

      cur = con.cursor()  # Create a new cursor
      # Prepare and execute a query
      cur.execute('select show_version()')
   
      result = cur.fetchall() # `fetchall` gets the entire data set
   
      print (f"Version: {result[0][0]}")

   The SQream version should be output, such as ``v2020.1``.

3. Close the connection:

   .. code-block:: python
   
      con.close()

Using the Cursor
--------------------------------------------
The DB-API specification includes several methods for fetching results from the cursor. This sections shows an example using the ``nba`` table, which looks as follows:

.. csv-table:: nba
   :file: nba-t10.csv
   :widths: auto
   :header-rows: 1 

As before, you must import the library and create a :py:meth:`~Connection`, followed by :py:meth:`~Connection.execute` on a simple ``SELECT *`` query:

.. code-block:: python
   
   import pysqream
   con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)

   cur = con.cursor() # Create a new cursor
   # The select statement:
   statement = 'SELECT * FROM nba'
   cur.execute(statement)

When the statement has finished executing, you have a :py:meth:`Connection<cursor>` cursor object waiting. A cursor is iterable, meaning that it advances the cursor to the next row when fetched.

You can use :py:meth:`~Connection.fetchone` to fetch one record at a time:

.. code-block:: python
   
   first_row = cur.fetchone() # Fetch one row at a time (first row)
   
   second_row = cur.fetchone() # Fetch one row at a time (second row)

To fetch several rows at a time, use :py:meth:`~Connection.fetchmany`:

.. code-block:: python
   
   # executing `fetchone` twice is equivalent to this form:
   third_and_fourth_rows = cur.fetchmany(2)

To fetch all rows at once, use :py:meth:`~Connection.fetchall`:

.. code-block:: python
   
   # To get all rows at once, use `fetchall`
   remaining_rows = cur.fetchall()

   # Close the connection when done
   con.close()

The following is an example of the contents of the row variables used in our examples:

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

Reading Result Metadata
----------------------------
When you execute a statement, the connection object also contains metadata about the result set, such as **column names**, **types**, etc).

The metadata is stored in the :py:attr:`Connection.description` object of the cursor:

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

You can fetch a list of column names by iterating over the ``description`` list:
   
.. code-block:: pycon
   
   >>> [ i[0] for i in cur.description ]
   ['Name', 'Team', 'Number', 'Position', 'Age (as of 2018)', 'Height', 'Weight', 'College', 'Salary']

Loading Data into a Table
---------------------------
This example shows how to load 10,000 rows of dummy data to an instance of SQream.

**To load data 10,000 rows of dummy data to an instance of SQream:**

1. Run the following:

   .. code-block:: python
   
      import pysqream
      from datetime import date, datetime
      from time import time

      con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                         , username='rhendricks', password='Tr0ub4dor&3'
                         , clustered=True)
   
2. Create a table for loading:

   .. code-block:: python

      create = 'create or replace table perf (b bool, t tinyint, sm smallint, i int, bi bigint, f real, d double, s varchar(12), ss text, dt date, dtt datetime)'
      con.execute(create)

3. Load your data into table using the ``INSERT`` command.

    ::

4. Create dummy data matching the table you created:

   .. code-block:: python

      data = (False, 2, 12, 145, 84124234, 3.141, -4.3, "Marty McFly" , u"キウイは楽しい鳥です" , date(2019, 12, 17), datetime(1955, 11, 4, 1, 23, 0, 0))
      
      row_count = 10**4

5. Get a new cursor:

   .. code-block:: python

      cur = con.cursor()
      insert = 'insert into perf values (?,?,?,?,?,?,?,?,?,?,?)'
      start = time()
      cur.executemany(insert, [data] * row_count)
      print (f"Total insert time for {row_count} rows: {time() - start} seconds")

6. Close this cursor:

   .. code-block:: python

      cur.close()
   
7. Verify that the data was inserted correctly.

    ::

8. Get a new cursor:

   .. code-block:: python

      cur = con.cursor()
      cur.execute('select count(*) from perf')
      result = cur.fetchall() # `fetchall` collects the entire data set
      print (f"Count of inserted rows: {result[0][0]}")

9. Close the cursor:

   .. code-block:: python

       cur.close()
   
10. Close the connection:

   .. code-block:: python

      con.close()

Reading Data from a CSV File for Loading into a Table
----------------------------------------------------------
This example shows how to write a helper function to create an :ref:`insert` statement, by reading an existing table's metadata.

**To read data from a CSV file for loading into a table:**

1. Run the following:

   .. code-block:: python
   
      import pysqream
      import datetime

      def insert_from_csv(cur, table_name, csv_filename, field_delimiter = ',', null_markers = []):
         """
2. Ask SQream for some table information.

   This is important for determining the number of columns, and helps create a matching ``INSERT`` statement:
   
   .. code-block:: python
   
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

3. Create enough placeholders (`?`) for the ``INSERT`` query string:


   .. code-block:: python

      qstring = ','.join(['?'] * len(column_info))
      insert_statement = f"insert into {table_name} values ({qstring})"

4. Open the CSV file:

   .. code-block:: python

      with open(csv_filename, mode='r') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=field_delimiter)

5. Execute the ``INSERT`` statement with the CSV data:

   .. code-block:: python

      cur.executemany(insert_statement, [row for row in csv_reader])


      con = pysqream.connect(host='127.0.0.1', port=3108, database='master'
                      , username='rhendricks', password='Tr0ub4dor&3'
                      , clustered=True)
   
      cur = con.cursor()
      insert_from_csv(cur, 'nba', 'nba.csv', field_delimiter = ',', null_markers = [])
   
      con.close()

Using SQLAlchemy ORM to Create and Populate Tables
-----------------------------------------------------------------------
This section shows how to use the ORM to create and populate tables from Python objects.

**To use SQLAlchemy ORM to create and populate tables:**

1. Run the following:

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
   
2. Build a metadata object and bind it:

   .. code-block:: python
   
      metadata = sa.MetaData()
      metadata.bind = engine
   
3. Create a table in the local metadata:
   
   .. code-block:: python
   
      employees = sa.Table(
      'employees'
      , metadata 
      , sa.Column('id', sa.Integer)
      , sa.Column('name', sa.VARCHAR(32))
      , sa.Column('lastname', sa.VARCHAR(32))
      , sa.Column('salary', sa.Float)
      )

   The ``create_all()`` function uses the SQream engine object.

4. Create all the defined table objects:

   .. code-block:: python

      metadata.create_all(engine)
   
5. Populate your table.

    ::
   
6. Build the data rows:

   .. code-block:: python

      insert_data = [ {'id': 1, 'name': 'Richard','lastname': 'Hendricks',   'salary': 12000.75}
                     ,{'id': 3,  'name': 'Bertram', 'lastname': 'Gilfoyle', 'salary': 8400.0}
                     ,{'id': 8,  'name': 'Donald', 'lastname': 'Dunn', 'salary': 6500.40}
                    ]

7. Build the ``INSERT`` command:
   
   .. code-block:: python

      ins = employees.insert(insert_data)
   
8. Execute the command:

   .. code-block:: python

      result = engine.execute(ins)

For more information, see the :ref:`python_api_reference_guide`.
