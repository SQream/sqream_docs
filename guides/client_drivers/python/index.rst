.. _pysqream:

*************************
Python (pysqream)
*************************

The SQream Python connector provides an interface for creating and running Python applications that can connect to a SQream DB database.  It provides a lighter-weight alternative to working through native C++ or Java bindings, including JDBC and ODBC drivers.

The connector is native and pure Python, with minimal requirements. It can be installed with ``pip`` on any operating system, including Linux, Windows, and macOS.

The platforms tested are Python >= 2.7.2 and Python >= 3.6, with Python 3.7 strongly recommended.

.. contents:: In this topic:
   :local:

Installing the Python connector
==================================

Prerequisites
----------------

**Python**

The connector requires Python 2.7.2 or newer, or Python 3.6 or newer. To verify your version of Python:

.. code-block:: console

   $ python --version
   Python 3.7.3
   

.. note:: If both Python 2.x and 3.x are installed, you can run ``python3`` and ``pip3`` instead of ``python`` and ``pip`` respectively for the rest of this guide

**PIP**
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

**OpenSSL for Linux**

Some distributions of Python do not include OpenSSL. The Python connector relies on OpenSSL for secure connections to SQream DB.

* To install OpenSSL on RHEL/CentOS

   .. code-block:: console
   
      $ sudo yum install -y libffi-devel openssl-devel

* To install OpenSSL on Ubuntu

   .. code-block:: console
   
      $ sudo apt-get install libssl-dev libffi-dev -y


Install via pip
-----------------

The Python connector is available via `PyPi <https://pypi.org/project/pysqream/>`_.

Install the connector with pip:

.. code-block:: console
   
   $ pip install pysqream

``pip`` will automatically installs all necessary libraries and modules.

Validate the installation
-----------------------------

Create a file called ``test.py``, containing the following:

.. literalinclude:: test.py
    :language: python
    :caption: pysqream Validation Script
    :linenos:

Make sure to replace the parameters in ``<`` ``>`` with the respective parameters for your SQream DB installation.

Run the test file to verify that you can connect to SQream DB:

.. code-block:: console
   
   $ python test.py
   PySqream version: 2.1.5
   SQream DB Protocol version: 7
   [{'bytesread': 'v2019.1.2'}]

If all went well, you are now ready to build an application using the SQream DB Python connector!

If any connection error appears, verify that you have access to a running SQream DB and that the connection parameters are correct.