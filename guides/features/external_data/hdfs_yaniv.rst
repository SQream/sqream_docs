.. _hdfs_yaniv.rst:

Configuring an HDFS Environment for the User **sqream**
======================================================
**NOTICE:** This section is only relevant for users with an HDFS environment.

**Note to self: merge this section into the Confluence page, and convert all content into our format: https://sqream.atlassian.net/wiki/spaces/DOC/pages/724467716/Sqream+manual+installation+as+systemd+services+with+Monit**

This section describes how to configure an HDFS environment for the user **sqream**.

**To configure an HDFS environment for the user sqream:**

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
      
**NOTICE:** If you cannot access Hadoop from your machine because it uses Kerberos, see [Connecting a SQream Server to Cloudera Hadoop with Kerberos].(https://sqream.atlassian.net/wiki/spaces/DOC/pages/822902789/How+to+connect+sqream+server+to+Cloudera+Hadoop+with+kerberos)

5. Verify that an HDFS environment exists for SQream services:

   .. code-block:: console
     
      $ ls -l /etc/sqream/sqream_env.sh
      
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
