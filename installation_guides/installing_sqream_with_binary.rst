.. _installing_sqream_with_binary:

*********************************************
Installing SQream Using Binary Packages
*********************************************
This procedure describes how to install SQream using Binary packages and must be done on all servers.

**To install SQream using Binary packages:**

1. Copy the SQream package to the **/home/sqream** directory for the current version:

   .. code-block:: console
   
      $ tar -xf sqream-db-v<2020.2>.tar.gz

2. Append the version number to the name of the SQream folder. The version number in the following example is **v2020.2**:

   .. code-block:: console
   
      $ mv sqream sqream-db-v<2020.2>

3. Move the new version of the SQream folder to the **/usr/local/** directory:

   .. code-block:: console
   
      $ sudo mv sqream-db-v<2020.2> /usr/local/
      
4. Change the ownership of the folder to **sqream folder**:

   .. code-block:: console
   
      $ sudo chown -R sqream:sqream  /usr/local/sqream-db-v<2020.2>

5. Navigate to the **/usr/local/** directory and create a symbolic link to SQream:

   .. code-block:: console
   
      $ cd /usr/local
      $ sudo ln -s sqream-db-v<2020.2> sqream
      
6. Verify that the symbolic link that you created points to the folder that you created:

   .. code-block:: console
   
      $ ls -l
      
7. Verify that the symbolic link that you created points to the folder that you created:

   .. code-block:: console
   
      $ sqream -> sqream-db-v<2020.2>
      
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
      
.. note:: Verify that the JSON files have been configured correctly and that all required flags have been set to the correct values.

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

It would be same on server running metadataserver and different on other server nodes.

11. **Optional** - To run additional SQream services, copy the required configuration files and create additional JSON files:

   .. code-block:: console
   
      $ cp sqream2_config.json sqream3_config.json
      $ vim sqream3_config.json
      
.. note:: A unique **instanceID** must be used in each JSON file. IN the example above, the instanceID **sqream_2** is changed to **sqream_3**.

12. **Optional** - If you created additional services in **Step 11**, verify that you have also created their additional configuration files:

    .. code-block:: console
   
       $ cp sqream2-service.conf sqream3-service.conf
       $ vim sqream3-service.conf
      
13. For each SQream service configuration file, do the following:

    1. Change the **SERVICE_NAME=sqream2** value to **SERVICE_NAME=sqream3**.
    
    2. Change **LOGFILE=/var/log/sqream/sqream2.log** to **LOGFILE=/var/log/sqream/sqream3.log**.
    
.. note:: If you are running SQream on more than one server, you must configure the ``serverpicker`` and ``metadatserver`` services to start on only one of the servers. If **metadataserver** is running on the first server, the ``metadataServerIP`` value in the second server's /etc/sqream/sqream1_config.json file must point to the IP of the server on which the ``metadataserver`` service is running.
    
14. Set up **servicepicker**:

    1. Do the following:

       .. code-block:: console
   
          $ vim /etc/sqream/server_picker.conf
    
    2. Change the IP **127.0.0.1** to the IP of the server that the **metadataserver** service is running on.    
    
    3. Change the **CLUSTER** to the value of the cluster path.
     
15. Set up your service files:      
      
    .. code-block:: console
   
       $ cd /usr/local/sqream/service/
       $ cp sqream2.service sqream3.service
       $ vim sqream3.service      
       
16. Increment each **EnvironmentFile=/etc/sqream/sqream2-service.conf** configuration file for each SQream service file, as shown below:

    .. code-block:: console
     
       $ EnvironmentFile=/etc/sqream/sqream<3>-service.conf
       
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
       $ sudo systemctl daemon-reload       
       
19. Copy the license into the **/etc/license** directory:

    .. code-block:: console
     
       $ cp license.enc /etc/sqream/   

       
If you have an HDFS environment, see :ref:`Configuring an HDFS Environment for the User sqream <hdfs>`.






Upgrading SQream Version
-------------------------
Upgrading your SQream version requires stopping all running services while you manually upgrade SQream.

**To upgrade your version of SQream:**

1. Stop all actively running SQream services.

.. note:: All SQream services must remain stopped while the upgrade is in process. Ensuring that SQream services remain stopped depends on the tool being used.

For an example of stopping actively running SQream services, see :ref:`Launching SQream with Monit <launching_sqream_with_monit>`.
   
2. Verify that SQream has stopped listening on ports **500X**, **510X**, and **310X**:

   .. code-block:: console

      $ sudo netstat -nltp    #to make sure sqream stopped listening on 500X, 510X and 310X ports.

3. Replace the old version ``sqream-db-v2021.1``, with the new version ``sqream-db-v2021.1``:

   .. code-block:: console
    
      $ cd /home/sqream
      $ mkdir tempfolder
      $ mv sqream-db-v2021.1.tar.gz tempfolder/
	  $ cd tempfolder/
      $ tar -xf sqream-db-v2021.1.tar.gz
      $ sudo mv sqream /usr/local/sqream-db-v2021.1
      $ cd /usr/local
      $ sudo chown -R sqream:sqream sqream-db-v2021.1
   
4. Remove the symbolic link:

   .. code-block:: console
   
      $ sudo rm sqream
   
5. Create a new symbolic link named "sqream" pointing to the new version:

   .. code-block:: console  

      $ sudo ln -s sqream-db-v2021.1 sqream

6. Verify that the symbolic SQream link points to the real folder:

   .. code-block:: console  

      $ ls -l
	 
   The following is an example of the correct output:

   .. code-block:: console
    
      $ sqream -> sqream-db-v2021.1

7. **Optional-** (for major versions) Upgrade your version of SQream storage cluster, as shown in the following example:

   .. code-block:: console  

      $ cat /etc/sqream/sqream1_config.json |grep cluster
      $ ./upgrade_storage <cluster path>
	  
   The following is an example of the correct output:
	  
   .. code-block:: console  

	  get_leveldb_version path{<cluster path>}
	  current storage version 23
      upgrade_v24
      upgrade_storage to 24
	  upgrade_storage to 24 - Done
	  upgrade_v25
	  upgrade_storage to 25
	  upgrade_storage to 25 - Done
	  upgrade_v26
	  upgrade_storage to 26
	  upgrade_storage to 26 - Done
	  validate_leveldb
	  ...
      upgrade_v37
	  upgrade_storage to 37
	  upgrade_storage to 37 - Done
	  validate_leveldb
      storage has been upgraded successfully to version 37
 
8. Verify that the latest version has been installed:

   .. code-block:: console
    
      $ ./sqream sql --username sqream --password sqream --host localhost --databasename master -c "SELECT SHOW_VERSION();"
      
   The following is an example of the correct output:
 
   .. code-block:: console
    
      v2021.1
      1 row
      time: 0.050603s 
 
For more information, see the :ref:`upgrade_storage<upgrade_storage_cli_reference>` command line program.

For more information about installing Studio on a stand-alone server, see :ref:`Installing Studio on a Stand-Alone Server<installing_studio_on_stand_alone_server>`.