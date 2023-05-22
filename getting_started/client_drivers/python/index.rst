.. _pysqream:

============================
Connecting BLUE Using Python
============================

The SQream Python connector is a set of packages that allows Python programs to connect to BLUE.

* ``pysqream-blue`` is a pure Python connector. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

* ``pysqream-blue-sqlalchemy`` is a SQLAlchemy dialect for ``pysqream-blue``

The connector supports Python 3.9.x. The base ``pysqream-blue`` package conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_.

**Before You Begin**

It is essential that you have Python 3.9x

Installing the Python Connector
===============================

The Python connector is installed via ``pip``, the Python package manager and installer. It is available for download via `PyPi <https://pypi.org/project/pysqream-blue/>`_. We recommend upgrading to the latest version of ``pip`` before installing.

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

.. only:: builder_html

:download:`Download <_downloads/sample.py>` or create a file named ``sample.py``, with the information from the following example.

   Verify that the parameters in the connection have been replaced with your respective BLUE installation parameters.
	
.. code-block:: python

	import pysqream_blue

	# Create a connection object
	con = pysqream_blue.connect(host=<'your-host-name.com'>, port=<port>, database=<'your_database_name'>, access_token='#########################')

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

2. Run the sample file to verify that you can connect to SQream.

A successful validation means you can go ahead and build an application using ``pysqream-blue``. 

If you receive a connection error, verify the following:

* You have access to BLUE.

* The connection parameters are correct.

SQLAlchemy Examples
===================

SQLAlchemy is an **Object-Relational Mapper (ORM) for Python. When you install the SQream dialect (``pysqream-blue-sqlalchemy``) you can use frameworks such as Pandas, TensorFlow, and Alembic to query SQream directly.

This section includes the following examples:


Standard Connection Example
---------------------------------

.. code-block:: python

	import sqlalchemy as sa

	_access_token = "##########################"
	conn_str = f"sqream_blue://blue_cluster.isqream.com:443/raviga"
	connect_args = {'access_token': _access_token}
	engine = sa.create_engine(conn_str, connect_args=connect_args)
	conn = engine.connect()

	res = conn.execute("select * from nba").fetchall()
	print(res)
	

Pulling a Table into Pandas
---------------------------

The following example shows how to pull a table in Pandas. This examples uses the URL method to create the connection string:

.. code-block:: python

	import sqlalchemy as sa
	import pandas as pd
	from sqlalchemy.engine.url import URL

	_access_token = "##########################"
	conn_str = f"sqream_blue://blue_cluster.isqream.com:443/raviga"
	connect_args = {'access_token': _access_token}
	engine = sa.create_engine(conn_str, connect_args=connect_args)
	conn = engine.connect()

	table_df = pd.read_sql("select * from nba", con=engine)
	print(table_df)

