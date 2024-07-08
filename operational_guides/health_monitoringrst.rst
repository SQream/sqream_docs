.. _health_monitoring:

*****************
Health Monitoring
*****************

The Health Monitoring service enhances observability, enabling shorter investigation times and facilitating both high-level and detailed drill-downs.

.. contents::
   :local:
   :depth: 1

Before You Begin
================

It is essential that you follow these prerequisites:

* :ref:`Log files<log_structure>` must be saved as ``JSON`` files

* :ref:`Set the path<export_open_snapshots>` to where you wish your open snapshot information be saved 

* Configure `Grafana authentication <https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/grafana/>`_, even if you're using `LDAP <https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/ldap/>`_ for authentication management


Installation
============

All Health Monitoring-related installations are on a stand-alone installations.  

Grafana
-------

Grafana is an open-source analytics and monitoring platform that visualizes data and is used to create dashboards that display real-time and historical data.

You may use both Grafana's open source version and its enterprise version, depending on your needs.

See `Grafana specification <https://grafana.com/docs/grafana/latest/setup-grafana/installation/#hardware-recommendations>`_

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

Best Practices
==============

Daily Usage
-----------

Grafana Alerts
--------------

Investigating Health Issues
---------------------------

Dealing with Open Snapshots
---------------------------

Dealing with Unreleased Locks
-----------------------------

Dealing with Slow Metadata
--------------------------

Dealing with Growing Statement Queue
------------------------------------

Dealing with Slow Workers
-------------------------

Dealing with Hung Workers
-------------------------

