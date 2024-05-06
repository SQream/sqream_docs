:orphan:

.. _pysqream:


********
Pysqream
********

The BLUE Python connector is a set of packages that allows Python programs to connect to BLUE.

* ``pysqream-blue`` is a pure Python connector. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

* ``pysqream-blue-sqlalchemy`` is a SQLAlchemy dialect for ``pysqream-blue``

The connector supports Python 3.9.x. The base ``pysqream-blue`` package conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_.

**Before You Begin**

It is essential that you have:

* Python 3.9x
* BLUE access token

Installing the Python Connector
===============================

The Python connector is installed via ``pip``, the Python package manager and installer. It is available for download via `pysqream-blue <https://pypi.org/project/pysqream-blue/>`_. We recommend upgrading to the latest version of ``pip`` before installing.

Upgrading ``pip``
-----------------

``pip3`` will automatically install all necessary libraries and modules.

.. code-block:: none
   
   pip install --upgrade pysqream-blue pysqream_blue_sqlalchemy

Installing ``pysqream-blue``
----------------------------

The Python drivers are updated periodically. To upgrade an existing pysqream-blue installation, use pip's ``-U`` flag:

.. code-block:: none
   
   pip3 install pysqream-blue pysqream-blue-sqlalchemy -U

Validating Your ``pysqream-blue`` Installation
----------------------------------------------

To validate your connection to BLUE, run the following Python script and make sure to replace ``host-name``, ``database``, and ``token`` with your respective BLUE parameters.
	
.. code-block:: python

	import pysqream_blue

	# Create a connection object
	con = pysqream_blue.connect(host=<'your-host-name.com'>, port=<443>, database=<'your_database_name'>, access_token=<'YourToken'>)

	# Create a new cursor
	cur = con.cursor() 
	# The select statement - in this example a CPU based query to list the defined databases in the Blue cluster
	statement = 'SELECT * FROM <table_name>'
	# Execute statement 
	cur.execute(statement)
	res = cur.fetchall()
	#Print results
	print(res)
	#Close the connection
	con.close()

Using SQLAlchemy and Pandas
===========================

SQLAlchemy is an Object-Relational Mapper (ORM) for Python. Installing the ``pysqream-blue-sqlalchemy`` BLUE dialect, enables the use of frameworks such as Pandas, TensorFlow, and Alembic to query BLUE directly.

**Before You Begin**

To use BLUE with SQLAlchemy, it is essential that you:

* Download the ``pysqream-blue-sqlalchemy`` dialect through `pysqream-blue-sqlalchemy <https://pypi.org/project/pysqream-blue-sqlalchemy/>`_
* :download:`Download <SQLAlchemy_blue_requirements.txt>` and run the dialect requirements file

SQLAlchemy
----------

SQLAlchemy simplifies working with query engines by providing a user-friendly Python interface. It offers a flexible SQL toolkit and object-relational mapper (ORM), allowing developers to write intuitive queries and switch between database engines easily.

To validate your SQLAlchemy connection to BLUE, run the following script and make sure to replace ``host-name``, ``database``, and ``token`` with your respective BLUE parameters.

.. code-block:: python

	import sqlalchemy as sa

	_access_token = <"YourToken">
	conn_str = f"sqream_blue://<your-host-name.com>:443/<your_database_name>"
	connect_args = {'access_token': _access_token}
	engine = sa.create_engine(conn_str, connect_args=connect_args)
	conn = engine.connect()

	res = conn.execute("SELECT * FROM nba").fetchall()
	print(res)

Pandas
------

Pandas is a popular Python library for efficient data manipulation, including query engine integration. Its DataFrame structure enables easy querying, filtering, and manipulation using Python syntax. By seamlessly working with query engines, Pandas provides a user-friendly experience for executing SQL queries and analyzing data.

To validate your Pandas connection to BLUE, run the following script and make sure to replace ``host-name``, ``database``, and ``token`` with your respective BLUE parameters.

.. code-block:: python

	import sqlalchemy as sa
	import pandas as pd
	from sqlalchemy.engine.url import URL

	_access_token = <"YourToken">
	conn_str = 
	
	"sqream_blue://<your-host-name.com>:443/<your_database_name>"
	connect_args = {'access_token': _access_token}
	engine = sa.create_engine(conn_str, connect_args=connect_args)
	conn = engine.connect()

	table_df = pd.read_sql("SELECT * FROM nba", engine)
	print(table_df)
	conn.close()
	engine.dispose()

Troubleshooting
===============

A successful validation means you can go ahead and build a Python application. However, if you receive a connection error, verify that:

* You have access to BLUE.

* The connection parameters are correct.
