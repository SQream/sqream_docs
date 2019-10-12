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

Use a dedicated username for SQream DB
========================================

Create a user for SQream DB, and optionally assign it to the ``wheel`` group for ``sudo`` access.

.. code-block:: console

   $ useradd -m -U sqream
   $ passwd sqream 
   $ usermod -aG wheel sqream 

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
   
      $ sudo yum install -y ntp
      $ sudo systemctl enable ntpd
      $ sudo systemctl start ntpd

If your organization has an NTP server, configure it by adding records to ``/etc/ntpd.conf``, and reloading the service:

   .. code-block:: console
   
      $ echo -e "\nserver <your NTP server address>\n" | sudo tee /etc/ntpd.conf
      $ sudo service ntp reload
      $ sudo ntpq -p

Install recommended utilities
===============================

The following packages contain tools that are recommended but not required for using SQream DB.

   .. code-block:: console
   
      $ sudo yum install -y bash-completion.noarch vim-enhanced.x86_64 vim-common.x86_64 net-tools iotop htop psmisc screen xfsprogs wget yum-utils deltarpm dos2unix tuned  pciutils
      

Tuning OS parameters for performance and stability
===================================================


Secure the server with a firewall
===================================

