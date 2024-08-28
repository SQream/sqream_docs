.. _sqreamdb_on_aws:

***************
SQreamDB on AWS
***************

Private cloud deployment on AWS provides the ability to maintain control and security similar to traditional private clouds, while utilizing AWS's scalable infrastructure, flexible resource management, and cost-efficient services.

The SQreamDB data processing and analytics acceleration platform on AWS marketplace is available `here <https://aws.amazon.com/marketplace/pp/prodview-ytpp4pwjcxdca>`_. 

.. contents:: 
   :local:
   :depth: 1

Before You Begin
================

It is essential that you have the following:

* An AWS account
* An existing EC2 key pair
* AWS administrator permissions

Usage Notes
===========

If you need to access data from an external bucket (one that is not part of the SqreamDB installation or used for ``tablespaceURL`` or ``tempPath``), you must manually grant access. Alternatively, you can copy data to and from the bucket using the AWS_ID and AWS_Secret parameters.

Configuration on AWS
====================

Under the **CloudFormation** > **Stacks** > **Specify stack details** tab, configure the following parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``environment``
     - The identifier used for naming all created resources
   * - ``region``
     - The AWS region where the machines will be deployed. For optimal performance and cost efficiency, the S3 bucket storing Sqream data should be in the same region
   * - ``availability_zones``
     - The availability zone within the specified region to place the machines. It should support GPU-enabled instances
   * - ``key_name``
     - The name of an existing EC2 key pair in your AWS account, used to log into all created instances
   * - ``office_cidrs``
     - A list of IP ranges (CIDRs) that are allowed access to the product and SSH access to the machines for security purposes
   * - ``sqream_ami``
     - The Amazon Machine Image (AMI) pre-configured with Sqream. For Sqream 4.7, use ``ami-07d82637b2dab962e``
   * - ``ui_instance_type``
     - The instance type for the UI server. A machine with 16GB of RAM and moderate CPU resources, such as a ``r6i.2xlarge``, is recommended
   * - ``md_instance_type``
     - The instance type for the metadata and server picker machine. Recommended starting point is a ``r6i.2xlarge``, but it may vary depending on your workload
   * - ``workers_instance_type``
     - The instance type for the worker machines, which must be GPU-enabled. Recommended options include ``g6.8xlarge`` or ``g5.8xlarge``
   * - ``workers_count``
     - The number of worker machines to be created
   * - ``tablespaceURL``
     - The location where the database will be stored, ideally in the same region as the instances to minimize costs. Important: A ``terraform_important`` directory will also be created here and should not be deleted unless the installation is completely removed. Deleting this directory prematurely may cause issues during upgrades or changes, leading to a full reinstall of the environment
   * - ``tempPath``
     - The temporary storage path, usually set to ``/mnt/ephemeral``, though it can also point to an S3 bucket. This storage is used for running queries and is automatically cleared once the queries are completed

License
=======

#. Get a list of machines using your AWS console by filtering EC2 instances with the **worker** keyword and the environment name given.
	 
#. Send the machines to SqreamDB to generate license.

#. On each machine, install the license by:

   a. Connecting to the machine (check "connect to AWS machine" section above) - only available from IPs given access by parameter ``office_cidrs``.
   b. Create a new file **in this path:**
   
      .. code-block:: console
   
	sudo vi /etc/sqream/license.enc

#. Place the license given by SqreamDB in it.

#. Wait 1-2 minutes for the Worker to automatically start.


Connecting to the Machine
=========================

For security purposes, all machines are assigned private IP addresses. To enable connections, an EC2 endpoint is configured during installation. You can connect either via the AWS Console UI or through the CLI.

Connecting Using the CLI
------------------------

You'll need your machine ID and region and the type of key file.

Run the following command:

.. code-block:: console

	ssh -i <key file> ec2-user@i-<ID> -o ProxyCommand="aws ec2-instance-connect opentunnel --instance-id i-<ID> --region=<region>"

Connecting to SQreamDB
======================

During installation, a Network Load Balancer (NLB) named ``sqream-<environment>-nlb`` is created to route traffic to various machines. After installation, SqreamDB is accessible via the NLB's DNS name. For the SqreamDB UI, use this URL in any browser, or connect to it from third-party software components.

#. To get the URL using AWS Console, copy the DNS of the Network Load Balancer.

Connection Troubleshooting 
--------------------------

If you are unable to connect, please ensure the following:

* The license file has been generated and distributed to all Worker nodes.
* Your IP address is included in the ``office_cidrs`` parameter, as only the specified IPs are allowed access to the cluster.

Adding a Signed Certificate to the Cluster
==========================================

To add your signed certificate to the Sqream cluster, follow these steps:

#. `Create a new listener <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-listener.html>`_ for the Network Load Balancer (sqream-<environment>-nlb) using the TLS protocol.

#. A TLS target group that points to the UI machine has already been created for your convenience. You can use it for the new listener. The group name is ``sqream-<environment>-nlb-ui-443``.

#. If you require a new DNS, you can retrieve the public IP of the Network Load Balancer by either:

   * Running the host CLI command with the NLB's URL

   * Finding it in the AWS console