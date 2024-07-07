.. _root_cause_analysis:

*******************
Root Cause Analysis
*******************

The Root Cause Analysis (RCA) service enhances observability, enabling shorter investigation times and facilitating both high-level and detailed drill-downs by automatically executing the :ref:`export_open_snapshots` and :ref:`get_open_snapshots` utility functions. 

.. contents::
   :local:
   :depth: 1

Before You Begin
================

It is essential that you follow these prerequisites:

* Log files must be saved as ``JSON`` files

Usage Notes
===========

By default, logs are saved as ``CSV`` files. To configure your log files to be saved as ``JSON`` instead, use the ``logFormat`` flag in your :ref:`legacy config file<current_method_flag_types>`. If your current logs are in ``CSV`` format and you require RCA, it's advisable to configure your logs to be saved in both ``CSV`` and ``JSON`` formats as outlined above.

.. note:

	The ``logFormat`` flag must be configured identically in both your legacy_config_file and your metadata_config_file

Installation
============

All RCA-related installations are on a stand-alone installations.  

Grafana
-------

Grafana is an open-source analytics and monitoring platform that visualizes data and is used to create dashboards that display real-time and historical data.

Manual Execution
~~~~~~~~~~~~~~~~

#. Download Grafana.

#. Start the Grafana server:

   .. code-block:: console

      /usr/share/grafana/bin/grafana server --config=/etc/grafana/grafana.ini --pidfile=/var/run/grafana/grafana-server.pid --packaging=rpm cfg:default.paths.logs=/var/log/grafana cfg:default.paths.data=/var/lib/grafana cfg:default.paths.plugins=/var/lib/grafana/plugins cfg:default.paths.provisioning=/etc/grafana/provisioning

Setting Linux Service
~~~~~~~~~~~~~~~~~~~~~

#. Create Service:

   .. code-block:: console

(Set the command above (case 2) as a linux service) -Slavi
 
#. Start the Grafa service:

   .. code-block:: console

      sudo systemctl <start / stop / restart> grafana-server.service

#. To view logs:

   .. code-block:: console

      journalctl -xe

Prometheus
----------

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. Prometheus can be used to scrape and store metrics, enabling real-time monitoring, alerting, and analysis of performance and health.

#. Download Prometheus.

#. (Prometheus Exporter installation) -Slavi

#. Set the YML path:

   .. code-block:: console

      PROMETHEUS_YML_PATH=<GRAFANA_PROJECT_PATH>/ymls/prometheus.yml

#. Start Prometheus server:

   .. code-block:: console

      sudo /usr/local/bin/prometheus --config.file <PROMETHEUS_YML_PATH> --storage.tsdb.path /var/lib/prometheus/ --web.console.templates=/etc/prometheus/consoles --web.console.libraries=/etc/prometheus/console_libraries &> prometheus.out &

Loki and Promtail
-----------------

Loki is a log aggregation system designed to store and query logs, while Promtail is an agent that collects logs and forwards them to Loki.

#. Download Loki and Promtail to ``<LOKI_PROJECT_PATH>``.

#. Set the Loki YML path:

   .. code-block:: console

      LOKI_YML_PATH=<GRAFANA_PROJECT_PATH>/ymls/loki-local-config.yaml

#. Set the Promtail YML path:

   .. code-block:: console

      PROMTAIL_YML_PATH=<GRAFANA_PROJECT_PATH>/ymls/promtail-local-config.yml   

#. Start Loki server:

   .. code-block:: console

      sudo <LOKI_PROJECT_PATH>/loki-linux-amd64 -config.file=<LOKI_YML_PATH> &> ~/loki.out &

#. Start Promtail server:

   .. code-block:: console

      sudo <LOKI_PROJECT_PATH>/promtail-linux-amd64 -config.file=<PROMTAIL_YML_PATH> &> ~/promtail.out &

Tempo
-----

Tempo is an open-source distributed tracing system designed to handle high volumes of trace data. Tempo can be used to trace database transactions and operations across distributed systems, providing insights into performance bottlenecks and aiding in troubleshooting complex queries.

#. `Download and install <https://grafana.com/docs/tempo/latest/setup/linux/>`_ Tempo.

#. Set the Tempo YML path:

   .. code-block:: console

      TEMPO_YML_PATH=<GRAFANA_PROJECT_PATH>/ymls/tempo.yml

#. Start Tempo server:

   .. code-block:: console

      /usr/bin/tempo -config.file /etc/tempo/config.yml &> ~/tempo.out &

Exporters
---------

An Exporter is a software component that gathers metrics from various sources (such as hardware, software, or services) and exposes them in a format that Prometheus can scrape and store.

GPU Exporter
~~~~~~~~~~~~



CPU Exporter
~~~~~~~~~~~~

#. Download the `CPU Exporter <https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-386.tar.gz>`_.

#. Start the Exporter:

   .. code-block:: console

      /usr/bin/node_exporter &> ~/node_exporter.out &

Process Exporter
~~~~~~~~~~~~~~~~

#. (Prometheus Exporter installation)-Slavi

#. Start the Exporter:

   .. code-block:: console

      /usr/bin/process-exporter --config.path /etc/process-exporter/all.yaml --web.listen-address=:9256 &> process_exporter.out &

SQream Dashboards
=================

https://sqream.atlassian.net/wiki/spaces/~477790253/pages/3134488697/RCA+-+Grafana+installation 

-Slavi

