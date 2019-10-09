.. _installing_sqream_db:

***********************
Installing SQream DB
***********************

See :ref:`Release Notes <releases>` to learn about what's new in the latest release of SQream DB. To upgrade to this release, see :ref:`Upgrading <upgrading>`.

SQream DB is installed on your hosts with NVIDIA Docker. There are several preparation steps to ensure before installing SQream DB, so follow these instructions carefully.

.. Note:: Installing SQream DB requires a license key. Contact support@sqream.com or your SQream account manager for your license key.

.. contents:: In this topic:

Preparing your machine for NVIDIA Docker
=========================================
To install NVIDIA Docker, we must first install the NVIDIA driver (the full toolkit is not required).

.. Note:: SQream DB runs best on NVIDIA Tesla series GPUs. The instructions below are written for NVIDIA Tesla GPUs.

CentOS 7 / RHEL 7 / Amazon Linux / Ubuntu 16.04 / Ubuntu 18.04
---------------------------------------------------------------

.. admonition:: Recommended

   Follow the installation instructions on `NVIDIA's CUDA Installation Guide`_ for full instructions suitable for your platform. The information listed below is a summary of the necessary steps, and does not cover the full range of options available.

#. Obtain the latest NVIDIA Driver release for your operating system from NVIDIA's driver download page titled `Latest Tesla driver for Linux x64`_. 

.. Note:: IBM POWER users should download the driver from `Latest Tesla driver for Linux x64 POWER LE`_.

#. The NVIDIA driver is a self-contained installer. The latest version at the time of this document's release is 418.87.01. In order to install the driver, make it an executable and run it.
   
   .. code-block:: bash
      
      $ chmod u+x NVIDIA-Linux-x86_64-418.87.01.run
      $ sudo ./NVIDIA-Linux-x86_64-418.87.01.run -s
      
      Verifying archive integrity... OK
      Uncompressing NVIDIA Accelerated Graphics Driver for Linux-x86_64 418.87.01..............
      .........................................................................................
      .........................................................................................
      .........................................................................................
      .............................

#. Verify the installation completed correctly, by asking ``nvidia-smi``, NVIDIA's system management interface application, to list the available GPUs.
   
   .. code-block:: bash
      
      $ nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)

#. Enable NVIDIA's persistence daemon. This is mandatory for IBM POWER, but is recommended for other platforms as well.
      
      .. code-block:: bash
         
         $ sudo systemctl enable nvidia-persistenced

     .. Important:: On POWER9 systems only, disable the udev rule for hot-pluggable memory probing.

         For Red Hat 7 this rule can be found in ``/lib/udev/rules.d/40-redhat.rules``
         
         For Ubuntu, this rule can be found in in ``/lib/udev/rules.d/40-vm-hotadd.rules``
         The rule generally takes a form where it detects the addition of a memory block and changes the 'state' attribute to online. For example, in RHEL7, the rule looks like this:
         
         ``SUBSYSTEM=="memory", ACTION=="add", PROGRAM="/bin/uname -p", RESULT!="s390*", ATTR{state}=="offline", ATTR{state}="online"``

         This rule must be disabled by copying the file to ``/etc/udev/rules.d`` and commenting out, removing, or changing the hot-pluggable memory rule in the ``/etc`` copy so that it does not apply to NVIDIA devices on POWER9. 
         
         * On RHEL 7.5 or earlier versions:
         
            .. code-block:: bash
               
               $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d
               $ sudo sed -i '/SUBSYSTEM=="memory", ACTION=="add"/d' /etc/udev/rules.d/40-redhat.rules

         * On RHEL 7.6 and later versions:
            
            .. code-block:: bash
               
               $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d 
               $ sudo sed -i 's/SUBSYSTEM!="memory", ACTION!="add", GOTO="memory_hotplug_end"/SUBSYSTEM=="*", GOTO="memory_hotplug_end"/' /etc/udev/rules.d/40-redhat.rules
      
      *You will need to reboot the system to initialize the above changes.*

Install Docker CE and NVIDIA docker
====================================

Follow the instructions for your OS and architecture.

CentOS 7 / RHEL 7 / Amazon Linux (x64)
--------------------------------------

#. Follow the instructions for Docker CE for your platform at `Get Docker Engine - Community for CentOS`_

#. Verify that docker is running

   .. code-block:: bash
      :emphasize-lines: 4
      
      $ sudo systemctl status docker
      ● docker.service - Docker Application Container Engine
      Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
      Active: active (running) since Mon 2019-08-12 08:22:30 IDT; 1 months 27 days ago
        Docs: https://docs.docker.com
        Main PID: 65794 (dockerd)
        Tasks: 76
      Memory: 124.5M
      CGroup: /system.slice/docker.service
              └─65794 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

#. Tell Docker to start after a reboot

   .. code-block:: bash
   
      $ sudo systemctl enable docker

#. Let your current user manage Docker, without requiring `sudo`

   .. code-block:: bash
   
      $ sudo usermod -aG docker $USER

   .. Note:: Log out and log back in again after this action

#. Install nvidia-docker

   .. code-block:: bash
   
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
      
      $ sudo yum install -y nvidia-container-toolkit
      $ sudo systemctl restart docker
      $ sudo yum install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
      $ sudo systemctl restart docker

#. Verify the NVIDIA docker installation

   .. code-block:: bash
   
      $ sudo docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)

CentOS 7 / RHEL 7 (IBM POWER)
-------------------------------

#. Install Docker for IBM POWER

   .. code-block:: bash
      
      $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/container-selinux-2.9-4.el7.noarch.rpm
      $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm
      $ yum install -y container-selinux-2.9-4.el7.noarch.rpm docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm

#. Tell Docker to start after a reboot

   .. code-block:: bash
   
      $ sudo systemctl enable docker
      $ sudo systemctl start docker

#. Verify that docker is running

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 4
      
      $ sudo systemctl status docker
      ● docker.service - Docker Application Container Engine
      Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
      Active: active (running) since Mon 2019-08-12 08:22:30 IDT; 1 months 27 days ago
        Docs: https://docs.docker.com
        Main PID: 65794 (dockerd)
        Tasks: 76
      Memory: 124.5M
      CGroup: /system.slice/docker.service
              └─65794 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

#. Let your current user manage Docker, without requiring `sudo`

   .. code-block:: bash
   
      $ sudo usermod -aG docker $USER

   .. Note:: Log out and log back in again after this action

#. Install nvidia-docker

   * Install the NVIDIA container and container runtime packages from NVIDIA's repository:
      
      .. code-block:: bash
      
         $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
         $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
         
         $ sudo yum install -y libnvidia-container*
         $ sudo yum install -y nvidia-container-runtime*

   * Add the NVIDIA runtime to the Docker daemon and restart docker:
      
      .. code-block:: bash
      
         $ sudo mkdir -p /etc/systemd/system/docker.service.d/
         $ echo -e "[Service]\nExecStart\nExecStart=/usr/bin/dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime" | sudo tee /etc/systemd/system/docker.service.d/override.conf

         $ sudo systemctl daemon-reload
         $ sudo systemctl restart docker

#. Verify the NVIDIA docker installation succeeded

   .. code-block:: bash
   
      $ docker run --runtime=nvidia --rm nvidia/cuda-ppc64le nvidia-smi -L
      GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-SXM2-16GB (UUID: GPU-...)



Ubuntu 16.04 / Ubuntu 18.04 (x64)
-----------------------------------

#. Follow the instructions for Docker CE for your platform at `Get Docker Engine - Community for CentOS`_

#. Verify that docker is running

   .. code-block:: bash
      :linenos:
      :emphasize-lines: 4
      
      $ sudo systemctl status docker
      ● docker.service - Docker Application Container Engine
      Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
      Active: active (running) since Mon 2019-08-12 08:22:30 IDT; 1 months 27 days ago
        Docs: https://docs.docker.com
        Main PID: 65794 (dockerd)
        Tasks: 76
      Memory: 124.5M
      CGroup: /system.slice/docker.service
              └─65794 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

#. Tell Docker to start after a reboot

   .. code-block:: bash
   
      $ sudo systemctl enable docker

#. Let your current user manage Docker, without requiring `sudo`

   .. code-block:: bash
   
      $ sudo usermod -aG docker $USER

   .. Note:: Log out and log back in again after this action

#. Install nvidia-docker

   .. code-block:: bash
   
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
      
      $ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
      $ sudo systemctl restart docker


#. Verify the NVIDIA docker installation

   .. code-block:: bash
   
      $ sudo docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)



.. _`Latest Tesla driver for Linux x64`: https://www.nvidia.com/Download/driverResults.aspx/152242/en-us
.. _`Latest Tesla driver for Linux x64 POWER LE`: https://www.nvidia.com/Download/driverResults.aspx/152241/en-us
.. _`NVIDIA's CUDA Installation Guide`: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions
.. _`Get Docker Engine - Community for CentOS`: https://docs.docker.com/install/linux/docker-ce/centos/
.. _`Get Docker Engine - Community for Ubuntu`: https://docs.docker.com/install/linux/docker-ce/ubuntu/