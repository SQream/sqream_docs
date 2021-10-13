.. _launching_sqream_with_monit:

*********************************************
Launching SQream with Monit
*********************************************
This procedure describes how to launch SQream using Monit.

Launching SQream
====================================  

After doing the following, you can launch SQream according to the instructions on this page.



1. :ref:`Installing Monit <installing_monit>`
2. :ref:`Installing SQream with Binary <installing_sqream_with_binary>`




The following is an example of a working monitrc file configured to monitor the ***metadataserver** and **serverpicker** commands, and **four sqreamd services**. The **monitrc** configuration file is located in the **conf/monitrc** directory.

Note that the **monitrc** in the following example is configured for eight ``sqreamd`` services, but that only the first four are enabled:

.. code-block:: console
     
   $ set daemon  5              # check services at 30 seconds intervals
   $ set logfile syslog
   $ 
   $ set httpd port 2812 and
   $      use address localhost  # only accept connection from localhost
   $      allow localhost        # allow localhost to connect to the server and
   $      allow admin:monit      # require user 'admin' with password 'monit'
   $  
   $  ##set mailserver smtp.gmail.com port 587
   $  ##        using tlsv12
   $  #METADATASERVER-START
   $  check process metadataserver with pidfile /var/run/metadataserver.pid
   $  start program = "/usr/bin/systemctl start metadataserver"
   $  stop program = "/usr/bin/systemctl stop metadataserver"
   $  #METADATASERVER-END
   $  #      alert user@domain.com on {nonexist, timeout}
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  metadataserver $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
   $  #SERVERPICKER-START
   $  check process serverpicker with pidfile /var/run/serverpicker.pid
   $  start program = "/usr/bin/systemctl start serverpicker"
   $  stop program = "/usr/bin/systemctl stop serverpicker"
   $  #SERVERPICKER-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #                                    with mail-format {
   $  #                                          from:     Monit@$HOST
   $  #                                          subject:  serverpicker $EVENT - $ACTION
   $  #                                         message:  This is an automate mail, sent from monit.
   $  #
   $  #
   $  #SQREAM1-START
   $  check process sqream1 with pidfile /var/run/sqream1.pid
   $  start program = "/usr/bin/systemctl start sqream1"
   $  stop program = "/usr/bin/systemctl stop sqream1"
   $  #SQREAM1-END
   $  #        alert user@domain.com on {nonexist, timeout}
   $  #               with mail-format {
   $  #                     from:     Monit@$HOST
   $  #                     subject:  sqream1 $EVENT - $ACTION
   $  #                     message:  This is an automate mail, sent from monit.
   $  #             }
   $  #SQREAM2-START
   $  check process sqream2 with pidfile /var/run/sqream2.pid
   $  start program = "/usr/bin/systemctl start sqream2"
   $  #SQREAM2-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #               with mail-format {
   $  #                     from:     Monit@$HOST
   $  #                     subject:  sqream1 $EVENT - $ACTION
   $  #                     message:  This is an automate mail, sent from monit.
   $  #             }
   $  #SQREAM3-START
   $  check process sqream3 with pidfile /var/run/sqream3.pid
   $  start program = "/usr/bin/systemctl start sqream3"
   $  stop program = "/usr/bin/systemctl stop sqream3"
   $  #SQREAM3-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #               with mail-format {
   $  #                     from:     Monit@$HOST
   $  #                     subject:  sqream2 $EVENT - $ACTION
   $  #                     message:  This is an automate mail, sent from monit.
   $  #             }
   $  #SQREAM4-START
   $  check process sqream4 with pidfile /var/run/sqream4.pid
   $  start program = "/usr/bin/systemctl start sqream4"
   $  stop program = "/usr/bin/systemctl stop sqream4"
   $  #SQREAM4-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  sqream2 $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
   $  #
   $  #SQREAM5-START
   $  #check process sqream5 with pidfile /var/run/sqream5.pid
   $  #start program = "/usr/bin/systemctl start sqream5"
   $  #stop program = "/usr/bin/systemctl stop sqream5"
   $  #SQREAM5-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  sqream2 $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
   $  #
   $  #SQREAM6-START
   $  #check process sqream6 with pidfile /var/run/sqream6.pid
   $  #start program = "/usr/bin/systemctl start sqream6"
   $  #stop program = "/usr/bin/systemctl stop sqream6"
   $  #SQREAM6-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  sqream2 $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
   $  #
   $  #SQREAM7-START
   $  #check process sqream7 with pidfile /var/run/sqream7.pid
   $  #start program = "/usr/bin/systemctl start sqream7"
   $  #stop program = "/usr/bin/systemctl stop sqream7"
   $  #SQREAM7-END
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  sqream2 $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
   $  #
   $  #SQREAM8-START
   $  #check process sqream8 with pidfile /var/run/sqream8.pid
   $  #start program = "/usr/bin/systemctl start sqream8"
   $  #stop program = "/usr/bin/systemctl stop sqream8"
   $  #SQREAM8-END
   $  #       alert user@domain.com on {nonexist, timeout}
   $  #                      with mail-format {
   $  #                            from:     Monit@$HOST
   $  #                            subject:  sqream2 $EVENT - $ACTION
   $  #                            message:  This is an automate mail, sent from monit.
   $  #                    }
     
Monit Usage Examples
====================================

This section shows examples of two methods for stopping the **sqream3** service use Monit's command syntax:



* :ref:`Stopping Monit and SQream separately <stopping_monit_and_sqream_separately>`
* :ref:`Stopping SQream using a Monit command <stopping_sqream_using_a_monit_command>`

.. _stopping_monit_and_sqream_separately: 

Stopping Monit and SQream Separately
-------------------------------------

You can stop the Monit service and SQream separately as follows:

.. code-block:: console
     
   $ sudo systemctl stop monit
   $ sudo systemctl stop sqream3

You can restart Monit as follows:

.. code-block:: console

   $ sudo systemctl start monit
      
Restarting Monit automatically restarts the SQream services. 

.. _stopping_sqream_using_a_monit_command:    

Stopping SQream Using a Monit Command
-------------------------------------

You can stop SQream using a Monit command as follows:

.. code-block:: console
     
   $ sudo monit stop sqream3

This command stops SQream only (and not Monit).

You can restart SQream as follows:

.. code-block:: console
     
   $ sudo monit start sqream3
       
Monit Command Line Options
-------------------------------------
The **Monit Command Line Options** section describes some of the most commonly used Monit command options.

You can show the command line options by running:

.. code-block:: console
     
   $ monit --help

.. code-block:: console
     
   $ start all             - Start all services
   $ start <name>          - Only start the named service
   $ stop all              - Stop all services
   $ stop <name>           - Stop the named service
   $ restart all           - Stop and start all services
   $ restart <name>        - Only restart the named service
   $ monitor all           - Enable monitoring of all services
   $ monitor <name>        - Only enable monitoring of the named service
   $ unmonitor all         - Disable monitoring of all services
   $ unmonitor <name>      - Only disable monitoring of the named service
   $ reload                - Reinitialize monit
   $ status [name]         - Print full status information for service(s)
   $ summary [name]        - Print short status information for service(s)
   $ report [up|down|..]   - Report state of services. See manual for options
   $ quit                  - Kill the monit daemon process
   $ validate              - Check all services and start if not running
   $ procmatch <pattern>   - Test process matching pattern

Using Monit While Upgrading Your Version of SQream
==================================================

While upgrading your version of SQream, you can use Monit to avoid conflicts (such as service start). This is done by pausing or stopping all running services while you manually upgrade SQream. When you finish successfully upgrading SQream, you can use Monit to restart all SQream services

**To use Monit while upgrading your version of SQream:**

1. Stop all actively running SQream services:

   .. code-block:: console
     
      $ sudo monit stop all
      
2. Verify that SQream has stopped listening on ports **500X**, **510X**, and **310X**:

   .. code-block:: console

      $ sudo netstat -nltp    #to make sure sqream stopped listening on 500X, 510X and 310X ports.

   The example below shows the old version ``sqream-db-v2020.2`` being replaced with the new version ``sqream-db-v2025.200``.

   .. code-block:: console
    
      $ cd /home/sqream
      $ mkdir tempfolder
      $ mv sqream-db-v2025.200.tar.gz tempfolder/
      $ tar -xf sqream-db-v2025.200.tar.gz
      $ sudo mv sqream /usr/local/sqream-db-v2025.200
      $ cd /usr/local
      $ sudo chown -R sqream:sqream sqream-db-v2025.200
      $ sudo rm sqream   #This only should remove symlink
      $ sudo ln -s sqream-db-v2025.200 sqream   #this will create new symlink named "sqream" pointing to new version
      $ ls -l

   The symbolic SQream link should point to the real folder:

   .. code-block:: console
    
      $ sqream -> sqream-db-v2025.200

4. Restart the SQream services:

   .. code-block:: console
    
      $ sudo monit start all
      
5. Verify that the latest version has been installed:

   .. code-block:: console
    
      $ SELECT SHOW_VERSION();
      
   The correct version is output.

6. Restart the UI:

   .. code-block:: console
    
      $ pm2 start all
