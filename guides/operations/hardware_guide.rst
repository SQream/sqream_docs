.. _hardware_guide:

***********************
Hardware Guide
***********************

This guide describes the SQream DB reference architecture, emphasizing the benefits to the technical audience, and provides guidance for end-users on selecting the right configuration for a SQream DB installation.


.. rubric:: Need help?

This page is intended as a "reference" to suggested hardware. However, different workloads require different solution sizes. SQream's experienced customer support has the experience to advise on these matters to ensure the best experience.

Visit `SQream's support portal <https://support.sqream.com>`_ for additional support.

A SQream DB cluster
============================

SQream recommends rackmount servers by server manufacturers Dell, Lenovo, HP, Cisco, Supermicro, IBM, and others.

A typical SQream DB cluster includes one or more nodes, consisting of

* Two-socket enterprise processors, like the Intel® Xeon® Gold processor family or an IBM® POWER9 processors, providing the high performance required for compute-bound database workloads. 

* NVIDIA Tesla GPU accelerators, with up to 5,120 CUDA and Tensor cores, running on PCIe or fast NVLINK busses, delivering high core count, and high-throughput performance on massive datasets

* High density chassis design, offering between 2 and 4 GPUs in a 1U, 2U, or 3U package, for best-in-class performance per cm\ :sup:`2`.

Example for a single-node cluster
-----------------------------------

A single-node SQream DB cluster can handle between 1 and 8 concurrent users, with up to 1PB of data storage (when connected via NAS).

An average single-node cluster can be a rackmount server or workstation, containing the following components:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Component
     - Type
   * - Server
     - Rackmount or workstation, like the Dell T640, Dell R740, Dell R940xa, HP ProLiant DL380 Gen10
   * - Processor
     - 2x Intel Xeon Gold 6240 (18C/36HT) 2.6GHz
   * - RAM
     - 384 GB LRDIMM 2666MT/s, ECC registered
   * - Onboard storage
     - 
         * 2x 960GB SSD 2.5in Hot-plug for OS, RAID1
         * 14x 3.84TB SSD 2.5in Hot-plug for storage, RAID5
   * - Networking
     - Intel X710 DP 10Gb DA/SFP+
   * - GPU
     - 2x or 4x NVIDIA Tesla T4 or P100

In this system configuration, SQream DB can store about 200TB of raw data (assuming average compression ratio and ~50TB of usable raw storage).

If a NAS is used, the 14x SSD drives can be omitted, but SQream recommends 2TB of local spool space on SSD or NVMe drives.

Example for multi-node clusters
-----------------------------------

Multi-node clusters can handle any number of concurrent users.

A typical SQream DB cluster relies on a shared storage connected over a network fabric like InfiniBand EDR, 40GbE, or 100GbE

An example of a cluster node providing the best performance:

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Component
     - Type
   * - Server
     - High-density GPU-capable rackmount server, like Dell C4140, IBM AC922, Lenovo SR650.
   * - Processor
     - 2x Intel Platinum 8180M (28C/56HT) 3.8GHz or 2x IBM POWER9
   * - RAM
     - 1024 GB RDIMM 2933T/s, ECC registered
   * - Onboard storage
     -   
         * 2x 960GB SSD 2.5in, for OS, RAID1
         * 2x 2TB SSD or NVMe, for temporary spooling, RAID1
   * - Networking
     - 
         Intel X710 DP 10Gb DA/SFP+ for BI fabric
      
         Mellanox ConnectX-4, EDR for storage fabric
   * - GPU
     - 4x NVIDIA Tesla V100 32GB

.. note:: With a NAS connected over GPFS, Lustre, or NFS - each SQream DB worker can read data at up to 5GB/s.


Considerations in cluster design
====================================

* In a SQream DB installation, the storage and compute are logically separated. While they may reside on the same machine in a standalone installation, they may also reside on different hosts, providing additional flexibility and scalability.

* SQream DB uses all resources in a machine, including CPU, RAM, and GPU to deliver the best performance. 256GB of RAM per physical GPU is recommended, but not required.

* Local disk space is required for good performance temporary spooling - particularly when performing intensive larger-than-RAM operations like sorting. SQream recommends an SSD or NVMe drive, in mirrored RAID 1 configuration, with about 2x the RAM size available for temporary storage. This can be shared with the operating system drive if necessary.

* When using SAN or NAS devices, SQream recommends around 5GB/s of burst throughput from storage, per GPU.

Balancing cost and performance
--------------------------------

Prior to designing and deploying a SQream DB cluster, there are a number of important factors to consider. 

This section provides a breakdown of deployment details intended to help ensure that this installation exceeds or meets the stated requirements. The rationale provided includes the necessary information for modifying configurations to suit the customer use-case scenario.

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

CPU compute
-------------

SQream DB relies on multi-core Intel® Xeon® processors or IBM® POWER9 processors.

SQream recommends a dual-socket machine populated with CPUs with 18C/36HT or better.

While a higher core count may not necessarily affect query performance, more cores will enable higher concurrency and better load performance.

GPU compute and RAM
-------------------------

The NVIDIA Tesla range of high-throughput GPU accelerators provides the best performance for enterprise environments. Most cards have ECC memory, which is crucial for delivering correct results every time.

SQream recommends the NVIDIA Tesla V100 32GB GPU for best performance and highest concurrent user support.

GPU RAM, sometimes called GRAM or VRAM is used for processing queries. It is possible to select GPUs with less RAM, like the NVIDIA Tesla V100 16GB or P100 16GB. However, the smaller GPU RAM available will result in reduced concurrency, as the GPU RAM is used extensively in operations like JOINs, ORDER BY, GROUP BY, and all SQL transforms.

RAM
--------

Use of error-correcting code memory (ECC) is a practical requirement for SQream DB and is standard on most enterprise server. SQream DB benefits from having large amounts of memory for improved performance on large 'external' operations like sorting and joining.

Although SQream DB can function with less, we recommend a key of 256GB of RAM per GPU in the machine. 

Operating system
---------------------

SQream DB can run on 64-bit Linux operating systems:

   * Red Hat Enterprise Linux (RHEL) v7
   * CentOS v7
   * Amazon Linux 2018.03
   * Ubuntu v16.04 LTS, v18.04 LTS
   * Other Linux distributions may be supported via nvidia-docker

Storage
-----------

For clustered scale-out installations, SQream DB relies on NAS/SAN storage. These devices have extremely high reliability and durability, with five 9s of up-time.

For stand-alone installations, SQream DB relies on redundant disk configurations, like RAID 5/6/10/50. These RAID configurations ensure that blocks of data are replicated between disks, so that failure of a number of disks will not result in data loss or availability of the system. 

Because storage reliability is important, SQream recommends enterprise-grade SAS SSD drives. However, as with other components – there is a tradeoff for cost/performance. When performance and reliability are important, SQream recommends SAS SSD or NVMe drives. 

SQream DB functions well with more cost-effective SATA drives and even large spinning-disk arrays.


Example cluster supporting 32 concurrent active users
==========================================================

For a 32-user configuration, the number of GPUs should roughly match the number of users. SQream DB recommends 1 Tesla V100 GPU per 2 users, for full, uninterrupted dedicated access.

Each of these servers can support about 8 users on average. The actual number of concurrent users can be higher, depending on the workload.

A SQream DB cluster for 32 users consists of the following components:

#. 
   4 high-density GPU-enabled servers, like the Dell C4140 (Configuration C) with 4x NVIDIA Tesla V100 32GB PCIe GPUs.
   
   Each server is equipped with dual Intel ® Xeon ® Gold 6240 CPU, and 1,024GB of RAM.
   
#. 
   NAS/SAN storage, capable of delivering 1 GB/s per GPU.
   
   For the system above, with 4x4 NVIDIA Tesla V100 GPUs, this results in 16GB/s, over multiple bonded, 40GigE or InfiniBand links via a fabric switch.

#. Top-of-Rack (ToR) 10GigE ethernet switch for the BI fabric

#. 40GigE or InfiniBand switches for the storage fabric

#.	At least 1 PDU

.. figure:: /_static/images/reference_architecture_30u.png
   :alt: A 4-node system, supporting up to 30 users with 1PB of storage


.. rubric:: Read more

Download the full `SQream DB Reference Architecture <https://sqream.com/product/hardware/#download>`_ document.
