.. _php:

*****************************
Connect to SQream Using PHP
*****************************

Overview
==========
PHP is an open source scripting language that executes scripts on servers. The **Connect to PHP** page explains how to connect to a SQream cluster, and describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Prerequisites
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Installing PHP
-------------------
**To install PHP:**

1. Download the JDBC driver installer from the `SQream Drivers page <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_.

    ::

2. Create a DSN.

    ::
	
3. Install the `uODBC <https://www.php.net/manual/en/intro.uodbc.php>`_ extension for your PHP installation.

Configuring PHP
-------------------
You can configure PHP in one of the following ways:
   
* When compiling, configure PHP to enable uODBC using ``./configure --with-pdo-odbc=unixODBC,/usr/local``.

   ::
   
* Install ``php-odbc`` and ``php-pdo`` along with PHP using your distribution package manager. SQream recommends a minimum of version 7.1 for the best results.
   
Launching PHP
-------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.

Operating PHP
-------------------
After configuring PHP, you can test your connection.

**To test your connection:**

#. Create a test connection file using the correct parameters for your SQream installation, as shown below:

   .. literalinclude:: test.php
      :language: php
      :emphasize-lines: 4
      :linenos:
	  
   For more information, download the sample :download:`PHP example connection file <test.php>` shown above.

   The following is an example of a valid DSN line:
      
   .. code:: php
         
      $dsn = "odbc:Driver={SqreamODBCDriver};Server=192.168.0.5;Port=5000;Database=master;User=rhendricks;Password=super_secret;Service=sqream";
      
#. Run the PHP file either directly with PHP (``php test.php``) or through a browser.

   For more information about supported DSN parameters, see :ref:`dsn_params`.

Troubleshooting PHP
-------------------------
**Comment** - The source doc doesn't include content related to this section. If so, this section will be removed.