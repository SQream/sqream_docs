.. _php:

*****************************
Connect to SQream Using PHP
*****************************

You can use PHP to interact with a SQream DB cluster.

This tutorial is a guide that will show you how to connect a PHP application to SQream DB.

.. contents:: In this topic:
   :local:

Prerequisites
===============

#. Install the :ref:`SQream DB ODBC driver for Linux<install_odbc_linux>` and create a DSN.

#. 
   Install the `uODBC <https://www.php.net/manual/en/intro.uodbc.php>`_ extension for your PHP installation.
   To configure PHP to enable uODBC, configure it with ``./configure --with-pdo-odbc=unixODBC,/usr/local`` when compiling php or install ``php-odbc`` and ``php-pdo`` along with php (version 7.1 minimum for best results) using your distribution package manager.

Testing the connection
===========================

#. 
   Create a test connection file. Be sure to use the correct parameters for your SQream DB installation.

   Download this :download:`PHP example connection file <test.php>` .

   .. literalinclude:: test.php
      :language: php
      :emphasize-lines: 4
      :linenos:

   .. tip::
      An example of a valid DSN line is:
      
      .. code:: php
         
         $dsn = "odbc:Driver={SqreamODBCDriver};Server=192.168.0.5;Port=5000;Database=master;User=rhendricks;Password=super_secret;Service=sqream";
      
      For more information about supported DSN parameters, see :ref:`dsn_params`.

#. Run the PHP file either directly with PHP (``php test.php``) or through a browser.

