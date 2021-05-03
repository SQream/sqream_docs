.. _installing_monit:

*********************************************
Installing Monit
*********************************************

Overview
==============================

The **Installing Monit** procedures describes how to install, configure, and start Monit.

You can install Monit in one of the following three ways:

 * :ref:`Installing Monit using CentOS <installing-monit-using-centos>`
 * :ref:`Installing Monit using Ubuntu <installing-monit-using-ubuntu>`
 * :ref:`Installing Monit using Ubuntu offline <installing-monit-using-ubuntu-offline>`

Installing Monit Using CentOS:
------------------------------------

.. _installing-monit-using-centos:

**To install Monit using CentOS:**   
   
1. Install Monit as a superuser using CentOS:
 
    .. code-block:: console
     
       $ sudo yum install monit  
       
Installing Monit Using Ubuntu:
------------------------------------

.. _installing-monit-using-ubuntu:

**To install Monit using Ubuntu:**   
   
1. Install Monit as a superuser using Ubuntu:

    .. code-block:: console
     
       $ sudo apt-get install monit

Installing Monit Using Ubuntu Offline:
-------------------------------------

.. _installing-monit-using-ubuntu-offline:

You can install Monit using Ubuntu when you do not have an internet connection.

**To install Monit using Ubuntu offline:**   
   
1. Compress the required file:

   .. code-block:: console
     
      $ tar zxvf monit-<x.y.z>-linux-x64.tar.gz
      
   **NOTICE:** *<x.y.z>* denotes the version number.

2. Navigate to the directory where you want to save the file:
   
   .. code-block:: console
     
      $ cd monit-x.y.z
       
3. Copy the **bin/monit** directory into the **/usr/local/bin/** directory:

   .. code-block:: console
     
      $ cp bin/monit /usr/local/bin/
       
4. Copy the **conf/monitrc** directory into the **/etc/** directory:
       
   .. code-block:: console
     
      $ cp conf/monitrc /etc/
       
Configuring Monit
====================================

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

The following is an example of a working monitrc file configured to monitor the ***metadataserver** and **serverpicker** commands, and **four sqreamd services**. Note that the monitrc in the example is configured for eight sqreamd services, but that only the first four are enabled:

      .. code-block:: console
     
         $ set daemon  5              # check services at 30 seconds intervals
         $ set logfile syslog
         $ 
         $ set httpd port 2812 and
         $     use address localhost  # only accept connection from localhost
         $     allow localhost        # allow localhost to connect to the server and
         $     allow admin:monit      # require user 'admin' with password 'monit'
         $ 
         $ ##set mailserver smtp.gmail.com port 587
         $ ##        using tlsv12
         $ #METADATASERVER-START
         $ check process metadataserver with pidfile /var/run/metadataserver.pid
         $ start program = "/usr/bin/systemctl start metadataserver"
         $ stop program = "/usr/bin/systemctl stop metadataserver"
         $ #METADATASERVER-END
         $ #      alert user@domain.com on {nonexist, timeout}
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  metadataserver $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         $ #SERVERPICKER-START
         $ check process serverpicker with pidfile /var/run/serverpicker.pid
         $ start program = "/usr/bin/systemctl start serverpicker"
         $ stop program = "/usr/bin/systemctl stop serverpicker"
         $ #SERVERPICKER-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #                                    with mail-format {
         $ #                                          from:     Monit@$HOST
         $ #                                          subject:  serverpicker $EVENT - $ACTION
         $ #                                         message:  This is an automate mail, sent from monit.
         $ #
         $ #
         $ #SQREAM1-START
         $ check process sqream1 with pidfile /var/run/sqream1.pid
         $ start program = "/usr/bin/systemctl start sqream1"
         $ stop program = "/usr/bin/systemctl stop sqream1"
         $ #SQREAM1-END
         $ #        alert user@domain.com on {nonexist, timeout}
         $ #               with mail-format {
         $ #                     from:     Monit@$HOST
         $ #                     subject:  sqream1 $EVENT - $ACTION
         $ #                     message:  This is an automate mail, sent from monit.
         $ #             }
         $ #SQREAM2-START
         $ check process sqream2 with pidfile /var/run/sqream2.pid
         $ start program = "/usr/bin/systemctl start sqream2"
         $ #SQREAM2-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #               with mail-format {
         $ #                     from:     Monit@$HOST
         $ #                     subject:  sqream1 $EVENT - $ACTION
         $ #                     message:  This is an automate mail, sent from monit.
         $ #             }
         $ #SQREAM3-START
         $ check process sqream3 with pidfile /var/run/sqream3.pid
         $ start program = "/usr/bin/systemctl start sqream3"
         $ stop program = "/usr/bin/systemctl stop sqream3"
         $ #SQREAM3-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #               with mail-format {
         $ #                     from:     Monit@$HOST
         $ #                     subject:  sqream2 $EVENT - $ACTION
         $ #                     message:  This is an automate mail, sent from monit.
         $ #             }
         $ #SQREAM4-START
         $ check process sqream4 with pidfile /var/run/sqream4.pid
         $ start program = "/usr/bin/systemctl start sqream4"
         $ stop program = "/usr/bin/systemctl stop sqream4"
         $ #SQREAM4-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  sqream2 $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         $ #
         $ #SQREAM5-START
         $ #check process sqream5 with pidfile /var/run/sqream5.pid
         $ #start program = "/usr/bin/systemctl start sqream5"
         $ #stop program = "/usr/bin/systemctl stop sqream5"
         $ #SQREAM5-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  sqream2 $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         $ #
         $ #SQREAM6-START
         $ #check process sqream6 with pidfile /var/run/sqream6.pid
         $ #start program = "/usr/bin/systemctl start sqream6"
         $ #stop program = "/usr/bin/systemctl stop sqream6"
         $ #SQREAM6-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  sqream2 $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         $ #
         $ #SQREAM7-START
         $ #check process sqream7 with pidfile /var/run/sqream7.pid
         $ #start program = "/usr/bin/systemctl start sqream7"
         $ #stop program = "/usr/bin/systemctl stop sqream7"
         $ #SQREAM7-END
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  sqream2 $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         $ #
         $ #SQREAM8-START
         $ #check process sqream8 with pidfile /var/run/sqream8.pid
         $ #start program = "/usr/bin/systemctl start sqream8"
         $ #stop program = "/usr/bin/systemctl stop sqream8"
         $ #SQREAM8-END
         $ #       alert user@domain.com on {nonexist, timeout}
         $ #                      with mail-format {
         $ #                            from:     Monit@$HOST
         $ #                            subject:  sqream2 $EVENT - $ACTION
         $ #                            message:  This is an automate mail, sent from monit.
         $ #                    }
         
Starting Monit
====================================  

After configuring Monit, you can start it.

**To start Monit:**

1. If the following SQream services are running, stop them:

   .. code-block:: console
     
      $ sudo systemctl stop sqream[1-4]
      $ sudo systemctl stop serverpicker
      $ sudo systemctl stop metadataserver
      
  The services may be running because the **Launching SQream with Monit** procedure required starting them to verify that they were functioning correctly.

2. Start Monit as a super user:

   .. code-block:: console
     
      $ sudo systemctl start monit
   
3. Verify that the following SQream processes are running and listening:
  
   .. code-block:: console
     
      $ sudo systemctl status metadataserver
      $ sudo systemctl status serverpicker
      $ sudo systemctl status sqream1
      $ sudo netstat -nltp
     
  The **sudo netstate -nltp** command is used for verifying that SQream is listening on the ports.
      
  **NOTICE:** The above SQream processes are only applicable on the main server.
 
4. View Monit's service status:

   .. code-block:: console
     
      $ sudo systemctl status monit

5. If all good, enable the Monit service to start on boot:

**Comment - if what is good?**
       
   .. code-block:: console
     
      $ sudo systemctl enable monit
