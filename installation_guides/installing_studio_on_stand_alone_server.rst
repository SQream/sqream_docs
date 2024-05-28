.. _installing_studio_on_stand_alone_server:

.. _install_studio_top:

*****************************************
Installing Studio on a Stand-Alone Server
*****************************************

A stand-alone server is a server that does not run SQreamDB based on binary files.

.. contents::
   :local:
   :depth: 1

Before You Begin
================

It is essential you have **NodeJS 16** installed.

-- link to NodeJS 16 in installation
	 
Installing Studio
=================
 
**To install Studio:**

1. Copy the SQream Studio package from SQream Artifactory into the target server. For access to the Sqream Studio package, contact `SQream Support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.

::

2. Extract the package:

   .. code-block:: console
     
      tar -xvf sqream-acceleration-studio-<version number>.x86_64.tar.gz

::
	
3. Navigate to the new package folder. 
 
   .. code-block:: console
     
      cd sqream-admin  
	  
.. _add_parameter:
	
4. Build the configuration file to set up Sqream Studio. You can use IP address **127.0.0.1** on a single server.
 
   .. code-block:: console
     
      npm run setup -- -y --host=<SQreamD IP> --port=3108

   The above command creates the **sqream-admin-config.json** configuration file in the **sqream-admin** folder and shows the following output:
   
   .. code-block:: console
   
      Config generated successfully. Run `npm start` to start the app.

   For more information about the available set-up arguments, see :ref:`Set-Up Arguments<setup_arguments>`.
  
5. To make the communication between Studio and SQreamDB secure, in your configuration file do the following:

   #. Change your ``port`` value to **3109**.
	   
   #. Change your ``ssl`` flag value to **true**.
   
      The following is an example of the correctly modified configuration file:
	  
      .. code-block:: json
     
         {
           "debugSqream": false,
           "webHost": "localhost",
           "webPort": 8080,
           "webSslPort": 8443,
           "logsDirectory": "",
           "clusterType": "standalone",
           "dataCollectorUrl": "",
           "connections": [
             {
               "host": "127.0.0.1",
               "port":3109,
               "isCluster": true,
               "name": "default",
               "service": "sqream",
               "ssl":true,
               "networkTimeout": 60000,
               "connectionTimeout": 3000
             }
           ]
         }
   
  Note that for the ``host`` value, you may use the IP address of your SQreamDB machine.  
   
5. If you have installed Studio on a server where SQream is already installed, move the **sqream-admin-config.json** file to **/etc/sqream/**:

   .. code-block:: console
     
      mv sqream-admin-config.json /etc/sqream

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Starting Studio
---------------

You can start Studio by running the following command:
 
.. code-block:: console
     
   cd /home/sqream/sqream-admin
   NODE_ENV=production pm2 start ./server/build/main.js --name=sqream-studio -- start --config-location=/etc/sqream/sqream-admin-config.json
 
The following output is displayed:

.. code-block:: console
     
   [PM2] Starting /home/sqream/sqream-admin/server/build/main.js in fork_mode (1 instance)
   [PM2] Done.
   ┌─────┬──────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
   │ id  │ name             │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
   ├─────┼──────────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
   │ 0   │ sqream-studio    │ default     │ 0.1.0   │ fork    │ 11540    │ 0s     │ 0    │ online    │ 0%       │ 15.6mb   │ sqream   │ disabled │
   └─────┴──────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘


1. If the **sqream-admin-config.json** file is not located in **/etc/sqream/**, run the following command:
 
     .. code-block:: console
     
        cd /home/sqream/sqream-admin
        NODE_ENV=production pm2 start ./server/build/main.js --name=sqream-studio -- start

2. To verify the process is running, use the ``pm2 list`` command:

     .. code-block::

	    pm2 list
		
2. Verify that Studio is running.
 
   .. code-block:: console
     
      netstat -nltp

3. Verify that SQream_studio is listening on port 8080, as shown below:

   .. code-block:: console

     (Not all processes could be identified, non-owned process info
      will not be shown, you would have to be root to see it all.)
     Active Internet connections (only servers)
     Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
     tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
     tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -
     tcp6       0      0 :::8080                 :::*                    LISTEN      11540/sqream-studio
     tcp6       0      0 :::22                   :::*                    LISTEN      -
     tcp6       0      0 ::1:25                  :::*                    LISTEN      -

	  

::
	
5. Verify the following:

   1. That you can access Studio from your browser (``http://<IP_Address>:8080``).
   
   ::  

   2. That you can log in to SQream.

6. Save the configuration to run on boot.
 
   .. code-block:: console
     
      pm2 startup
  
   The following is an example of the output:

   .. code-block:: console
     
      sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u sqream --hp /home/sqream

7. Copy and paste the output above and run it.

::

8. Save the configuration.

   .. code-block:: console
     
      pm2 save

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Accessing Studio
----------------

The Studio page is available on port 8080: ``http://<server ip>:8080``.

If port 8080 is blocked by the server firewall, you can unblock it by running the following command:
 
   .. code-block:: console
     
      firewall-cmd --zone=public --add-port=8080/tcp --permanent
      firewall-cmd --reload
 
Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Maintaining Studio with the Process Manager (PM2)
-------------------------------------------------

Sqream uses the **Process Manager (PM2)** to maintain Studio.
 
You can use PM2 to do one of the following:

* To check the PM2 service status: ``pm2 list``
   
   ::  

* To restart the PM2 service: ``pm2 reload sqream-studio``
   
   ::  

* To see the PM2 service logs: ``pm2 logs sqream-studio``

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Upgrading Studio
----------------

To upgrade Studio you need to stop the version that you currently have.

**To stop the current version of Studio:**

1. List the process name: 
 
   .. code-block:: console
     
      pm2 list
	  
   The process name is displayed.
 
   .. code-block:: console
   
      <process name>

::
	  
2. Run the following command with the process name:

   .. code-block:: console

      pm2 stop <process name>

::
		  
3. If only one process is running, run the following command:

   .. code-block:: console

      pm2 stop all

::
	
4. Change the name of the current **sqream-admin** folder to the old version.

   .. code-block:: console

      mv sqream-admin sqream-admin-<old_version>

::
	
5. Extract the new Studio version.

   .. code-block:: console

      tar -xf sqream-acceleration-studio-<version>tar.gz

::
	
6. Rebuild the configuration file. You can use IP address **127.0.0.1** on a single server.

   .. code-block:: console

      npm run setup -- -y --host=<SQreamD IP> --port=3108

  The above command creates the **sqream-admin-config.json** configuration file in the **sqream_admin** folder.

::
	
7. Copy the **sqream-admin-config.json** configuration file to **/etc/sqream/** to overwrite the old configuration file.
  
::  

8. Start PM2.

   .. code-block:: console

      pm2 start all

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

