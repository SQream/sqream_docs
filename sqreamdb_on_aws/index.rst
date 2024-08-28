.. _sqreamdb_on_aws:

***************
SQreamDB on AWS
***************

The SQreamDB Data Processing and Analytics Acceleration Platform on AWS marketplace is available `here <https://aws.amazon.com/marketplace/pp/prodview-ytpp4pwjcxdca>`_. 

.. contents:: 
   :local:
   :depth: 1

Before You Begin
================

It is essential that you have the following:

* An AWS account
* AWS **Key Pairs**
* AWS permissions (verify specific permissions)

Configuration on AWS
====================

Specify stack details
-----------------------

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``environment``
     - The name used for all objects created
   * - ``region``
     - Region where we want the machines to be created. The bucket we store sqream contents in should also use the same region for better performance and price
   * - ``availability_zones``
     - Availability zone to place the machines inside the region. Should be a zone with GPU machines
   * - ``key_name``
     - The name of an EC2 key pair already present in the account that will be used by all created machines to log into them
   * - ``office_cidrs``
     - A list of IPs which will be given access to the product and to ssh to the machines (for security)
   * - ``sqream_ami``
     - The AMI with Sqream product on it. Currently for Sqream 4.7 use ``ami07d82637b2dab962e``
   * - ``ui_instance_type``
     - Machine type of the UI. Recommended is 16G RAM and some medium CPU such as in ``t2.xlarge``
   * - ``md_instance_type``
     - Machine type of the metadata and server picker machine. Depends on the workflow, but a good starting point is ``t2.2xlarge``
   * - ``workers_instance_type``
     - Machine type of the Workers machines. Must be a GPU machine. Recommended machines are ``g5.xlarge`` or ``g4dn.xlarge``
   * - ``workers_count``
     - Number of worker machines to create 
   * - ``tablespaceURL``
     - Where the database will be stored. Should be at the same Region as the machine to reduce costs. PAY ATTENTION that a folder terraform_important dir will also be created here and shouldn't be deleted as long as the installation wasn't deleted. Deleting it will cause upgrades and changes to reinstall a new environment instead of using the existing. Uninstall also uses this data, so only after uninstall it should be manually removed
   * - ``tempPath``
     - Should typically be ``/mnt/ephemeral``, though it can also be a path in S3. Temp storage used for running queries and is auto-deleted when they are done

Parameters table (read me)

License
=======

#. Get the list of machines:

   * Using the CLI:
   
     **Terraform:** run Terraform script:
	 
    .. code-block:: console
	 
        ./get_machines.sh
		
     **AWS Console:** filter EC2 instances using the keyword **worker** and the environment name given.
	 
#. Send the machines to Sqream to generate license.

#. Install on each machine the license by:

   a. Connecting to the machine (check "connect to AWS machine" section above) - only available from IPs given access by parameter ``office_cidrs``.
   b. Create a new file **in this path:**
   
      .. code-block:: console
   
	sudo vi /etc/sqream/license.enc

#. Place the license given by Sqream in it.

#. Wait 1-2 minutes for the worker to automatically start.


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

#. To get the URL using SQreamDB CLI, run the following script:

   .. code-block:: console

	./get_url.sh 

#. To get the URL using AWS Console, copy the DNS of the Network Load Balancer.
