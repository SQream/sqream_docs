.. _hadoop_server_requires_kerberos_authentication:

*********************************************
Hadoop Servers that Require Kerberos Authentication
*********************************************

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

5. Look for a recently updated folder containing the text **hdfs**:

   .. code-block:: console
   
      $ cd <number>-hdfs-<something>

   This folder should contain a file named **hdfs.keytab** or another similar .keytab file.

6. Copy the .keytab file to user **sqream's** Home directory on the remote machines that you are planning to use Hadoop on.

7. Copy the following files to the **sqream sqream@server:<sqream folder>/hdfs/hadoop/etc/hadoop:** directory:

   1. core-site.xml
   2. hdfs-site.xml

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

    1. If the list is generated, continue with Step 17.
    2. If the list is not generated, verify that your environment has been set up correctly. If any of the following are empty verify that you followed **<Step #>** correctly:
    
**Comment - which step does this correspond to within this document?**

  .. code-block:: console
   
      $ echo $JAVA_HOME
      $ echo $SQREAM_HOME
      $ echo $CLASSPATH
      $ echo $HADOOP_COMMON_LIB_NATIVE_DIR
      $ echo $LD_LIBRARY_PATH
      $ echo $PATH

16. Verify that you copied the correct keytab file.

17. Review this procedure to verify that you have followed each step.
