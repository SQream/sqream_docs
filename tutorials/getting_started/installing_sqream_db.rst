.. _installing_sqream_db:

***********************
Installing SQream DB
***********************

See :ref:`Release Notes <releases>` to learn about what's new in the latest release of SQream DB. To upgrade to this release, see :ref:`Upgrading SQream DB <upgrading_sqream_db>`.

SQream DB is installed on your hosts with NVIDIA Docker. There are several preparation steps to ensure before installing SQream DB, so follow these instructions carefully.

.. Note:: Installing SQream DB requires a license key. Go to `SQream Support <http://support.sqream.com/>`_. or contact your SQream account manager for your license key.

.. contents:: In this topic:
   :local:

Preparing your machine for NVIDIA Docker
=========================================
To install NVIDIA Docker, we must first install the NVIDIA driver.

.. Note:: SQream DB runs best on NVIDIA Tesla series GPUs. The instructions below are written for NVIDIA Tesla GPUs.

.. contents:: Follow the instructions for your OS and architecture:
   :local:

CentOS 7 / RHEL 7 / Amazon Linux
---------------------------------------------------------------

.. admonition:: Recommended

   Follow the installation instructions on `NVIDIA's CUDA Installation Guide`_ for full instructions suitable for your platform. The information listed below is a summary of the necessary steps, and does not cover the full range of options available.

#. Enable EPEL

   EPEL provides additional open-source and free packages from the RHEL ecosystem. The NVIDIA driver depends on packages such as DKMS and libvdpau which are only available on third-party repositories, such as EPEL.

   .. code-block:: console
      
      $ sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

.. There are other ways of installing EPEL: $ sudo yum -y install epel-release
.. Do we need DKMS? $ sudo yum -y install dkms

#. Install the kernel headers and development tools necessary to compile the NVIDIA driver

   .. code-block:: console
      
      $ sudo yum update
      $ sudo yum -y install kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc

#. Install the CUDA repository and install the latest display driver

   .. code-block:: console
      
      $ sudo rpm -Uvh https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-repo-rhel7-10.1.243-1.x86_64.rpm
      $ sudo yum update && sudo yum install -y nvidia-driver-latest

.. note:: If you are running Linux with X, you'll have to switch to text-only mode before installing the display driver
   
   .. code-block:: console
   
      $ sudo systemctl isolate multi-user.target

#. Restart your machine

   .. code-block:: console
      
      ``sudo reboot``


#. Verify the installation completed correctly, by asking ``nvidia-smi``, NVIDIA's system management interface application, to list the available GPUs.
   
   .. code-block:: console
      
      $ nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)

#. Enable NVIDIA's persistence daemon. This is mandatory for IBM POWER, but is recommended for other platforms as well.
      
      .. code-block:: console
         
         $ sudo systemctl enable nvidia-persistenced && sudo systemctl start nvidia-persistenced

     .. Important:: On POWER9 systems only, disable the udev rule for hot-pluggable memory probing.

         For Red Hat 7 this rule can be found in ``/lib/udev/rules.d/40-redhat.rules``
         
         For Ubuntu, this rule can be found in in ``/lib/udev/rules.d/40-vm-hotadd.rules``
         The rule generally takes a form where it detects the addition of a memory block and changes the 'state' attribute to online. For example, in RHEL7, the rule looks like this:
         
         ``SUBSYSTEM=="memory", ACTION=="add", PROGRAM="/bin/uname -p", RESULT!="s390*", ATTR{state}=="offline", ATTR{state}="online"``

         This rule must be disabled by copying the file to ``/etc/udev/rules.d`` and commenting out, removing, or changing the hot-pluggable memory rule in the ``/etc`` copy so that it does not apply to NVIDIA devices on POWER9. 
         
         * On RHEL 7.5 or earlier versions:
         
            .. code-block:: console
               
               $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d
               $ sudo sed -i '/SUBSYSTEM=="memory", ACTION=="add"/d' /etc/udev/rules.d/40-redhat.rules

         * On RHEL 7.6 and later versions:
            
            .. code-block:: console
               
               $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d 
               $ sudo sed -i 's/SUBSYSTEM!="memory", ACTION!="add", GOTO="memory_hotplug_end"/SUBSYSTEM=="*", GOTO="memory_hotplug_end"/' /etc/udev/rules.d/40-redhat.rules
      
      *You will need to reboot the system to initialize the above changes.*

#. Continue to :ref:`installing NVIDIA Docker for RHEL <docker_rhel>`

Ubuntu 18.04
---------------------------------------------------------------

.. admonition:: Recommended

   Follow the installation instructions on `NVIDIA's CUDA Installation Guide`_ for full instructions suitable for your platform. The information listed below is a summary of the necessary steps, and does not cover the full range of options available.

#. Install the kernel headers and development tools necessary

   .. code-block:: console
      
      $ sudo apt-get update
      $ sudo apt-get install linux-headers-$(uname -r) gcc

#. Install the CUDA repository and driver on Ubuntu

   .. code-block:: console
      
      $ curl -O https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
      $ sudo dpkg -i cuda-repo-ubuntu1804_10.1.243-1_amd64.deb
      $ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
      $ sudo apt-get update && sudo apt-get install -y nvidia-driver-418

#. Restart your machine

   ``sudo reboot``

#. Verify the installation completed correctly, by asking ``nvidia-smi``, NVIDIA's system management interface application, to list the available GPUs.
   
   .. code-block:: console
      
      $ nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)

#. Enable NVIDIA's persistence daemon. This is mandatory for IBM POWER, but is recommended for other platforms as well.
      
      .. code-block:: console
         
         $ sudo systemctl enable nvidia-persistenced

#. Continue to :ref:`installing NVIDIA Docker for Ubuntu <docker_ubuntu>`

Install Docker CE and NVIDIA docker
====================================

.. contents:: Follow the instructions for your OS and architecture:
   :local:

.. _docker_rhel:

CentOS 7 / RHEL 7 / Amazon Linux (x64)
--------------------------------------

.. note:: For IBM POWER9, see the next section :ref:`installing NVIDIA Docker for IBM POWER <docker_power>`

#. Follow the instructions for Docker CE for your platform at `Get Docker Engine - Community for CentOS`_

#. Tell Docker to start after a reboot

   .. code-block:: console
   
      $ sudo systemctl enable docker && sudo systemctl start docker

#. Verify that docker is running

   .. code-block:: console
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

   .. code-block:: console
   
      $ sudo usermod -aG docker $USER

   Then, log out and log back in:
   
   .. code-block:: console
   
      $ exit

#. Install nvidia-docker

   .. code-block:: console
   
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
      
      $ sudo yum install -y nvidia-container-toolkit
      $ sudo systemctl restart docker
      $ sudo yum install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
      $ sudo systemctl restart docker

#. Verify the NVIDIA docker installation

   .. code-block:: console
   
      $ sudo docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)
      
#. Continue to :ref:`Installing the SQream DB Docker container <installing_sqream_db_docker>`

.. _docker_power:

CentOS 7 / RHEL 7 (IBM POWER)
-------------------------------

#. Install Docker for IBM POWER

   .. code-block:: console
      
      $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/container-selinux-2.9-4.el7.noarch.rpm
      $ wget http://ftp.unicamp.br/pub/ppc64el/rhel/7_1/docker-ppc64el/docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm
      $ yum install -y container-selinux-2.9-4.el7.noarch.rpm docker-ce-18.03.1.ce-1.el7.centos.ppc64le.rpm

#. Tell Docker to start after a reboot

   .. code-block:: console
   
      $ sudo systemctl enable docker && sudo systemctl start docker

#. Verify that docker is running

   .. code-block:: console
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

   .. code-block:: console
   
      $ sudo usermod -aG docker $USER

   .. Note:: Log out and log back in again after this action

#. Install nvidia-docker

   * Install the NVIDIA container and container runtime packages from NVIDIA's repository:
      
      .. code-block:: console
      
         $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
         $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
         
         $ sudo yum install -y libnvidia-container* nvidia-container-runtime*

   * Add the NVIDIA runtime to the Docker daemon and restart docker:
      
      .. code-block:: console
      
         $ sudo mkdir -p /etc/systemd/system/docker.service.d/
         $ echo -e "[Service]\nExecStart\nExecStart=/usr/bin/dockerd --add-runtime=nvidia=/usr/bin/nvidia-container-runtime" | sudo tee /etc/systemd/system/docker.service.d/override.conf

         $ sudo systemctl daemon-reload && sudo systemctl restart docker

#. Verify the NVIDIA docker installation succeeded

   .. code-block:: console
   
      $ docker run --runtime=nvidia --rm nvidia/cuda-ppc64le nvidia-smi -L
      GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-SXM2-16GB (UUID: GPU-...)

#. Continue to :ref:`Installing the SQream DB Docker container <installing_sqream_db_docker>`

.. _docker_ubuntu:

Ubuntu 18.04 (x64)
-----------------------------------

#. Follow the instructions for Docker CE for your platform at `Get Docker Engine - Community for CentOS`_

#. Tell Docker to start after a reboot

   .. code-block:: console
   
      $ sudo systemctl enable docker && sudo systemctl start docker

#. Verify that docker is running

   .. code-block:: console
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

   .. code-block:: console
   
      $ sudo usermod -aG docker $USER

   .. Note:: Log out and log back in again after this action

#. Install nvidia-docker

   .. code-block:: console
   
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
      
      $ sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
      $ sudo systemctl restart docker


#. Verify the NVIDIA docker installation

   .. code-block:: console
   
      $ sudo docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi -L
      GPU 0: Tesla V100-PCIE-16GB (UUID: GPU-...)
      GPU 1: Tesla V100-PCIE-16GB (UUID: GPU-...)

#. Continue to :ref:`Installing the SQream DB Docker container <installing_sqream_db_docker>`


.. _preparing_mounts:

Preparing directories and mounts for SQream DB
===============================================

SQream DB contains several directories that you may be asked to define

.. list-table:: Directories and paths
   :widths: 40 60
   :header-rows: 1
   
   * - Path name
     - Definition
   * - ``storage``
     - The location where SQream DB stores data, metadata, and logs
   * - ``exposed path``
     - A location that SQream DB can read and write to. Used for allowing access to shared raw files like CSVs on local or NFS drives
   * - ``logs``
     - Optional location for debug logs

.. note:: By default, SQream DB can't access any OS path. You must explicitly allow it.


.. _installing_sqream_db_docker:

Install the SQream DB Docker container
=========================================

#. Download the SQream DB tarball and license package

   In the e-mail from your account manager at SQream, you have received a download link for the SQream DB installer and a license package.
   Download the SQream DB tarball to the user home directory. For example:

   .. code-block:: console
   
      $ cd ~
      $ curl -O https://get.sqream.com/x86/sqream_installer-2.0.7-DB2019.2.1.4-CO1.7.5-ED3.0.1-x86_64.tar.gz

#. Extract the tarball into your home directory

   .. code-block:: console
      
      $ tar xf sqream_installer-2.0.7-DB2019.2.1.4-CO1.7.5-ED3.0.1-x86_64.tar.gz

#. Copy the license package

   Copy the license package from your home directory to the license subdirectory which is located in the newly created SQream installer directory.
   
   For example, if the licence package you received is titled ``license_package.tar.gz``:
   
   .. code-block:: console
      
      $ cp ~/license_package.tar.gz sqream_installer-2.0.7-DB2019.2.1.4-CO1.7.5-ED3.0.1-x86_64/license

#. Enter the installer directory

   .. code-block:: console
   
      $ cd sqream_installer-2.0.7-DB2019.2.1.4-CO1.7.5-ED3.0.1-x86_64

#. Install SQream DB
   
   In most cases, the installation command will look like this:
   
   .. code-block:: console
   
      $ ./sqream-install -i -k -v <path to storage> -d <path to shared folder> -l <path to debug logs directory>
   
   For example, if the main storage path for SQream DB is ``/mnt/largedrive`` and the desired shared access path is ``/mnt/nfs/source_files``, the command will look like:
   
   .. code-block:: console
   
      $ ./sqream-install -i -k -v /mnt/largedrive -d /mnt/nfs/source_files
   
   For a full list of options and commands, see the :ref:`Docker installer reference <docker_installer_ref>`

#. SQream DB is now successfully installed, but not yet running.


.. _start_local_cluster:

Starting your first local cluster
=========================================

#. Enter the console, which helps coordinate SQream DB components
   
   .. code-block:: console
   
      $ ./sqream-console

#. Start the master components:
   
   .. code-block:: console
   
      sqream-console>sqream master --start
        starting master server in single_host mode ...
        sqream_single_host_master is up and listening on ports:   3105,3108


#. Start workers to join the cluster:
   
   .. code-block:: console
   
      sqream-console>sqream worker --start 2
        started sqream_single_host_worker_0 on port 5000, allocated gpu: 0
        started sqream_single_host_worker_1 on port 5001, allocated gpu: 1

   .. note:: By default, each worker is allocated a full GPU. To launch more workers than available GPUs, see the :ref:`Console reference <console_ref>`

#. SQream DB is now running! You can exit the console by typing ``exit``.

.. rubric:: What's next?

* :ref:`Create your first table <create_first_table>`

* :ref:`Connect an external tool to SQream DB <connect_first_tool>`

* :ref:`Additional system configuration for performance and stability <recommended_configuration>`


.. Some replacements:

.. _`Latest Tesla driver for Linux x64`: https://www.nvidia.com/Download/driverResults.aspx/152242/en-us
.. _`Latest Tesla driver for Linux x64 POWER LE`: https://www.nvidia.com/Download/driverResults.aspx/152241/en-us
.. _`NVIDIA's CUDA Installation Guide`: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions
.. _`Get Docker Engine - Community for CentOS`: https://docs.docker.com/install/linux/docker-ce/centos/
.. _`Get Docker Engine - Community for Ubuntu`: https://docs.docker.com/install/linux/docker-ce/ubuntu/
