.. _installing_sqream_with_kubernetes:

*********************************************
Installing SQream with Kubernetes
*********************************************

Overview
========
The **Installing SQream with Kubernetes** guide describes the following:

* How to prepare the SQream environment for installing SQream using Kubernetes.
* Install the SQream software using a Kubernetes package.

**Kubernetes**, also known as **k8s**, is a portable open source platform that automates Linux container operations. Kubernetes supports outsourcing data centers to public cloud service providers or can be scaled for web hosting. SQream uses Kubernetes as an orchestration and recovery solution.

Getting Started
===============
A minimum of three servers is required when installing SQream using Kubernetes.

Kubernetes uses clusters, which are sets of nodes running containterized applications. A cluster consists of at least 2 GPU nodes and 1 slim server to act as Quorum manager. All three servers are set as **master.**

**Comment - what does this mean? 2 servers with GPU and 1 without.**   

Each server must have the following IP addresses:

* An IP address located in the management network.
* An additional IP address from the same subnet to function as a floating IP.

All servers must be mounted in the same shared storage folder.

The following list shows the server host name format requirements:

* A maximum of 253 characters.
* Only lowercase alphanumeric characters, such as **-** or **.**.
* Starts and ends with alphanumeric characters.

Operating System Requirements
------------------------------
Installing SQream with Kubernetes includes the following operating system requirements:

* SQream tested and verified on x86 CentOS version higher than 7.6.
* SWAP disabled on all nodes.

Compute Server Specifications
------------------------------
Installing SQream with Kubernetes includes the following compute server specifications:

* **CPU:** 4 cores
* **RAM:** 16GB
* **HD:** 500GB

Setting Up Hosts
===============================
SQream lets you use set up your hosts.

**Comment - the Confluence doc cross references the user to the "Configure Hosts" section in the "Prerequisites" page:**

**https://sqream.atlassian.net/wiki/spaces/DOC/pages/17170437/SQream+production+server+and+OS+pre-requisites#Configure-%2Fetc%2Fhosts%3A**

**If that is the only relevant procedure for "Setting Up Hosts," it can be written here instead of making a cross reference.**

Setting up your hosts requires you to verify the following:

* User ID
* Installing required packages
* Disable Linux UI (if installed)
* IP Forwarding
* Disable SELinux
* Disable SWAP
* Cuda

Verifying a User ID
------------------

**To verify a user ID:**

1. Verify that the new user's ID is identical across all servers:

   .. code-block:: postgres
   
      $ id
      
   Verifying that the new user's ID generates the following output:
   
   .. code-block:: postgres
   
      $ iduid=1000(sqream) gid=1000(sqream) groups=1000(sqream),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023

2. If the **uid** and the **groupid** values are not identical across all nodes, update them so that they are identical.

   In the example below, the **uid** and **groupid** are changed from **1000** to **2000**:
   
   .. code-block:: postgres
   
      $ usermod -u 2000 sqream
      $ groupmod -g 2000 sqream

Installing the Required Packages
---------------------------------
You can install the required packages as follows:

   .. code-block:: postgres
   
      $ sudo yum install ntp  pciutils python36 python36-pip kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc jq net-tools
      
Disabling Linux
----------------------------------
If Linux has been installed, you can disable it as follows:

   .. code-block:: postgres
   
      $ sudo systemctl set-default multi-user.target

Enabling ID Forwarding
-----------------------------------
**IP Forwarding** must be enabled for Kubernetes and Docker.

**To enable ID Forwarding:**

**Comment - Why is Docker mentioned here?**

1. Check if IP Forwarding has been enabled:

   .. code-block:: postgres
   
      $ sysctl net.ipv4.ip_forward
      
   If the output shows **net.ipv41p_forward = 1**, IP Forwarding is enabled. If the output shows **net.ipv41p_forward = 0**, IP Forwarding is disabled.
   
2. If IP Forwarding is disabled, enable it.

   The following command lets you enable IP Forwarding without rebooting the system:

   .. code-block:: postgres
   
      $ echo 1 > /proc/sys/net/ipv4/ip_forward
      
3. If you have not enabled **ipv4 forwarding,** enable it when the system has rebooted.

4. Open the **/etc/sysctl.conf** configuration file for editing:

   .. code-block:: postgres
   
      $ sudo vim /etc/sysctl.conf
      
      bytesread
      ---------
      v<xxxx.x>      
      
5. Append the following line at the end of the file:

   **Comment - at the end of the name of the file?**

   .. code-block:: postgres
   
      $ net.ipv4.ip_forward = 1

6. Reboot the system.

   **Comment - see Step 3. Why is that Step written in that order when Step 6 is to reboot the system?**

7. Verify that output is **1**:

   .. code-block:: postgres
   
      $ cat /proc/sys/net/ipv4/ip_forward      
      
Disabling SELinux
----------------------------------

**To disable SELinux:**
 
 **Comment - do we want to give a short explanation of why we are disabling SELinux?**
 
 1.  **Comment - what do the "-i" and "-e" commands do with "sed?" Ignore and run a second command on the same line?**
 
    .. code-block:: postgres
   
       $ sed -i -e s/enforcing/disabled/g /etc/selinux/config
       $ sudo reboot
      
 2. Reboot the system as a root user:
      
    .. code-block:: postgres
   
       $ sudo reboot      
      
Disabling SWAP
----------------------------------
 
In some installations, System Administration installs the server operating system with SWAP enabled. If so, SWAP must be disabled.

**To disable SWAP:**
 
 1. Check if SWAP is enabled by determining if it is using any memory:
 
    .. code-block:: postgres
   
       $ free -m
       
The following is an example of the generated output:

    .. code-block:: postgres
   
       $ free -m 
       $ total        used        free      shared  buff/cache   availableMem:          
       $ 31886         360       31375           9         150       31216
       $ Swap:         16064           0       16064
      
The output above shows that SWAP is using **16064** MB of memory, indicating that it is enabled.
 
If SWAP is disabled, all SWAP memory usage values show **0**:

    .. code-block:: postgres
   
       $ [sqream@DEV-KS1 ~]$ free -m
       $               total        used        free      shared  buff/cache   available
       $ Mem:          31951         301       31502           8         146       31345
       $ Swap:             0           0           0
      
2. If SWAP is enabled, disable it on all servers:

   1. Comment out the line that points to **swap mounting**:

      .. code-block:: postgres
   
         $ sudo swapoff -a
      
   2. Disable the SWAP line(s) in the **/etc/fstab** directory:
   
      .. code-block:: postgres
   
         $ sudo vim /etc/fstab

   3. Replace ``/dev/mapper/centos-swap swap                    swap    defaults        0 0`` with ``##/dev/mapper/centos-swap swap                    swap    defaults        0 0``.

Rebooting All Servers
----------------------------------

**To reboot all servers:**

**Comment - the title is "Reboot All Servers," but the step only says to check the CUDA version. Need clarification.**

1. Check the CUDA version:

   .. code-block:: postgres
   
      $ nvidia-smi
      
   The following is an example of the correct output:

   .. code-block:: postgres
   
      $ +-----------------------------------------------------------------------------+
      $ | NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
      $ |-------------------------------+----------------------+----------------------+
      $ | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
      $ | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
      $ |===============================+======================+======================|
      $ |   0  GeForce GTX 105...  Off  | 00000000:01:00.0 Off |                  N/A |
      $ | 32%   38C    P0    N/A /  75W |      0MiB /  4039MiB |      0%      Default |
      $ +-------------------------------+----------------------+----------------------+
      $                                                                                
      $ +-----------------------------------------------------------------------------+
      $ | Processes:                                                       GPU Memory |
      $ |  GPU       PID   Type   Process name                             Usage      |
      $ |=============================================================================|
      $ |  No running processes found                                                 |
      $ +-----------------------------------------------------------------------------+

In the above output, the CUDA version is **10.1**.

Running Docker Runtime (Community Edition)
================================================
A container runtime functions similarly to the latter—it's software that runs and manages the components required to run containers. As mentioned above, these tools make it easier to securely execute and efficiently deploy containers, and are a key component of container management

The Community Edition of Docker Runtime must be run on all hosts (GPU and Compute).

Running Docker Runtime on an x86_64 Bit Processor
------------------------------------
If you are using an x86-64 bit processor, your version of Docker CE must be 18.03 or higher.

Installing Docker Runtime on CentOS
------------------------------------
**To install Docker Runtime on CentOS:**

1. Install the most current version of Docker Engine and containerd:

   .. code-block:: postgres
   
      $ sudo yum install docker-ce docker-ce-cli containerd.io
      
   If you are prompted to accept the GPG key, verify that the fingerprint matches ``060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35``. If it matches, accept it.

2. Start Docker Runtime:

   .. code-block:: postgres
   
      $ sudo systemctl start docker

3. Verify that Docker Engine has been installed correctly:

   .. code-block:: postgres
   
      $ sudo docker run hello-world

Running this command downloads and runs a test image in a container. The running container prints an informational message and exits.

4. Create the ``docker`` group:

   .. code-block:: postgres
   
      $ sudo groupadd docker
      
5. Add your user to the ``docker`` group:

   .. code-block:: postgres
   
      $ sudo usermod -aG docker $USER

 6. Do one of the following:
 
    * Log out and back in for your group membership to be re-evaluated.
    
      If you are testing on a virtual machine, you may need to restart your virtual machine for the changes to take effect.
      
    * If you are testing on a desktop Linux environment, such as X Windows, log out of your session completely and log back in.
    
    * On Linux, you can run the following command for the changes made to the groups to take effect:
 
      .. code-block:: postgres
   
         $ newgrp docker
         
For more information on installing Docker Runtime with CentOS, see `Install Docker Engine on CentOS <https://docs.docker.com/install/linux/docker-ce/centos/>`_

Installing Docker Runtime on Ubuntu
------------------------------------
**To install Docker Runtime on Ubuntu:**

1. Update the **apt** package index, and install the most current version of Docker Engine and containerd:

   .. code-block:: postgres
   
      $ sudo apt-get update
      $ sudo apt-get install docker-ce docker-ce-cli containerd.io

2. Verify that Docker Engine has been installed correctly:

   .. code-block:: postgres
   
      $ sudo docker run hello-world

Running this command downloads and runs a test image in a container. The running container prints an informational message and exits.

4. Create the ``docker`` group:

   .. code-block:: postgres
   
      $ sudo groupadd docker
      
5. Add your user to the ``docker`` group:

   .. code-block:: postgres
   
      $ sudo usermod -aG docker $USER

 6. Do one of the following:
 
    * Log out and back in for your group membership to be re-evaluated.
    
      If you are testing on a virtual machine, you may need to restart your virtual machine for the changes to take effect.
      
    * If you are testing on a desktop Linux environment, such as X Windows, log out of your session completely and log back in.
    
    * On Linux, you can run the following command for the changes made to the groups to take effect:
 
      .. code-block:: postgres
   
         $ newgrp docker

     For more information on installing Docker Runtime with Ubuntu, see `Install Docker Engine on Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

Setting Docker Runtime Post-Installation Configurations
================================================

**To set Docker Runtime post-installation configurations:

1. Configure Docker Runtime to run automatically when started:

      .. code-block:: postgres
   
         $ sudo systemctl enable docker && sudo systemctl start docker

2. Manage Docker Runtime as a non-root user:

      .. code-block:: postgres
   
         $ sudo usermod -aG docker $USER

3. Manage Docker Runtime as a non-root user:

      .. code-block:: postgres
   
         $ sudo usermod -aG docker $USER

4. Log out and back in for your group membership to be re-evaluated.

**Comment - this step was included in Installing Docker Runtime on CentOS/Ubuntu above. Is it needed here as well?**

5. Verify that Docker Engine has been installed correctly:

   .. code-block:: postgres
   
      $ sudo docker run hello-world
 
**Comment - this step was included in Installing Docker Runtime on CentOS/Ubuntu above. Is it needed here as well?**

Installing the NVIDIA Docker2 Toolkit
=====================================
The **NVIDIA Docker2 Toolkit** lets users build and run GPU-accelerated Docker containers, and must be run only on GPU servers. The NVIDIA Docker2 Toolkit includes a container runtime library and utilities that automatically configure containers to leverage NVIDIA GPUs.

Installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on CentOS
------------------------------------
**To install the NVIDIA Docker2 Toolkit on an x86_64 bit processor on CentOS:**

1. Add the repository for your distribution:

   .. code-block:: postgres
   
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | \
      $ sudo tee /etc/yum.repos.d/nvidia-docker.repo

2. Install the **nvidia-docker2** package and reload the Docker daemon configuration:
   
   .. code-block:: postgres
   
      $ sudo yum install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd

3. Verify that the nvidia-docker2 package has been installed correctly:

   .. code-block:: postgres
   
      $ docker run --runtime=nvidia --rm nvidia/cuda:10.1-base nvidia-smi

The following is an example of the correct output:

   .. code-block:: postgres
   
      $ docker run --runtime=nvidia --rm nvidia/cuda:10.1-base nvidia-smi
      $ Unable to find image 'nvidia/cuda:10.1-base' locally
      $ 10.1-base: Pulling from nvidia/cuda
      $ d519e2592276: Pull complete 
      $ d22d2dfcfa9c: Pull complete 
      $ b3afe92c540b: Pull complete 
      $ 13a10df09dc1: Pull complete 
      $ 4f0bc36a7e1d: Pull complete 
      $ cd710321007d: Pull complete 
      $ Digest: sha256:635629544b2a2be3781246fdddc55cc1a7d8b352e2ef205ba6122b8404a52123
      $ Status: Downloaded newer image for nvidia/cuda:10.1-base
      $ Sun Feb 14 13:27:58 2021       
      $ +-----------------------------------------------------------------------------+
      $ | NVIDIA-SMI 418.87.00    Driver Version: 418.87.00    CUDA Version: 10.1     |
      $ |-------------------------------+----------------------+----------------------+
      $ | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
      $ | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
      $ |===============================+======================+======================|
      $ |   0  GeForce GTX 105...  Off  | 00000000:01:00.0 Off |                  N/A |
      $ | 32%   37C    P0    N/A /  75W |      0MiB /  4039MiB |      0%      Default |
      $ +-------------------------------+----------------------+----------------------+
      $                                                                                
      $ +-----------------------------------------------------------------------------+
      $ | Processes:                                                       GPU Memory |
      $ |  GPU       PID   Type   Process name                             Usage      |
      $ |=============================================================================|
      $ |  No running processes found                                                 |
      $ +-----------------------------------------------------------------------------+

     For more information on installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on CentOS, see `NVIDIA Docker Installation - CentOS distributions <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker>`_
     
Installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on Ubuntu
------------------------------------
**To install the NVIDIA Docker2 Toolkit on an x86_64 bit processor on Ubuntu:**

1. Add the repository for your distribution:

   .. code-block:: postgres
   
      $ curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
      $ sudo apt-key add -     
      $ distribution=$(. /etc/os-release;echo $ID$VERSION_ID)  
      $ curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
      $ sudo tee /etc/apt/sources.list.d/nvidia-docker.list  
      $ sudo apt-get update
     
2. Install the **nvidia-docker2** package and reload the Docker daemon configuration:
   
   .. code-block:: postgres
   
      $ sudo apt-get install nvidia-docker2
      $ sudo pkill -SIGHUP dockerd
     
 3. Verify that the nvidia-docker2 package has been installed correctly:

   .. code-block:: postgres
   
      $ docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi  
     
      For more information on installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on Ubuntu, see `NVIDIA Docker Installation - Ubuntu distributions <https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#ubuntu-distributions-1>`_
    
Modifying the Docker Daemon JSON File for GPU Nodes
======================================
You can modify the Docker daemon JSON file for GPU and for Compute nodes.

Modifying the Docker Daemon JSON File for GPU Nodes
------------------------------------
**To modify the Docker daemon JSON file for GPU nodes:**     
     
1. Enable GPU passthrough and set HTTP access to the local Kubernetes Docker registry.

**NOTICE:** Contact SQream IT for a virtual IP.

**Comment - should we leave contact information here?**

2. Replace the <VIP address> with your assigned VIP address.

3. Connect as a root user:

   .. code-block:: postgres
   
      $  sudo -i
     
4. Set a variable that includes the VIP address:    
     
   .. code-block:: postgres
   
      $ export VIP_IP=<VIP IP>

5. Replace the <VIP IP> with the VIP address:      
     
    .. code-block:: postgres
   
      $ cat <<EOF > /etc/docker/daemon.json
      $ {
      $    "insecure-registries": ["$VIP_IP:6000"],
      $     "default-runtime": "nvidia",
      $     "runtimes": {
      $         "nvidia": {
      $             "path": "nvidia-container-runtime",
      $             "runtimeArgs": []
      $         }
      $     }
      $ }
      $ EOF   

6. Clear the changes and restart Docker:

   .. code-block:: postgres
   
      $ systemctl daemon-reload && systemctl restart docker
      
7. Exit the root:
 
**Exit the root user?**
 
  .. code-block:: postgres
   
     $ exit
      
Modifying the Docker Daemon JSON File for Compute Nodes
------------------------------------
**To modify the Docker daemon JSON file for Compute nodes:**

1. Set HTTP access to the local Kubernetes Docker registry.

2. Switch to a root user:

   .. code-block:: postgres
   
      $  sudo -i

3. Set a variable that includes a VIP address.

**NOTICE:** Contact SQream IT for a virtual IP.

**Comment - should we leave contact information here?**

4. Replace the <VIP address> with your assigned VIP address.

   .. code-block:: postgres
   
      $ cat <<EOF > /etc/docker/daemon.json
      $ {
      $    "insecure-registries": ["$VIP_IP:6000"]
      $ }
      $ EOF 

5. Restart the services:

   .. code-block:: postgres
   
      $ systemctl daemon-reload && systemctl restart docker

7. Exit the root:
 
**Exit the root user?**
 
  .. code-block:: postgres
   
     $ exit
     
Installing the Kubernetes Cluster
===================================
**To install the Kubernetes cluster**:

Getting Started
-----------------------------------
The Kubernetes and SQream software must be installed from the management host.

**Comment - does Step 1 refer to any of the above procedures? If so, make a cross-reference.**

**NOTICE:** Installing the Kubernetes and SQream software must only be done from the management host.

The Kubernetes and SQream software can be installed on any server in the cluster.

Generating an Sharing an SSH Keypair Across Nodes
------------------------------------
An SSH keypair can be generated and shared across all existing nodes. Sharing SSH keypairs across all nodes enables passwordless access from the management server to all nodes in the cluster. All nodes in the cluster require passwordless access.

**Comment - the document said, "DO THIS STEP EVEN IF INSTALLING ON SINGLE HOST!"**

**Comment - does this note refer to the entire section, or to Step 1, below?**

**To generate and share an SSH keypair:**

1. Switch to a root user:

  .. code-block:: postgres
   
     $ $ sudo -i

2. Generate an rsa key pair:

  .. code-block:: postgres
   
     $ ssh-keygen

The following is an example of the correct output:

  .. code-block:: postgres
   
     $ ssh-keygen
     $ Generating public/private rsa key pair.
     $ Enter file in which to save the key (/root/.ssh/id_rsa):
     $ Created directory '/root/.ssh'.
     $ Enter passphrase (empty for no passphrase):
     $ Enter same passphrase again:
     $ Your identification has been saved in /root/.ssh/id_rsa.
     $ Your public key has been saved in /root/.ssh/id_rsa.pub.
     $ The key fingerprint is:
     $ SHA256:xxxxxxxxxxxxxxdsdsdffggtt66gfgfg root@localhost.localdomain
     $ The key's randomart image is:
     $ +---[RSA 2048]----+
     $ |            =*.  |
     $ |            .o   |
     $ |            ..o o|
     $ |     .     .oo +.|
     $ |      = S =...o o|
     $ |       B + *..o+.|
     $ |      o * *..o .+|
     $ |       o * oo.E.o|
     $ |      . ..+..B.+o|
     $ +----[SHA256]-----+

3. Copy the content of the output public key for all servers in the cluster to the **authorized_keys** file:

  .. code-block:: postgres
   
     $ ssh-copy-id -i ~/.ssh/id_rsa.pub root@remote-host

   The public key is located in the **/root/.ssh/id_rsa.pub** directory.
   
   The **authorized_keys** file is located in the **/root/.ssh/authorized_keys** directory:
   
4. Replace the following:

   * The <user name> with your local user name.
   * The <remote host> with your host IP address.
      
**Comment - do we want to show sample output here?**      
      
Installing and Deploying a Kubernetes Cluster with Kubespray
=============================================================
SQream uses the Kubespray software pack to install and deploy Kubernetes clusters.

Copying Files into the Correct Directory
-----------------------------------------
Before downloading Kubespray, you must copy all of your files into the correct directory.

**To :**

**Comment - is the final result of this procedure to copy all files into the correct directory?**

The Kubernetes files to be installed with Kubespray are located in the **/usr/local/bin** directory.

1. Append **.bash_profile** to all files located in the **/usr/local/bin** directory:

  .. code-block:: postgres
   
     $ vi ~/.bash_profile

**Comment - verify that this step has been understood correctly.**

2. Append ``/usr/local/bin`` to ``PATH``:

  .. code-block:: postgres
   
     $ PATH=$PATH:$HOME/bin:/usr/local/bin

3. Save and exit:

  .. code-block:: postgres
   
     $ exit
     
4. Login and apply the modified ``PATH``: 

  .. code-block:: postgres
   
     $ && sudo -i

**Confirm Step 4.**

Downloading and Configuring Kubespray
-------------------------------------
1. Run the following command:

**Comment - what does "-i" do?**

2. Install the following files:

   * python36-devel
   * openssl-devel
   * python3-pip.noarch
   
  .. code-block:: postgres
   
     $ yum install git python36-devel openssl-devel python3-pip.noarch
     
**Comment - is the above correct?**

3. Run the following commands:

**Comment - what do the following commands do?**

  .. code-block:: postgres
   
     $ pip3 install --upgrade pip
     $ pip3 install ansible==2.9.0 netaddr==0.7.19

4. Clone Kubernetes:

   1. Clone the **kubespray.git** file:

  .. code-block:: postgres
   
     $ git clone https://github.com/kubernetes-incubator/kubespray.git
     
   2. Nagivate to the **kubespray** directory:
     
       .. code-block:: postgres
   
     $ cd kubespray
     
   3. **Comment - what does command do?**
   
     .. code-block:: postgres
   
     $ pip3 install -r requirements.txt











      
      
      
      
