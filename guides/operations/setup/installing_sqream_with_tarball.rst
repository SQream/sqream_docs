.. _installing_sqream_with_tarball:

*********************************************
Installing SQream with Tarball
*********************************************
This procedure describes how to install SQream using Tarball.

**Comment - speak with Ori about the proper name for this**

**To launch SQream with Tarball:**

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

It would be same on server running metadataserver and different on other server nodes.

11. **Optional** - To run additional SQream services, copy the required configuration files and create additional JSON files:

   .. code-block:: console
   
      $ cp sqream2_config.json sqream3_config.json
      $ vim sqream3_config.json
      
**NOTICE:** A unique **instanceID** must be used in each JSON file. IN the example above, the instanceID **sqream_2** is changed to **sqream_3**.

12. **Optional** - If you created additional services in **Step 11**, verify that you have also created their additional configuration files:

    .. code-block:: console
   
       $ cp sqream2-service.conf sqream3-service.conf
       $ vim sqream3-service.conf
      
13. For each SQream service configuration file, do the following:

    1. Change the **SERVICE_NAME=sqream2** value to **SERVICE_NAME=sqream3**.
    
    2. Change LOGFILE=/var/log/sqream/sqream2.log to LOGFILE=/var/log/sqream/sqream3.log
    
14. Set up **servicepicker**:

    1. Do the following:

       .. code-block:: console
   
          $ vim /etc/sqream/server_picker.conf
    
    2. Change the IP **127.0.0.1** to the IP of the server that the **metadataserver** service is running on.
    
    **Comment: can the host name be used instead of the IP address? See Step 4 in Configuring an HDFS Environment for the user sqream.**
    
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
       
If you have an HDFS environment, see Configuring an HDFS Environment for the User sqream :ref:`.. _recommended_configurations_updated:`.
