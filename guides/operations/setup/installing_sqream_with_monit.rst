.. _installing_sqream_with_monit:

*********************************************
Installing SQream with Monit
*********************************************
Monit is an Open Source utility for managing and monitoring Unix systems and conducting automatic maintenance and repair. For example, it can be used for executing meaningful causal actions in error situations, such as starting processes that are not running.

This procedure describes how to manually install SQream with Monit using the **systemd** initialization system.

Before Installing SQream with Monit
====================================
Before installing SQream with Monit verify that you have already followed the required Recommended Configuration procedures. **Note to self - make xref here.**

Installing SQream with Monit
====================================
**To install SQream with Monit:**

1. Copy the SQream package to the **/home/sqream** directory:

   .. code-block:: console
   
      $ tar -xf sqream-db-v2020.2.tar.gz

2. Append the version number to the name of the SQream folder. The version number in the following example is **v2020.2**:

   **Comment - Jake Wheat: can we have the release (and code drop) tarballs built with these paths instead of just ‘sqream/’?**
 
   **Comment - Slavi: I believe we can, but it will require Makefile change.I’ll check.**

   .. code-block:: console
   
      $ mv sqream sqream-db-v2020.2

3. Move the new version of the SQream folder to the **/usr/local/** directory:

   .. code-block:: console
   
      $ sudo mv sqream-db-v2020.2 /usr/local/
      
4. Change the ownership of the folder to **sqream folder**:

   .. code-block:: console
   
      $ sudo chown -R sqream:sqream  /usr/local/sqream-db-v2020.2

5. Navigate to the **/usr/local/** directory and create a symbolic link to SQream:

   .. code-block:: console
   
      $ cd /usr/local
      $ sudo ln -s sqream-db-v2020.2 sqream
      
6. Verify that the symbolic link that you created points to the folder that you created:

   .. code-block:: console
   
      $ ls -l
      
7. Verify that the symbolic link that you created points to the folder that you created:

   .. code-block:: console
   
      $ sqream -> sqream-db-v2020.2
      
8. Create the SQream configuration file destination folders and set their ownership to **sqream**:

   .. code-block:: console
   
      $ sudo mkdir /etc/sqream
      $ sudo chown -R sqream:sqream /etc/sqream
      
9. Create the SQream service log destination folders and set their ownership to **sqream**:

   .. code-block:: console
   
      $ sudo mkdir /var/log/sqream
      $ sudo chown -R sqream:sqream /var/log/sqream

10. Navigate to the **/usr/local/** directory and copy the SQream configuration files from them:

   .. code-block:: console
   
      $ cd /usr/local/sqream/etc/
      $ cp * /etc/sqream
      
The configuration files are **service configuration files**, and the JSON files are **SQream configuration files**, for a total of four files. The number of SQream configuration files and JSON files must be identical.
      
**NOTICE** - Verify that the JSON files have been configured correctly and that all required flags have been set to the correct values.

In each JSON file, the following parameters **must be updated**:

* instanceId
* machineIP
* metadataServerIp
* spoolMemoryGB
* limitQueryMemoryGB
* gpu
* port
* ssl_port

Note the following:

* The value of the **metadataServerIp** parameter must point to the IP that the metadata is running on.
* The value of the **machineIP** parameter must point to the IP of your local machine.

It **(comment** - what is *it*?) would be same on server running metadataserver and different on other server nodes.

11. **Optional** - To run additional SQream services, copy the required configuration files and create additional JSON files: **Comment: verify step**

   .. code-block:: console
   
      $ cp sqream2_config.json sqream3_config.json
      $ vim sqream3_config.json
      
**NOTICE:** A unique **instanceID** must be used in each JSON file. IN the example above, the instanceID **sqream_02** is changed to **sqream_03**.

**Comment: The note says sqream_02, but the example says sqream_2, i.e., without the 0. Which is the correct one?**

**Comment: Also, what happens if a non-unique instance ID is used? Depending on the answer, the NOTICE above may have to be a WARNING instead.**

12. **Optional** - If you created additional services in **Step 11**, verify that you have also created their additional configuration files:

    .. code-block:: console
   
       $ cp sqream2-service.conf sqream3-service.conf
       $ vim sqream3-service.conf
      
13. For each SQream service configuration file, do the following:

    1. Change the **SERVICE_NAME=sqream2** value to **SERVICE_NAME=sqream3**. **Comment - I think we should show the command line for this step.**
    
    2. Change LOGFILE=/var/log/sqream/sqream2.log to LOGFILE=/var/log/sqream/sqream3.log **Comment - I think we should show the command line for this step.**
    
14. Set up **servicepicker**:

    1. Do the following:

       .. code-block:: console
   
       $ vim /etc/sqream/server_picker.conf
    
    2. Change the IP **192.168.5.82** to the value of the **metadataserver IP**:
    
       .. code-block:: console
   
       $ IP=192.168.5.82 to IP=<metadataserver IP value>
       
    3. Change the **CLUSTER** to the value of the cluster path.
     
15. Set up your service files:      
      
    .. code-block:: console
   
       $ cd /usr/local/sqream/service/
       $ cp sqream2.service sqream3.service
       $ vim sqream3.service      
       
16. Increment each **EnvironmentFile=/etc/sqream/sqream2-service.conf** configuration file for each SQream service file, as shown below:

    .. code-block:: console
     
       $ EnvironmentFile=/etc/sqream/sqream3-service.conf
       
17. Copy and register your service files into systemd:       
       
    .. code-block:: console
     
       $ sudo cp metadataserver.service /usr/lib/systemd/system/
       $ sudo cp serverpicker.service /usr/lib/systemd/system/
       $ sudo cp sqream*.service /usr/lib/systemd/system/
       
18. Verify that your service files have been copied into systemd:

    .. code-block:: console
     
       $ ls -l /usr/lib/systemd/system/sqream*
       $ ls -l /usr/lib/systemd/system/metadataserver.service
       $ ls -l /usr/lib/systemd/system/serverpicker.service
       $ sudo systemctl daemon-reload **Comment - Is this a separate step, i.e., to reload the system?**     
       
19. Copy the license into the **/etc/license** directory:

    .. code-block:: console
     
       $ cp license.enc /etc/sqream/

Configuring an HDFS Environment Under a SQream User
===================================================
**To configure an HDFS environment under a SQream user:**

**Comment - Is it correct to say "under" a SQream user instead of "for" or "in"?**

1. Open your **bash_profile** configuration file for editing:

   .. code-block:: console
     
       $ vim /home/sqream/.bash_profile
       
2. Make the following edits:

   .. code-block:: console
     
      $ #PATH=$PATH:$HOME/.local/bin:$HOME/bin

      $ #export PATH

      $ # PS1
      $ #MYIP=$(curl -s -XGET "http://ip-api.com/json" | python -c 'import json,sys; jstr=json.load(sys.stdin); print jstr["query"]')
      $ #PS1="\[\e[01;32m\]\D{%F %T} \[\e[01;33m\]\u@\[\e[01;36m\]$MYIP \[\e[01;31m\]\w\[\e[37;36m\]\$ \[\e[1;37m\]"

      $ SQREAM_HOME=/usr/local/sqream
      $ export SQREAM_HOME

      $ export JAVA_HOME=${SQREAM_HOME}/hdfs/jdk
      $ export HADOOP_INSTALL=${SQREAM_HOME}/hdfs/hadoop
      $ export CLASSPATH=`${HADOOP_INSTALL}/bin/hadoop classpath --glob`
      $ export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_INSTALL}/lib/native
      $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${SQREAM_HOME}/lib:$HADOOP_COMMON_LIB_NATIVE_DIR


      $ PATH=$PATH:$HOME/.local/bin:$HOME/bin:${SQREAM_HOME}/bin/:${JAVA_HOME}/bin:$HADOOP_INSTALL/bin
      $ export PATH

3. Verify that the edits have been made:

   .. code-block:: console
     
      $ source /home/sqream/.bash_profile
       
4. Check if you can access Hadoop from your machine:       
       
  .. code-block:: console
     
     $ hadoop fs -ls hdfs://<hadoop server name or ip>:8020/
      
**NOTICE:** If you cannot access Hadoop from your machine because it uses Kerberos, see [Connecting a SQream Server to Cloudera Hadoop with Kerberos].(https://sqream.atlassian.net/l/c/31tQvsrB)
   
5. Verify that an HDFS environment exists for SQream services:

   .. code-block:: console
     
      $ ls -l /etc/sqream/sqream_env.sh
      
6. If an HDFS environment does not exist for SQream services, create one (sqream_env.sh): **Comment - Is sqream_env.sh the file name?**

   .. code-block:: console
     
      $ #!/bin/bash

      $ SQREAM_HOME=/usr/local/sqream
      $ export SQREAM_HOME

      $ export JAVA_HOME=${SQREAM_HOME}/hdfs/jdk
      $ export HADOOP_INSTALL=${SQREAM_HOME}/hdfs/hadoop
      $ export CLASSPATH=`${HADOOP_INSTALL}/bin/hadoop classpath --glob`
      $ export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_INSTALL}/lib/native
      $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${SQREAM_HOME}/lib:$HADOOP_COMMON_LIB_NATIVE_DIR


      $ PATH=$PATH:$HOME/.local/bin:$HOME/bin:${SQREAM_HOME}/bin/:${JAVA_HOME}/bin:$HADOOP_INSTALL/bin
      $ export PATH
      
 7. Start the following SQream services manually and verify that they are functioning correctly:     
      
    .. code-block:: console
     
       $ sudo systemctl start metadataserver
       $ sudo systemctl start serverpicker
       $ sudo systemctl start sqream1
       $ sudo systemctl start sqream2
       $ sudo systemctl start sqream3
       $ sudo systemctl start sqream4  
      
 8. Verify that the following SQream processes are running and listening:
 
    .. code-block:: console
     
       $ sudo systemctl status metadataserver
       $ sudo systemctl status serverpicker
       $ sudo systemctl status sqream1  #... etc
       $ sudo netstat -nltp   #to see that sqream is listening on ports
      
   **NOTICE:** - Depending on the GPU package build optimization, it may take sqreamd 3 - 5 minutes to begin listening on its ports. To verify that sqreamd has begun listening, view the service logs located in the **/var/log/sqream** directory.   
      
Installing Monit
====================================

**To install Monit:**   
   
1. Install Monit as a superuser:
 
    .. code-block:: console
     
       $ sudo yum install monit  
       
**Comment - This was the only step in the Confluence page. Does the user have to do anything else to install Monit? Is there a procedure in some other place that is already written?**
       
Configuring Monit
====================================

Monit can be configured by modifying the Monit configuration file, called **monitrc**. This file contains blocks for each service that you want to monitor.

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
       
For servers that don't run the **metadataserver** and **serverpicker** commands, you can use the block example above, but hash the related commands, as shown below:

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
 
    **Comment - Should this step be moved to after the example configuration file below?**
 
      .. code-block:: console
     
      $ cd /etc/sqream
      $ sudo ln -s /etc/monit.d/monitrc monitrc
   
The following is an example of a working monitrc file configured to monitor the ***metadataserver** and **serverpicker** commands, and **four sqreamd services**. Note that the monitrc in the example is configured for eight sqreamd services, but that only the first four are enabled:

**Comment - I wonder if this file should be created on a separate page and linked here because it is a very large example. From a structural perspective, this may not be the best idea because it would be a "floating" page created only for the sake of the example.**

**Comment - Is "set daemon 5" what enables only the first four services?**

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

**To start Monit:**

1. Stop all actively running SQream services:

   .. code-block:: console
     
      $ sudo systemctl stop sqream[1-4]  #This command stops sqream1, sqream2,..,sqream4
      $ sudo systemctl stop serverpicker
      $ sudo systemctl stop metadataserver

2. Start Monit as a super user:

   .. code-block:: console
     
      $ sudo systemctl start monit
   
3. Verify that the following SQream processes are running and listening:
  
   .. code-block:: console
     
      $ sudo systemctl status metadataserver
      $ sudo systemctl status serverpicker
      $ sudo systemctl status sqream1  #... etc
      $ sudo netstat -nltp   #to see that sqream is listening on ports  
 
4. View Monit's service status:

   .. code-block:: console
     
      $ sudo systemctl status monit

5. If all good, enable the Monit service to start on boot: **Comment - What status result(s) are we looking for?**       
       
   .. code-block:: console
     
      $ sudo systemctl enable monit
      
Using Monit
====================================

Using Monit is simple and intuitive, and is used for starting processes that are not running and executing other actions in error situations. In addition, Monit has its own command syntax.

For example, you can stop the **sqream3** service (being monitored by Monit) in one of the following ways:

* Stopping Monit and SQream separately.
* Stopping SQream using a Monit command.

Both examples above are described in more detail below.

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

Stopping SQream Using a Monit Command
-------------------------------------

You can stop SQream using a Monit command as follows:

.. code-block:: console
     
   $ sudo monit stop sqream3

This command spots SQream only (and not Monit).

You can restart SQream as follows:

.. code-block:: console
     
   $ sudo monit start sqream3
       
Monit Command Line Options
-------------------------------------
This section describes some of the most commonly used Monit command options:

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

Using Monit to Upgrade your Version of SQream
=============================================

You can use Monit to upgrade your version of SQream.

**To use Monit to upgrade your version of SQream:**

1. Stop all actively running SQream services:

   .. code-block:: console
     
      $ sudo monit stop all
      
2. Verify that SQream has stopped listening on ports **500X**, **510X**, and **310X**:

   .. code-block:: console

      $ sudo netstat -nltp    #to make sure sqream stopped listening on 500X, 510X and 310X ports.

3. Stop the UI (not as a super user, but as a SQream user):

   .. code-block:: console
    
      $ pm2 stop all

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

The symbolic SQream link pointing should be pointing to the real folder:

.. code-block:: console
    
   $ sqream -> sqream-db-v2025.200

4. Restart the SQream services:

   .. code-block:: console
    
      $ sudo monit start all

5. Restart the UI:

   .. code-block:: console
    
      $ pm2 start all
