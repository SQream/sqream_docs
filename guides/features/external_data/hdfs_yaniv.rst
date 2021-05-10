.. _hdfs_yaniv.rst:

.. _back_to_top:

Launching SQream in an HDFS Environment
=======================================
This page describes how to:



* :ref:`Configure an HDFS environment for the user sqream <configuring_an_hdfs_environment_for_the_user_sqream>`
* :ref:`Authenticate Hadoop servers that require Kerberos <authenticate_hadoop_servers_that_require_kerberos>`

.. _configuring_an_hdfs_environment_for_the_user_sqream:

Configuring an HDFS Environment for the User **sqream**
----------------------------------------------------------

This section describes how to configure an HDFS environment for the user **sqream** and is only relevant for users with an HDFS environment.

**To configure an HDFS environment for the user sqream:**

1. Open your **bash_profile** configuration file for editing:

   .. code-block:: console
     
       $ vim /home/sqream/.bash_profile
       
2. Make the following edits:

..
   Comment: - see below; do we want to be a bit more specific on what changes we're talking about?

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
     
      source /home/sqream/.bash_profile
       
4. Check if you can access Hadoop from your machine:       
       
  .. code-block:: console
     
     $ hadoop fs -ls hdfs://<hadoop server name or ip>:8020/
      
..
   Comment: - 
   **NOTICE:** If you cannot access Hadoop from your machine because it uses Kerberos, see `Connecting a SQream Server to Cloudera Hadoop with Kerberos <https://sqream.atlassian.net/wiki/spaces/DOC/pages/822902789/How+to+connect+sqream+server+to+Cloudera+Hadoop+with+kerberos>`_


5. Verify that an HDFS environment exists for SQream services:

   .. code-block:: console
     
      $ ls -l /etc/sqream/sqream_env.sh
	  
.. _step_6:

      
6. If an HDFS environment does not exist for SQream services, create one (sqream_env.sh):
   
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
	  
:ref:`Back to top <back_to_top>`

	  
.. _authenticate_hadoop_servers_that_require_kerberos:

Authenticate Hadoop Servers that Require Kerberos
---------------------------------------------------

If your Hadoop server requires Kerberos authentication, do the following:

1. Create a principal for the user **sqream**.

   .. code-block:: console
   
      $ kadmin -p root/admin@SQ.COM
      $ addprinc sqream@SQ.COM
      
2. If you do not know yor Kerberos root credentials, connect to the Kerberos server as a root user with ssh and run **kadmin.local**:

   .. code-block:: console
   
      $ kadmin.local
      
   Running **kadmin.local** does not require a password.

3. If a password is not required, change your password to **sqream@SQ.COM**.

   .. code-block:: console
   
      $ change_password sqream@SQ.COM

4. Connect to the hadoop name node using ssh:

   .. code-block:: console
   
      $ cd /var/run/cloudera-scm-agent/process

5. Check the most recently modified content of the directory above:

   .. code-block:: console
   
      $ ls -lrt

5. Look for a recently updated folder containing the text **hdfs**.

The following is an example of the correct folder name:

   .. code-block:: console
   
      cd <number>-hdfs-<something>
	  
   This folder should contain a file named **hdfs.keytab** or another similar .keytab file.
   

 
..
   Comment: - Does "something" need to be replaced with "file name"
   

6. Copy the .keytab file to user **sqream's** Home directory on the remote machines that you are planning to use Hadoop on.

7. Copy the following files to the **sqream sqream@server:<sqream folder>/hdfs/hadoop/etc/hadoop:** directory:

   * core-site.xml
   * hdfs-site.xml

8. Connect to the sqream server and verify that the .keytab file's owner is a user sqream and is granted the correct permissions:

   .. code-block:: console
   
      $ sudo chown sqream:sqream /home/sqream/hdfs.keytab
      $ sudo chmod 600 /home/sqream/hdfs.keytab

9. Log into the sqream server.

10. Log in as the user **sqream**.

11. Navigate to the Home directory and check the name of a Kerberos principal represented by the following .keytab file:

   .. code-block:: console
   
      $ klist -kt hdfs.keytab

   The following is an example of the correct output:

   .. code-block:: console
   
      $ sqream@Host-121 ~ $ klist -kt hdfs.keytab
      $ Keytab name: FILE:hdfs.keytab
      $ KVNO Timestamp           Principal
      $ ---- ------------------- ------------------------------------------------------
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 HTTP/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM
      $    5 09/15/2020 18:03:05 hdfs/nn1@SQ.COM

12. Verify that the hdfs service named **hdfs/nn1@SQ.COM** is shown in the generated output above.

13. Run the following:

   .. code-block:: console
   
      $ kinit -kt hdfs.keytab hdfs/nn1@SQ.COM

 13. Check the output:
  
   .. code-block:: console
   
      $ klist
      
   The following is an example of the correct output:

   .. code-block:: console
   
      $ Ticket cache: FILE:/tmp/krb5cc_1000
      $ Default principal: sqream@SQ.COM
      $ 
      $ Valid starting       Expires              Service principal
      $ 09/16/2020 13:44:18  09/17/2020 13:44:18  krbtgt/SQ.COM@SQ.COM

14. List the files located at the defined server name or IP address:

   .. code-block:: console
   
      $ hadoop fs -ls hdfs://<hadoop server name or ip>:8020/

15. Do one of the following:

    * If the list below is output, continue with Step 16.
    * If the list is not output, verify that your environment has been set up correctly.
	
If any of the following are empty, verify that you followed :ref:`Step 6 <step_6>` in the **Configuring an HDFS Environment for the User sqream** section above correctly:

  .. code-block:: console
   
      $ echo $JAVA_HOME
      $ echo $SQREAM_HOME
      $ echo $CLASSPATH
      $ echo $HADOOP_COMMON_LIB_NATIVE_DIR
      $ echo $LD_LIBRARY_PATH
      $ echo $PATH

16. Verify that you copied the correct keytab file.

17. Review this procedure to verify that you have followed each step.

:ref:`Back to top <back_to_top>`
