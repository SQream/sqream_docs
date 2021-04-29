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
SQream lets you use set up your hosts.

**Comment - the Confluence doc cross references the user to the "Configure Hosts" section in the "Prerequisites" page:**

**https://sqream.atlassian.net/wiki/spaces/DOC/pages/17170437/SQream+production+server+and+OS+pre-requisites#Configure-%2Fetc%2Fhosts%3A**

**If that is the only relevant procedure for "Setting Up Hosts," it can be written here instead of making a cross reference.**

Setting up your hosts requires you to verify the following:

* User ID
* Installing required packages
* Disable Linux UI (if installed)
* IP Forwarding
* Disable SELinux
* Disable SWAP
* Cuda

Verifying User ID
------------------
1. Verify that the new user's ID is identical across all servers:

   .. code-block:: postgres
   
      $ id
      
   Verifying that the new user's ID generates the following output:
   
   .. code-block:: postgres
   
      $ iduid=1000(sqream) gid=1000(sqream) groups=1000(sqream),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

2. If the **uid** and the **groupid** values are not identical across all nodes, update them so that they are identical.

   In the example below, the **uid** and **groupid** are changed from **1000** to **2000**:
   
   .. code-block:: postgres
   
      $ usermod -u 2000 sqream
      $ groupmod -g 2000 sqream

Installing the Required Packages
---------------------------------
You can install the required packages as follows:

   .. code-block:: postgres
   
      $ sudo yum install ntp  pciutils python36 python36-pip kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc jq net-tools
      
Disabling Linux
----------------------------------
If Linux has been installed, you can disable it as follows:

   .. code-block:: postgres
   
      $ sudo systemctl set-default multi-user.target

Enabling ID Forwarding
-----------------------------------
**IP Forwarding** must be enabled for Kubernetes and Docker.

**Comment - Why is Docker mentioned here?**

1. Check if IP Forwarding has been enabled:

   .. code-block:: postgres
   
      $ sysctl net.ipv4.ip_forward
      
   If the output shows **net.ipv41p_forward = 1**, IP Forwarding is enabled. If the output shows **net.ipv41p_forward = 0**, IP Forwarding is disabled.
   
2. If IP Forwarding is disabled, enable it.

   The following command lets you enable IP Forwarding without rebooting the system:

   .. code-block:: postgres
   
      $ echo 1 > /proc/sys/net/ipv4/ip_forward
      
3. If you have not enabled **ipv4 forwarding,** enable it when the system has rebooted.

4. Open the **/etc/sysctl.conf** configuration file for editing:

   .. code-block:: postgres
   
      $ sudo vim /etc/sysctl.conf
      
      bytesread
      ---------
      v<xxxx.x>
      
      
      
5. Append the following line at the end of the file:

   **Comment - at the end of the name of the file?**

   .. code-block:: postgres
   
      $ net.ipv4.ip_forward = 1

6. Reboot the system.

   **Comment - see Step 3. Why is that Step written in that order when Step 6 is to reboot the system?**

7. Verify that output is **1**:

   .. code-block:: postgres
   
      $ cat /proc/sys/net/ipv4/ip_forward      
      
 Disabling Linux
 ----------------------------------
 In some installations, System Administration installs the server operating system with SWAP enabled. SWAP must be disabled.
 
 1. Check if SWAP is enabled:
 
    If SWAP is enabled, 
      
      
      
      
      


