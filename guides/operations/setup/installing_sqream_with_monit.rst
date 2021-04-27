.. _installing_sqream_with_monit:

*********************************************
Installing SQream with Monit
*********************************************
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

11. **Optional** - To run more than two instances of SQream, copy the required configuration files and create a new file: **Comment: verify step**

   .. code-block:: console
   
      $ cp sqream2_config.json sqream3_config.json
      $ vim sqream3_config.json

