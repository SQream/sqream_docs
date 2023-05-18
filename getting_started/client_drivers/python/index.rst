.. _pysqream:

*************************
Connecting to SQream Using Python (pysqream-blue)
*************************
The **Python** connector page describes the following:


Overview
=============
The SQream Python connector is a set of packages that allows Python programs to connect to SQream DB.

* ``pysqream-blue`` is a pure Python connector. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

* ``pysqream-blue-sqlalchemy`` is a SQLAlchemy dialect for ``pysqream-blue``

The connector supports Python 3.9.x. The base ``pysqream-blue`` package conforms to Python DB-API specifications `PEP-249 <https://www.python.org/dev/peps/pep-0249/>`_.

Installing the Python Connector
==================================

Prerequisites
----------------
Installing the Python connector includes the following prerequisites:


Python
^^^^^^^^^^^^

The connector requires Python 3.9.x To verify your version of Python:

.. code-block:: console

   $ python --version
   Python 3.9.13
   

PIP
^^^^^^^^^^^^
The Python connector is installed via ``pip``, the Python package manager and installer.

We recommend upgrading to the latest version of ``pip`` before installing. To verify that you are on the latest version, run the following command:

Installing via PIP
-----------------
The Python connector is available via `PyPi <https://pypi.org/project/pysqream-blue/>`_.

Install the connector with ``pip``:

.. code-block:: console
   
   $ pip install --upgrade pysqream-blue pysqream_blue_sqlalchemy

``pip3`` will automatically install all necessary libraries and modules.

Upgrading an Existing Installation
--------------------------------------
The Python drivers are updated periodically. To upgrade an existing pysqream-blue installation, use pip's ``-U`` flag:

.. code-block:: console
   
   $ pip3 install pysqream-blue pysqream-blue-sqlalchemy -U

Validating Your Installation
-----------------------------
This section describes how to validate your installation.

**To validate your installation**:

1. Create a file called ``sample.py``, containing the following:

.. literalinclude:: sample.py
    :language: python
    :caption: pysqream-blue Validation Script
    :linenos:

2. Verify that the parameters in the connection have been replaced with your respective SQream installation parameters.

    ::

3. Run the sample file to verify that you can connect to SQream:

   .. code-block:: console
   
      $ python sample.py
      [['Avery Bradley', 'Boston Celtics', 0, 'PG', 25, '6-2', 180, 'Texas', 7730337], ['Jae Crowder', 'Boston Celtics', 99, 'SF', 25, '6-6', 235, 'Marquette', 6796117], ['John Holland', 'Boston Celtics', 30, 'SG', 27, '6-5', 205, 'Boston University', None], ['R.J. Hunter', 'Boston Celtics', 28, 'SG', 22, '6-5', 185, 'Georgia State', 1148640], ['Jonas Jerebko', 'Boston Celtics', 8, 'PF', 29, '6-10', 231, None, 5000000]]

   If the validation was successful, you can build an application using the SQream Python connector. If you receive a connection error, verify the following:

   * You have access to a running SQream database.

      ::

   * The connection parameters are correct.

SQLAlchemy Examples
========================
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

