.. _hdfs:

***********************
HDFS
***********************

SQream DB has a native HDFS connector for inserting data. The ``hdfs://`` URI specifies an external file path on a Hadoop Distributed File System.

File names may contain wildcard characters and the files can be a CSV or columnar format like Parquet and ORC.


.. contents:: In this topic:
   :local:

Verifying HDFS configuration
==============================

SQream DB's built-in HDFS relies on the host's Hadoop HDFS configuration. 

Before you can use HDFS, you should verify that all SQream DB hosts are configured correctly.

Use built-in Hadoop libraries
-------------------------------

SQream DB comes with Hadoop libraries built-in. In a typical SQream DB installation, you'll find Hadoop and JDK libraries in the ``hdfs`` subdirectory of the package.

If you are using the built-in libraries, it's important to note where they are.


For example, if SQream DB was installed to ``/opt/sqream``, here's how to set-up the environment variables from the shell:


.. _set_hadoop_classpath:

.. code-block:: console

   $ export JAVA_HOME=/opt/sqream/hdfs/jdk

   $ export HADOOP_INSTALL=/opt/sqream/hdfs/hadoop
   
   $ export PATH=$PATH:${HADOOP_INSTALL}/bin:${HADOOP_INSTALL}/sbin
   $ export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_INSTALL}/lib/native
   $ export CLASSPATH=$CLASSPATH:`${HADOOP_INSTALL}/bin/hadoop classpath --glob`
   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_COMMON_LIB_NATIVE_DIR

   $ export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
   $ export HADOOP_COMMON_HOME=$HADOOP_INSTALL
   $ export HADOOP_HDFS_HOME=$HADOOP_INSTALL
   $ export YARN_HOME=$HADOOP_INSTALL
   
   $ export HADOOP_CONF_DIR=$HADOOP_INSTALL/etc/hadoop
   $ export YARN_CONF_DIR=$HADOOP_INSTALL/etc/hadoop
   $ export HADOOP_HOME=$HADOOP_INSTALL
   $ export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=${HADOOP_COMMON_LIB_NATIVE_DIR}"
   $ export ARROW_LIBHDFS_DIR=${HADOOP_COMMON_LIB_NATIVE_DIR}


You'll find ``core-site.xml`` and other configuration files in ``/opt/sqream/hdfs/hadoop/etc/hadoop``

To persist these settings, place these variable settings in a 'run commands' file like ``.bashrc``. Test this by examining the output of ``$ echo $ARROW_LIBHDFS_DIR``.

.. note:: 
   
   * This process needs to be repeated for every host in the SQream DB cluster, and from SQream DB's host username (often ``sqream``)
   
   * Restart SQream DB workers on the host after setting these parameters for them to take effect.


If they don't already exist, place these variable settings in a 'run commands' file like ``.bashrc``. Test this by examining the output of ``$ echo $ARROW_LIBHDFS_DIR``.

.. note:: This process needs to be repeated for every host in the SQream DB cluster.


(Optional) Overriding the Hadoop environment
------------------------------------------------------

If you have an existing Hadoop environment set-up on the host, you can override SQream DB's built-in Hadoop by setting the environment variables accordingly.

For example,

.. code-block:: console

   $ export JAVA_HOME=/usr/local/java-1.8.0/

   $ export HADOOP_INSTALL=/usr/local/hadoop-3.2.1
   
   $ export PATH=$PATH:${HADOOP_INSTALL}/bin:${HADOOP_INSTALL}/sbin
   $ export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_INSTALL}/lib/native
   $ export CLASSPATH=$CLASSPATH:`${HADOOP_INSTALL}/bin/hadoop classpath --glob`
   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HADOOP_COMMON_LIB_NATIVE_DIR

   $ export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
   $ export HADOOP_COMMON_HOME=$HADOOP_INSTALL
   $ export HADOOP_HDFS_HOME=$HADOOP_INSTALL
   $ export YARN_HOME=$HADOOP_INSTALL
   
   $ export HADOOP_CONF_DIR=$HADOOP_INSTALL/etc/hadoop
   $ export YARN_CONF_DIR=$HADOOP_INSTALL/etc/hadoop
   $ export HADOOP_HOME=$HADOOP_INSTALL
   $ export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=${HADOOP_COMMON_LIB_NATIVE_DIR}"
   $ export ARROW_LIBHDFS_DIR=${HADOOP_COMMON_LIB_NATIVE_DIR}


To persist these settings, place these variable settings in a 'run commands' file like ``.bashrc``. Test this by examining the output of ``$ echo $ARROW_LIBHDFS_DIR``.

.. note:: 
   
   * This process needs to be repeated for every host in the SQream DB cluster, and from SQream DB's host username (often ``sqream``)
   
   * Restart SQream DB workers on the host after setting these parameters for them to take effect.


Place these variable settings in a 'run commands' file like ``.bashrc``. Test this by examining the output of ``$ echo $ARROW_LIBHDFS_DIR``.

.. note:: This process needs to be repeated for every host in the SQream DB cluster.


Configuring the node
======================

A Hadoop administrator will want to edit the configuration XMLs to allow access to your Hadoop cluster.

If using the SQream DB Hadoop libraries, modify the following files to match your cluster settings:

* ``/opt/sqream/hdfs/hadoop/etc/hadoop/core-site.xml``
* ``/opt/sqream/hdfs/hadoop/etc/hadoop/yarn-site.xml``
* ``/opt/sqream/hdfs/hadoop/etc/hadoop/hdfs-site.xml``

If using the system Hadoop libraries, be sure to override ``JAVA_HOME``, ``CLASSPATH``, ``HADOOP_HOME``, and ``ARROW_LIBHDFS_DIR`` as described above.

Verifying Hadoop configuration
==================================

To test HDFS access, try accessing files using the HDFS shell:

.. code-block:: console

   $ hdfs dfs -ls
   Found 2 items
   -rw-r--r--   3 hdfs supergroup      63446 2020-02-29 16:37 MD1.csv
   -rw-r--r--   3 hdfs supergroup      63906 2020-02-29 16:37 MD2.csv
   $ hdfs dfs -tail MD1.csv
   985,Obediah,Reith,oreithrc@time.com,Male,Colombia,859.28
   986,Lennard,Hairesnape,lhairesnaperd@merriam-webster.com,Male,North Korea,687.60
   987,Valaree,Pieper,vpieperre@tinyurl.com,Female,Kazakhstan,1116.23
   988,Rosemaria,Legan,rleganrf@slideshare.net,Female,Indonesia,62.19
   989,Rafaellle,Hartill,rhartillrg@marketwatch.com,Male,Albania,1308.17
   990,Symon,Edmett,sedmettrh@tinyurl.com,Male,China,1216.97
   991,Hiram,Slayton,hslaytonri@amazon.de,Male,China,510.55
   992,Sylvan,Dalgliesh,sdalglieshrj@booking.com,Male,China,1503.60
   993,Alys,Sedgebeer,asedgebeerrk@va.gov,Female,Moldova,1947.58
   994,Ninette,Hearl,nhearlrl@sakura.ne.jp,Female,Palau,917.66
   995,Tommy,Atterley,tatterleyrm@homestead.com,Female,Philippines,1660.22
   996,Sean,Mully,smullyrn@rakuten.co.jp,Female,Brunei,938.04
   997,Gabe,Lytell,glytellro@cnn.com,Male,China,491.12
   998,Clementius,Battison,cbattisonrp@dedecms.com,Male,Norway,1781.92
   999,Kyle,Vala,kvalarq@paginegialle.it,Male,France,11.26
   1000,Korrie,Odd,koddrr@bigcartel.com,Female,China,471.96

If the command succeeded and the file was read correctly, you HDFS has been configured correctly and can now be used in SQream DB.

If an access error occured, check your Hadoop configuration or contact SQream support.


Configuring HDFS for Kerberos access
========================================

This section describes how to configure SQream DB to access HDFS secured with Kerberos.

When a Hadoop cluster is Kerberized, SQream DB's user must be configured to to authenticate through Kerberos.

Prerequisites
----------------

This section assumes you already have Java and Hadoop installed on your SQream DB hosts.

* SQream DB hosts and Kerberos servers should have the same JCE (Java Cryptography Extension). You can copy the JCE files from the Kerberos server to the SQream DB hosts if needed, to the ``$JAVA_HOME/jre/lib/security`` path.

* Install the Kerberos clients
   
   CentOS / RHEL: ``$ sudo yum install krb5-libs krb5-workstation``
   
   Ubuntu: ``$ sudo apt-get install krb5-user``

* Configure Hadoop as per your distribution.

Creating keytabs
----------------------

#. Sign into your Kerberos Key Distribution Center (KDC) as a root user

#. 
   Create a new principal for the SQream DB OS users (e.g. ``sqream`` by default):
   
   .. code-block:: console

      # kadmin.local -q "addprinc -randkey sqream@KRLM.PIEDPIPER.COM"
   
   Make sure to replace the realm (``KRLM.PIEDPIPER.COM``) with your actual Kerberos realm.

#. 
   Create a Kerberos service principal for each SQream DB host in the cluster.
   
   In this example, three cluster hosts:
   
   .. code-block:: console
   
      # kadmin.local -q "addprinc -randkey sqream/sqreamdb-01.piedpiper.com@KRLM.PIEDPIPER.COM"
      # kadmin.local -q "addprinc -randkey sqream/sqreamdb-02.piedpiper.com@KRLM.PIEDPIPER.COM"
      # kadmin.local -q "addprinc -randkey sqream/sqreamdb-03.piedpiper.com@KRLM.PIEDPIPER.COM"
   
   The format for each principal is ``user/host@realm``, where:
   
   * ``user`` is the OS username
   
   * ``host`` is the hostname (typically the output of ``hostname -f``)
   
   * ``realm`` is the Kerberos realm

#. Generate a keytab for each principal.
   
   .. code-block:: console
      
      # kadmin.local -q "xst -k /etc/security/keytabs/sqreamdb-01.service.keytab sqream/sqreamdb-01 sqream/sqreamdb-01.piedpiper.com@KRLM.PIEDPIPER.COM"
      # kadmin.local -q "xst -k /etc/security/keytabs/sqreamdb-02.service.keytab sqream/sqreamdb-02 sqream/sqreamdb-02.piedpiper.com@KRLM.PIEDPIPER.COM"
      # kadmin.local -q "xst -k /etc/security/keytabs/sqreamdb-03.service.keytab sqream/sqreamdb-03 sqream/sqreamdb-03.piedpiper.com@KRLM.PIEDPIPER.COM"

   You can now exit ``kadmin``.
   
#. Change permissions and ownership on each keytab:
   
   .. code-block:: console
      
      # chown sqream:sqream /etc/security/keytabs/sqreamdb*
      # chmod 440 /etc/security/keytabs/sqreamdb*

#. Copy the keytab files for each service principal to its respective SQream DB host:
   
   .. code-block:: console
   
      # scp /etc/security/keytabs/sqreamdb-01.service.keytab sqreamdb-01.piedpiper.com:/home/sqream/sqreamdb-01.service.keytab
      # scp /etc/security/keytabs/sqreamdb-02.service.keytab sqreamdb-02.piedpiper.com:/home/sqream/sqreamdb-02.service.keytab
      # scp /etc/security/keytabs/sqreamdb-03.service.keytab sqreamdb-03.piedpiper.com:/home/sqream/sqreamdb-03.service.keytab

Configuring HDFS for Kerberos
---------------------------------

#. 
   Edit the ``core-site.xml`` configuration file on each SQream DB host to enable authorization.

   For example, editing ``/opt/sqream/hdfs/hadoop/etc/hadoop/core-site.xml``:
   
   .. code-block:: xml

      <property>
          <name>hadoop.security.authorization</name>
          <value>true</value>
      </property>

#. Edit the ``yarn-site.xml`` configuration file on each SQream DB host to set the Yarn Kerberos principal

   For example, editing ``/opt/sqream/hdfs/hadoop/etc/hadoop/yarn-site.xml``:
   
   .. code-block:: xml

      <property>
          <name>yarn.resourcemanager.address</name>
          <value>hadoop-nn.piedpiper.com:8032</value>
      </property>
      <property>
          <name>yarn.resourcemanager.principal</name>
          <value>yarn/_hostname@KRLM.PIEDPIPER.COM</value>
      </property>

#. 
   
   Edit the ``hdfs-site.xml`` configuration file on each SQream DB host to set the NameNode Kerberos principals, the location of the Kerberos keytab file, and the principal:

   For example, editing ``/opt/sqream/hdfs/hadoop/etc/hadoop/hdfs-site.xml`` on the first host (``sqreamdb-01``):
   
   .. code-block:: xml

      <property>
          <name>dfs.namenode.kerberos.principal</name>
          <value>sqream/sqreamdb-01.piedpiper.com@KRLM.PIEDPIPER.COM</value>
      </property>
      <property>
          <name>dfs.namenode.https.principal</name>
          <value>sqream/sqreamdb-01.piedpiper.com@KRLM.PIEDPIPER.COM</value>
      </property>
      <property>
          <name>com.emc.greenplum.gpdb.hdfsconnector.security.user.keytab.file</name>
          <value>/home/sqream/sqreamdb-01.service.keytab</value>
      </property>
      <property>
          <name>com.emc.greenplum.gpdb.hdfsconnector.security.user.name</name>
          <value>sqream/sqreamdb-01.piedpiper.com@KRLM.PIEDPIPER.CO</value>
      </property>

Test the access
--------------------

To confirm that Kerberized HDFS is accessible on all SQream DB hosts, run the following command to list a directory:

.. code-block:: console

   $ hdfs dfs -ls hdfs://hadoop-nn.piedpiper.com:8020

Repeat the command on all hosts.
If the command succeeds and you see a directory listing, Kerberized HDFS has been configured correctly and can now be used in SQream DB.

If an error occured, check your configuration or contact SQream support.


Testing HDFS access in SQream DB
=====================================

HDFS access from SQream DB is from :ref:`copy_from` and :ref:`external_tables`.

* :ref:`Example for an HDFS-stored external table<hdfs_external_table_demo>`

* :ref:`Example for inserting data from a CSV on HDFS<hdfs_copy_from_example>`


Troubelshooting HDFS access
==================================

``class not found`` error
---------------------------------

If you get a ``class not found`` error that looks like this:

   java.lang.ClassNotFoundException: Class org.apache.hadoop.hdfs.DistributedFileSystem not found

#. Verify that the CLASSPATH and ARROW_LIBHDFS_DIR are set correctly. Read more about :ref:`setting the environment variables<set_hadoop_classpath>` above.

#. Try restarting SQream DB after setting the environment variables.

