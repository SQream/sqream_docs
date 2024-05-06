:orphan:

.. _dbeaver:

*******
DBeaver
*******

This page provides the necessary information for establishing a connection to BLUE from DBeaver.

Before You Begin
================

* Java 1.8 or newer
* Download the :ref:`BLUE JDBC driver<java_jdbc>`

Connection String 
=================

This section provides the database server location, authentication details, and other connection string parameters and values.

URL Template
------------

.. code-block:: java

	jdbc:Sqream://{host}:{port}/{database};accessToken={xxxxxxx}

Connection Parameters
---------------------
   
.. list-table:: 
   :widths: 3 10 4
   :header-rows: 1
   
   * - Parameter
     - Description
     - Example
   * - ``host``
     - Your BLUE host name 
     - ``sqream.isqream.com``
   * - ``port``
     - Your BLUE port number
     - ``443``
   * - ``database``
     - The BLUE database you wish to establish a connection to 
     - ``master``
   * - ``accessToken``
     - A BLUE access token
     - ``RFlFblB2WVpIQmVBalpNRE9JU2dTUFN4MHZvcFZwb1Z5Q21YaD``
	 
URL Template Example
--------------------

.. code-block:: java

	jdbc:Sqream://sqream.isqream.com:443/master;accessToken=RFlFblB2WVpIQmVBalpNRE9JU2dTUFN4MHZvcFZwb1Z5Q21YaD





