.. _installing_prometheus_exporters:

*********************************************
Installing Prometheus Exporter
*********************************************

The **Installing Prometheus Exporters** guide includes the following sections:

.. contents::
   :local:
   :depth: 1

Overview
==============================
The **Prometheus** exporter is an open-source systems monitoring and alerting toolkit. It is used for collecting metrics from an operating system and exporting them to a graphic user interface. 

The Installing Prometheus Exporters guide describes how to installing the following exporters:

* The **Node_exporter** - the basic exporter used for displaying server metrics, such as CPU and memory.

* The **Nvidia_exporter** - shows Nvidia GPU metrics.

* The **process_exporter** - shows data belonging to the server's running processes.

For information about more exporters, see `Exporters and Integration <https://prometheus.io/docs/instrumenting/exporters/>`_

Adding a User and Group
=====================
Adding a user and group determines who can run processes.

You can add users with the following command:

.. code-block:: console
     
   $ sudo groupadd --system prometheus
	  
You can add groups with the following command:

.. code-block:: console
     
   $ sudo useradd -s /sbin/nologin --system -g prometheus prometheus

Cloning the Prometheus GIT Project
=====================
After adding a user and group you must clone the Prometheus GIT project.

You can clone the Prometheus GIT project with the following command:

.. code-block:: console
     
   $ git clone http://gitlab.sq.l/IT/promethues.git prometheus
	  
.. note:: If you experience difficulties cloning the Prometheus GIT project or receive an error, contact your IT department.

The following shows the result of cloning your Prometheus GIT project:

.. code-block:: console
     
   $ prometheus/
   $ ├── node_exporter
   $ │   └── node_exporter
   $ ├── nvidia_exporter
   $ │   └── nvidia_exporter
   $ ├── process_exporter
   $ │   └── process-exporter_0.5.0_linux_amd64.rpm
   $ ├── README.md
   $ └── services
   $     ├── node_exporter.service
   $     └── nvidia_exporter.service	  
	  
Installing the Node Exporter and NVIDIA Exporter
=====================
After cloning the Prometheus GIT project you must install the **node_exporter** and **NVIDIA_exporter**.

**To install the node_exporter and NVIDIA_exporter:**

1. Navigate to the cloned folder:

   .. code-block:: console
     
      $ cd prometheus
   
2. Copy **node_exporter** and **nvidia_exporter** to **/usr/bin/**.	  

   .. code-block:: console
     
      $ sudo cp node_exporter/node_exporter /usr/bin/
      $ sudo cp nvidia_exporter/nvidia_exporter /usr/bin/
   	  
3. Copy the **services** files to the services folder:	  

   .. code-block:: console
     
      $ sudo cp services/node_exporter.service /etc/systemd/system/
      $ sudo cp services/nvidia_exporter.service /etc/systemd/system/
   	  
4. Reload the services so that they can be run:	  

   .. code-block:: console
     
      $ sudo systemctl daemon-reload  
   	  
5. Set the permissions and group for both service files:

   .. code-block:: console
     
      $ sudo chown prometheus:prometheus /usr/bin/node_exporter
      $ sudo chmod u+x /usr/bin/node_exporter
      $ sudo chown prometheus:prometheus /usr/bin/nvidia_exporter
      $ sudo chmod u+x /usr/bin/nvidia_exporter
   
6. Start both services:

   .. code-block:: console
     
      $ sudo systemctl start node_exporter && sudo systemctl enable node_exporter
   
7. Set both services to start automatically when the server is booted up:

   .. code-block:: console

      $ sudo systemctl start nvidia_exporter && sudo systemctl enable nvidia_exporter
   
8. Verify that the server's status is **active (running)**:

   .. code-block:: console
     
      $ sudo systemctl status node_exporter && sudo systemctl status nvidia_exporter
   
   The following is the correct output:

   .. code-block:: console
     
      $ ● node_exporter.service - Node Exporter
      $    Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: disabled)
      $    Active: active (running) since Wed 2019-12-11 12:28:31 IST; 1 months 5 days ago
      $  Main PID: 28378 (node_exporter)
      $    CGroup: /system.slice/node_exporter.service
      $ 
      $ ● nvidia_exporter.service - Nvidia Exporter
      $    Loaded: loaded (/etc/systemd/system/nvidia_exporter.service; enabled; vendor preset: disabled)
      $    Active: active (running) since Wed 2020-01-22 13:40:11 IST; 31min ago
      $  Main PID: 1886 (nvidia_exporter)
      $    CGroup: /system.slice/nvidia_exporter.service
      $            └─1886 /usr/bin/nvidia_exporter
   	  
Installing the Process Exporter
=====================
After installing the **node_exporter** and **Nvidia_exporter** you must install the **process_exporter**.

**To install the process_exporter:**

1. Do one of the following:

   * For **CentOS**, run ``sudo rpm -i process_exporter/process-exporter_0.5.0_linux_amd64.rpm``.
   * For **Ubuntu**, run ``sudo dpkg -i process_exporter/process-exporter_0.6.0_linux_amd64.deb``.
   
2. Verify that the process_exporter is running:

   .. code-block:: console
     
      $ sudo systemctl status process-exporter  
	  
3. Set the process_exporter to start automatically when the server is booted up:
	  
   .. code-block:: console
     
      $ sudo systemctl enable process-exporter
	  
Opening the Firewall Ports
=====================
After installing the **process_exporter** you must open the firewall ports for the following services:

* **node_exporter** - port: 9100

* **nvidia_exporter** - port: 9445

* **process-exporter** - port: 9256

.. note:: This procedure is only relevant if your firwall is running.

**To open the firewall ports:**

1. Run the following command:
	  
   .. code-block:: console
     
      $ sudo firewall-cmd --zone=public --add-port=<PORT NUMBER>/tcp --permanent
	  
2. Reload the firewall:
	  
   .. code-block:: console
     
      $ sudo firewall-cmd --reload
	  
3. Verify that the changes have taken effect.