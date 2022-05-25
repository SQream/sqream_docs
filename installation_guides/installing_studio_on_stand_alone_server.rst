.. _installing_studio_on_stand_alone_server:

.. _install_studio_top:

***********************
Installing Studio on a Stand-Alone Server
***********************
The **Installing Studio on a Stand-Alone Server** guide describes how to install SQream Studio on a stand-alone server. A stand-alone server is a server that does not run SQream based on binary files, Docker, or Kubernetes.

The Installing Studio on a Stand-Alone Server guide includes the following sections:

.. contents::
   :local:
   :depth: 1

Installing NodeJS Version 12 on the Server
^^^^^^^^^^^^^^^
Before installing Studio you must install NodeJS version 12 on the server.

**To install NodeJS version 12 on the server:**

1. Check if a version of NodeJS older than version *12.<x.x>* has been installed on the target server.

   .. code-block:: console
     
      $ node -v
      
   The following is the output if a version of NodeJS has already been installed on the target server:

   .. code-block:: console
     
      bash: /usr/bin/node: No such file or directory
  
2. If a version of NodeJS older than *12.<x.x>* has been installed, remove it as follows:

   * On CentOS:

     .. code-block:: console
     
        $ sudo yum remove -y nodejs

3. If you have not installed NodeJS version 12, run the following commands:

   * On CentOS:

     .. code-block:: console
     
        $ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash -
        $ sudo yum clean all && sudo yum makecache fast
        $ sudo yum install -y nodejs
		
  The following output is displayed if your installation has completed successfully:

  .. code-block:: console
     
     Transaction Summary
     ==============================================================================================================================
     Install  1 Package

     Total download size: 22 M
     Installed size: 67 M
     Downloading packages:
     warning: /var/cache/yum/x86_64/7/nodesource/packages/nodejs-12.22.1-1nodesource.x86_64.rpm: Header V4 RSA/SHA512 Signature, key ID 34fa74dd: NOKEY
     Public key for nodejs-12.22.1-1nodesource.x86_64.rpm is not installed
     nodejs-12.22.1-1nodesource.x86_64.rpm                                                                  |  22 MB  00:00:02
     Retrieving key from file:///etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL
     Importing GPG key 0x34FA74DD:
      Userid     : "NodeSource <gpg-rpm@nodesource.com>"
      Fingerprint: 2e55 207a 95d9 944b 0cc9 3261 5ddb e8d4 34fa 74dd
      Package    : nodesource-release-el7-1.noarch (installed)
      From       : /etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL
     Running transaction check
     Running transaction test
     Transaction test succeeded
     Running transaction
     Warning: RPMDB altered outside of yum.
       Installing : 2:nodejs-12.22.1-1nodesource.x86_64                                                                        1/1
       Verifying  : 2:nodejs-12.22.1-1nodesource.x86_64                                                                        1/1

     Installed:
       nodejs.x86_64 2:12.22.1-1nodesource

     Complete!

4. Confirm the Node version.

   .. code-block:: console
     
      $ node -v	  

  The following is an example of the correct output:
   
  .. code-block:: console
     
     v12.22.1

5. Install Prometheus using binary packages.

   For more information on installing Prometheus using binary packages, see :ref:`installing_prometheus_using_binary_packages`.

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`


	 
Installing Studio
^^^^^^^^^^^^^^^
After installing the Dashboard Data Collector, you can install Studio.
 
**To install Studio:**

1. Copy the SQream Studio package from SQream Artifactory into the target server. For access to the Sqream Studio package, contact SQream Support.

::

2. Extract the package:

   .. code-block:: console
     
      $ tar -xvf sqream-acceleration-studio-<version number>.x86_64.tar.gz

::
	
3. Navigate to the new package folder. 
 
   .. code-block:: console
     
      $ cd sqream-admin  
	  
.. _add_parameter:
	
4. Build the configuration file to set up Sqream Studio. You can use IP address **127.0.0.1** on a single server.
 
   .. code-block:: console
     
      $ npm run setup -- -y --host=<SQreamD IP> --port=3108 --data-collector-url=http://<data collector IP address>:8100/api/dashboard/data

   The above command creates the **sqream-admin-config.json** configuration file in the **sqream-admin** folder and shows the following output:
   
   .. code-block:: console
   
      Config generated successfully. Run `npm start` to start the app.

   For more information about the available set-up arguments, see :ref:`Set-Up Arguments<setup_arguments>`.

  ::
  
5. To access Studio over a secure connection, in your configuration file do the following:

   #. Change your ``port`` value to **3109**.
   
       ::
	   
   #. Change your ``ssl`` flag value to **true**.
   
      The following is an example of the correctly modified configuration file:
	  
      .. code-block:: console
     
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
   
5. If you have installed Studio on a server where SQream is already installed, move the **sqream-admin-config.json** file to **/etc/sqream/**:

   .. code-block:: console
     
      $ mv sqream-admin-config.json /etc/sqream

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Starting Studio Manually
^^^^^^^^^^^^^^^
You can start Studio manually by running the following command:
 
.. code-block:: console
     
   $ cd /home/sqream/sqream-admin
   $ NODE_ENV=production pm2 start ./server/build/main.js --name=sqream-studio -- start
 
The following output is displayed:

.. code-block:: console
     
   [PM2] Starting /home/sqream/sqream-admin/server/build/main.js in fork_mode (1 instance)
   [PM2] Done.
   ┌─────┬──────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
   │ id  │ name             │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
   ├─────┼──────────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
   │ 0   │ sqream-studio    │ default     │ 0.1.0   │ fork    │ 11540    │ 0s     │ 0    │ online    │ 0%       │ 15.6mb   │ sqream   │ disabled │
   └─────┴──────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘

Starting Studio as a Service
^^^^^^^^^^^^^^^
Sqream uses the **Process Manager (PM2)** to maintain Studio.

**To start Studio as a service:**

1. Run the following command:
 
   .. code-block:: console
     
      $ sudo npm install -g pm2

::
	   
2. Verify that the PM2 has been installed successfully.
 
   .. code-block:: console
     
      $ pm2 list

   The following is the output:

   .. code-block:: console     

     ┌─────┬──────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
     │ id  │ name             │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
     ├─────┼──────────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
     │ 0   │ sqream-studio    │ default     │ 0.1.0   │ fork    │ 11540    │ 2m     │ 0    │ online    │ 0%       │ 31.5mb   │ sqream   │ disabled │
     └─────┴──────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘

::

2. Start the service with PM2:

   * If the **sqream-admin-config.json** file is located in **/etc/sqream/**, run the following command:
 
     .. code-block:: console
     
        $ cd /home/sqream/sqream-admin
        $ NODE_ENV=production pm2 start ./server/build/main.js --name=sqream-studio -- start --config-location=/etc/sqream/sqream-admin-config.json

   * If the **sqream-admin-config.json** file is not located in **/etc/sqream/**, run the following command:
 
     .. code-block:: console
     
        $ cd /home/sqream/sqream-admin
        $ NODE_ENV=production pm2 start ./server/build/main.js --name=sqream-studio -- start

:: 
		
3. Verify that Studio is running.
 
   .. code-block:: console
     
      $ netstat -nltp

4. Verify that SQream_studio is listening on port 8080, as shown below:

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
     
      $ pm2 startup
  
   The following is an example of the output:

   .. code-block:: console
     
      $ sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u sqream --hp /home/sqream

7. Copy and paste the output above and run it.

::

8. Save the configuration.

   .. code-block:: console
     
      $ pm2 save

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Accessing Studio
^^^^^^^^^^^^^^^
The Studio page is available on port 8080: ``http://<server ip>:8080``.

If port 8080 is blocked by the server firewall, you can unblock it by running the following command:
 
   .. code-block:: console
     
      $ firewall-cmd --zone=public --add-port=8080/tcp --permanent
      $ firewall-cmd --reload
 
Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Maintaining Studio with the Process Manager (PM2)
^^^^^^^^^^^^^^^
Sqream uses the **Process Manager (PM2)** to maintain Studio.
 
You can use PM2 to do one of the following:

* To check the PM2 service status: ``pm2 list``
   
   ::  

* To restart the PM2 service: ``pm2 reload sqream-studio``
   
   ::  

* To see the PM2 service logs: ``pm2 logs sqream-studio``

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

Upgrading Studio
^^^^^^^^^^^^^^^
To upgrade Studio you need to stop the version that you currently have.

**To stop the current version of Studio:**

1. List the process name: 
 
   .. code-block:: console
     
      $ pm2 list
	  
   The process name is displayed.
 
   .. code-block:: console
   
      <process name>

::
	  
2. Run the following command with the process name:

   .. code-block:: console

      $ pm2 stop <process name>

::
		  
3. If only one process is running, run the following command:

   .. code-block:: console

      $ pm2 stop all

::
	
4. Change the name of the current **sqream-admin** folder to the old version.

   .. code-block:: console

      $ mv sqream-admin sqream-admin-<old_version>

::
	
5. Extract the new Studio version.

   .. code-block:: console

      $ tar -xf sqream-acceleration-studio-<version>tar.gz

::
	
6. Rebuild the configuration file. You can use IP address **127.0.0.1** on a single server.

   .. code-block:: console

      $ npm run setup -- -y --host=<SQreamD IP> --port=3108

  The above command creates the **sqream-admin-config.json** configuration file in the **sqream_admin** folder.

::
	
7. Copy the **sqream-admin-config.json** configuration file to **/etc/sqream/** to overwrite the old configuration file.
  
::  

8. Start PM2.

   .. code-block:: console

      $ pm2 start all

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`

.. _install_studio_docker_container:

Installing Studio in a Docker Container
^^^^^^^^^^^^^^^^^^^^^^^
This guide explains how to install SQream Studio in a Docker container and includes the following sections:

.. contents::
   :local:
   :depth: 1

Installing Studio
--------------
If you have already installed Docker, you can install Studio in a Docker container.

**To install Studio:**

1. Copy the downloaded image onto the target server.
  
::  

2. Load the Docker image.

   .. code-block:: console

      $ docker load -i <docker_image_file>

::
	
3. If the downloaded image is called **sqream-acceleration-studio-5.1.3.x86_64.docker18.0.3.tar,** run the following command:

   .. code-block:: console

      $ docker load -i sqream-acceleration-studio-5.1.3.x86_64.docker18.0.3.tar

::
	
4. Start the Docker container.

   .. code-block:: console

      $ docker run -d --restart=unless-stopped -p <external port>:8080 -e runtime=docker -e SQREAM_K8S_PICKER=<SQream host IP or VIP> -e SQREAM_PICKER_PORT=<SQream picker port> -e SQREAM_DATABASE_NAME=<SQream database name> -e SQREAM_ADMIN_UI_PORT=8080 --name=sqream-admin-ui <docker_image_name>

   The following is an example of the command above:

   .. code-block:: console

      $ docker run -d --name sqream-studio  -p 8080:8080 -e runtime=docker -e SQREAM_K8S_PICKER=192.168.0.183 -e SQREAM_PICKER_PORT=3108 -e SQREAM_DATABASE_NAME=master -e SQREAM_ADMIN_UI_PORT=8080 sqream-acceleration-studio:5.1.3

Back to :ref:`Installing Studio in a Docker Container<install_studio_docker_container>`

Accessing Studio
-----------------
You can access Studio from Port 8080: ``http://<server ip>:8080``.

If you want to use Studio over a secure connection (https), you must use the parameter values shown in the following table:
	 
.. list-table::
   :widths: 10 25 65
   :header-rows: 1  
   
   * - Parameter
     - Default Value
     - Description
   * - ``--web-ssl-port``
     - 8443
     - 
   * - ``--web-ssl-key-path``
     - None
     - The path of SSL key PEM file for enabling https. Leave empty to disable.
   * - ``--web-ssl-cert-path``
     - None
     - The path of SSL certificate PEM file for enabling https. Leave empty to disable.	 

You can configure the above parameters using the following syntax:

.. code-block:: console

  $ npm run setup -- -y --host=127.0.0.1 --port=3108
  
.. _using_docker_container_commands:

Back to :ref:`Installing Studio in a Docker Container<install_studio_docker_container>`

Using Docker Container Commands
---------------
When installing Studio in Docker, you can run the following commands:

* View Docker container logs:

  .. code-block:: console

     $ docker logs -f sqream-admin-ui
	  
* Restart the Docker container: 

  .. code-block:: console

     $ docker restart sqream-admin-ui
	  
* Kill the Docker container:

  .. code-block:: console

     $ docker rm -f sqream-admin-ui
      
Back to :ref:`Installing Studio in a Docker Container<install_studio_docker_container>`

Setting Up Argument Configurations
----------------
When creating the **sqream-admin-config.json** configuration file, you can add ``-y`` to create the configuration file in non-interactive mode. Configuration files created in non-interactive mode use all the parameter defaults not provided in the command.

The following table shows the available arguments:

.. list-table::
   :widths: 10 25 65
   :header-rows: 1  
   
   * - Parameter
     - Default Value
     - Description
   * - ``--web--host``
     - 8443
     - 
   * - ``--web-port``
     - 8080
     - 
   * - ``--web-ssl-port``
     - 8443
     - 
   * - ``--web-ssl-key-path``
     - None
     - The path of the SSL Key PEM file for enabling https. Leave empty to disable.
   * - ``--web-ssl-cert-path``
     - None
     - The path of the SSL Certificate PEM file for enabling https. Leave empty to disable.
   * - ``--debug-sqream (flag)``
     - false
     - 
   * - ``--host``
     - 127.0.0.1
     - 
   * - ``--port``
     - 3108
     - 
   * - ``is-cluster (flag)``
     - true
     - 
   * - ``--service``
     - sqream
     - 
   * - ``--ssl (flag)``
     - false
     - Enables the SQream SSL connection.
   * - ``--name``
     - default
     - 
   * - ``--data-collector-url``
     - localhost:8100/api/dashboard/data
     - Enables the Dashboard. Leaving this blank disables the Dashboard. Using a mock URL uses mock data.
   * - ``--cluster-type``
     - standalone (``standalone`` or ``k8s``)
     - 
   * - ``--config-location``
     - ./sqream-admin-config.json
     - 
   * - ``--network-timeout``
     - 60000 (60 seconds)
     - 
   * - ``--access-key``
     - None
     - If defined, UI access is blocked unless ``?ui-access=<access key>`` is included in the URL.
	 
Back to :ref:`Installing Studio in a Docker Container<install_studio_docker_container>`

  ::	 

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`