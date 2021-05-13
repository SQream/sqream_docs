.. _running_sqream_in_a_docker_container:


***********************
Running SQream in a Docker Container
***********************

This document describes how to prepare your machine's environment for installing and running SQream in a Docker container.

Setting Up a Host
====================================

Operating System Requirements
------------------------------------

Setting up a host requires a clean operating system that has been tested and verified on one of the following versions of Linux:

  * x86 CentOS 7.3
  * IBM RHEL 7.5

Creating a Local User
----------------

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

Setting Up a Local Language
----------------

**To set up a local language:**

1. Set the local language:

    .. code-block:: console
     
       $ sudo localectl set-locale LANG=en_US.UTF-8

2. Set the time stamp (time and date) of the locale:

<!-- Is "location" better than "locale?" -->

    .. code-block:: console

       $ sudo timedatectl set-timezone Asia/Jerusalem

You can run the ``timedatectl list-timezones`` command to see your timezone.

Adding the EPEL Repository
----------------

**To add the EPEL repository:**

1. As a root user, upgrade the **epel-release-latest-7.noarch.rpm** repository:

    .. code-block:: console

       $ sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

<!-- Is it being added or upgraded? -->

Installing the Required Packages
----------------

You can install the required NTP packages by running the following command:

 .. code-block:: console

    $ sudo yum install ntp  pciutils python36 kernel-devel-$(uname -r) kernel-headers-$(uname -r) 	gcc

Installing the Recommended Tools
----------------

SQream recommends installing the following recommended tools:

<!-- What value does installing these tools offer to the user? -->

 .. code-block:: console

    $ sudo yum install bash-completion.noarch  vim-enhanced.x86_64 vim-common.x86_64 net-tools iotop htop psmisc screen xfsprogs wget yum-utils deltarpm dos2unix

Updating to the Current Version of the Operating System
----------------

SQream recommends updating to the current version of the operating system. This is not recommended if the nvidia driver has **not been installed.**

<!-- What happens if the user does not update to the current version? What happens if the user updates to the current version without installing the nvidia driver? -->

You can verify if the nvidia driver has been installed by running the following command if the command result in GPU information doesn't run the update:

 .. code-block:: console

    $ sudo yum update

<!-- Clarification required: ...if the command result in GPU information doesn't run the update. -->

Configuring the NTP Package
----------------

**To configure the NTP package:**

1. Add your local servers to the NTP configuration.

 <!-- If you have local servers? See Confluence doc. --> 

 <!-- NTP configuration file? -->

 <!-- What does this mean? "[adding how to configure local NTP servers]"-->

2. Configure the **ntpd** service to begin running when your machine is started:

 .. code-block:: console

    $ sudo systemctl enable ntpd
    $ sudo systemctl start ntpd

 <!-- What does the following command do?-->
    
 .. code-block:: console

    $ sudo ntpq -p

Configuring the Performance Profile
----------------

**To configure the performance profile:**

1. Switch the active profile:

<!-- Switch it to which one? The source file didn't specify which one.-->

 .. code-block:: console

    $ sudo tuned-adm profile throughput-performance 

2. Change the multi-user's default run level:

<!-- Switch it to what?-->

 .. code-block:: console

    $ sudo systemctl set-default multi-user.target

Configuring Your Security Limits
----------------

Configuring your security limits refers to configuring the number of open files, processes, etc.

<!-- Does open = active/running? -->

1. Run the **bash** shell as a super-user: 

 .. code-block:: console

    $ sudo bash

2. Run the following command:

.. code-block:: console

    $ echo -e "sqream soft nproc 500000\nsqream hard nproc 500000\nsqream soft nofile 500000\nsqream hard nofile 500000\nsqream soft core unlimited\nsqream hard core unlimited" >> /etc/security/limits.conf

<!-- Verify function of the above command.-->

3. Run the following command:

.. code-block:: console

    $ echo -e "vm.dirty_background_ratio = 5 \n vm.dirty_ratio = 10 \n vm.swappiness = 10 \n vm.zone_reclaim_mode = 0 \n vm.vfs_cache_pressure = 200 \n"  >> /etc/sysctl.conf

<!-- Verify function of the above command. Notice the ">> /etc/sysctl.conf."-->

Disabling Automatic Bug Reporting Tools
----------------
The following automatic bug reporting tools must be disabled by running the following command:

.. code-block:: console

    $ for i in abrt-ccpp.service abrtd.service abrt-oops.service abrt-pstoreoops.service abrt-vmcore.service abrt-xorg.service ; do sudo systemctl disable $i; sudo systemctl stop $i; done

<!-- The command text starts with "for i." Should this be part of the command text? -->

Preparing the Nvidia CUDA Drive for Installation
----------------
**To prepare the Nvidia CUDA drive for installation:**

1. Reboot all servers.
2. Verify that the Tesla NVIDIA card has been installed and is detected by the system:

.. code-block:: console

    $ lspci | grep -i nvidia

The correct output is a list of Nvidia graphic cards. If you do not receive this output, verify that an NVIDIA GPU card has been installed.

<!-- Try to get this output. -->

3. Verify that the open-source upstream Nvidia driver is running:

.. code-block:: console

    $ lsmod | grep nouveau

No output should be generated.

4. If you receive any output, do the following:

   1. Disable the open-source upstream Nvidia driver:

   .. code-block:: console

       $ sudo bash
       $ echo "blacklist nouveau" > /etc/modprobe.d/blacklist-nouveau.conf
       $ echo "options nouveau modeset=0"  >> /etc/modprobe.d/blacklist-nouveau.conf
       $ dracut --force
       $ modprobe --showconfig | grep nouveau
    
      <!-- The source content said to disable "it," which I assume refers to the Nvidia driver. Confirm. -->

   2. Reboot the server and verify that the Nouveau model has not been loaded:

   .. code-block:: console

       $ lsmod | grep nouveau
   



Installing the Nvidia CUDA Driver

**To install the Nvidia CUDA driver:**

1. Check if the Nvidia CUDA driver has already been installed:

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

2. Verify that the installed CUDA version shown in the output above is ``10.1``

3. Do one of the following: <!-- Create cross-reference in GitHub in Step 1 below. -->
   
   1. If CUDA version 10.1 has already been installed, skip to Docktime Runtime (Community Edition).

   2. If CUDA version 10.1 has not been installed yet, continue with Step 4 below.

4. Do one of the following:

    * Install :ref:`CUDA Driver version 10.1 for x86_64 <CUDA_10.1_x8664>`.
    * Install :ref:`CUDA driver version 10.1 for IBM Power9 <CUDA_10.1_IBMPower9>`.

.. _CUDA_10.1_x8664:

Installing the CUDA Driver Version 10.1 for x86_64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the CUDA driver version 10.1 for x86_64:**

1. Make the following target platform selections:

   * **Operating system**: Linux
   * **Architecture**: x86_64
   * **Distribution**: CentOS
   * **Version**: 7
   * **Installer type**: the relevant installer type

<!-- Is Step 4 actually to install CUDA version 10.1, or is one of the steps required for installing it? -->

<!-- The source document included a link to the page from where I got these steps. Is downloading installer for Linux CentOS 7 86_64 one of the required steps? -->

For installer type, SQream recommends selecting **runfile (local)**. The available selections shows only the supported platforms.

<!-- Do the users need to make exactly the selections above, or do they need to make the selections relevant to them? -->

<!-- Do the users need to follow all of the instructions on the linked page, or just **Select Target Platform**? I documented the entire page, and will delete it if needed. -->

<!-- Note to self: do I need to include the image? -->

2. Download the base installer for Linux CentOS 7 x86_64.
3. Install the base installer for Linux CentOS 7 x86_64:

   1. Run the following command:

   .. code-block:: console

       $ sudo sh cuda_10.1.105_418.39_linux.run

   2. Follow the command line prompts.

4. Enable the Nvidia service to start at boot and start it:

   .. code-block:: console

       $ sudo systemctl enable nvidia-persistenced.service && sudo systemctl start nvidia-persistenced.service

<!-- Confirm the above. -->

5. Create a symbolic link from the **/etc/systemd/system/multi-user.target.wants/nvidia-persistenced.service** file to the **/usr/lib/systemd/system/nvidia-persistenced.service** file.

<!-- The source document said "created symlink" instead of "create symlink." Does this mean that it was a result of Step 7, or that it is actually Step 8 as I documented above? -->

6. Reboot the server.
7. Verify that the Nvidia driver has been installed and shows all available GPU's:

<!-- NVidia driver 10.1? -->

   .. code-block:: console

       $ nvidia-smi

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To install the CUDA driver version 10.1 for IBM Power9:**

1. Make the following target platform selections:

   * **Operating system**: Linux
   * **Architecture**: ppc64le
   * **Distribution**: RHEL
   * **Version**: 7
   * **Installer type**: the relevant installer type

<!-- See all comments left in x86_64 -->

For installer type, SQream recommends selecting **runfile (local)**. The available selections shows only the supported platforms.

Disabling the udev Rule

The ``udev`` rule must be disabled.

**To disable the ``udev`` rule:**

1. Copy the file to the **/etc/udev/rules.d** directory.
2. Comment out, remove, or change the hot-pluggable memory rule located in file copied to the **/etc/udev/rules.d** directory. This prevents it from affecting the Power9 Nvidia systems.
3. Do one of the following:
    
   1. Run the following on RHEL version 7.5 or earlier:

   .. code-block:: console

       $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d
       $ sudo sed -i '/SUBSYSTEM=="memory", ACTION=="add"/d' /etc/udev/rules.d/40-redhat.rules 

   2. Run the following on RHEL version 7.6 or later:  

   .. code-block:: console

       $ sudo cp /lib/udev/rules.d/40-redhat.rules /etc/udev/rules.d 
       $ sudo sed -i 's/SUBSYSTEM!="memory", ACTION!="add", GOTO="memory_hotplug_end"/SUBSYSTEM=="*", GOTO="memory_hotplug_end"/' /etc/udev/rules.d/40-redhat.rules

4. Enable the **nvidia-persisted.service** file:

   .. code-block:: console

       $ sudo systemctl enable nvidia-persistenced.service 

5. Create a symbolic link from the **/etc/systemd/system/multi-user.target.wants/nvidia-persistenced.service** file to the **/usr/lib/systemd/system/nvidia-persistenced.service** file.

6. Reboot your system to initialize the above modifications.

7. Verify that the Nvidia driver and the **nvidia-persistenced.service** files are running:

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
8. Verify that the **nvidia-persistenced** service is running:

   .. code-block:: console

       $ ystemctl status nvidia-persistenced

The following is the correct output:

   .. code-block:: console

       root@gpudb ~]systemctl status nvidia-persistenced
       ● nvidia-persistenced.service - NVIDIA Persistence Daemon
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
This section describes how to install the Docker engine on the following processors:

* :ref:`x86_64 <dockerx8664>`
* :ref:`IBM Power9 (PPC64le) <docker_ibmpower9>`

.. _dockerx8664:

Installing the Docker Engine Using an x86_64 Processor on CentOS
The x86_64 processor supports installing the **Docker Community Edition (CE)** versions 18.03 and higher.

For more information on installing the Docker Engine CE on an x86_64 processor, see ref:`Install Docker Engine on CentOS
 <https://docs.docker.com/engine/install/centos/>`.

.. _docker_ibmpower9:

Installing the Docker Engine Using an x86_64 Processor on Ubuntu
The x86_64 processor supports installing the **Docker Community Edition (CE)** versions 18.03 and higher.

For more information on installing the Docker Engine CE on an x86_64 processor, see ref:`Install Docker Engine on Ubuntu
 <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`.




Installing the Docker Engine on an IBM Power9 Processor
The x86_64 processor only supports installing the **Docker Community Edition (CE)** version 18.03.





Nvidia Docker2 ToolKit
=======================

Preparing the Environment
=======================

Getting the SQream package
=======================

Sqream-install
=======================

Sqream-console
=======================

Console Advance Commands
=======================

Check the status of the sqream services
=======================

SQream upgrade

