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

11. Create a cluster.

    A cluster can be created either on your machine or in storage.
	
    For more information on creating clusters, see `SqreamStorage <https://docs.sqream.com/en/latest/reference/cli/sqream_storage.html>`_.
	
12. Copy path to the directory where you cluster is contained, and paste it in the sqream.json file, as shown below:

  .. note:: A separate sqream.json file exists for each worker on your system. The name of each current configuration file includes the number of the worker. For example, the current configuration file for Worker 8 is **sqream8_config.json**.

13. Update all parameters in the current configuration files for each worker, as in the following example:

   .. code-block:: console
   
      {
          "cluster": "/home/sqream/sqream_cluster/sqreamdb",
          "cudaMemQuota": 96,
          "gpu": 0,
          "legacyConfigFilePath": "sqream1_config_legacy.json",
          "licensePath": "/home/sqream/etc/license.enc",
          "limitQueryMemoryGB": 15,
          "machineIP": "192.168.4.58",
          "metadataServerIp": "192.168.4.58",
          "initialSubscribedServices": "sqream",
          "instanceId": "sqream_01",
          "metadataServerPort": 3105,
          "port": 5000,
          "ssl_port": 5100,
          "useConfigIP": true
      }

Note the following:

* The value of the **metadataServerIp** parameter must point to the IP that the metadata is running on.
* The value of the **machineIP** parameter must point to the IP of your local machine.

The values are the same on servers running metadataserver, and different on other server nodes.

14. Insert your license file path into the ``licensePath`` parameter in your current configuration file (see above).

    The following is an example of a license file path:

.. code-block:: console   
   6C5B5CEF705FD72C21CA991E6A00A7410589DED028366FF9441AC6FA8C5FB8FDF2BD22BF328261FCD84455941634EC38FDB361DC0B2DE81A5A4120C1AE58D0B4EECCE2AD9D97C047C54838413F50ACC78F74603407AC864B81D23745F84135CFFF60561886546CF3A8F9A4E0049BB099210CB43FB332DDB3B91E9EB9774B39065E7DBB6E1982E8DACCD732AC6B8532A15BD2C8049A1975C470C3A091DFFE382E4F52A0C5E24C8F16490DC2D192EB9AED2CE7F2B76F513FCEA6C5B648E370DDABA9FC29AEB77AC620FDFBC71663FAE18CCE64A2DB7E69750F74288AD474930CDF3F38023766AE371DC3B6393A6547620F   
	
15. Update all parameters in the previous configuration files for each worker, as follows:

   .. code-block:: console
   
      {
          "diskSpaceMinFreePercent": 10,
          "enableLogDebug": false,
          "insertCompressors": 8,
          "insertParsers": 8,
          "isUnavailableNode": false,
          "logBlackList": "webui",
          "logDebugLevel": 6,
          "nodeInfoLoggingSec": 60,
          "useClientLog": true,
          "useMetadataServer": true,
          "spoolMemoryGB": 5,
          "waitForClientSeconds": 18000
      }

16. **Optional** - To run additional SQream services, copy the required configuration files and create additional JSON files:

    .. code-block:: console
   
       $ cp sqream2_config.json sqream3_config.json
       $ vim sqream3_config.json
      
  .. note:: A unique **instanceID** must be used in each JSON file. IN the example above, the instanceID **sqream_2** is changed to **sqream_3**.

17. **Optional** - If you created additional services in **Step 11**, verify that you have also created their additional configuration files:

    .. code-block:: console
   
       $ cp sqream2-service.conf sqream3-service.conf
       $ vim sqream3-service.conf
      
18. For each SQream service configuration file, do the following:

    1. Change the **SERVICE_NAME=sqream2** value to **SERVICE_NAME=sqream3**.
	
	    ::
    
    2. Change **LOGFILE=/var/log/sqream/sqream2.log** to **LOGFILE=/var/log/sqream/sqream3.log**.
    
**NOTE:** If you are running SQream on more than one server, you must configure the ``serverpicker`` and ``metadatserver`` services to start on only one of the servers. If **metadataserver** is running on the first server, the ``metadataServerIP`` value in the second server's /etc/sqream/sqream1_config.json file must point to the IP of the server on which the ``metadataserver`` service is running.
    
19. Set up **servicepicker**:

    1. Do the following:

       .. code-block:: console
   
          $ vim /etc/sqream/server_picker.conf
    
    2. Change the IP **127.0.0.1** to the IP of the server that the **metadataserver** service is running on.

        ::	
    
    3. Change the **CLUSTER** to the value of the cluster path.
     
20. Set up your service files:      
      
    .. code-block:: console
   
       $ cd /usr/local/sqream/service/
       $ cp sqream2.service sqream3.service
       $ vim sqream3.service      
       
21. Increment each **EnvironmentFile=/etc/sqream/sqream2-service.conf** configuration file for each SQream service file, as shown below:

    .. code-block:: console
     
       $ EnvironmentFile=/etc/sqream/sqream<3>-service.conf
       
22. Copy and register your service files into systemd:       
       
    .. code-block:: console
     
       $ sudo cp metadataserver.service /usr/lib/systemd/system/
       $ sudo cp serverpicker.service /usr/lib/systemd/system/
       $ sudo cp sqream*.service /usr/lib/systemd/system/
       
 
    .. code-block:: console
     
       $ ls -l /usr/lib/systemd/system/sqream*
       $ ls -l /usr/lib/systemd/system/metadataserver.service
       $ ls -l /usr/lib/systemd/system/serverpicker.service
       $ sudo systemctl daemon-reload       
       
24. Copy the license into the **/etc/license** directory:

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

3. Replace the old version ``sqream-db-v2020.2``, with the new version ``sqream-db-v2021.1``:

   .. code-block:: console
    
      $ cd /home/sqream
      $ mkdir tempfolder
      $ mv sqream-db-v2021.1.tar.gz tempfolder/
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
 
For more information, see the `upgrade_storage <https://docs.sqream.com/en/latest/reference/cli/upgrade_storage.html>`_ command line program.

For more information about installing Studio on a stand-alone server, see `Installing Studio on a Stand-Alone Server <https://docs.sqream.com/en/latest/guides/operations/sqream_studio_5.4.2.html>`_.