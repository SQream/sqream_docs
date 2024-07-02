.. _installing_monit:

****************
Installing Monit
****************

Monit is a free open source supervision utility for managing and monitoring Unix and Linux. Monit lets you view system status directly from the command line or from a native HTTP web server. Monit can be used to conduct automatic maintenance and repair, such as executing meaningful causal actions in error situations.

SQreamDB uses Monit as a watchdog utility, but you can use any other utility that provides the same or similar functionality.

The **Installing Monit** procedures describes how to install, configure, and start Monit.

You can install Monit in one of the following ways:

Getting Started
===============

Before installing SQreamDB with Monit, verify that you have followed the required :ref:`recommended pre-installation configurations <recommended_pre-installation_configurations>`. 

The procedures in the **Installing Monit** guide must be performed on each SQreamDB cluster node.

Installing Monit on RHEL:
=========================
   
1. Install Monit as a superuser:
 
    .. code-block:: console
     
       $ sudo yum install monit  
       
.. _building_monit_from_source_code:

Building Monit
==============

Building Monit from Source Code
-------------------------------

**To build Monit from source code:**

1. Copy the Monit package for the current version:
       
   .. code-block:: console
     
      $ tar zxvf monit-<x.y.z>.tar.gz
       
 The value ``x.y.z`` denotes the version numbers.
       
2. Navigate to the directory where you want to store the package:

   .. code-block:: console
     
      $ cd monit-x.y.z
 
3. Configure the files in the package:

   .. code-block:: console
     
      $ ./configure (use ./configure --help to view available options)
 
4. Build and install the package:

   .. code-block:: console
     
      $ make && make install
      
The following are the default storage directories:

* The Monit package: **/usr/local/bin/**
* The **monit.1 man-file**: **/usr/local/man/man1/**

5. **Optional** - To change the above default location(s), use the **--prefix** option to ./configure.

..
  _**Comment - I took this line directly from the external online documentation. Is the "prefix option" referrin gto the "--help" in Step 3? URL: https://mmonit.com/wiki/Monit/Installation**

6. **Optional** - Create an RPM package for RHEL directly from the source code:

   .. code-block:: console
     
      $ rpmbuild -tb monit-x.y.z.tar.gz
      

.. _building_monit_from_pre_built_binaries:   

Building Monit from Pre-Built Binaries
--------------------------------------

**To build Monit from pre-built binaries:**

1. Copy the Monit package for the current version:
       
   .. code-block:: console

      $ tar zxvf monit-x.y.z-linux-x64.tar.gz
      
   The value ``x.y.z`` denotes the version numbers.

2. Navigate to the directory where you want to store the package:

   .. code-block:: console$ cd monit-x.y.z
   
3. Copy the **bin/monit** and **/usr/local/bin/** directories:
 
    .. code-block:: console

      $ cp bin/monit /usr/local/bin/
 
4. Copy the **conf/monitrc** and **/etc/** directories:
 
    .. code-block:: console

      $ cp conf/monitrc /etc/
       
..
  _**Comment - please review this procedure.**

For examples of pre-built Monit binarties, see :ref:`Download Precompiled Binaries<https://mmonit.com/monit/#download>`.

       
Configuring Monit
=================

When the installation is complete, you can configure Monit. You configure Monit by modifying the Monit configuration file, called **monitrc**. This file contains blocks for each service that you want to monitor.

The following is an example of a service block:

    .. code-block:: console
     
       $ #SQREAM1-START
       $ check process sqream1 with pidfile /var/run/sqream1.pid
       $ start program = "/usr/bin/systemctl start sqream1"
       $ stop program = "/usr/bin/systemctl stop sqream1"
       $ #SQREAM1-END

For example, if you have 16 services, you can configure this block by copying the entire block 15 times and modifying all service names as required, as shown below:

    .. code-block:: console
     
       $ #SQREAM2-START
       $ check process sqream2 with pidfile /var/run/sqream2.pid
       $ start program = "/usr/bin/systemctl start sqream2"
       $ stop program = "/usr/bin/systemctl stop sqream2"
       $ #SQREAM2-END
       
For servers that don't run the **metadataserver** and **serverpicker** commands, you can use the block example above, but comment out the related commands, as shown below:

    .. code-block:: console
     
       $ #METADATASERVER-START
       $ #check process metadataserver with pidfile /var/run/metadataserver.pid
       $ #start program = "/usr/bin/systemctl start metadataserver"
       $ #stop program = "/usr/bin/systemctl stop metadataserver"
       $ #METADATASERVER-END

**To configure Monit:**   
   
1. Copy the required block for each required service.
2. Modify all service names in the block.
3. Copy the configured **monitrc** file to the **/etc/monit.d/** directory:

   .. code-block:: console
     
      $ cp monitrc /etc/monit.d/
       
4. Set file permissions to **600** (full read and write access):
 
    .. code-block:: console

       $ sudo chmod 600 /etc/monit.d/monitrc
       
5. Reload the system to activate the current configurations:
 
    .. code-block:: console
     
       $ sudo systemctl daemon-reload
 
6. **Optional** - Navigate to the **/etc/sqream** directory and create a symbolic link to the **monitrc** file:
 
    .. code-block:: console
     
      $ cd /etc/sqream
      $ sudo ln -s /etc/monit.d/monitrc monitrc    
         
Starting Monit
==============  

After configuring Monit, you can start it.

**To start Monit:**

1. Start Monit as a super user:

   .. code-block:: console
     
      $ sudo systemctl start monit   
 
2. View Monit's service status:

   .. code-block:: console
     
      $ sudo systemctl status monit

3. If Monit is functioning correctly, enable the Monit service to start on boot:
    
   .. code-block:: console
     
      $ sudo systemctl enable monit
