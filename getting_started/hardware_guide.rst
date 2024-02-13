.. _hardware_guide:

**************
Hardware Guide
**************

The **Hardware Guide** describes the SQreamDB reference architecture, emphasizing the benefits to the technical audience, and provides guidance for end-users on selecting the right configuration for a SQreamDB installation.

.. rubric:: Need help?

This page is intended as a "reference" to suggested hardware. However, different workloads require different solution sizes. SQreamDB's experienced customer support has the experience to advise on these matters to ensure the best experience.

Visit `SQreamDB's support portal <https://sqream.atlassian.net/servicedesk/customer/portals>`_ for additional support.

.. contents:: 
   :local:
   :depth: 2


Cluster Architectures
=====================

SQreamDB recommends rackmount servers by server manufacturers Dell, Lenovo, HP, Cisco, Supermicro, IBM, and others.

A typical SQreamDB cluster includes one or more nodes, consisting of:

* Two-socket enterprise processors, such as Intel® Xeon® Gold processors or the IBM® POWER9 processors, providing the high performance required for compute-bound database workloads.

   ::

* NVIDIA Tesla GPU accelerators, with up to 5,120 CUDA and Tensor cores, running on PCIe or fast NVLINK busses, delivering high core count, and high-throughput performance on massive datasets.

   ::

* High density chassis design, offering between 2 and 4 GPUs in a 1U, 2U, or 3U package, for best-in-class performance per cm\ :sup:`2`.

Single-Node Cluster
---------------------------

A single-node SQreamDB cluster can handle between 1 and 8 concurrent users, with up to 1PB of data storage (when connected via NAS).

An average single-node cluster can be a rackmount server or workstation, containing the following components:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Component
     - Type
   * - Server
     - Dell R750, Dell R940xa, HP ProLiant DL380 Gen10 or similar (Intel only)
   * - Processors
     - 2x Intel Xeon Gold 6348 (28C/56HT) 3.5GHz or similar
   * - RAM
     - 1.5 TB
   * - Onboard storage
     - 
         * 2x 960GB SSD 2.5in hot plug for OS, RAID1
         * 2x 2TB SSD or NVMe, for temporary spooling, RAID0
         * 10x 3.84TB SSD 2.5in Hot plug for storage, RAID6

   * - GPU
     - 
        NVIDIA 2x A100, H100, or L40S
		
   * - Operating System
     - Red Hat Enterprise Linux v7.9 or CentOS v7.9 or Amazon Linux

.. note:: If you are using internal storage, your volumes must be formatted as xfs.

In this system configuration, SQreamDB can store about 100TB of raw data (assuming an average compression ratio and ~30TB of usable raw storage).

If a NAS is used, the 10x SSD drives can be omitted, but SQreamDB recommends 2TB of local spool space on SSD or NVMe drives.

Multi-Node Cluster
---------------------------

Multi-node clusters can handle any number of concurrent users. A typical SQreamDB cluster relies on a minimum of two GPU-enabled servers and shared storage connected over a network fabric, such as InfiniBand EDR, 40GbE, or 100GbE.

The **Multi-Node Cluster Examples** section describes the following specifications: 

.. contents:: 
   :local:
   :depth: 1
   
Hardware Specifications
~~~~~~~~~~~~~~~~~~~~~~~

The following table shows SQreamDB's recommended hardware specifications:

.. list-table::
   :widths: 15 65
   :header-rows: 1
   
   * - Component
     - Type
   * - Server
     - Dell R750, Dell R940xa, HP ProLiant DL380 Gen10 or similar (Intel only)
   * - Processors
     - 2x Intel Xeon Gold 6348 (28C/56HT) 3.5GHz or similar
   * - RAM
     - 2 TB
   * - Onboard storage
     -   
         * 2x 960GB SSD 2.5in hot plug for OS, RAID1
         * 2x 2TB SSD or NVMe, for temporary spooling, RAID0
   * - External Storage
     -   
         * Mellanox Connectx5/6 100G NVIDIA Network Card (if applicable) or other high-speed network card minimum 40G compatible with customer’s infrastructure
         * 50 TB (NAS connected over GPFS, Lustre, Weka, or VAST) GPFS recommended
   * - GPU
     - NVIDIA 2x A100, H100, or L40S
   * - Operating System
     - Red Hat Enterprise Linux v7.9 or CentOS v7.9 or Amazon Linux
	 
Metadata Specifications
~~~~~~~~~~~~~~~~~~~~~~~
	 
The following table shows SQreamDB's recommended metadata server specifications:

.. list-table::
   :widths: 15 90
   :header-rows: 1
   
   * - Component
     - Type
   * - Processors
     - 2x Intel Xeon Gold 6342 2.8 Ghz 24C processors or similar
   * - RAM
     - 512GB DDR4 RAM 8x64GB RDIMM or similar
   * - Onboard storage
     - 2x 960 GB MVMe SSD drives in RAID 1 or similar
   * - Network Card (Storage)
     - 2x Mellanox ConnectX-6 Single Port HDR VPI InfiniBand Adapter cards at 100GbE or similar.
   * - Network Card (Client)
     - 2x 1 GbE cards or similar
   * - Operating System
     - Red Hat Enterprise Linux v7.9 or CentOS v7.9 or Amazon Linux

.. note:: With a NAS connected over GPFS, Lustre, Weka, or VAST, each SQreamDB worker can read data at 5GB/s or more.

SQreamDB Studio Server
------------------------------

The following table shows SQreamDB's recommended Studio server specifications:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Component
     - Type
   * - Server
     - Physical or virtual machine
   * - Processor
     - 1x Intel Core i7
   * - RAM
     - 16 GB
   * - Onboard storage
     - 50 GB SSD 2.5in Hot-plug for OS, RAID1
   * - Operating System
     - Red Hat Enterprise Linux v7.9 or CentOS v7.9

Cluster Design Considerations
=============================

This section describes the following cluster design considerations:

* In a SQreamDB installation, the storage and computing are logically separated. While they may reside on the same machine in a standalone installation, they may also reside on different hosts, providing additional flexibility and scalability.

 ::

* SQreamDB uses all resources in a machine, including CPU, RAM, and GPU to deliver the best performance. At least 256GB of RAM per physical GPU is recommended.

 ::

* Local disk space is required for good temporary spooling performance, particularly when performing intensive operations exceeding the available RAM, such as sorting. SQreamDB recommends an SSD or NVMe drive in RAID0 configuration with about twice the RAM size available for temporary storage. This can be shared with the operating system drive if necessary.

 ::

* When using NAS devices, SQreamDB recommends approximately 5GB/s of burst throughput from storage per GPU.

Balancing Cost and Performance
------------------------------

Prior to designing and deploying a SQreamDB cluster, a number of important factors must be considered. 

The **Balancing Cost and Performance** section provides a breakdown of deployment details to ensure that this installation exceeds or meets the stated requirements. The rationale provided includes the necessary information for modifying configurations to suit the customer use-case scenario, as shown in the following table:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Component
     - Value
   * - Compute - CPU
     - Balance price and performance
   * - Compute – GPU
     - Balance price with performance and concurrency
   * - Memory – GPU RAM
     - Balance price with concurrency and performance.
   * - Memory - RAM
     - Balance price and performance
   * - Operating System
     - Availability, reliability, and familiarity
   * - Storage
     - Balance price with capacity and performance
   * - Network
     - Balance price and performance

CPU Compute
-----------

SQreamDB relies on multi-core Intel Gold Xeon processors or IBM POWER9 processors and recommends a dual-socket machine populated with CPUs with 18C/36HT or better. While a higher core count may not necessarily affect query performance, more cores will enable higher concurrency and better load performance.

GPU Compute and RAM
-------------------

The NVIDIA Tesla range of high-throughput GPU accelerators provides the best performance for enterprise environments. Most cards have ECC memory, which is crucial for delivering correct results every time. SQreamDB recommends the  NVIDIA Tesla A100 80GB GPU for the best performance and highest concurrent user support.

GPU RAM, sometimes called GRAM or VRAM, is used for processing queries. It is possible to select GPUs with less RAM. However, the smaller GPU RAM results in reduced concurrency, as the GPU RAM is used extensively in operations like JOINs, ORDER BY, GROUP BY, and all SQL transforms.

RAM
---

SQreamDB requires using **Error-Correcting Code memory (ECC)**, standard on most enterprise servers. Large amounts of memory are required for improved performance for heavy external operations, such as sorting and joining.

SQreamDB recommends at least 256GB of RAM per GPU on your machine. 

Operating System
----------------

SQreamDB can run on the following 64-bit Linux operating systems:

   * Red Hat Enterprise Linux (RHEL) v7.9
   * CentOS v7.9
   * Amazon Linux 2018.03


Storage
-------

For clustered scale-out installations, SQreamDB relies on NAS storage. For stand-alone installations, SQreamDB relies on redundant disk configurations, such as RAID 5, 6, or 10. These RAID configurations replicate blocks of data between disks to avoid data loss or system unavailability. 

SQreamDB recommends using enterprise-grade SAS SSD or NVMe drives. For a 32-user configuration, the number of GPUs should roughly match the number of users. SQreamDB recommends 1 Tesla A100 / H100 or L40S GPU per 2 users, for full, uninterrupted dedicated access.

