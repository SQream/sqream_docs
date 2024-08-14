.. _pre-installation_configurations:

******************************
Pre-Installation Configuration
******************************

Before installing SQreamDB, it is essential that you tune your system for better performance and stability.

.. contents:: 
   :local:
   :depth: 1

Basic Input/Output System Settings
==================================

The first step when setting your pre-installation configurations is to use the basic input/output system (BIOS) settings.

The BIOS settings may have a variety of names, or may not exist on your system. Each system vendor has a different set of settings and variables. It is safe to skip any and all of the configuration steps, but this may impact performance.

If any doubt arises, consult the documentation for your server or your hardware vendor for the correct way to apply the settings.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1
   
   * - Item
     - Setting
     - Rationale
   * - **Management console access**
     - **Connected**
     - Connection to Out-of-band (OOB) required to preserve continuous network uptime.
   * - **All drives**
     - **Connected and displayed on RAID interface**
     - Prerequisite for cluster or OS installation.
   * - **RAID volumes**
     - **Configured according to project guidelines. Must be rebooted to take effect.**
     - Clustered to increase logical volume and provide redundancy.
   * - **Fan speed Thermal Configuration.**
     - Dell fan speed: **High Maximum**. Specified minimum setting: **60**. HPe thermal configuration: **Increased cooling**.
     - NVIDIA Tesla GPUs are passively cooled and require high airflow to operate at full performance.
   * - **Power regulator or iDRAC power unit policy**   
     - HPe: **HP static high performance** mode enabled. Dell: **iDRAC power unit policy** (power cap policy) disabled.
     - Other power profiles (such as "balanced") throttle the CPU and diminishes performance. Throttling may also cause GPU failure.   
   * - **System Profile**, **Power Profile**, or **Performance Profile**
     - **High Performance**
     - The Performance profile provides potentially increased performance by maximizing processor frequency, and the disabling certain power saving features such as C-states. Use this setting for environments that are not sensitive to power consumption.
   * - **Power Cap Policy** or **Dynamic power capping**
     - **Disabled**
     - Other power profiles (like "balanced") throttle the CPU and may diminish performance or cause GPU failure. This setting may appear together with the above (Power profile or Power regulator). This setting allows disabling system ROM power calibration during the boot process. Power regulator settings are named differently in BIOS and iLO/iDRAC.
   * - **Intel Turbo Boost**
     - **Enabled**
     - Intel Turbo Boost enables overclocking the processor to boost CPU-bound operation performance. Overclocking may risk computational jitter due to changes in the processor's turbo frequency. This causes brief pauses in processor operation, introducing uncertainty into application processing time. Turbo operation is a function of power consumption, processor temperature, and the number of active cores. 	 
   * - **Intel Virtualization Technology** (VT-d)
     - **Disable**
     - VT-d is optimal for running VMs. However, when running Linux natively, disabling VT-d boosts performance by up to 10%.	 
   * - **Logical Processor**
     - **HPe**: Enable **Hyperthreading** **Dell**: Enable **Logical Processor**
     - Hyperthreading doubles the amount of logical processors, which may improve performance by ~5-10% for CPU-bound operations.	 	 
   * - **Intel Virtualization Technology** (VT-d)
     - **Disable**
     - VT-d is optimal for running VMs. However, when running Linux natively, disabling VT-d boosts performance by up to 10%.	  
   * - **Processor C-States** (Minimum processor idle power core state)
     - **Disable** 
     - Processor C-States reduce server power when the system is in an idle state. This causes slower cold-starts when the system transitions from an idle to a load state, and may reduce query performance by up to 15%.	 	 
   * - **HPe**: **Energy/Performance bias**
     - **Maximum performance**
     - Configures processor sub-systems for high-performance and low-latency. Other power profiles (like "balanced") throttle the CPU and may diminish performance. Use this setting for environments that are not sensitive to power consumption.		 
   * - **HPe**: **DIMM voltage**
     - **Optimized for Performance**
     - Setting a higher voltage for DIMMs may increase performance.		 
   * - **Memory Operating Mode**
     - **Optimizer Mode**, **Disable Node Interleaving**, **Auto Memory Operating Voltage**
     - Memory Operating Mode is tuned for performance in **Optimizer** mode. Other modes may improve reliability, but reduce performance. **Node Interleaving** should be disabled because enabling it interleaves the memory between memory nodes, which harms NUMA-aware applications such as SQreamDB.	 
   * - **HPe**: **Memory power savings mode**
     - **Maximum performance**
     - This setting configures several memory parameters to optimize the performance of memory sub-systems. The default setting is **Balanced**.	 
   * - **HPe ACPI SLIT**
     - **Enabled**
     - ACPI SLIT sets the relative access times between processors and memory and I/O sub-systems. ACPI SLIT enables operating systems to use this data to improve performance by more efficiently allocating resources and workloads.	 
   * - **QPI Snoop**
     - **Cluster on Die** or **Home Snoop**
     - QPI (QuickPath Interconnect) Snoop lets you configure different Snoop modes that impact the QPI interconnect. Changing this setting may improve the performance of certain workloads. The default setting of **Home Snoop** provides high memory bandwidth in an average NUMA environment. **Cluster on Die** may provide increased memory bandwidth in highly optimized NUMA workloads. **Early Snoop** may decrease memory latency, but may result in lower overall bandwidth compared to other modes.
	 
Installing the Operating System
================================ 

Before You Begin
-------------------

* Your system must have at least 200 gigabytes of free space on the root ``/`` mount.

* For a multi-node cluster, you must have external shared storage provided by systems like General Parallel File System (GPFS), Weka, or VAST.

* Once the BIOS settings have been set, you must install the operating system.

* A SQreamDB installation requires RHEL8.8/8.9

* Verify the exact RHEL8 version with your storage vendor to avoid driver incompatibility.

Installation
----------------

#. Select a language (English recommended).
#. From **Software Selection**, select **Minimal** and check the **Development Tools** group checkbox.

   Selecting the **Development Tools** group installs the following tools:

	* autoconf
	* automake
	* binutils
	* bison
	* flex
	* gcc
	* gcc-c++
	* gettext
	* libtool
	* make
	* patch
	* pkgconfig
	* redhat-rpm-config
	* rpm-build
	* rpm-sign

#. Continue the installation.
#. Set up the necessary drives and users as per the installation process.

   The OS shell is booted up.

Configuring the Operating System
==================================

When configuring the operating system, several basic settings related to creating a new server are required. Configuring these as part of your basic set-up increases your server's security and usability.

Creating a ``sqream`` User
----------------------------

**The sqream user must have the same UID and GID across all servers in your cluster.**

If the ``sqream`` user does not have the same UID and GID across all servers and there is no critical data stored under ``/home/sqream``, it is recommended to delete the ``sqream`` user and sqream group from your servers. Subsequently, create new ones with the same ID, using the following command:

   .. code-block:: console

      sudo userdel sqream
      sudo rm /var/spool/mail/sqream
   
Before adding a user with a specific UID and GID, it is crucial to verify that such Ids do not already exist.

The steps below guide you on creating a ``sqream`` user with an exemplary ID of ``1111``.
   
1. Verify that a ``1111`` UID does not already exists:  
   
   .. code-block:: console
   
      cat /etc/passwd |grep 1111
	  
2. Verify that a ``1111`` GID does not already exists:  
   
   .. code-block:: console
   
      cat /etc/group |grep 1111
   
3. Add a user with an identical UID on all cluster nodes:

   .. code-block:: console

      useradd -u 1111 sqream
   
4. Add a ``sqream`` user to the ``wheel`` group.

   .. code-block:: console

      sudo usermod -aG wheel sqream
   
   You can remove the ``sqream`` user from the ``wheel`` group when the installation and configuration are complete:

   .. code-block:: console

      passwd sqream
   
5. Log out and log back in as ``sqream``.

6. If you deleted the ``sqream`` user and recreated it to have a new ID, you must change its ownership to ``/home/sqream`` in order to avoid permission errors.

   .. code-block:: console

      sudo chown -R sqream:sqream /home/sqream
   
Setting Up A Locale
-----------------------

SQreamDB enables you to set up a locale using your own location. To find out your current time-zone, run the ``timedatectl list-timezones`` command.

1. Set the language of the locale:

   .. code-block:: console

      sudo localectl set-locale LANG=en_US.UTF-8

2. Set the time stamp (time and date) of the locale:

   .. code-block:: console

      sudo timedatectl set-timezone Asia/Jerusalem
   
Installing Required Software 
---------------------------------

.. contents:: 
   :local:
   :depth: 1

Installing EPEL Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: console

      sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

Enabling Additional Red Hat Repositories
"""""""""""""""""""""""""""""""""""""""""

Enabling additional Red Hat repositories is essential to install the required packages in the subsequent procedures.

   .. code-block:: console

      sudo subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
      sudo subscription-manager repos --enable rhel-8-for-x86_64-appstream-rpms
      sudo subscription-manager repos --enable rhel-8-for-x86_64-baseos-rpms

Installing Required Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: console

      sudo dnf install chrony pciutils monit zlib-devel openssl-devel kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc net-tools wget jq libffi-devel xz-devel ncurses-compat-libs libnsl gdbm-devel tk-devel sqlite-devel readline-devel texinfo 

Installing Recommended Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: console

      sudo dnf install bash-completion.noarch vim-enhanced vim-common net-tools iotop htop psmisc screen xfsprogs wget yum-utils dos2unix
	  
**For SQreamDB version 4.4 or newer, install Python 3.9.13.**
  
1. Download the Python 3.9.13 source code tarball file from the following URL into the ``/home/sqream`` directory:

   .. code-block:: console

      wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tar.xz
   
2. Extract the Python 3.9.13 source code into your current directory:

   .. code-block:: console

      tar -xf Python-3.9.13.tar.xz
   
3. Navigate to the Python 3.9.13 directory:

   .. code-block:: console

      cd Python-3.9.13
  
4. Run the ``./configure`` script:

   .. code-block:: console

      ./configure --enable-loadable-sqlite-extensions
   
5. Build the software:

   .. code-block:: console

      make -j30
  
6. Install the software:

   .. code-block:: console

      sudo make install
  
7. Verify that Python 3.9.13 has been installed:

   .. code-block:: console

      python3 --version
  
.. _installing_nodejs:
  
Installing NodeJS 
^^^^^^^^^^^^^^^^^^

NodeJS is necessary only when the UI runs on the same server as SqreamDB. If not, you can skip this step.

1. Download the NodeJS source code tarball file from the following URL into the ``/home/sqream`` directory:

   .. code-block:: console

      wget https://nodejs.org/dist/v16.20.0/node-v16.20.0-linux-x64.tar.xz
      tar -xf node-v16.20.0-linux-x64.tar.xz
	  
2. Move the node-v16.20.0-linux-x64 file to the */usr/local* directory.

   .. code-block:: console

      sudo mv  node-v16.20.0-linux-x64 /usr/local  
	  
3. Navigate to the ``/usr/bin/`` directory:

   .. code-block:: console

      cd /usr/bin 
	  
4. Create a symbolic link to the ``/local/node-v16.20.0-linux-x64/bin/node node`` directory:

   .. code-block:: console

      sudo ln -s ../local/node-v16.20.0-linux-x64//bin/node node
	  
5. Create a symbolic link to the ``/local/node-v16.20.0-linux-x64/bin/npm npm`` directory:

   .. code-block:: console

      sudo ln -s ../local/node-v16.20.0-linux-x64/bin/npm npm 
	  
6. Create a symbolic link to the ``/local/node-v16.20.0-linux-x64/bin/npx npx`` directory:

   .. code-block:: console

      sudo ln -s ../local/node-v16.20.0-linux-x64/bin/npx npx	  
	  
7. Install the ``pm2`` process management:

   .. code-block:: console
   
      sudo npm install pm2 -g
      cd /usr/bin
      sudo ln -s ../local/node-v16.20.0-linux-x64/bin/pm2 pm2
  
8. If installing the ``pm2`` process management fails, install it offline:	 
  
  a. On a machine with internet access, install the following:

   * nodejs
   * npm
   * pm2
   
  b. Extract the pm2 module to the correct directory:   

     .. code-block:: console

        cd /usr/local/node-v16.20.0-linux-x64/lib/node_modules
        tar -czvf pm2_x86.tar.gz pm2
		
  c. Copy the ``pm2_x86.tar.gz`` file to a server without access to the internet and extract it.
  
    ::
  
  d. Move the ``pm2`` folder to the ``/usr/local/node-v16.20.0-linux-x64/lib/node_modules`` directory:

     .. code-block:: console

        sudo mv pm2 /usr/local/node-v16.20.0-linux-x64/lib/node_modules

  e. Navigate back to the ``/usr/bin`` directory:

     .. code-block:: console

        cd /usr/bin

  f. Create a symbolink to the ``pm2`` service:

     .. code-block:: console

        sudo ln -s /usr/local/node-v16.20.0-linux-x64/lib/node_modules/pm2/bin/pm2 pm2

  g. Verify that installation was successful without using ``sudo``:

     .. code-block:: console

        pm2 list
  
  h. Verify that the node versions for the above are correct:

     .. code-block:: console

        node --version
					
Configuring Chrony for RHEL8 Only
----------------------------------

#. Start the Chrony service:

   .. code-block:: console

      sudo systemctl start chronyd
	
#. Enable the Chrony service to start automatically at boot time:

   .. code-block::

      sudo systemctl enable chronyd
	
#. Check the status of the Chrony service:

   .. code-block::

      sudo systemctl status chronyd
		
Configuring the Server to Boot Without Linux GUI
----------------------------------------------------

We recommend that you configure your server to boot without a Linux GUI by running the following command:					 

   .. code-block:: console

      sudo systemctl set-default multi-user.target	

Running this command activates the **NO-UI** server mode.

Configuring the Security Limits
--------------------------------

The security limits refer to the number of open files, processes, etc.

   .. code-block:: console

      sudo bash

   .. code-block:: console

      echo -e "sqream soft nproc 1000000\nsqream hard nproc 1000000\nsqream soft nofile 1000000\nsqream hard nofile 1000000\nroot soft nproc 1000000\nroot hard nproc 1000000\nroot soft nofile 1000000\nroot hard nofile 1000000\nsqream soft core unlimited\nsqream hard core unlimited" >> /etc/security/limits.conf
  
Configuring the Kernel Parameters
---------------------------------

1. Insert a new line after each kernel parameter:

   .. code-block:: console

      echo -e "vm.dirty_background_ratio = 5 \n vm.dirty_ratio = 10 \n vm.swappiness = 10 \n vm.vfs_cache_pressure = 200 \n vm.zone_reclaim_mode = 0 \n" >> /etc/sysctl.conf
  
2. Check the maximum value of the ``fs.file``: 

   .. code-block:: console

      sysctl -n fs.file-max

Configuring the Firewall
--------------------------

The example in this section shows the open ports for four ``sqreamd`` sessions. If more than four are required, open the required ports as needed. Port 8080 in the example below is a new UI port.

The ports listed below are required, and the same logic applies to all additional SQreamDB Worker ports.

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Port
     - Use
   * - 8080
     - UI port
   * - 443
     - UI over HTTPS ( requires nginx installation )
   * - 3105
     - SqreamDB metadataserver service
   * - 3108
     - SqreamDB serverpicker service
   * - 3109
     - SqreamDB serverpicker service over ssl
   * - 5000
     - SqreamDB first worker default port
   * - 5100
     - SqreamDB first worker over ssl default port
   * - 5001
     - SqreamDB second worker default port
   * - 5101
     - SqreamDB second worker over ssl default port

1. Start the service and enable FirewallID on boot:

   .. code-block:: console

      systemctl start firewalld
  
2. Add the following ports to the permanent firewall:

   .. code-block:: console

      firewall-cmd --zone=public --permanent --add-port=8080/tcp
      firewall-cmd --zone=public --permanent --add-port=3105/tcp
      firewall-cmd --zone=public --permanent --add-port=3108/tcp
      firewall-cmd --zone=public --permanent --add-port=5000-5003/tcp
      firewall-cmd --zone=public --permanent --add-port=5100-5103/tcp
      firewall-cmd --permanent --list-all

3. Reload the firewall:

   .. code-block:: console

      firewall-cmd --reload

4. Enable FirewallID on boot:

   .. code-block:: console

      systemctl enable firewalld 

   If you do not need the firewall, you can disable it:
  
   .. code-block:: console

      sudo systemctl stop firewalld
      sudo systemctl disable firewalld  
  
Disabling SELinux
-------------------

Disabling SELinux is a recommended action.

1. Show the status of ``selinux``:

   .. code-block:: console

      sudo sestatus

2. If the output is not ``disabled``, edit the ``/etc/selinux/config`` file: 

   .. code-block:: console

      sudo vim /etc/selinux/config
  
3. Change ``SELINUX=enforcing`` to ``SELINUX=disabled``:
  
   The above changes will only take effect after rebooting the server.

   You can disable selinux immediately after rebooting the server by running the following command:

   .. code-block:: console

      sudo setenforce 0

Configuring the ``/etc/hosts`` File
------------------------------------

1. Edit the ``/etc/hosts`` file:

   .. code-block:: console

      sudo vim /etc/hosts

2. Call your local host:

   .. code-block:: console

      127.0.0.1	localhost
      <server1 ip>	<server_name>
      <server2 ip>	<server_name>

Installing the NVIDIA CUDA Driver
==================================

After configuring your operating system, you must install the NVIDIA CUDA driver.

.. warning:: If your Linux GUI runs on the server, it must be stopped before installing the CUDA drivers.

Before You Begin 
----------------

1. Verify that the NVIDIA card has been installed and is detected by the system:

   .. code-block:: console

      lspci | grep -i nvidia
  
2. Verify that ``gcc`` has been installed:

   .. code-block:: console

      gcc --version
  
3. If ``gcc`` has not been installed, install it for RHEL:

   .. code-block:: console

        sudo yum install -y gcc

Updating the Kernel Headers  
---------------------------

1. Update the kernel headers on RHEL:

   .. code-block:: console

      sudo yum install kernel-devel-$(uname -r) kernel-headers-$(uname -r)
		  
2. Make sure kernel-devel and kernel-headers match installed kernel:
		  
   .. code-block:: console
	 
      uname -r
      rpm -qa |grep kernel-devel-$(uname -r)
      rpm -qa |grep kernel-headers-$(uname -r) 
		  		  
Disabling Nouveau  
-----------------

Disable Nouveau, which is the default operating system driver.

1. Check if the Nouveau driver has been loaded:

   .. code-block:: console

      lsmod | grep nouveau

   If the Nouveau driver has been loaded, the command above generates output. If the Nouveau driver has not been loaded, you may skip step 2 and 3.

2. Blacklist the Nouveau driver to disable it:

   .. code-block:: console

      cat <<EOF | sudo tee /etc/modprobe.d/blacklist-nouveau.conf
      blacklist nouveau
      options nouveau modeset=0
      EOF 
 
3. Regenerate the kernel ``initramfs`` directory set:

  a. Modify the ``initramfs`` directory set:
  
     .. code-block:: console

        sudo dracut --force
	
  b. Reboot the server:

     .. code-block:: console

        sudo reboot

Installing the CUDA Driver
--------------------------
  
The current recommendation is for CUDA 12.3.2.
  
.. contents:: 
   :local:
   :depth: 1
  
For questions related to which driver to install, contact `SqreamDB support <https://sqream.atlassian.net/servicedesk/customer/portal/2/group/8/create/26>`_.

Installing the CUDA Driver from the Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the CUDA driver from the Repository is the recommended installation method.

1. Install the CUDA dependencies for one of the following operating systems:

     .. code-block:: console

        sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
	
2. (Optional) Install the CUDA dependencies from the ``epel`` repository:

   .. code-block:: console

      sudo yum install dkms libvdpau

   Installing the CUDA depedendencies from the ``epel`` repository is only required for installing ``runfile``.

3. Download and install the required local repository:
		 

    * **RHEL8.8/8.9 CUDA 12.3.2 repository ( INTEL ) installation ( Required for H/L Series GPU models ):**

	  .. code-block:: console
	  
		 wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda-repo-rhel8-12-3-local-12.3.2_545.23.08-1.x86_64.rpm
		 sudo dnf localinstall cuda-repo-rhel8-12-3-local-12.3.2_545.23.08-1.x86_64.rpm
		 
	  .. code-block:: console
	  
		 sudo dnf clean all
		 sudo dnf -y module install nvidia-driver:latest-dkms	  
	  
Tuning Up NVIDIA Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following procedures exclusively relate to Intel.	
	
.. contents:: 
   :local:
   :depth: 1
	
.. note::  Setting up the NVIDIA POWER9 CUDA driver includes additional set-up requirements. The NVIDIA POWER9 CUDA driver will not function properly if the additional set-up requirements are not followed. See `POWER9 Setup <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#power9-setup>`__ for the additional set-up requirements.
	
Tune Up NVIDIA Performance when Driver Installed from the Repository
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. Check the service status:

   .. code-block:: console

      sudo systemctl status nvidia-persistenced
		 
   If the service exists, it will be stopped by default.

2. Start the service:

   .. code-block:: console

      sudo systemctl start nvidia-persistenced
		 
3. Verify that no errors have occurred:

   .. code-block:: console

      sudo systemctl status nvidia-persistenced
		 
4. Enable the service to start up on boot:   

   .. code-block:: console

      sudo systemctl enable nvidia-persistenced
	  
5. For **H100/A100**, add the following lines:

   .. code-block:: console

      nvidia-persistenced
		 
6. Reboot the server and run the **NVIDIA System Management Interface (NVIDIA SMI)**:

   .. code-block:: console

      nvidia-smi
	  

		
Tune Up NVIDIA Performance when Driver Installed from the Runfile
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. Change the permissions on the ``rc.local`` file to ``executable``:

     .. code-block:: console

        sudo chmod +x /etc/rc.local	  
	  
2. Edit the ``/etc/yum.repos.d/cuda-10-1-local.repo`` file:

     .. code-block:: console

        sudo vim /etc/rc.local		 
		 
3. Add the following lines:

   * **For H100/A100**:

      .. code-block:: console

        nvidia-persistenced

4. Reboot the server and run the ``NVIDIA System Management Interface (NVIDIA SMI)``:

   .. code-block:: console

        nvidia-smi
	  
  
Enabling Core Dumps
===================

While this procedure is optional, SQreamDB recommends that core dumps be enabled. Note that the default ``abrt`` format is not ``gdb`` compatible, and that for SQreamDB support to be able to analyze your core dumps, they must be ``gdb`` compatible.

.. contents:: 
   :local:
   :depth: 1

Checking the ``abrtd`` Status
-----------------------------

1. Check if ``abrtd`` is running:

   .. code-block:: console

      sudo ps -ef |grep abrt

2. If **abrtd** is running, stop it:	  
	  
   .. code-block:: console

      for i in abrt-ccpp.service abrtd.service abrt-oops.service abrt-pstoreoops.service abrt-vmcore.service abrt-xorg.service ; do sudo systemctl disable $i; sudo systemctl stop $i; done

Setting the Limits
------------------
	  
1. Set the limits:

   .. code-block:: console

      ulimit -c
	  
2. If the output is ``0``, add the following lines to the ``/etc/security/limits.conf`` file:	  
	  
   .. code-block:: console

      *          soft     core           unlimited
      *          hard     core           unlimited	  
	  
3. To apply the limit changes, log out and log back in.	

Creating the Core Dump Directory
--------------------------------

Because the core dump file may be the size of total RAM on the server, verify that you have sufficient disk space. In the example above, the core dump is configured to the ``/tmp/core_dumps`` directory. If necessary, replace path according to your own environment and disk space.

1. Make the ``/tmp/core_dumps`` directory:

   .. code-block:: console

      mkdir /tmp/core_dumps

2. Set the ownership of the ``/tmp/core_dumps`` directory:

   .. code-block:: console

      sudo chown sqream.sqream /tmp/core_dumps
  
3. Grant read, write, and execute permissions to all users:

   .. code-block:: console

      sudo chmod -R 777 /tmp/core_dumps
	 	  

Setting the Output Directory on the ``/etc/sysctl.conf`` File 
-------------------------------------------------------------

1. Open the ``/etc/sysctl.conf`` file in the Vim text editor:

   .. code-block:: console

      sudo vim /etc/sysctl.conf

2. Add the following to the bottom of the file:

   .. code-block:: console

      kernel.core_uses_pid = 1
      kernel.core_pattern = /tmp/core_dumps/core-%e-%s-%u-%g-%p-%t
      fs.suid_dumpable = 2

3. To apply the changes without rebooting the server, run the following:
	  
  .. code-block:: console

     sudo sysctl -p

4. Check that the core output directory points to the following:

  .. code-block:: console

     sudo cat /proc/sys/kernel/core_pattern
	  
  The following shows the correct generated output:
	  
  .. code-block:: console

     /tmp/core_dumps/core-%e-%s-%u-%g-%p-%t	  
	  
Verifying that the Core Dumps Work 
----------------------------------

You can verify that the core dumps work only after installing and running SQreamDB. This causes the server to crash and a new ``core.xxx`` file to be included in the folder that is written in ``/etc/sysctl.conf``.

1. Stop and restart all SQreamDB services.

    ::

2. Connect to SQreamDB with ClientCmd and run the following command:

  .. code-block:: console

      select abort_server();
   
Verify Your SQreamDB Installation
------------------------------------

1. Verify that the ``sqream`` user exists and has the same ID on all cluster servers.

  .. code-block:: console

      id sqream       

2. please verify that the storage is mounted on all cluster servers.

   .. code-block:: console

      mount           

3. make sure that the driver is properly installed.

   .. code-block:: console

      nvidia-smi      

4. Verify that the kernel file-handles allocation is greater than or equal to ``2097152``:

   .. code-block:: console

      sysctl -n fs.file-max   

5. Verify limits (run this command as a ``sqream`` user):

   .. code-block:: console

      ulimit -c -u -n 
	
      Desired output:
      core file size (blocks, -c) unlimited
      max user processes (-u) 1000000
      open files (-n) 1000000
   
Troubleshooting Core Dumping 
------------------------------

This section describes the troubleshooting procedure to be followed if all parameters have been configured correctly, but the cores have not been created.

1. Reboot the server.

    ::

2. Verify that you have folder permissions:

   .. code-block:: console

      sudo chmod -R 777 /tmp/core_dumps  
   
3. Verify that the limits have been set correctly:

   .. code-block:: console

      ulimit -c

   If all parameters have been configured correctly, the correct output is:

   .. code-block:: console

      core file size          (blocks, -c) unlimited

4. If all parameters have been configured correctly, but running ``ulimit -c`` outputs ``0``, run the following:

   .. code-block:: console

      sudo vim /etc/profile

5. Search for the following line and disable it using the ``#`` symbol:

   .. code-block:: console

      ulimit -S -c 0 > /dev/null 2>&1

6. Log out and log back in.

    ::

7. Run the ``ulimit -c`` command:

   .. code-block:: console

      ulimit -a 	  

8. If the line is not found in ``/etc/profile``, do the following:	  
	  
   a. Run the following command:

      .. code-block:: console

         sudo vim /etc/init.d/functions

   b. Search for the following line disable it using the ``#`` symbol and reboot the server.
   
      .. code-block:: console

         ulimit -S -c ${DAEMON_COREFILE_LIMIT:-0} >/dev/null 2>&1
