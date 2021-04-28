.. _installing_sqream_with_kubernetes:

*********************************************
Installing SQream with Kubernetes
*********************************************

Overview
========
The **Installing SQream with Kubernetes** guide describes the following:

* How to prepare the SQream environment for installing SQream using Kubernetes.
* Install the SQream software using a Kubernetes package.

**Kubernetes**, also known as **k8s**, is a portable open source platform that automates Linux container operations. Kubernetes supports outsourcing data centers to public cloud service providers or can be scaled for web hosting. SQream uses Kubernetes as an orchestration and recovery solution.

Getting Started
===============
A minimum of three servers is required when installing SQream using Kubernetes.

Kubernetes uses clusters, which are sets of nodes running containterized applications. A cluster consists of at least 2 GPU nodes and 1 slim server to act as Quorum manager. All three servers are set as **master.**

**Comment - what does this mean? 2 servers with GPU and 1 without.**   

Each server must have the following IP addresses:

* An IP address located in the management network.
* An additional IP address from the same subnet to function as a floating IP.

All servers must be mounted in the same shared storage folder.

The following list shows the server host name format requirements:

* A maximum of 253 characters.
* Only lowercase alphanumeric characters, such as **-** or **.**.
* Starts and ends with alphanumeric characters.

Operating System Requirements
------------------------------
Installing SQream with Kubernetes includes the following operating system requirements:

* SQream tested and verified on x86 CentOS version higher than 7.6.
* SWAP disabled on all nodes.

Compute Server Specifications
------------------------------
Installing SQream with Kubernetes includes the following compute server specifications:

* **CPU:** 4 cores
* **RAM:** 16GB
* **HD:** 500GB

Setting Up Hosts
===============================
