.. _recommended_pre-installation_configurations:

*********************************************
Recommended Pre-Installation Configuration
*********************************************
Before :ref:`installing SQream DB<installing_sqream_db_docker>`, SQream recommends you to tune your system for better performance and stability.

This page provides recommendations for production deployments of SQream and describes the following:

.. contents:: 
   :local:
   :depth: 1

Recommended BIOS Settings
==========================
The first step when setting your pre-installation configurations is to use the recommended BIOS settings.

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
     - Connection to OOB required to preserve continuous network uptime.
   * - **All drives**
     - **Connected and displayed on RAID interface**
     - Prerequisite for cluster or OS installation.
   * - **RAID volumes.**
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
   * - **Logical Processor**
     - **HPe**: Enable **Hyperthreading** **Dell**: Enable **Logical Processor**
     - Hyperthreading doubles the amount of logical processors, which may improve performance by ~5-10% for CPU-bound operations.	 	 
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
     - Memory Operating Mode is tuned for performance in **Optimizer** mode. Other modes may improve reliability, but reduce performance. **Node Interleaving** should be disabled because enabling it interleaves the memory between memory nodes, which harms NUMA-aware applications such as SQream DB.	 
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
===================================================	 
Once the BIOS settings have been set, you must install the operating system. Either the CentOS (versions 7.6-7.9) or RHEL (versions 7.6-7.9) must be installed before installing the SQream database, by either the customer or a SQream representative.

**To install the operating system:**

#. Select a language (English recommended).
#. From **Software Selection**, select **Minimal**.
#. Select the **Development Tools** group checkbox.
#. Continue the installation.
#. Set up the necessary drives and users as per the installation process.

   Using Debugging Tools is recommended for future problem-solving if necessary.

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

The root user is created and the OS shell is booted up.  

Configuring the Operating System
===================================================
Once you've installted your operation system, you can configure it. When configuring the operating system, several basic settings related to creating a new server are required. Configuring these as part of your basic set-up increases your server's security and usability. 

Logging In to the Server
--------------------------------
You can log in to the server using the server's IP address and password for the **root** user. The server's IP address and **root** user were created while installing the operating system above.

Automatically Creating a SQream User
------------------------------------

**To automatically create a SQream user:**

#. If a SQream user was created during installation, verify that the same ID is used on every server:

   .. code-block:: console

      $ sudo id sqream
  
  The ID **1000** is used on each server in the following example:
    
  .. code-block:: console

     $ uid=1000(sqream) gid=1000(sqream) groups=1000(sqream)
   
2. If the ID's are different, delete the SQream user and SQream group from both servers:

   .. code-block:: console

      $ sudo userdel sqream
   
3. Recreate it using the same ID:
   
   .. code-block:: console

      $ sudo rm /var/spool/mail/sqream

Manually Creating a SQream User
--------------------------------

**To manually create a SQream user:**

SQream enables you to manually create users. This section shows you how to manually create a user with the UID **1111**. You cannot manually create during the operating system installation procedure.
   
1. Add a user with an identical UID on all cluster nodes:

   .. code-block:: console

      $ useradd -u 1111 sqream
   
2. Add the user **sqream** to the **wheel** group.

   .. code-block:: console

      $ sudo usermod -aG wheel sqream
   
   You can remove the SQream user from the **wheel** group when the installation and configuration are complete:

   .. code-block:: console

      $ passwd sqream
   
3. Log out and log back in as **sqream**.

  .. note:: If you deleted the **sqream** user and recreated it with different ID, to avoid permission errors, you must change its ownership to /home/sqream.

4. Change the **sqream** user's ownership to /home/sqream:

   .. code-block:: console

      $ sudo chown -R sqream:sqream /home/sqream
   
Setting Up A Locale
--------------------------------

SQream enables you to set up a locale. In this example, the locale used is your own location.

**To set up a locale:**   

1. Set the language of the locale:

   .. code-block:: console

      $ sudo localectl set-locale LANG=en_US.UTF-8

2. Set the time stamp (time and date) of the locale:

   .. code-block:: console

      $ sudo timedatectl set-timezone Asia/Jerusalem

If needed, you can run the **timedatectl list-timezones** command to see your current time-zone.
  
   
Installing the Required Packages
--------------------------------
You can install the required packages by running the following command:

.. code-block:: console

   $ sudo yum install ntp pciutils monit zlib-devel openssl-devel kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc net-tools wget jq
  
   
Installing the Recommended Tools
--------------------------------
You can install the recommended tools by running the following command:

.. code-block:: console

   $ sudo yum install bash-completion.noarch vim-enhanced vim-common net-tools iotop htop psmisc screen xfsprogs wget yum-utils deltarpm dos2unix   
   

Installing Python 3.6.7
--------------------------------
1. Download the Python 3.6.7 source code tarball file from the following URL into the **/home/sqream** directory:

   .. code-block:: console

      $ wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz
   
2. Extract the Python 3.6.7 source code into your current directory:

   .. code-block:: console

      $ tar -xf Python-3.6.7.tar.xz
   
3. Navigate to the Python 3.6.7 directory:

   .. code-block:: console

      $ cd Python-3.6.7
  
4. Run the **./configure** script:

   .. code-block:: console

      $ ./configure
   
5. Build the software:

   .. code-block:: console

      $ make -j30
  
6. Install the software:

   .. code-block:: console

      $ sudo make install
  
7. Verify that Python 3.6.7 has been installed:

   .. code-block:: console

      $ python3
  
Installing NodeJS on CentOS 
--------------------------------
**To install the node.js on CentOS:**

1. Download the `setup_12.x file <https://rpm.nodesource.com/setup_12.x>`__ as a root user logged in shell:

   .. code-block:: console

      $ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash -
  
2. Clear the YUM cache and update the local metadata:

   .. code-block:: console

      $ sudo yum clean all && sudo yum makecache fast
  
3. Install the **node.js** file:

   .. code-block:: console

      $ sudo yum install -y nodejs
	  
4. Install npm and make it available for all users:

   .. code-block:: console

      $ sudo npm install pm2 -g

Installing NodeJS on Ubuntu
--------------------------------
**To install the node.js file on Ubuntu:**
  
1. Download the `setup_12.x file <https://deb.nodesource.com/setup_12.x>`__ as a root user logged in shell:

   .. code-block:: console

      $ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash -
  
2. Install the node.js file:

   .. code-block:: console

      $ sudo apt-get install -y nodejs  
  
3. Install npm and make it available for all users:

   .. code-block:: console

      $ sudo npm install pm2 -g
	  
Installing NodeJS Offline
-------------------------------------------
**To install NodeJS Offline**

1. Download the NodeJS source code tarball file from the following URL into the **/home/sqream** directory:

   .. code-block:: console

      $ wget https://nodejs.org/dist/v12.13.0/node-v12.13.0-linux-x64.tar.xz
	  
2. Move the node-v12.13.0-linux-x64 file to the */usr/local* directory.

   .. code-block:: console

      $ sudo mv node-v12.13.0-linux-x64  /usr/local

3. Navigate to the */usr/bin/* directory:

   .. code-block:: console

      $ cd /usr/bin
	  
4. Create a symbolic link to the */local/node-v12.13.0-linux-x64/bin/node node* directory:

   .. code-block:: console

      $ sudo ln -s ../local/node-v12.13.0-linux-x64/bin/node node
	  
5. Create a symbolic link to the */local/node-v12.13.0-linux-x64/bin/npm npm* directory:

   .. code-block:: console

      $ sudo ln -s ../local/node-v12.13.0-linux-x64/bin/npm npm
	  
6. Create a symbolic link to the */local/node-v12.13.0-linux-x64/bin/npx npx* directory:

   .. code-block:: console

      $ sudo ln -s ../local/node-v12.13.0-linux-x64/bin/npx npx

7. Verify that the node versions for the above are correct:

   .. code-block:: console

      $ node --version
	  
Installing the pm2 Service Offline
-------------------------------------------
**To install the pm2 Service Offline**

1. On a machine with internet access, install the following:

   * nodejs
   * npm
   * pm2

2. Extract the pm2 module to the correct directory:   

   .. code-block:: console

      $ cd /usr/local/node-v12.13.0-linux-x64/lib/node_modules
      $ tar -czvf pm2_x86.tar.gz pm2

3. Copy the **pm2_x86.tar.gz** file to a server without access to the internet and extract it.

    ::

4. Move the **pm2** folder to the */usr/local/node-v12.13.0-linux-x64/lib/node_modules* directory:

   .. code-block:: console

      $ sudo mv pm2 /usr/local/node-v12.13.0-linux-x64/lib/node_modules
	  
5. Navigate back to the */usr/bin* directory:

   .. code-block:: console

      $ cd /usr/bin again

6.  Create a symbolink to the **pm2** service:

   .. code-block:: console

      $ sudo ln -s /usr/local/node-v12.22.3-linux-x64/lib/node_modules/pm2/bin/pm2 pm2

7. Verify that installation was successful:

   .. code-block:: console

      $ pm2 list

  .. note:: This must be done as a **sqream** user, and not as a **sudo** user.

8.  Verify that the node version is correct:

   .. code-block:: console

      $ node -v
  
Configuring the Network Time Protocol
------------------------------------------- 
This section describes how to configure your **Network Time Protocol (NTP)**.

If you don't have internet access, see `Configure NTP Client to Synchronize with NTP Server <https://www.thegeekstuff.com/2014/06/linux-ntp-server-client/>`__.

**To configure your NTP:**
  
1. Install the NTP file.

   .. code-block:: console

      $ sudo yum install ntp
  
2. Enable the **ntpd** program.

   .. code-block:: console

      $ sudo systemctl enable ntpd
  
3. Start the **ntdp** program.

   .. code-block:: console

      $ sudo systemctl start ntpd
  
4. Print a list of peers known to the server and a summary of their states.   
  
   .. code-block:: console

      $ sudo ntpq -p
  
Configuring the Network Time Protocol Server
--------------------------------------------
If your organization has an NTP server, you can configure it.

**To configure your NTP server:**

1. Output your NTP server address and append ``/etc/ntpd.conf`` to the outuput.

   .. code-block:: console

      $ echo -e "\nserver <your NTP server address>\n" | sudo tee -a /etc/ntp.conf

2. Restart the service.

   .. code-block:: console

      $ sudo systemctl restart ntpd

3. Check that synchronization is enabled:

   .. code-block:: console

      $ sudo timedatectl
  
   Checking that synchronization is enabled generates the following output:

   .. code-block:: console

      $ Local time: Sat 2019-10-12 17:26:13 EDT
     Universal time: Sat 2019-10-12 21:26:13 UTC
           RTC time: Sat 2019-10-12 21:26:13
          Time zone: America/New_York (EDT, -0400)
        NTP enabled: yes
    NTP synchronized: yes
    RTC in local TZ: no
         DST active: yes
    Last DST change: DST began at
                     Sun 2019-03-10 01:59:59 EST
                     Sun 2019-03-10 03:00:00 EDT
    Next DST change: DST ends (the clock jumps one hour backwards) at
                     Sun 2019-11-03 01:59:59 EDT
                     Sun 2019-11-03 01:00:00 EST 
					 
Configuring the Server to Boot Without the UI
---------------------------------------------
You can configure your server to boot without a UI in cases when it is not required (recommended) by running the following command:					 

.. code-block:: console

  $ sudo systemctl set-default multi-user.target	

Running this command activates the **NO-UI** server mode.

Configuring the Security Limits
--------------------------------
The security limits refers to the number of open files, processes, etc.

You can configure the security limits by running the **echo -e** command as a root user logged in shell:

.. code-block:: console

  $ sudo bash

.. code-block:: console

  $ echo -e "sqream soft nproc 1000000\nsqream hard nproc 1000000\nsqream soft nofile 1000000\nsqream hard nofile 1000000\nsqream soft core unlimited\nsqream hard core unlimited" >> /etc/security/limits.conf
  
Configuring the Kernel Parameters
---------------------------------
**To configure the kernel parameters:**

1. Insert a new line after each kernel parameter:

   .. code-block:: console

      $ echo -e "vm.dirty_background_ratio = 5 \n vm.dirty_ratio = 10 \n vm.swappiness = 10 \n vm.vfs_cache_pressure = 200 \n vm.zone_reclaim_mode = 0 \n" >> /etc/sysctl.conf
  
  .. note:: In the past, the **vm.zone_reclaim_mode** parameter was set to **7.** In the latest Sqream version, the vm.zone_reclaim_mode parameter must be set to **0**. If it is not set to **0**, when a numa node runs out of memory, the system will get stuck and will be unable to pull memory from other numa nodes.
  
2. Check the maximum value of the **fs.file**. 

   .. code-block:: console

      $ sysctl -n fs.file-max

3. If the maximum value of the **fs.file** is smaller than **2097152**, run the following command:

   .. code-block:: console

      $ echo "fs.file-max=2097152" >> /etc/sysctl.conf

   **IP4 forward** must be enabled for Docker and K8s installation only.
   
4. Run the following command:

   .. code-block:: console

      $ sudo echo “net.ipv4.ip_forward = 1” >> /etc/sysctl.conf

5. Reboot your system:

   .. code-block:: console

      $ sudo reboot

Configuring the Firewall
--------------------------------
The example in this section shows the open ports for four sqreamd sessions. If more than four are required, open the required ports as needed. Port 8080 in the example below is a new UI port.

**To configure the firewall:**

1. Start the service and enable FirewallID on boot:

   .. code-block:: console

      $ systemctl start firewalld
  
2. Add the following ports to the permanent firewall:

   .. code-block:: console

      $ firewall-cmd --zone=public --permanent --add-port=8080/tcp
      $ firewall-cmd --zone=public --permanent --add-port=3105/tcp
      $ firewall-cmd --zone=public --permanent --add-port=3108/tcp
      $ firewall-cmd --zone=public --permanent --add-port=5000-5003/tcp
      $ firewall-cmd --zone=public --permanent --add-port=5100-5103/tcp
      $ firewall-cmd --permanent --list-all

3. Reload the firewall:

   .. code-block:: console

      $ firewall-cmd --reload

4. Enable FirewallID on boot:

   .. code-block:: console

      $ systemctl enable firewalld 

   If you do not need the firewall, you can disable it:
  
   .. code-block:: console

      $ sudo systemctl disable firewalld  
  
Disabling selinux
--------------------------------
**To disable selinux:**

1. Show the status of **selinux**:

   .. code-block:: console

      $ sudo sestatus

2. If the output is not **disabled**, edit the **/etc/selinux/config** file: 

   .. code-block:: console

      $ sudo vim /etc/selinux/config
  
3. Change **SELINUX=enforcing** to **SELINUX=disabled**.
  
   The above changes will only take effect after rebooting the server.

   You can disable selinux immediately after rebooting the server by running the following command:

   .. code-block:: console

     $ sudo setenforce 0

Configuring the /etc/hosts File
--------------------------------
**To configure the /etc/hosts file:**

1. Edit the **/etc/hosts** file:

   .. code-block:: console

      $ sudo vim /etc/hosts

2. Call your local host:

   .. code-block:: console

      $ 127.0.0.1	localhost
      $ <server1 ip>	<server_name>
      $ <server2 ip>	<server_name>
    
Configuring the DNS
--------------------------------
**To configure the DNS:**

1. Run the **ifconfig** commasnd to check your NIC name. In the following example, **eth0** is the NIC name:

   .. code-block:: console

      $ sudo vim /etc/sysconfig/network-scripts/ifcfg-eth0 

2. Replace the DNS lines from the example above with your own DNS addresses :

   .. code-block:: console

      $ DNS1="4.4.4.4"
      $ DNS2="8.8.8.8"

Installing the Nvidia CUDA Driver
===================================================
After configuring your operating system, you must install the Nvidia CUDA driver.

  .. warning:: If your UI runs on the server, the server must be stopped before installing the CUDA drivers.

CUDA Driver Prerequisites  
--------------------------------
1. Verify that the NVIDIA card has been installed and is detected by the system:

   .. code-block:: console

      $ lspci | grep -i nvidia
  
2. Check which version of gcc has been installed:

   .. code-block:: console

      $ gcc --version
  
3. If gcc has not been installed, install it for one of the following operating systems:

   * On RHEL/CentOS: 

     .. code-block:: console

        $ sudo yum install -y gcc

   * On Ubuntu: 

     .. code-block:: console

        $ sudo apt-get install gcc

Updating the Kernel Headers  
--------------------------------
**To update the kernel headers:**

1. Update the kernel headers on one of the following operating systems:

   * On RHEL/CentOS:

     .. code-block:: console

        $ sudo yum install kernel-devel-$(uname -r) kernel-headers-$(uname -r)
		  
   * On Ubuntu:
   
     .. code-block:: console

        $ sudo apt-get install linux-headers-$(uname -r)
		  
2. Install **wget** one of the following operating systems:

   * On RHEL/CentOS:
   
     .. code-block:: console

        $ sudo yum install wget
		  
   * On Ubuntu:   
		  
     .. code-block:: console

        $ sudo apt-get install wget
		  		  
Disabling Nouveau  
--------------------------------
You can disable Nouveau, which is the default driver.

**To disable Nouveau:**

1. Check if the Nouveau driver has been loaded:

   .. code-block:: console

      $ lsmod | grep nouveau

   If the Nouveau driver has been loaded, the command above generates output.

2. Blacklist the Nouveau drivers to disable them:

   .. code-block:: console

      $ cat <<EOF | sudo tee /etc/modprobe.d/blacklist-nouveau.conf
        blacklist nouveau
        options nouveau modeset=0
        EOF 
 
3. Regenerate the kernel **initramfs** directory set:

  1. Modify the **initramfs** directory set:
  
     .. code-block:: console

        $ sudo dracut --force
	
  2. Reboot the server:

     .. code-block:: console

        $ sudo reboot

Installing the CUDA Driver
--------------------------------
This section describes how to install the CUDA driver.  
  
.. note:: The version of the driver installed on the customer's server must be equal or higher than the driver included in the Sqream release package. Contact a Sqream customer service representative to identify the correct version to install.

The **Installing the CUDA Driver** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Installing the CUDA Driver from the Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Installing the CUDA driver from the Repository is the recommended installation method.

.. warning:: For A100 GPU and other A series GPUs, you must install the **cuda 11.4.3 driver**. The version of the driver installed on the customer server must be equal to or higher than the one used to build the SQream package. For questions related to which driver to install, contact SQream Customer Support.

**To install the CUDA driver from the Repository:**

1. Install the CUDA dependencies for one of the following operating systems:

   * For RHEL:

     .. code-block:: console

        $ sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

   * For CentOS:

     .. code-block:: console

        $ sudo yum install epel-release
	
2. Install the CUDA dependencies from the **epel** repository:

   .. code-block:: console

      $ sudo yum install dkms libvdpau

   Installing the CUDA depedendencies from the **epel** repository is only required for installing **runfile**.

3. Download and install the required local repository:

   * **Intel - CUDA 10.1 for RHEL7**:

      .. code-block:: console

         $ wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.x86_64.rpm
         $ sudo yum localinstall cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.x86_64.rpm
		 
   * **Intel - 11.4.3 repository**:

      .. code-block:: console

         $ wget https://developer.download.nvidia.com/compute/cuda/11.4.3/local_installers/cuda-repo-rhel7-11-4-local-11.4.3_470.82.01-1.x86_64.rpm
         $ sudo yum localinstall cuda-repo-rhel7-11-4-local-11.4.3_470.82.01-1.x86_64.rpm

   * **IBM Power9 - CUDA 10.1 for RHEL7**:

      .. code-block:: console

         $ wget https://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.ppc64le.rpm
         $ sudo yum localinstall cuda-repo-rhel7-10-1-local-10.1.243-418.87.00-1.0-1.ppc64le.rpm
		 
.. warning:: For Power9 with V100 GPUs, you must install the **CUDA 10.1** driver.

4. Install the CUDA drivers:

   a. Clear the YUM cache:
  
      .. code-block:: console

         $ sudo yum clean all
	  
   b. Install the most current DKMS (Dynamic Kernel Module Support) NVIDIA driver:
  
      .. code-block:: console

         $ sudo yum -y install nvidia-driver-latest-dkms

5. Verify that the installation was successful:

   .. code-block:: console

      $ nvidia-smi
	  
.. note:: If you do not have access to internet, you can set up a local repository offline. 

You can prepare the CUDA driver offline from a server connected to the CUDA repo by running the following commands as a *root* user:
	  
6. Query all the packages installed in your system, and verify that cuda-repo has been installed:

   .. code-block:: console

      $ rpm -qa |grep cuda-repo

7. Navigate to the correct repository:

   .. code-block:: console

      $ cd /etc/yum.repos.d/

8. List in long format and print lines matching a pattern for the cuda file:

   .. code-block:: console

      $ ls -l |grep cuda

   The following is an example of the correct output:

   .. code-block:: console

      $ cuda-10-1-local.repo

9. Edit the **/etc/yum.repos.d/cuda-10-1-local.repo** file:

   .. code-block:: console

      $ vim /etc/yum.repos.d/cuda-10-1-local.repo

   The following is an example of the correct output:

   .. code-block:: console

      $ name=cuda-10-1-local
   
10. Clone the repository to a location where it can be copied from:

   .. code-block:: console

      $ reposync -g -l -m --repoid=cuda-10-1-local --download_path=/var/cuda-repo-10.1-local

11. Copy the repository to the installation server and create the repository:

   .. code-block:: console

      $ createrepo -g comps.xml /var/cuda-repo-10.1-local

12. Add a repo configuration file in **/etc/yum.repos.d/** by editing the **/etc/yum.repos.d/cuda-10.1-local.repo** repository:
 
   .. code-block:: console

      $ [cuda-10.1-local]
      $ name=cuda-10.1-local
      $ baseurl=file:///var/cuda-repo-10.1-local
      $ enabled=1
      $ gpgcheck=1
      $ gpgkey=file:///var/cuda-repo-10-1-local/7fa2af80.pub   
   
13. Install the CUDA drivers by installing the most current DKMS (Dynamic Kernel Module Support) NVIDIA driver as a root user logged in shell:
  
   .. code-block:: console

      $ sudo yum -y install nvidia-driver-latest-dkms
	  
Tuning Up NVIDIA Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section describes how to tune up NVIDIA performance.

.. note::  The procedures in this section are relevant to Intel only.	
	
.. contents:: 
   :local:
   :depth: 1

To Tune Up NVIDIA Performance when Driver Installed from the Repository
~~~~~~~~~~~~~~~~~~~~   
**To tune up NVIDIA performance when the driver was installed from the repository:**

1. Check the service status:

   .. code-block:: console

      $ sudo systemctl status nvidia-persistenced
		 
   If the service exists, it will be stopped be default.

2. Start the service:

   .. code-block:: console

      $ sudo systemctl start nvidia-persistenced
		 
3. Verify that no errors have occurred:

   .. code-block:: console

      $ sudo systemctl status nvidia-persistenced
		 
4. Enable the service to start up on boot:   

   .. code-block:: console

      $ sudo systemctl enable nvidia-persistenced
	  
5. For **V100/A100**, add the following lines:

   .. code-block:: console

      $ nvidia-persistenced
		 
   .. note::  The following are mandatory for IBM:
	  
              .. code-block:: console

                 $ sudo systemctl start nvidia-persistenced
                 $ sudo systemctl enable nvidia-persistenced
		 
6. Reboot the server and run the **NVIDIA System Management Interface (NVIDIA SMI)**:

   .. code-block:: console

      $ nvidia-smi
	  
.. note::  Setting up the NVIDIA POWER9 CUDA driver includes additional set-up requirements. The NVIDIA POWER9 CUDA driver will not function properly if the additional set-up requirements are not followed. See `POWER9 Setup <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#power9-setup>`__ for the additional set-up requirements.
		
To Tune Up NVIDIA Performance when Driver Installed from the Runfile
~~~~~~~~~~~~~~~~~~~~
**To tune up NVIDIA performance when the driver was installed from the runfile:**		

1. Change the permissions on the **rc.local** file to **executable**:

     .. code-block:: console

        $ sudo chmod +x /etc/rc.local	  
	  
2. Edit the **/etc/yum.repos.d/cuda-10-1-local.repo** file:

     .. code-block:: console

        $ sudo vim /etc/rc.local		 
		 
3. Add the following lines:

   * **For V100/A100**:

      .. code-block:: console

         $ nvidia-persistenced

   * **For IBM (mandatory)**:
	  
      .. code-block:: console

         $ sudo systemctl start nvidia-persistenced
         $ sudo systemctl enable nvidia-persistenced
		   
   * **For K80**:
	  
      .. code-block:: console

         $ nvidia-persistenced
         $ nvidia-smi -pm 1
         $ nvidia-smi -acp 0
         $ nvidia-smi --auto-boost-permission=0
         $ nvidia-smi --auto-boost-default=0

4. Reboot the server and run the **NVIDIA System Management Interface (NVIDIA SMI)**:

   .. code-block:: console

      $ nvidia-smi
	  
.. note::  Setting up the NVIDIA POWER9 CUDA driver includes additional set-up requirements. The NVIDIA POWER9 CUDA driver will not function properly if the additional set-up requirements are not followed. See `POWER9 Setup <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#power9-setup>`__ for the additional set-up requirements.

Disabling Automatic Bug Reporting Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**To disable automatic bug reporting tools:**

1. Run the following **abort** commands:

   .. code-block:: console

      $ for i in abrt-ccpp.service abrtd.service abrt-oops.service abrt-pstoreoops.service abrt-vmcore.service abrt-xorg.service ; do sudo systemctl disable $i; sudo systemctl stop $i; done

The server is ready for the SQream software installation.

2. Run the following checks:

   a. Check the OS release:
   
      .. code-block:: console
	  
         $ cat /etc/os-release
	  
   b. Verify that a SQream user exists and has the same ID on all cluster member services:
   
      .. code-block:: console
	  
         $ id sqream
		 
   c. Verify that the storage is mounted:
   
      .. code-block:: console
	  
         $ mount
		 
   d. Verify that the driver has been installed correctly:
   
      .. code-block:: console
	  
         $ nvidia-smi
		 
   e. Check the maximum value of the **fs.file**: 

      .. code-block:: console

         $ sysctl -n fs.file-max
		 	 
   f. Run the following command as a SQream user:
		 
      .. code-block:: console

         $ ulimit -c -u -n	
		 
    The following shows the desired output:

    .. code-block:: console

       $ core file size (blocks, -c) unlimited
       $ max user processes (-u) 1000000
       $ open files (-n) 1000000
	  
Enabling Core Dumps
===================================================
After installing the Nvidia CUDA driver, you can enable your core dumps. While SQream recommends enabling your core dumps, it is optional.

The **Enabling Core Dumps** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Checking the abrtd Status
---------------------------------------------------
**To check the abrtd status:**

1. Check if **abrtd** is running:

   .. code-block:: console

      $ sudo ps -ef |grep abrt

2. If **abrtd** is running, stop it:	  
	  
   .. code-block:: console

      $ sudo service abrtd stop
      $ sudo chkconfig abrt-ccpp off
      $ sudo chkconfig abrt-oops off
      $ sudo chkconfig abrt-vmcore off
      $ sudo chkconfig abrt-xorg off
      $ sudo chkconfig abrtd off

Setting the Limits
---------------------------------------------------
**To set the limits:**  
	  
1. Set the limits:

   .. code-block:: console

      $ ulimit -c
	  
2. If the output is **0**, add the following lines to the **limits.conf** file (/etc/security):	  
	  
   .. code-block:: console

      $ *          soft     core           unlimited
      $ *          hard     core           unlimited	  
	  
3. Log out and log in to apply the limit changes.	

Creating the Core Dumps Directory
---------------------------------------------------
**To set the core dumps directory:** 

1. Make the **/tmp/core_dumps** directory:

   .. code-block:: console

      $ mkdir /tmp/core_dumps

2. Set the ownership of the **/tmp/core_dumps** directory:

   .. code-block:: console

      $ sudo chown sqream.sqream /tmp/core_dumps
  
3. Grant read, write, and execute permissions to all users:

   .. code-block:: console

      $ sudo chmod -R 777 /tmp/core_dumps
	  
.. warning:: Because the core dump file may be the size of total RAM on the server, verify that you have sufficient disk space. In the example above, the core dump is configured to the */tmp/core_dumps* directory. You must replace path according to your own environment and disk space.	  

Setting the Output Directory of the /etc/sysctl.conf File 
-----------------------------------------------------------------
**To set the output directory of the /etc/sysctl.conf file:** 

1. Edit the **/etc/sysctl.conf** file:

   .. code-block:: console

      $ sudo vim /etc/sysctl.conf

2. Add the following to the bottom of the file:

   .. code-block:: console

      $ kernel.core_uses_pid = 1
      $ kernel.core_pattern = /<tmp/core_dumps>/core-%e-%s-%u-%g-%p-%t
      $ fs.suid_dumpable = 2

3. To apply the changes without rebooting the server, run the following:
	  
  .. code-block:: console

     $ sudo sysctl -p

4. Check that the core output directory points to the following:

  .. code-block:: console

     $ sudo cat /proc/sys/kernel/core_pattern
	  
  The following shows the correct generated output:
	  
  .. code-block:: console

     $ /tmp/core_dumps/core-%e-%s-%u-%g-%p-%t	  
	  
5. Verify that the core dumping works:	  
	  
  .. code-block:: console

     $ select abort_server();
	  
Verifying that the Core Dumps Work 
---------------------------------------------------	
You can verify that the core dumps work only after installing and running SQream. This causes the server to crash and a new core.xxx file to be included in the folder that is written in **/etc/sysctl.conf**

**To verify that the core dumps work:**

1. Stop and restart all SQream services.

    ::

2. Connect to SQream with ClientCmd and run the following command:

  .. code-block:: console

     $ select abort_server();
   
Troubleshooting Core Dumping 
---------------------------------------------------	
This section describes the troubleshooting procedure to be followed if all parameters have been configured correctly, but the cores have not been created.

**To troubleshoot core dumping:**

1. Reboot the server.

    ::

2. Verify that you have folder permissions:

   .. code-block:: console

      $ sudo chmod -R 777 /tmp/core_dumps   
   
3. Verify that the limits have been set correctly:

   .. code-block:: console

      $ ulimit -c

   If all parameters have been configured correctly, the correct output is:

   .. code-block:: console

      $ core file size          (blocks, -c) unlimited
      $ open files                      (-n) 1000000	  

4. If all parameters have been configured correctly, but running **ulimit -c** outputs **0**, run the following:

   .. code-block:: console

      $ sudo vim /etc/profile

5. Search for line and tag it with the **hash** symbol:

   .. code-block:: console

      $ ulimit -S -c 0 > /dev/null 2>&1

6. Log out and log in.

    ::

7. Run the ulimit -c command:

   .. code-block:: console

      $ ulimit -c command	  

8. If the line is not found in **/etc/profile** directory, do the following:	  
	  
   a. Run the following command:

      .. code-block:: console

         $ sudo vim /etc/init.d/functions

   b. Search for the following:
   
      .. code-block:: console

         $ ulimit -S -c ${DAEMON_COREFILE_LIMIT:-0} >/dev/null 2>&1

   c. If the line is found, tag it with the **hash** symbol and reboot the server.
