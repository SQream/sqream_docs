.. _launching_sqream_with_monit:

*********************************************
Launching SQream with Monit
*********************************************
This procedure describes how to launch SQream using Monit.

Launching SQream
====================================  

After configuring Monit and verifying that SQream is running, you can launch it by doing the following:

**Comment - cross reference to Install Monit procedure**

* Installing Monit :ref:`installing_monit`

* Installing SQream with Tarbell :ref:`installing_sqream_with_tarball`



The following is an example of a working monitrc file configured to monitor the ***metadataserver** and **serverpicker** commands, and **four sqreamd services**. The **monitrc** configuration file is located in the **conf/monitrc** directory.

Note that the monitrc in the example is configured for eight sqreamd services, but that only the first four are enabled:

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
         
