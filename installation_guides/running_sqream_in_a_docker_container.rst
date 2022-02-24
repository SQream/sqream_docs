.. _running_sqream_in_a_docker_container:



***********************
Installing and Running SQream in a Docker Container
***********************
The **Running SQream in a Docker Container** page describes how to prepare your machine's environment for installing and running SQream in a Docker container.

This page describes the following:

.. contents::
   :local:
   :depth: 1 

Setting Up a Host
====================================

Operating System Requirements
------------------------------------
SQream was tested and verified on the following versions of Linux:

  * x86 CentOS/RHEL 7.6 - 7.9
  * IBM RHEL 7.6
  
SQream recommends installing a clean OS on the host to avoid any installation issues.
  
.. warning:: Docker-based installation supports only single host deployment and cannot be used on a multi-node cluster. Installing Docker on a single host you will not be able to scale it to a multi-node cluster.

Creating a Local User
----------------
To run SQream in a Docker container you must create a local user.

**To create a local user:**

1. Add a local user:

   .. code-block:: console
     
      $ useradd -m -U <local user name>

2. Set the local user's password:

   .. code-block:: console
     
      $ passwd <local user name>

3. Add the local user to the ``wheel`` group:

   .. code-block:: console
     
      $ usermod -aG wheel <local user name>

   You can remove the local user from the ``wheel`` group when you have completed the installation.

4. Log out and log back in as the local user.

Setting a Local Language
----------------
After creating a local user you must set a local language.

**To set a local language:**

1. Set the local language:

   .. code-block:: console
     
      $ sudo localectl set-locale LANG=en_US.UTF-8

2. Set the time stamp (time and date) of the locale:

   .. code-block:: console

      $ sudo timedatectl set-timezone Asia/Jerusalem

You can run the ``timedatectl list-timezones`` command to see your timezone.

Adding the EPEL Repository
----------------
After setting a local language you must add the EPEL repository.

**To add the EPEL repository:**

1. As a root user, upgrade the **epel-release-latest-7.noarch.rpm** repository:

   1. RedHat (RHEL 7):

   .. code-block:: console

      $ sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
      
   2. CentOS 7
    
   .. code-block:: console

      $ sudo yum install epel-release

Installing the Required NTP Packages
----------------
After adding the EPEL repository, you must install the required NTP packages.

You can install the required NTP packages by running the following command:

.. code-block:: console

   $ sudo yum install ntp  pciutils python36 kernel-devel-$(uname -r) kernel-headers-$(uname -r) 	gcc

Installing the Recommended Tools
----------------
After installin gthe required NTP packages you must install the recommended tools.

SQream recommends installing the following recommended tools:

.. code-block:: console

   $ sudo yum install bash-completion.noarch  vim-enhanced.x86_64 vim-common.x86_64 net-tools iotop htop psmisc screen xfsprogs wget yum-utils deltarpm dos2unix

Updating to the Current Version of the Operating System
----------------
After installing the recommended tools you must update to the current version of the operating system.

SQream recommends updating to the current version of the operating system. This is not recommended if the nvidia driver has **not been installed.**

Configuring the NTP Package
----------------
After updating to the current version of the operating system you must configure the NTP package.

**To configure the NTP package:**

1. Add your local servers to the NTP configuration.

    ::

2. Configure the **ntpd** service to begin running when your machine is started:

   .. code-block:: console

      $ sudo systemctl enable ntpd
      $ sudo systemctl start ntpd
      $ sudo ntpq -p

Configuring the Performance Profile
----------------
After configuring the NTP package you must configure the performance profile.

**To configure the performance profile:**

1. Switch the active profile:

   .. code-block:: console

      $ sudo tuned-adm profile throughput-performance 

2. Change the multi-user's default run level:

   .. code-block:: console

      $ sudo systemctl set-default multi-user.target

Configuring Your Security Limits
----------------
After configuring the performance profile you must configure your security limits. Configuring your security limits refers to configuring the number of open files, processes, etc.

**To configure your security limits:**

1. Run the **bash** shell as a super-user: 

   .. code-block:: console

      $ sudo bash

2. Run the following command:

   .. code-block:: console

      $ echo -e "sqream soft nproc 500000\nsqream hard nproc 500000\nsqream soft nofile 500000\nsqream hard nofile 500000\nsqream soft core unlimited\nsqream hard core unlimited" >> /etc/security/limits.conf

3. Run the following command:

   .. code-block:: console

      $ echo -e "vm.dirty_background_ratio = 5 \n vm.dirty_ratio = 10 \n vm.swappiness = 10 \n vm.zone_reclaim_mode = 0 \n vm.vfs_cache_pressure = 200 \n"  >> /etc/sysctl.conf

Disabling Automatic Bug-Reporting Tools
----------------
After configuring your security limits you must disable the following automatic bug-reporting tools:

* ccpp.service
* oops.service
* pstoreoops.service
* vmcore.service
* xorg.service

You can abort the above but-reporting tools by running the following command:

.. code-block:: console

   $ for i in abrt-ccpp.service abrtd.service abrt-oops.service abrt-pstoreoops.service abrt-vmcore.service abrt-xorg.service ; do sudo systemctl disable $i; sudo systemctl stop $i; done
   
Installing the Nvidia CUDA Driver
-------------------------------------
**To install the Nvidia CUDA driver:**

1. Verify that the Tesla NVIDIA card has been installed and is detected by the system:

   .. code-block:: console

      $ lspci | grep -i nvidia

   The correct output is a list of Nvidia graphic cards. If you do not receive this output, verify that an NVIDIA GPU card has been installed.

#. Verify that the open-source upstream Nvidia driver is running:

   .. code-block:: console

      $ lsmod | grep nouveau

   No output should be generated.

#. If you receive any output, do the following:

   1. Disable the open-source upstream Nvidia driver:

      .. code-block:: console

         $ sudo bash
         $ echo "blacklist nouveau" > /etc/modprobe.d/blacklist-nouveau.conf
         $ echo "options nouveau modeset=0"  >> /etc/modprobe.d/blacklist-nouveau.conf
         $ dracut --force
         $ modprobe --showconfig | grep nouveau
    
   2. Reboot the server and verify that the Nouveau model has not been loaded:

      .. code-block:: console

         $ lsmod | grep nouveau
	 
#. Check if the Nvidia CUDA driver has already been installed:

   .. code-block:: console

      $ nvidia-smi

   The following is an example of the correct output:

   .. code-block:: console

      nvidia-smi
      Wed Oct 30 14:05:42 2019
      +-----------------------------------------------------------------------------+
      | NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
      |-------------------------------+----------------------+----------------------+
      | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
      | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
      |===============================+======================+======================|
      |   0  Tesla V100-SXM2...  On   | 00000004:04:00.0 Off |                    0 |
      | N/A   32C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      |   1  Tesla V100-SXM2...  On   | 00000035:03:00.0 Off |                    0 |
      | N/A   33C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      
      +-----------------------------------------------------------------------------+
      | Processes:                                                       GPU Memory |
      |  GPU       PID   Type   Process name                             Usage      |
      |=============================================================================|
      |  No running processes found                                                 |
      +-----------------------------------------------------------------------------+

#. Verify that the installed CUDA version shown in the output above is ``10.1``.
    
	::


#. Do one of the following:

    ::
   
   1. If CUDA version 10.1 has already been installed, skip to Docktime Runtime (Community Edition).
    ::

   2. If CUDA version 10.1 has not been installed yet, continue with Step 7 below.

#. Do one of the following:

   * Install :ref:`CUDA Driver version 10.1 for x86_64 <CUDA_10.1_x8664>`.
   
      ::
	  
   * Install :ref:`CUDA driver version 10.1 for IBM Power9 <CUDA_10.1_IBMPower9>`.

.. _CUDA_10.1_x8664:

Installing the CUDA Driver Version 10.1 for x86_64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the CUDA driver version 10.1 for x86_64:**

1. Make the following target platform selections:
   
    ::

   * **Operating system**: Linux
   * **Architecture**: x86_64
   * **Distribution**: CentOS
   * **Version**: 7
   * **Installer type**: the relevant installer type

For installer type, SQream recommends selecting **runfile (local)**. The available selections shows only the supported platforms.

2. Download the base installer for Linux CentOS 7 x86_64:

   .. code-block:: console

      wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.x86_64.rpm


3. Install the base installer for Linux CentOS 7 x86_64 by running the following commands:

   .. code-block:: console

      $ sudo yum localinstall cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.x86_64.rpm
      $ sudo yum clean all
      $ sudo yum install nvidia-driver-latest-dkms

.. warning:: Verify that the output indicates that driver **418.87** will be installed.

4. Follow the command line prompts.


    ::


5. Enable the Nvidia service to start at boot and start it:

   .. code-block:: console

      $ sudo systemctl enable nvidia-persistenced.service && sudo systemctl start nvidia-persistenced.service

6. Create a symbolic link from the **/etc/systemd/system/multi-user.target.wants/nvidia-persistenced.service** file to the **/usr/lib/systemd/system/nvidia-persistenced.service** file.

    ::

7. Reboot the server.

    ::
8. Verify that the Nvidia driver has been installed and shows all available GPU's:

   .. code-block:: console

      $ nvidia-smi
	  
   The following is the correct output:

   .. code-block:: console
      
      nvidia-smi
      Wed Oct 30 14:05:42 2019
      +-----------------------------------------------------------------------------+
      | NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
      |-------------------------------+----------------------+----------------------+
      | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
      | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
      |===============================+======================+======================|
      |   0  Tesla V100-SXM2...  On   | 00000004:04:00.0 Off |                    0 |
      | N/A   32C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      |   1  Tesla V100-SXM2...  On   | 00000035:03:00.0 Off |                    0 |
      | N/A   33C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      
      +-----------------------------------------------------------------------------+
      | Processes:                                                       GPU Memory |
      |  GPU       PID   Type   Process name                             Usage      |
      |=============================================================================|
      |  No running processes found                                                 |
      +-----------------------------------------------------------------------------+

.. _CUDA_10.1_IBMPower9:

Installing the CUDA Driver Version 10.1 for IBM Power9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the CUDA driver version 10.1 for IBM Power9:**

1. Download the base installer for Linux CentOS 7 PPC64le:

   .. code-block:: console

      wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.ppc64le.rpm


#. Install the base installer for Linux CentOS 7 x86_64 by running the following commands:

   .. code-block:: console

      $ sudo rpm -i cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.ppc64le.rpm
      $ sudo yum clean all
      $ sudo yum  install nvidia-driver-latest-dkms
		 
.. warning:: Verify that the output indicates that driver **418.87** will be installed.

		 

3. Copy the file to the **/etc/udev/rules.d** directory.

    ::
   
4. If you are using RHEL 7 version (7.6 or later), comment out, remove, or change the hot-pluggable memory rule located in file copied to the **/etc/udev/rules.d** directory by running the following command:

   .. code-block:: console

      $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d 
      $ sudo sed -i 's/SUBSYSTEM!="memory",.*GOTO="memory_hotplug_end"/SUBSYSTEM=="*", GOTO="memory_hotplug_end"/' /etc/udev/rules.d/40-redhat.rules

#. Enable the **nvidia-persisted.service** file:

   .. code-block:: console

      $ sudo systemctl enable nvidia-persistenced.service 

#. Create a symbolic link from the **/etc/systemd/system/multi-user.target.wants/nvidia-persistenced.service** file to the **/usr/lib/systemd/system/nvidia-persistenced.service** file.

    ::
   
#. Reboot your system to initialize the above modifications.

    ::
   
#. Verify that the Nvidia driver and the **nvidia-persistenced.service** files are running:

   .. code-block:: console

      $ nvidia smi

   The following is the correct output:

   .. code-block:: console       

      nvidia-smi
      Wed Oct 30 14:05:42 2019
      +-----------------------------------------------------------------------------+
      | NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
      |-------------------------------+----------------------+----------------------+
      | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
      | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
      |===============================+======================+======================|
      |   0  Tesla V100-SXM2...  On   | 00000004:04:00.0 Off |                    0 |
      | N/A   32C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      |   1  Tesla V100-SXM2...  On   | 00000035:03:00.0 Off |                    0 |
      | N/A   33C    P0    37W / 300W |      0MiB / 16130MiB |      0%      Default |
      +-------------------------------+----------------------+----------------------+
      
      +-----------------------------------------------------------------------------+
      | Processes:                                                       GPU Memory |
      |  GPU       PID   Type   Process name                             Usage      |
      |=============================================================================|
      |  No running processes found                                                 |
      +-----------------------------------------------------------------------------+

#. Verify that the **nvidia-persistenced** service is running:

   .. code-block:: console

      $ systemctl status nvidia-persistenced

   The following is the correct output:

   .. code-block:: console

      root@gpudb ~]systemctl status nvidia-persistenced
        nvidia-persistenced.service - NVIDIA Persistence Daemon
         Loaded: loaded (/usr/lib/systemd/system/nvidia-persistenced.service; enabled; vendor preset: disabled)
         Active: active (running) since Tue 2019-10-15 21:43:19 KST; 11min ago
        Process: 8257 ExecStart=/usr/bin/nvidia-persistenced --verbose (code=exited, status=0/SUCCESS)
       Main PID: 8265 (nvidia-persiste)
          Tasks: 1
         Memory: 21.0M
         CGroup: /system.slice/nvidia-persistenced.service
          └─8265 /usr/bin/nvidia-persistenced --verbose

Installing the Docker Engine (Community Edition)
=======================
After installing the Nvidia CUDA driver you must install the Docker engine.

This section describes how to install the Docker engine using the following processors:

* :ref:`Using x86_64 processor on CentOS <dockerx8664centos>`
* :ref:`Using x86_64 processor on Ubuntu <dockerx8664ubuntu>`
* :ref:`Using IBM Power9 (PPC64le) processor <docker_ibmpower9>`


.. _dockerx8664centos:

Installing the Docker Engine Using an x86_64 Processor on CentOS
---------------------------------
The x86_64 processor supports installing the **Docker Community Edition (CE)** versions 18.03 and higher.

For more information on installing the Docker Engine CE on an x86_64 processor, see `Install Docker Engine on CentOS <https://docs.docker.com/engine/install/centos/>`_



.. _dockerx8664ubuntu:

Installing the Docker Engine Using an x86_64 Processor on Ubuntu
-----------------------------------------------------


The x86_64 processor supports installing the **Docker Community Edition (CE)** versions 18.03 and higher.

For more information on installing the Docker Engine CE on an x86_64 processor, see `Install Docker Engine on Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

.. _docker_ibmpower9:

Installing the Docker Engine on an IBM Power9 Processor
----------------------------------------
The x86_64 processor only supports installing the **Docker Community Edition (CE)** version 18.03.


**To install the Docker Engine on an IBM Power9 processor:**

You can install the Docker Engine on an IBM Power9 processor by running the following command:

.. code-block:: console

   $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/container-selinux-2.9-4.el7.noarch.rpm
   $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm
   $ yum install -y container-selinux-2.9-4.el7.noarch.rpm
   $ docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm
 
For more information on installing the Docker Engine CE on an IBM Power9 processor, see `Install Docker Engine on Ubuntu <https://developer.ibm.com/components/ibm-power/tutorials/install-docker-on-linux-on-power/>`_.

Docker Post-Installation
=================================
After installing the Docker engine you must configure Docker on your local machine.

**To configure Docker on your local machine:**

1. Enable Docker to start on boot:

   .. code-block:: console

      $ sudo systemctl enable docker && sudo systemctl start docker
	  
2. Enable managing Docker as a non-root user:

   .. code-block:: console

      $ sudo usermod -aG docker $USER

3. Log out and log back in via SSH. This causes Docker to re-evaluate your group membership.

    ::

4. Verify that you can run the following Docker command as a non-root user (without ``sudo``):

   .. code-block:: console

      $ docker run hello-world

If you can run the above Docker command as a non-root user, the following occur:

* Docker downloads a test image and runs it in a container.
* When the container runs, it prints an informational message and exits.

For more information on installing the Docker Post-Installation, see `Docker Post-Installation <https://docs.docker.com/install/linux/linux-postinstall/>`_.

Installing the Nvidia Docker2 ToolKit
==========================================
After configuring Docker on your local machine you must install the Nvidia Docker2 ToolKit.  The NVIDIA Docker2 Toolkit lets you build and run GPU-accelerated Docker containers. The Toolkit includes a container runtime library and related utilities for automatically configuring containers to leverage NVIDIA GPU's.

This section describes the following:

* :ref:`Installing the NVIDIA Docker2 Toolkit on an x86_64 processor. <install_nvidia_docker2_toolkit_x8664_processor>`
* :ref:`Installing the NVIDIA Docker2 Toolkit on a PPC64le processor. <install_nvidia_docker2_toolkit_ppc64le_processor>`

.. _install_nvidia_docker2_toolkit_x8664_processor:

Installing the NVIDIA Docker2 Toolkit on an x86_64 Processor
----------------------------------------

This section describes the following:

* :ref:`Installing the NVIDIA Docker2 Toolkit on a CentOS operating system <install_nvidia_docker2_toolkit_centos>`

* :ref:`Installing the NVIDIA Docker2 Toolkit on an Ubuntu operating system <install_nvidia_docker2_toolkit_ubuntu>`

.. _install_nvidia_docker2_toolkit_centos:

Installing the NVIDIA Docker2 Toolkit on a CentOS Operating System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the NVIDIA Docker2 Toolkit on a CentOS operating system:**

1. Install the repository for your distribution:

   .. code-block:: console

      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L
      $ https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | \
      $ sudo tee /etc/yum.repos.d/nvidia-docker.repo

2. Install the ``nvidia-docker2`` package and reload the Docker daemon configuration:

   .. code-block:: console

      $ sudo yum install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd

3. Do one of the following:

   * If you received an error when installing the ``nvidia-docker2`` package, skip to :ref:`Step 4 <step_4_centos>`.
   * If you successfully installed the ``nvidia-docker2`` package, skip to :ref:`Step 5 <step_5_centos>`.

.. _step_4_centos:

4. Do the following:

    1. Run the ``sudo vi /etc/yum.repos.d/nvidia-docker.repo`` command if the following error is displayed when installing the ``nvidia-docker2`` package:
    

       .. code-block:: console

          https://nvidia.github.io/nvidia-docker/centos7/ppc64le/repodata/repomd.xml:
          [Errno -1] repomd.xml signature could not be verified for nvidia-docker

    2. Change ``repo_gpgcheck=1`` to ``repo_gpgcheck=0``.

.. _step_5_centos:

5. Verify that the NVIDIA-Docker run has been installed correctly:

   .. code-block:: console

      $ docker run --runtime=nvidia --rm nvidia/cuda:10.1-base nvidia-smi

For more information on installing the NVIDIA Docker2 Toolkit on a CentOS operating system, see :ref:`Installing the NVIDIA Docker2 Toolkit on a CentOS operating system <https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#centos-distributions-1>`


.. _install_nvidia_docker2_toolkit_ubuntu:

Installing the NVIDIA Docker2 Toolkit on an Ubuntu Operating System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the NVIDIA Docker2 Toolkit on an Ubuntu operating system:**

1. Install the repository for your distribution:

   .. code-block:: console

      $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
      $ sudo apt-key add -
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L
      $ https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
      $ sudo tee /etc/apt/sources.list.d/nvidia-docker.list
      $ sudo apt-get update

2. Install the ``nvidia-docker2`` package and reload the Docker daemon configuration:

   .. code-block:: console

      $ sudo apt-get install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
3. Do one of the following:
   * If you received an error when installing the ``nvidia-docker2`` package, skip to :ref:`Step 4 <step_4_ubuntu>`.
   * If you successfully installed the ``nvidia-docker2`` package, skip to :ref:`Step 5 <step_5_ubuntu>`.

 .. _step_4_ubuntu:

4. Do the following:

    1. Run the ``sudo vi /etc/yum.repos.d/nvidia-docker.repo`` command if the following error is displayed when installing the ``nvidia-docker2`` package:

       .. code-block:: console

          https://nvidia.github.io/nvidia-docker/centos7/ppc64le/repodata/repomd.xml:
          [Errno -1] repomd.xml signature could not be verified for nvidia-docker

    2. Change ``repo_gpgcheck=1`` to ``repo_gpgcheck=0``.

.. _step_5_ubuntu:

5. Verify that the NVIDIA-Docker run has been installed correctly:

   .. code-block:: console

      $ docker run --runtime=nvidia --rm nvidia/cuda:10.1-base nvidia-smi

For more information on installing the NVIDIA Docker2 Toolkit on a CentOS operating system, see :ref:`Installing the NVIDIA Docker2 Toolkit on an Ubuntu operating system <https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#ubuntu-distributions-1>`

.. _install_nvidia_docker2_toolkit_ppc64le_processor:

Installing the NVIDIA Docker2 Toolkit on a PPC64le Processor
--------------------------------------

This section describes how to install the NVIDIA Docker2 Toolkit on an IBM RHEL operating system:

**To install the NVIDIA Docker2 Toolkit on an IBM RHEL operating system:**

1. Import the repository and install the ``libnvidia-container`` and the ``nvidia-container-runtime`` containers.

   .. code-block:: console

      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | \
        sudo tee /etc/yum.repos.d/nvidia-docker.repo
      $ sudo yum install -y libnvidia-container*

2. Do one of the following:

   * If you received an error when installing the containers, skip to :ref:`Step 3 <step_3_installing_nvidia_docker2_toolkit_ppc64le_processor>`.
   * If you successfully installed the containers, skip to :ref:`Step 4 <step_4_installing_nvidia_docker2_toolkit_ppc64le_processor>`.

.. _step_3_installing_nvidia_docker2_toolkit_ppc64le_processor:

3. Do the following:

   1. Run the ``sudo vi /etc/yum.repos.d/nvidia-docker.repo`` command if the following error is displayed when installing the containers:
    
      .. code-block:: console

         https://nvidia.github.io/nvidia-docker/centos7/ppc64le/repodata/repomd.xml:
         [Errno -1] repomd.xml signature could not be verified for nvidia-docker

   2. Change ``repo_gpgcheck=1`` to ``repo_gpgcheck=0``.
	
	    ::
		
   3. Install the ``libnvidia-container`` container.
    
      .. code-block:: console

         $ sudo yum install -y libnvidia-container*         

 .. _step_4_installing_nvidia_docker2_toolkit_ppc64le_processor:

4. Install the ``nvidia-container-runtime`` container:

   .. code-block:: console
       
      $ sudo yum install -y nvidia-container-runtime*

5. Add ``nvidia runtime`` to the Docker daemon:

   .. code-block:: console

      $ sudo mkdir -p /etc/systemd/system/docker.service.d/
      $ sudo vi /etc/systemd/system/docker.service.d/override.conf

      $ [Service]
      $ ExecStart=
      $ ExecStart=/usr/bin/dockerd

6. Restart Docker:

   .. code-block:: console

      $ sudo systemctl daemon-reload
      $ sudo systemctl restart docker

7. Verify that the NVIDIA-Docker run has been installed correctly:

   .. code-block:: console
      
      $ docker run --runtime=nvidia --rm nvidia/cuda-ppc64le nvidia-smi
	  
.. _accessing_hadoop_kubernetes_configuration_files:
	  
Accessing the Hadoop and Kubernetes Configuration Files
--------------------------------------
The information this section is optional and is only relevant for Hadoop users. If you require Hadoop and Kubernetes (Krb5) connectivity, contact your IT department for access to the following configuration files:

* Hadoop configuration files: 
  
  * core-site.xml
  * hdfs-site.xml
  
   ::

* Kubernetes files:
  
  * Configuration file - krb.conf
  * Kubernetes Hadoop client certificate - hdfs.keytab

Once you have the above files, you must copy them into the correct folders in your working directory.

For more information about the correct directory to copy the above files into, see the :ref:`Installing the SQream Software <installing_sqream_software>` section below.

For related information, see the following sections:

* :ref:`Configuring the Hadoop and Kubernetes Configuration Files <configure_hadoop_kubernetes_configuration_files>`.
* :ref:`Setting the Hadoop and Kubernetes Configuration Parameters <setting_hadoop_kubernetes_connectivity_parameters>`.

.. _installing_sqream_software:

Installing the SQream Software
==============================

Preparing Your Local Environment
-------------------------
After installing the Nvidia Docker2 toolKit you must prepare your local environment.

.. note:: You must install the SQream software under a *sqream* and not a *root* user.

The Linux user preparing the local environment must have **read/write** access to the following directories for the SQream software to correctly read and write the required resources:

* **Log directory** - default: /var/log/sqream/
* **Configuration directory** - default: /etc/sqream/
* **Cluster directory** - the location where SQream writes its DB system, such as */mnt/sqreamdb*
* **Ingest directory** - the location where the required data is loaded, such as */mnt/data_source/*

.. _download_sqream_software:

Deploying the SQream Software
-------------------------
After preparing your local environment you must deploy the SQream software. Deploying the SQream software requires you to access and extract the required files and to place them in the correct directory.

**To deploy the SQream software:**

1. Contact the SQream Support team for access to the **sqream_installer-nnn-DBnnn-COnnn-EDnnn-<arch>.tar.gz** file.

The **sqream_installer-nnn-DBnnn-COnnn-EDnnn-<arch>.tar.gz** file includes the following parameter values:

* **sqream_installer-nnn** - sqream installer version
* **DBnnn** - SQreamDB version
* **COnnn** - SQream console version
* **EDnnn** - SQream editor version
* **arch** - server arch (applicable to X86.64 and ppc64le)

2. Extract the tarball file:

   .. code-block:: console

      $ tar -xvf sqream_installer-1.1.5-DB2019.2.1-CO1.5.4-ED3.0.0-x86_64.tar.gz

When the tarball file has been extracted, a new folder will be created. The new folder is automatically given the name of the tarball file:

   .. code-block:: console

      drwxrwxr-x 9 sqream sqream 4096 Aug 11 11:51 sqream_istaller-1.1.5-DB2019.2.1-CO1.5.4-ED3.0.0-x86_64/
      -rw-rw-r-- 1 sqream sqream 3130398797 Aug 11 11:20 sqream_installer-1.1.5-DB2019.2.1-CO1.5.4-ED3.0.0-x86_64.tar.gz
	  
3. Change the directory to the new folder that you created in the previous step.

::

4. Verify that the folder you just created contains all of the required files.

   .. code-block:: console

      $ ls -la

   The following is an example of the files included in the new folder:

   .. code-block:: console

      drwxrwxr-x. 10 sqream sqream   198 Jun  3 17:57 .
      drwx------. 25 sqream sqream  4096 Jun  7 18:11 ..
      drwxrwxr-x.  2 sqream sqream   226 Jun  7 18:09 .docker
      drwxrwxr-x.  2 sqream sqream    64 Jun  3 12:55 .hadoop
      drwxrwxr-x.  2 sqream sqream  4096 May 31 14:18 .install
      drwxrwxr-x.  2 sqream sqream    39 Jun  3 12:53 .krb5
      drwxrwxr-x.  2 sqream sqream    22 May 31 14:18 license
      drwxrwxr-x.  2 sqream sqream    82 May 31 14:18 .sqream
      -rwxrwxr-x.  1 sqream sqream  1712 May 31 14:18 sqream-console
      -rwxrwxr-x.  1 sqream sqream  4608 May 31 14:18 sqream-install

For information relevant to Hadoop users, see the following sections:

* :ref:`Accessing the Hadoop and Kubernetes Configuration Files <accessing_hadoop_kubernetes_configuration_files>`.
* :ref:`Configuring the Hadoop and Kubernetes Configuration Files <configure_hadoop_kubernetes_configuration_files>`.
* :ref:`Setting the Hadoop and Kubernetes Configuration Parameters <setting_hadoop_kubernetes_connectivity_parameters>`.

.. _configure_hadoop_kubernetes_configuration_files:
	  
Configuring the Hadoop and Kubernetes Configuration Files
-----------------------------
The information in this section is optional and is only relevant for Hadoop users. If you require Hadoop and Kubernetes (Krb5) connectivity, you must copy the Hadoop and Kubernetes files into the correct folders in your working directory as shown below:

* .hadoop/core-site.xml
* .hadoop/hdfs-site.xml
* .krb5/krb5.conf
* .krb5/hdfs.keytab

For related information, see the following sections:

* :ref:`Accessing the Hadoop and Kubernetes Configuration Files <accessing_hadoop_kubernetes_configuration_files>`.
* :ref:`Setting the Hadoop and Kubernetes Configuration Parameters <setting_hadoop_kubernetes_connectivity_parameters>`.

Configuring the SQream Software
-------------------------------
After deploying the SQream software, and optionally configuring the Hadoop and Kubernetes configuration files, you must configure the SQream software.

Configuring the SQream software requires you to do the following:

* Configure your local environment
* Understand the ``sqream-install`` flags
* Install your SQream license
* Validate your SQream icense
* Change your data ingest folder

Configuring Your Local Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've downloaded the SQream software, you can begin configuring your local environment. The following commands must be run (as **sudo**) from the same directory that you located your packages.

For example, you may have saved your packages in **/home/sqream/sqream-console-package/**.

The following table shows the flags that you can use to configure your local directory:

.. list-table::
   :widths: 10 50 40
   :header-rows: 1
   
   * - Flag
     - Function
     - Note
   * - **-i**
     - Loads all software from the hidden folder **.docker**.
     - Mandatory	 
   * - **-k**
     - Loads all license packages from the **/license** directory.
     - Mandatory	 
   * - **-f**
     - Overwrites existing folders. **Note** Using ``-f`` overwrites **all files** located in mounted directories.
     - Mandatory	 
   * - **-c**
     - Defines the origin path for writing/reading SQream configuration files. The default location is ``/etc/sqream/``.
     - If you are installing the Docker version on a server that already works with SQream, do not use the default path.	 
   * - **-v**
     - The SQream cluster location. If a cluster does not exist yet, ``-v`` creates one. If a cluster already exists, ``-v`` mounts it. 
     - Mandatory	 
   * - **-l**
     - SQream system startup logs location, including startup logs and docker logs. The default location is ``/var/log/sqream/``.
     - 	 
   * - **-d**
     - The directory containing customer data to be imported and/or copied to SQream.
     - 	 
   * - **-s**
     - Shows system settings. 
     - 	 
   * - **-r**
     - Resets the system configuration. This value is run without any other variables.
     - Mandatory	 
   * - **-h**
     - Help. Shows the available flags. 
     - Mandatory	 
   * - **-K**
     - Runs license validation
     - 
   * - **-e**
     - Used for inserting your RKrb5 server DNS name. For more information on setting your Kerberos configuration parameters, see :ref:`Setting the Hadoop and Kubernetes Configuration Parameters <setting_hadoop_kubernetes_connectivity_parameters>`.
     - 	 
   * - **-p**
     - Used for inserting your Kerberos user name.  For more information on setting your Kerberos configuration parameters, see :ref:`Setting the Hadoop and Kubernetes Configuration Parameters <setting_hadoop_kubernetes_connectivity_parameters>`.
     - 	 


Installing Your License
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've configured your local environment, you must install your license by copying it into the SQream installation package folder located in the **./license** folder:

.. code-block:: console

   $ sudo ./sqream-install -k

You do not need to extract this folder after uploading into the **./license**.


Validating Your License
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can copy your license package into the SQream console folder located in the **/license** folder by running the following command:
   
.. code-block:: console

   $ sudo ./sqream-install -K

The following mandatory flags must be used in the first run:
   
.. code-block:: console

   $ sudo ./sqream-install -i -k -v <volume path>

The following is an example of the correct command syntax:
   
.. code-block:: console

   $ sudo ./sqream-install -i -k -c /etc/sqream -v /home/sqream/sqreamdb -l /var/log/sqream -d /home/sqream/data_ingest
   
.. _setting_hadoop_kubernetes_connectivity_parameters:

Setting the Hadoop and Kubernetes Connectivity Parameters
-------------------------------
The information in this section is optional, and is only relevant for Hadoop users. If you require Hadoop and Kubernetes (Krb5) connectivity, you must set their connectivity parameters.

The following is the correct syntax when setting the Hadoop and Kubernetes connectivity parameters:

.. code-block:: console

   $ sudo ./sqream-install -p <Kerberos user name> -e  <Kerberos server DNS name>:<Kerberos server IP>

The following is an example of setting the Hadoop and Kubernetes connectivity parameters:

.. code-block:: console

   $ sudo ./sqream-install -p <nn1@SQ.COM> -e  kdc.sq.com:<192.168.1.111>
   
For related information, see the following sections:

* :ref:`Accessing the Hadoop and Kubernetes Configuration Files <accessing_hadoop_kubernetes_configuration_files>`.
* :ref:`Configuring the Hadoop and Kubernetes Configuration Files <configure_hadoop_kubernetes_configuration_files>`.
   
Modifying Your Data Ingest Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've validated your license, you can modify your data ingest folder after the first run by running the following command:
   
.. code-block:: console

   $ sudo ./sqream-install -d /home/sqream/data_in

Configuring Your Network for Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've modified your data ingest folder (if needed), you must validate that the server network and Docker network that you are setting up do not overlap.

**To configure your network for Docker:**

1. To verify that your server network and Docker network do not overlap, run the following command:

.. code-block:: console

   $ ifconfig | grep 172.

2. Do one of the following:

  * If running the above command output no results, continue the installation process.
  * If running the above command output results, run the following command:

    .. code-block:: console

       $ ifconfig | grep 192.168.


Checking and Verifying Your System Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've configured your network for Docker, you can check and verify your system settings.

Running the following command shows you all the variables used by your SQream system:

.. code-block:: console

   $ ./sqream-install -s

The following is an example of the correct output:

.. code-block:: console

   SQREAM_CONSOLE_TAG=1.5.4
   SQREAM_TAG=2019.2.1
   SQREAM_EDITOR_TAG=3.0.0
   license_worker_0=f0:cc:
   license_worker_1=26:91:
   license_worker_2=20:26:
   license_worker_3=00:36:
   SQREAM_VOLUME=/media/sqreamdb
   SQREAM_DATA_INGEST=/media/sqreamdb/data_in
   SQREAM_CONFIG_DIR=/etc/sqream/
   LICENSE_VALID=true
   SQREAM_LOG_DIR=/var/log/sqream/
   SQREAM_USER=sqream
   SQREAM_HOME=/home/sqream
   SQREAM_ENV_PATH=/home/sqream/.sqream/env_file
   PROCESSOR=x86_64
   METADATA_PORT=3105
   PICKER_PORT=3108
   NUM_OF_GPUS=2
   CUDA_VERSION=10.1
   NVIDIA_SMI_PATH=/usr/bin/nvidia-smi
   DOCKER_PATH=/usr/bin/docker
   NVIDIA_DRIVER=418
   SQREAM_MODE=single_host

Using the SQream Console
=========================
After configuring the SQream software and veriying your system settings you can begin using the SQream console.

SQream Console - Basic Commands
---------------------------------
The SQream console offers the following basic commands:

* :ref:`Starting your SQream console <starting_sqream_console>`
* :ref:`Starting Metadata and Picker <starting_metadata_and_picker>`
* :ref:`Starting the running services <starting_running_services>`
* :ref:`Listing the running services <listing_running_services>`
* :ref:`Stopping the running services <stopping_running_services>`
* :ref:`Using the SQream editor <using_sqream_editor>`
* :ref:`Using the SQream Client <using_sqream_client>`

.. _starting_sqream_console:

Starting Your SQream Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can start your SQream console by running the following command:

.. code-block:: console

   $ ./sqream-console

.. _starting_metadata_and_picker:

Starting the SQream Master
~~~~~~~~~~~~~~~~~

**To listen to metadata and picker:**

1. Start the metadata server (default port 3105) and picker (default port 3108) by running the following command:

   .. code-block:: console

      $ sqream master --start
      
   The following is the correct output:

   .. code-block:: console

      sqream-console> sqream master --start
      starting master server in single_host mode ...
      sqream_single_host_master is up and listening on ports: 3105,3108
       

2. *Optional* - Change the metadata and server picker ports by adding ``-p <port number>`` and ``-m <port number>``:

   .. code-block:: console

      $ sqream-console>sqream master --start -p 4105 -m 43108
      $ starting master server in single_host mode ...
      $ sqream_single_host_master is up and listening on ports: 4105,4108



.. _starting_running_services:

Starting SQream Workers
~~~~~~~~~~~~~~~~~


When starting SQream workers, setting the ``<number of workers>`` value sets how many workers to start. Leaving the ``<number of workers>`` value unspecified runs all of the available resources.


.. code-block:: console

   $ sqream worker --start <number of workers> 

   The following is an example of expected output when setting the ``<number of workers>`` value to ``2``:

   .. code-block:: console

      sqream-console>sqream worker --start 2
      started sqream_single_host_worker_0 on port 5000, allocated gpu: 0
      started sqream_single_host_worker_1 on port 5001, allocated gpu: 1


.. _listing_running_services:

Listing the Running Services
~~~~~~~~~~~~~~~~~

You can list running SQream services to look for container names and ID's by running the following command:

.. code-block:: console

   $ sqream master --list

The following is an example of the expected output:

.. code-block:: console

   sqream-console>sqream master --list
   container name: sqream_single_host_worker_0, container id: c919e8fb78c8
   container name: sqream_single_host_master, container id: ea7eef80e038--


.. _stopping_running_services:

Stopping the Running Services
~~~~~~~~~~~~~~~~~

You can stop running services either for a single SQream worker, or all SQream services for both master and worker.

The following is the command for stopping a running service for a single SQream worker:

.. code-block:: console
     
   $ sqream worker --stop <full worker name>

The following is an example of expected output when stopping a running service for a single SQream worker:

.. code-block:: console

   sqream worker stop <full worker name>
   stopped container sqream_single_host_worker_0, id: 892a8f1a58c5


You can stop all running SQream services (both master and worker) by running the following command:

.. code-block:: console

   $ sqream-console>sqream master --stop --all

The following is an example of expected output when stopping all running services:

.. code-block:: console

   sqream-console>sqream master --stop --all
   stopped container sqream_single_host_worker_0, id: 892a8f1a58c5
   stopped container sqream_single_host_master, id: 55cb7e38eb22


.. _using_sqream_editor:

Using SQream Studio
~~~~~~~~~~~~~~~~~
SQream Studio is an SQL statement editor.

**To start SQream Studio:**

1. Run the following command:

   .. code-block:: console

      $ sqream studio --start

The following is an example of the expected output:

   .. code-block:: console

      SQream Acceleration Studio is available at http://192.168.1.62:8080

2. Click the ``http://192.168.1.62:8080`` link shown in the CLI.


**To stop SQream Studio:**

You can stop your SQream Studio by running the following command:

.. code-block:: console

   $ sqream studio --stop

The following is an example of the expected output:

.. code-block:: console

   sqream_admin    stopped


.. _using_sqream_client:

Using the SQream Client
~~~~~~~~~~~~~~~~~


You can use the embedded SQream Client on the following nodes:

* Master node
* Worker node


When using the SQream Client on the Master node, the following default settings are used:

* **Default port**: 3108. You can change the default port using the  ``-p`` variable.
* **Default database**: master. You can change the default database using the ``-d`` variable.

The following is an example:

.. code-block:: console

   $ sqream client --master -u sqream -w sqream


When using the SQream Client on a Worker node (or nodes), you should use the ``-p`` variable for Worker ports. The default database is ``master``, but you can use the ``-d`` variable to change databases.

The following is an example:

.. code-block:: console

   $ sqream client --worker -p 5000 -u sqream -w sqream


Moving from Docker Installation to Standard On-Premises Installation
-----------------------------------------------

Because Docker creates all files and directories on the host at the **root** level, you must grant ownership of the SQream storage folder to the working directory user.

SQream Console - Advanced Commands
-----------------------------

The SQream console offers the following advanced commands:


* :ref:`Controlling the spool size <controlling_spool_size>`
* :ref:`Splitting a GPU <splitting_gpu>`
* :ref:`Splitting a GPU and setting the spool size <splitting_gpu_setting_spool_size>`
* :ref:`Using a custom configuration file <using_custom_configuration_file>`
* :ref:`Clustering your Docker environment <clustering_docker_environment>`




.. _controlling_spool_size:

Controlling the Spool Size
~~~~~~~~~~~~~~~~~~

From the console you can define a spool size value.

The following example shows the spool size being set to ``50``:

.. code-block:: console

   $ sqream-console>sqream worker --start 2 -m 50


If you don't define the SQream spool size, the SQream console automatically distributes the available RAM between all running workers.

.. _splitting_gpu:

Splitting a GPU
~~~~~~~~~~~~~~~~~~

You can start more than one sqreamd on a single GPU by splitting it.


The following example shows the GPU being split into **two** sqreamd's on the GPU in **slot 0**:

.. code-block:: console

   $ sqream-console>sqream worker --start 2 -g 0

.. _splitting_gpu_setting_spool_size:

Splitting GPU and Setting the Spool Size
~~~~~~~~~~~~~~~~~~

You can simultaneously split a GPU and set the spool size by appending the ``-m`` flag:

.. code-block:: console

   $ sqream-console>sqream worker --start 2 -g 0 -m 50

.. note:: The console does not validate whether the user-defined spool size is available. Before setting the spool size, verify that the requested resources are available.

.. _using_custom_configuration_file:

Using a Custom Configuration File
~~~~~~~~~~~~~~~~~~

SQream lets you use your own external custom configuration json files. You must place these json files in the path mounted in the installation. SQream recommends placing the json file in the Configuration folder.

The SQream console does not validate the integrity of your external configuration files.

When using your custom configuration file, you can use the ``-j`` flag to define the full path to the Configuration file, as in the example below: 

.. code-block:: console

   $ sqream-console>sqream worker --start 1 -j /etc/sqream/configfile.json

.. note:: To start more than one sqream daemon, you must provide files for each daemon, as in the example below:

.. code-block:: console

   $ sqream worker --start 2 -j /etc/sqream/configfile.json /etc/sqream/configfile2.json

.. note:: To split a specific GPU, you must also list the GPU flag, as in the example below:
   
.. code-block:: console

   $ sqream worker --start 2 -g 0 -j /etc/sqream/configfile.json /etc/sqream/configfile2.json

.. _clustering_docker_environment:

Clustering Your Docker Environment
~~~~~~~~~~~~~~~~~~

SQream lets you connect to a remote Master node to start Docker in Distributed mode. If you have already connected to a Slave node server in Distributed mode, the **sqream Master** and **Client** commands are only available on the Master node.
   
.. code-block:: console

   $ --master-host
   $ sqream-console>sqream worker --start 1 --master-host 192.168.0.1020

Checking the Status of SQream Services
---------------------------
SQream lets you check the status of SQream services from the following locations:

* :ref:`From the Sqream console <inside_sqream_console>`
* :ref:`From outside the Sqream console <outside_sqream_console>`

.. _inside_sqream_console:

Checking the Status of SQream Services from the SQream Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the SQream console, you can check the status of SQream services by running the following command:
   
.. code-block:: console

   $ sqream-console>sqream master --list

The following is an example of the expected output:
   
.. code-block:: console

   $ sqream-console>sqream master --list
   $ checking 3 sqream services:
   $ sqream_single_host_worker_1 up, listens on port: 5001 allocated gpu: 1
   $ sqream_single_host_worker_0 up, listens on port: 5000 allocated gpu: 1
   $ sqream_single_host_master up listens on ports: 3105,3108

.. _outside_sqream_console:

Checking the Status of SQream Services from Outside the SQream Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From outside the Sqream Console, you can check the status of SQream services by running the following commands:
 
.. code-block:: console
     
   $ sqream-status
   $ NAMES STATUS PORTS
   $ sqream_single_host_worker_1 Up 3 minutes 0.0.0.0:5001->5001/tcp
   $ sqream_single_host_worker_0 Up 3 minutes 0.0.0.0:5000->5000/tcp
   $ sqream_single_host_master Up 3 minutes 0.0.0.0:3105->3105/tcp, 0.0.0.0:3108->3108/tcp
   $ sqream_editor_3.0.0 Up 3 hours (healthy) 0.0.0.0:3000->3000/tcp

Upgrading Your SQream System
----------------------------
This section describes how to upgrade your SQream system.

**To upgrade your SQream system:**

1. Contact the SQream Support team for access to the new SQream package tarball file.

    ::
	
2. Set a maintenance window to enable stopping the system while upgrading it.

    ::
	
3. Extract the following tarball file received from the SQream Support team, under it with the same user and in the same folder that you used while :ref:`Downloading the SQream Software <_download_sqream_software>`.

 
   .. code-block:: console
     
      $ tar -xvf sqream_installer-2.0.5-DB2019.2.1-CO1.6.3-ED3.0.0-x86_64/

4. Navigate to the new folder created as a result of extracting the tarball file:

   .. code-block:: console
     
      $ cd sqream_installer-2.0.5-DB2019.2.1-CO1.6.3-ED3.0.0-x86_64/

5. Initiate the upgrade process:

   .. code-block:: console
   
      $ ./sqream-install -i

   Initiating the upgrade process checks if any SQream services are running. If any services are running, you will be prompted to stop them.

6. Do one of the following:

   * Select **Yes** to stop all running SQream workers (Master and Editor) and continue the upgrade process.
   * Select **No** to stop the upgrade process.

   SQream periodically upgrades the metadata structure. If an upgrade version includes a change to the metadata structure, you will be prompted with an approval request message. Your approval is required to finish the upgrade process.

   Because SQream supports only certain metadata versions, all SQream services must be upgraded at the same time.
 
7. When the upgrade is complete, load the SQream console and restart your services.

   For assistance, contact SQream Support.
