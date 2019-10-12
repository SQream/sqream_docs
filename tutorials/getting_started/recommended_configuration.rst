.. _recommended_configuration:

*********************************************
Recommended post-installation configuration
*********************************************

Once you've :ref:`installed SQream DB <installing_sqream_db>`, you can tune your system for better performance and stability.

This page provides recommendations for production deployments of SQream DB.

.. contents:: In this topic:
   :local:

Recommended BIOS settings
==========================

The below settings may have a variety of names, or may not exist on your system. It is safe to skip any and all of the configuration steps, but this may impact performance.

If any doubt arises, consult the documentation for your server for the correct way to apply the settings.

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Item
     - Setting
     - Rationale
   * - **Fan speed** or **Thermal Configuration**
     - **High**, **Maximum**, or **Increased cooling**
     - NVIDIA Tesla GPUs are passively cooled and require high amounts of airflow to function properly
   * - **System Profile**, **Power Profile**, or **Performance Profile**
     - **High Performance**
     - The Performance profile provides potentially increased performance by maximizing processor frequency, and the disabling certain power saving features such as C-states. Use this setting for environments that are not sensitive to power consumption.
   * - **Power Cap Policy** or **Dynamic power capping**
     - **Disabled**
     - Other power profiles (like "balanced") throttle CPU performance which diminish performance. This setting may appear together with the above (Power profile or Power regulator). This option allows for disabling System ROM Power Calibration during the boot process.
   * - **Intel Turbo Boost**
     - **Enable**
     - Intel Turbo Boost allows the processor to be overclocked under high load, which may improve performance in CPU-bound operations, but at the risk of computational jitter if the processor changes its turbo frequency. When that happens, processing stops for a small period of time, introducing uncertainty in application processing time. Turbo operation is a function of power consumption, processor temperature, and the number of active cores.
   * - **Hyperthreading** or **Logical processor**
     - **Enable**
     - Hyperthreading doubles the amount of logical processors, which may improve performance generally by ~5-10% in CPU-bound operations
   * - **Intel Virtualization Technology** and **VT-d**
     - **Disable**
     - Unless you are running VMs, disabling this setting boosts performance by up to 10%.
   * - **C-States** or **Minimum processor idle power core state**
     - **Disable** 
     - Processor C-States allows the server to reduce power when the system is idle. This causes slower 'cold-starts' when the system is transitioning from idle to load, and could reduce query performance by up to 15%.
   * - **Energy/Performance bias**
     - **Maximum performance**
     - Configures processor subsystems for high-performance/low-latency. Other power profiles (like "balanced" or "power savings") throttle CPU performance, which diminish performance. Use this setting for environments that are not sensitive to power consumption.
   * - **DIMM voltage**
     - **Optimized for Performance**
     - Setting a higher voltage for DIMMs can increases performance
   * - **Memory Operating Mode**
     - **Optimizer Mode**, **Disable Node Interleaving**, **Auto Memory Operating Voltage**
     - Memory Operating Mode is tuned for performance in Optimizer mode. Other modes may improve reliability but reduce performance. Enabling Node Interleaving means the memory is interleaved between memory nodes, which harms NUMA-aware applications like SQream DB, so leave disabled.
   * - **Memory power savings mode**
     - **Maximum performance**
     - This option configures several memory parameters to optimize the memory subsystems performance and is configured to Balanced by default.
   * - **ACPI SLIT**
     - **Enabled**
     - ACPI SLIT describes the relative access times between processors, memory subsystems, and I/O subsystems. Operating systems that support the SLIT can use this information to improve performance by allocating resources and workloads more efficiently.
   * - **QPI Snoop**
     - **Cluster on Die** or **Home Snoop**
     - This option allows for the configurations of different snoop modes that impact the QPI interconnect. Changing this option may improve performance in certain workloads. Home Snoop provides high memory bandwidth in an average NUMA environment (default setting). Cluster on Die may provide increased memory bandwidth in highly optimized NUMA workloads. Early Snoop may decrease memory latency but may also result in lower overall bandwidth as compared to other modes.

Use a dedicated SQream DB administration account
===================================================

Create a user for SQream DB, and optionally assign it to the ``wheel`` group for ``sudo`` access.

.. code-block:: console

   $ useradd -m -U sqream
   $ passwd sqream 
   $ usermod -aG wheel sqream 

.. warning:: SQream DB should not run as ``root`` or ``sudo``.

Configure the OS locale and timezone
=====================================

#. Set your OS to use UTF-8, which SQream DB uses for non-English language support.
   
   .. code-block:: console
   
      $ sudo localectl set-locale LANG=en_US.UTF-8

#. Set the correct timezone for your server.
   Refer to `the list of available timezones <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_ to find a timezone that matches your location.
   
   .. code-block:: console
   
      $ sudo timedatectl set-timezone America/New_York


Configure NTP for clock synchronization
=========================================

SQream DB clusters rely on clock synchronization to function correctly.


   .. code-block:: console
   
      $ sudo yum install -y ntp ntpdate
      $ sudo systemctl enable ntpd
      $ sudo systemctl start ntpd

If your organization has an NTP server, configure it by adding records to ``/etc/ntpd.conf``, reloading the service, and checking that synchronization is enabled:

   .. code-block:: console
   
      $ echo -e "\nserver <your NTP server address>\n" | sudo tee -a /etc/ntp.conf
      $ sudo systemctl restart ntpd
      $ sudo timedatectl
               Local time: Sat 2019-10-12 17:26:13 EDT
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



Install recommended utilities
===============================

The following packages contain tools that are recommended but not required for using SQream DB.

   .. code-block:: console
   
      $ sudo yum install -y bash-completion.noarch vim-enhanced.x86_64 vim-common.x86_64 net-tools iotop htop psmisc screen xfsprogs wget yum-utils deltarpm dos2unix tuned  pciutils


Tuning OS parameters for performance and stability
===================================================

SQream DB requires certain OS parameters to be set on all hosts in your cluster.

These settings affect:

* Shared memory - Most OS installations may try to limit high throughput software like SQream DB.
* Network - On high throughput operations like ingest, optimizing network connection parameters can boost performance
* User limits - SQream DB may open a large amount of files. The default OS settings may cause some statements to fail if the system runs out of file descriptors.

#. Tell the OS to set the high throughput profile for network and memory access

   #. Use ``tuned-adm`` profiles
      
      .. code-block:: console
         
            $ sudo tuned-adm profile throughput-performance
   
   #. Set ``sysctl`` overrides to tune system performance (for systems with over 64GB of RAM)
      
      .. code-block:: console
         
            $ sudo tee /etc/sysctl.d/sqreamdb.conf > /dev/null <<EOT
            kernel.shmmax = 500000000
            kernel.shmmni = 4096
            kernel.shmall = 4000000000
            kernel.sysrq = 1
            kernel.core_uses_pid = 1
            kernel.core_pattern = /tmp/core_dumps/%f-core-%e-%s-%u-%g-%p-%t
            kernel.msgmnb = 65536
            kernel.msgmax = 65536
            kernel.msgmni = 2048
            kernel.pid_max = 524288
            vm.max_map_count = 2042292
            vm.dirty_background_ratio = 5
            vm.dirty_ratio = 3
            vm.swappiness = 1
            vm.vfs_cache_pressure = 200
            vm.zone_reclaim_mode = 0
            net.ipv4.tcp_syncookies = 1
            net.ipv4.conf.default.accept_source_route = 0
            net.ipv4.tcp_tw_recycle = 1
            net.ipv4.tcp_max_syn_backlog = 4096
            net.ipv4.conf.all.arp_filter = 1
            net.core.netdev_max_backlog = 10000
            net.core.rmem_max = 2097152
            net.core.wmem_max = 2097152
            fs.suid_dumpable = 2
            fs.file-max = 2097152
            EOT


#. Increase the limit of open files and processes 

   .. code-block:: console
      
         $ sudo tee -a /etc/security/limits.conf > /dev/null <<EOT
         * soft nproc 524288
         * hard nproc 524288
         * soft nofile 524288
         * hard nofile 524288
         * soft core unlimited
         * hard core unlimited
         EOT

#. Verify mount options for drives

   SQream recommends XFS for local data storage.
   The recommended XFS mount options are:
   
   ``rw,nodev,noatime,nobarrier,inode64``

.. note:: Reboot your system for the above settings to take effect.

Disable SELinux
=================

SELinux may interfere with NVIDIA driver installation and some SQream DB operations. Unless absolutely necessary, we recommend disabling it.

#. Check if SELinux is enabled

   .. code-block:: console
      
      $ sudo sestatus
      SELinux status:                 disabled

#. You can disable SELinux by changing the value of ``SELINUX`` parameter to ``disabled`` in ``/etc/selinux/config`` and rebooting.

Secure the server with a firewall
===================================

Opening up ports in the firewall
---------------------------------

The example below shows how to open up all ports required by SQream DB and related management interfaces. The example also takes into account up to 4 instances on the host.

   .. code-block:: console
      
      $ sudo systemctl start firewalld
      $ sudo systemctl enable firewalld
      $ for p in {2812,3000,3001,3105,3108,5000-5003,5100-5103}; do sudo firewall-cmd --zone=public --permanent --add-port=${p}/tcp; done
      $ sudo firewalld --reloadi


Disabling the built in firewall
---------------------------------

If not required, you can disable the server's firewall. This will reduce connectivity issues, but should only be done inside your internal network.

   .. code-block:: console
      
      $ sudo systemctl disable firewalld
      $ sudo systemctl stop firewalld


