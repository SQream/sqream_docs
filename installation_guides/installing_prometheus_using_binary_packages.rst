.. _installing_prometheus_using_binary_packages:

.. _install_prometheus_binary_top:

***********************
Installing Prometheus Using Binary Packages
***********************



The **Installing Prometheus Using Binary Packages** guide includes the following sections:

.. contents::
   :local:
   :depth: 1

Overview
^^^^^^^^^^^^^^^
Prometheus is an application used for event monitoring and alerting.

Installing Prometheus
^^^^^^^^^^^^^^^
You must install Prometheus before installing the Dashboard Data Collector.

**To install Prometheus:**

1. Verify the following:

   1. That you have **sudo** access to your Linux server.
   2. That your server has access to the internet (for downloading the Prometheus binary package).
   3. That your firewall rules are opened for accessing Prometheus Port 9090.
   
2. Navigate to the Prometheus `Download <https://prometheus.io/download/>`_ page and download the **prometheus-2.32.0-rc.1.linux-amd64.tar.gz** package.

    ::

3. Do the following:

   1. Download the source using the ``curl`` command:

      .. code-block:: console
     
         $ curl -LO url -LO https://github.com/prometheus/prometheus/releases/download/v2.22.0/prometheus-2.22.0.linux-amd64.tar.gz

   2. Extract the file contents:

      .. code-block:: console
     
         $ tar -xvf prometheus-2.22.0.linux-amd64.tar.gz

   3. Rename the extracted folder **prometheus-files**:

      .. code-block:: console
     
         $ mv prometheus-2.22.0.linux-amd64 prometheus-files

4. Create a Prometheus user:

   .. code-block:: console
     
      $ sudo useradd --no-create-home --shell /bin/false prometheus

5. Create your required directories:

   .. code-block:: console
     
      $ sudo mkdir /etc/prometheus
      $ sudo mkdir /var/lib/prometheus
	  
6. Set the Prometheus user as the owner of your required directories:

   .. code-block:: console
     
      $ sudo chown prometheus:prometheus /etc/prometheus
      $ sudo chown prometheus:prometheus /var/lib/prometheus
	  
7. Copy the Prometheus and Promtool binary packages from the **prometheus-files** folder to **/usr/local/bin**:

   .. code-block:: console
     
      $ sudo cp prometheus-files/prometheus /usr/local/bin/
      $ sudo cp prometheus-files/promtool /usr/local/bin/

8. Change the ownership to the prometheus user:

   .. code-block:: console
     
      $ sudo chown prometheus:prometheus /usr/local/bin/prometheus
      $ sudo chown prometheus:prometheus /usr/local/bin/promtool

9. Move the **consoles** and **consoles_libraries** directories from **prometheus-files** folder to **/etc/prometheus** folder:

   .. code-block:: console
     
      $ sudo cp -r prometheus-files/consoles /etc/prometheus
	  $ sudo cp -r prometheus-files/console_libraries /etc/prometheus

10. Change the ownership to the prometheus user:

    .. code-block:: console
     
       $ sudo chown -R prometheus:prometheus /etc/prometheus/consoles
       $ sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries

For more information on installing the Dashboard Data Collector, see `Installing the Dashboard Data Collector <https://docs.sqream.com/en/v2021.2/installation_guides/installing_dashboard_data_collector.html>`_.

Back to :ref:`Installing Prometheus Using Binary Packages<install_prometheus_binary_top>`

Configuring Your Prometheus Settings
^^^^^^^^^^^^^^^
After installing Prometheus you must configure your Prometheus settings. You must perform all Prometheus configurations in the **/etc/prometheus/prometheus.yml** file.

**To configure your Prometheus settings:**

1. Create your **prometheus.yml** file:

   .. code-block:: console
     
      $ sudo vi /etc/prometheus/prometheus.yml
	  
2. Copy the contents below into your prometheus.yml file:

   .. code-block:: console
     
      $ #node_exporter port : 9100
      $ #nvidia_exporter port: 9445
      $ #process-exporter port: 9256
      $ 
      $ global:
      $   scrape_interval: 10s
      $ 
      $ scrape_configs:
      $   - job_name: 'prometheus'
      $     scrape_interval: 5s
      $     static_configs:
      $       - targets:
      $         - <prometheus server IP>:9090
      $   - job_name: 'processes'
      $     scrape_interval: 5s
      $     static_configs:
      $       - targets:
      $         - <process exporters iP>:9256
      $         - <another process exporters iP>:9256
      $   - job_name: 'nvidia'
      $     scrape_interval: 5s
      $     static_configs:
      $       - targets:
      $         - <nvidia exporter IP>:9445
      $         - <another nvidia exporter IP>:9445
      $   - job_name: 'nodes'
      $     scrape_interval: 5s
      $     static_configs:
      $       - targets:
      $         - <node exporter IP>:9100
      $         - <another node exporter IP>:9100
  
3. Change the ownership of the file to the prometheus user:

   .. code-block:: console
     
      $ sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml
	  
Back to :ref:`Installing Prometheus Using Binary Packages<install_prometheus_binary_top>`

Configuring Your Prometheus Service File	  
^^^^^^^^^^^^^^^
After configuring your Prometheus settings you must configure your Prometheus service file.

**To configure your Prometheus service file**:

1. Create your **prometheus.yml** file:

   .. code-block:: console
     
      $ sudo vi /etc/systemd/system/prometheus.service
	  
2. Copy the contents below into your prometheus service file:

   .. code-block:: console
     
      $ [Unit]
      $ Description=Prometheus
      $ Wants=network-online.target
      $ After=network-online.target
      $ 
      $ [Service]
      $ User=prometheus
      $ Group=prometheus
      $ Type=simple
      $ ExecStart=/usr/local/bin/prometheus \
      $     --config.file /etc/prometheus/prometheus.yml \
      $     --storage.tsdb.path /var/lib/prometheus/ \
      $     --web.console.templates=/etc/prometheus/consoles \
      $     --web.console.libraries=/etc/prometheus/console_libraries
      $ 
      $ [Install]
      $ WantedBy=multi-user.target

3. Register the prometheus service by reloading the **systemd** service:

   .. code-block:: console
     
      $ sudo systemctl daemon-reload
	  
4. Start the prometheus service:

   .. code-block:: console
     
      $ sudo systemctl start prometheus

5. Check the status of the prometheus service:

   .. code-block:: console
     
      $ sudo systemctl status prometheus
	  
 If the status is ``active (running)``, you have configured your Prometheus service file correctly.

Back to :ref:`Installing Prometheus Using Binary Packages<install_prometheus_binary_top>`

Accessing the Prometheus User Interface
^^^^^^^^^^^^^^^
After configuring your prometheus service file, you can access the Prometheus user interface.

You can access the Prometheus user interface by running the following command:

.. code-block:: console
     
   $ http://<prometheus-ip>:9090/graph

The Prometheus user interface is displayed.

From the **Query** tab you can query metrics.

Back to :ref:`Installing Prometheus Using Binary Packages<install_prometheus_binary_top>`