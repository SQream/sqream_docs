.. _installing_sqream_with_kubernetes:

*********************************************
Installing SQream with Kubernetes
*********************************************
**Kubernetes**, also known as **k8s**, is a portable open source platform that automates Linux container operations. Kubernetes supports outsourcing data centers to public cloud service providers or can be scaled for web hosting. SQream uses Kubernetes as an orchestration and recovery solution.

The **Installing SQream with Kubernetes** guide describes the following:

.. contents:: 
   :local:
   :depth: 1
   
.. _preparing_sqream_environment:
   
Preparing the SQream Environment to Launch SQream Using Kubernetes 
===============

The **Preparing the SQream environment to Launch SQream Using Kubernetes** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Overview
--------------
   
A minimum of three servers is required for preparing the SQream environment using Kubernetes.

Kubernetes uses clusters, which are sets of nodes running containterized applications. A cluster consists of at least two GPU nodes and one additional server without GPU to act as the quorum manager.

Each server must have the following IP addresses:

* An IP address located in the management network.
* An additional IP address from the same subnet to function as a floating IP.

All servers must be mounted in the same shared storage folder.

The following list shows the server host name format requirements:

* A maximum of 253 characters.
* Only lowercase alphanumeric characters, such as ``-`` or ``.``.
* Starts and ends with alphanumeric characters.

Go back to :ref:`Preparing the SQream Environment to Launch SQream Using Kubernetes<preparing_sqream_environment>`


Operating System Requirements
------------------------------
The required operating system is a version of x86 CentOS/RHEL between 7.6 and 7.9. Regarding PPC64le, the required version is RHEL 7.6.

Go back to :ref:`Preparing the SQream Environment to Launch SQream Using Kubernetes<preparing_sqream_environment>`


Compute Server Specifications
------------------------------
Installing SQream with Kubernetes includes the following compute server specifications:

* **CPU:** 4 cores
* **RAM:** 16GB
* **HD:** 500GB

Go back to :ref:`Preparing the SQream Environment to Launch SQream Using Kubernetes<preparing_sqream_environment>`

.. _set_up_your_hosts:

Setting Up Your Hosts
===============================
SQream requires you to set up your hosts. Setting up your hosts requires the following:

.. contents:: 
   :local:
   :depth: 1

Configuring the Hosts File
--------------------------------
**To configure the /etc/hosts file:**

1. Edit the **/etc/hosts** file:

   .. code-block:: console

      $ sudo vim /etc/hosts

2. Call your local host:

   .. code-block:: console

      $ 127.0.0.1	localhost
      $ <server ip>	<server_name>
 

Installing the Required Packages
----------------------------------
The first step in setting up your hosts is to install the required packages.

**To install the required packages:**

1. Run the following command based on your operating system:

   * RHEL:
    
    .. code-block:: postgres
   
       $ sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm    
 
   * CentOS:
    
    .. code-block:: postgres
   
       $ sudo yum install epel-release	   
       $ sudo yum install pciutils openssl-devel python36 python36-pip kernel-devel-$(uname -r) kernel-headers-$(uname -r) gcc jq net-tools ntp

2. Verify that that the required packages were successfully installed. The following is the correct output:
    
    .. code-block:: postgres
   
       ntpq --version
       jq --version
       python3 --version
       pip3 --version
       rpm -qa |grep kernel-devel-$(uname -r)
       rpm -qa |grep kernel-headers-$(uname -r)
       gcc --version

3. Enable the **ntpd (Network Time Protocol daemon)** program on all servers:
    
    .. code-block:: postgres
   
       $ sudo systemctl start ntpd
       $ sudo systemctl enable ntpd
       $ sudo systemctl status ntpd
       $ sudo ntpq -p
	   
Go back to :ref:`Setting Up Your Hosts<set_up_your_hosts>`

     
Disabling the Linux UI
----------------------------------
After installing the required packages, you must disable the Linux UI if it has been installed.

You can disable Linux by running the following command:

   .. code-block:: postgres
   
      $ sudo systemctl set-default multi-user.target

Go back to :ref:`Setting Up Your Hosts<set_up_your_hosts>`


Disabling SELinux
----------------------------------
After disabling the Linux UI you must disable SELinux.

**To disable SELinux:**

 1.  Run the following command:
 
    .. code-block:: postgres
   
       $ sed -i -e s/enforcing/disabled/g /etc/selinux/config
       $ sudo reboot
      
 2. Reboot the system as a root user:
      
    .. code-block:: postgres
   
       $ sudo reboot      

Go back to :ref:`Setting Up Your Hosts<set_up_your_hosts>`

Disabling Your Firewall
----------------------------------
After disabling SELinux, you must disable your firewall by running the following commands:
   
      .. code-block:: postgres
   
         $ sudo systemctl stop firewalld
         $ sudo systemctl disable firewalld

Go back to :ref:`Setting Up Your Hosts<set_up_your_hosts>`

  
Checking the CUDA Version
----------------------------------
After completing all of the steps above, you must check the CUDA version.

**To check the CUDA version:**

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

If the above output is not generated, CUDA has not been installed. To install CUDA, see `Installing the CUDA driver <https://docs.sqream.com/en/latest/guides/operations/setup/recommended_pre-installation_configurations.html?highlight=install%20CUDA#installing-the-cuda-driver>`_.


Go back to :ref:`Setting Up Your Hosts<set_up_your_hosts>`

.. _install_kubernetes_cluster:

Installing Your Kubernetes Cluster
===================================
After setting up your hosts, you must install your Kubernetes cluster. The Kubernetes and SQream software must be installed from the management host, and can be installed on any server in the cluster.

Installing your Kubernetes cluster requires the following:

.. contents:: 
   :local:
   :depth: 1

Generating and Sharing SSH Keypairs Across All Existing Nodes
------------------------------------
You can generate and share SSH keypairs across all existing nodes. Sharing SSH keypairs across all nodes enables passwordless access from the management server to all nodes in the cluster. All nodes in the cluster require passwordless access.

.. note::  You must generate and share an SSH keypair across all nodes even if you are installing the Kubernetes cluster on a single host.

**To generate and share an SSH keypair:**

1. Switch to root user access:

  .. code-block:: postgres
   
     $ sudo su -

2. Generate an RSA key pair:

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

The generated file is ``/root/.ssh/id_rsa.pub``.
	 
3. Copy the public key to all servers in the cluster, including the one that you are running on. 

  .. code-block:: postgres
   
     $ ssh-copy-id -i ~/.ssh/id_rsa.pub root@remote-host
   
4. Replace the ``remote host`` with your host IP address.
      
Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

Installing and Deploying a Kubernetes Cluster Using Kubespray
------------------------------------
SQream uses the Kubespray software package to install and deploy Kubernetes clusters.

**To install and deploy a Kubernetes cluster using Kubespray:**


1. Clone Kubernetes:

   1. Clone the **kubespray.git** repository:

      .. code-block:: postgres
   
         $ git clone https://github.com/kubernetes-incubator/kubespray.git
     
   2. Nagivate to the **kubespray** directory:
     
       .. code-block:: postgres
   
          $ cd kubespray
     
   3. Install the **requirements.txt** configuration file:
   
      .. code-block:: postgres
   
         $ pip3 install -r requirements.txt		 

2. Create your SQream inventory directory:

   1. Run the following command:
   
      .. code-block:: postgres
   
         $ cp -rp inventory/sample inventory/sqream
   
   2. Replace the **<cluster node IP>** with the defined cluster node IP address(es).
   
      .. code-block:: postgres
   
         $ declare -a IPS=(<host>, <cluster node IP address>) 
   
      For example, the following replaces ``192.168.0.93`` with ``192.168.0.92``:

      .. code-block:: postgres
   
         $ declare -a IPS=(host-93,192.168.0.93 host-92,192.168.0.92)

Note the following:
 * Running a declare requires defining a pair (host name and cluster node IP address), as shown in the above example.
 * You can define more than one pair.
 
3. When the reboot is complete, switch back to the root user:
   
    .. code-block:: postgres
   
       $ sudo su -

4. Navigate to **root/kubespray**:
   
    .. code-block:: postgres
   
       $ cd /root/kubespray

5. Copy ``inventory/sample`` as ``inventory/sqream``:
   
    .. code-block:: postgres
   
       $ cp -rfp inventory/sample inventory/sqream

6. Update the Ansible inventory file with the inventory builder:
   
    .. code-block:: postgres
   
       $ declare -a IPS=(<hostname1>,<IP1> <hostname2>,<IP2> <hostname3>,<IP3>)
	   
7. In the **kubespray hosts.yml** file, set the node IP's: 

   .. code-block:: postgres
   
      $ CONFIG_FILE=inventory/sqream/hosts.yml python3 contrib/inventory_builder/inventory.py ${IPS[@]}
	  
   If you do not set a specific hostname in declare, the server hostnames will change to ``node1``, ``node2``, etc. To maintain specific hostnames, run declare as in the following example:

   .. code-block:: postgres
   
      $ declare -a IPS=(eks-rhl-1,192.168.5.81 eks-rhl-2,192.168.5.82 eks-rhl-3,192.168.5.83)

   Note that the declare must contain pairs (hostname,ip).
   
::
	  
8. Verify that the following have been done:
 
   * That the **hosts.yml** file is configured correctly.
   * That all children are included with their relevant nodes.

You can save your current server hostname by replacing <nodeX> with your server hostname.

9. Generate the content output of the **hosts.yml** file. Make sure to include the file's directory:

   .. code-block:: postgres
   
      $ cat  inventory/sqream/hosts.yml
	  
The hostname can be lowercase and contain ``-`` or ``.`` only, and must be aligned with the server's hostname.

The following is an example of the correct output. Each host and IP address that you provided in Step 2 should be displayed once:

   .. code-block:: postgres
   
      $ all:
      $   hosts:
      $     node1:
      $       ansible_host: 192.168.5.81
      $       ip: 192.168.5.81
      $       access_ip: 192.168.5.81
      $     node2:
      $       ansible_host: 192.168.5.82
      $       ip: 192.168.5.82
      $       access_ip: 192.168.5.82
      $     node3:
      $       ansible_host: 192.168.5.83
      $       ip: 192.168.5.83
      $       access_ip: 192.168.5.83
      $   children:
      $     kube-master:
      $       hosts:
      $         node1:
      $         node2:
      $         node3:
      $     kube-node:
      $       hosts:
      $         node1:
      $         node2:
      $         node3:
      $     etcd:
      $       hosts:
      $         node1:
      $         node2:
      $         node3:
      $     k8s-cluster:
      $       children:
      $         kube-master:
      $         kube-node:
      $     calico-rr:
      $       hosts: {}
	  
Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
     
Adjusting Kubespray Deployment Values
-------------------------------------    
After downloading and configuring Kubespray, you can adjust your Kubespray deployment values. A script is used to modify how the Kubernetes cluster is deployed, and you must set the cluster name variable before running this script.

.. note:: The script must be run from the **kubespray** folder.

**To adjust Kubespray deployment values:**

1. Add the following export to the local user’s **~/.bashrc** file by replacing the <VIP IP> with the user's Virtual IP address:

   .. code-block:: postgres
   
      $ export VIP_IP=<VIP IP>
	  
2. Logout, log back in, and verify the following:

   .. code-block:: postgres
   
      $ echo $VIP_IP
	  
3. Make the following replacements to the **kubespray.settings.sh** file:

   .. code-block:: postgres
   
      $ cat <<EOF > kubespray_settings.sh
      $ sed -i "/cluster_name: cluster.local/c   \cluster_name: cluster.local.$cluster_name" inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ sed -i "/dashboard_enabled/c   \dashboard_enabled\: "false"" inventory/sqream/group_vars/k8s-cluster/addons.yml
      $ sed -i "/kube_version/c   \kube_version\: "v1.18.3"" inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ sed -i "/metrics_server_enabled/c   \metrics_server_enabled\: "true"" inventory/sample/group_vars/k8s-cluster/addons.yml
      $ echo 'kube_apiserver_node_port_range: "3000-6000"' >> inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ echo 'kube_controller_node_monitor_grace_period: 20s' >> inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ echo 'kube_controller_node_monitor_period: 2s' >> inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ echo 'kube_controller_pod_eviction_timeout: 30s' >> inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ echo 'kubelet_status_update_frequency: 4s' >> inventory/sqream/group_vars/k8s-cluster/k8s-cluster.yml
      $ echo 'ansible ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
      $ EOF
	  
.. note:: In most cases, the Docker data resides on the system disk. Because Docker requires a high volume of data (images, containers, volumes, etc.), you can change the default Docker data location to prevent the system disk from running out of space.

4. *Optional* - Change the default Docker data location:

   .. code-block:: postgres
   
      $ sed -i "/docker_daemon_graph/c   \docker_daemon_graph\: "</path/to/desired/location>"" inventory/sqream/group_vars/all/docker.yml
 	  
5. Make the **kubespray_settings.sh** file executable for your user:

   .. code-block:: postgres
   
      $ chmod u+x kubespray_settings.sh && ./kubespray_settings.sh
	  
6. Run the following script:

   .. code-block:: postgres
   
      $ ./kubespray_settings.sh

7. Run a playbook on the **inventory/sqream/hosts.yml cluster.yml** file:

   .. code-block:: postgres
   
      $ ansible-playbook -i inventory/sqream/hosts.yml cluster.yml -v

The Kubespray installation takes approximately 10 - 15 minutes.

The following is an example of the correct output:

   .. code-block:: postgres
   
      $ PLAY RECAP
      $ *********************************************************************************************
      $ node-1             : ok=680  changed=133  unreachable=0    failed=0
      $ node-2             : ok=583  changed=113  unreachable=0    failed=0
      $ node-3             : ok=586  changed=115  unreachable=0    failed=0
      $ localhost          : ok=1    changed=0    unreachable=0    failed=0

In the event that the output is incorrect, or a failure occurred during the installation, please contact a SQream customer support representative.

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`.   
      
Checking Your Kubernetes Status
-------------------------------
After adjusting your Kubespray deployment values, you must check your Kubernetes status.

**To check your Kuberetes status:**

1. Check the status of the node:

   .. code-block:: postgres
   
      $ kubectl get nodes
	  
The following is an example of the correct output:

   .. code-block:: postgres
   
      $ NAME        STATUS   ROLES                  AGE   VERSION
      $ eks-rhl-1   Ready    control-plane,master   29m   v1.21.1
      $ eks-rhl-2   Ready    control-plane,master   29m   v1.21.1
      $ eks-rhl-3   Ready    <none>                 28m   v1.21.1

2. Check the status of the pod:

   .. code-block:: postgres
   
      $ kubectl get pods --all-namespaces 

   The following is an example of the correct output:

      .. code-block:: postgres
   
         $ NAMESPACE                NAME                                         READY   STATUS    RESTARTS   AGE
         $ kube-system              calico-kube-controllers-68dc8bf4d5-n9pbp     1/1     Running   0          160m
         $ kube-system              calico-node-26cn9                            1/1     Running   1          160m
         $ kube-system              calico-node-kjsgw                            1/1     Running   1          160m
         $ kube-system              calico-node-vqvc5                            1/1     Running   1          160m
         $ kube-system              coredns-58687784f9-54xsp                     1/1     Running   0          160m
         $ kube-system              coredns-58687784f9-g94xb                     1/1     Running   0          159m
         $ kube-system              dns-autoscaler-79599df498-hlw8k              1/1     Running   0          159m
         $ kube-system              kube-apiserver-k8s-host-1-134                1/1     Running   0          162m
         $ kube-system              kube-apiserver-k8s-host-194                  1/1     Running   0          161m
         $ kube-system              kube-apiserver-k8s-host-68                   1/1     Running   0          161m
         $ kube-system              kube-controller-manager-k8s-host-1-134       1/1     Running   0          162m
         $ kube-system              kube-controller-manager-k8s-host-194         1/1     Running   0          161m
         $ kube-system              kube-controller-manager-k8s-host-68          1/1     Running   0          161m
         $ kube-system              kube-proxy-5f42q                             1/1     Running   0          161m
         $ kube-system              kube-proxy-bbwvk                             1/1     Running   0          161m
         $ kube-system              kube-proxy-fgcfb                             1/1     Running   0          161m
         $ kube-system              kube-scheduler-k8s-host-1-134                1/1     Running   0          161m
         $ kube-system              kube-scheduler-k8s-host-194                  1/1     Running   0          161m

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
        
Adding a SQream Label to Your Kubernetes Cluster Nodes
-------------------------------------------------
After checking your Kubernetes status, you must add a SQream label on your Kubernetes cluster nodes.

**To add a SQream label on your Kubernetes cluster nodes:**

1. Get the cluster node list:

   .. code-block:: postgres
   
      $ kubectl get nodes
	  
   The following is an example of the correct output:
   
   .. code-block:: postgres
   
      $ NAME        STATUS   ROLES                  AGE   VERSION
      $ eks-rhl-1   Ready    control-plane,master   29m   v1.21.1
      $ eks-rhl-2   Ready    control-plane,master   29m   v1.21.1
      $ eks-rhl-3   Ready    <none>                 28m   v1.21.1
	  
2. Set the node label, change the ``node-name`` to the node NAME(s) in the above example:

   .. code-block:: postgres

      $ kubectl label nodes <node-name> cluster=sqream
   
   The following is an example of the correct output:

   .. code-block:: postgres
   
      $ [root@edk-rhl-1 kubespray]# kubectl label nodes eks-rhl-1 cluster=sqream
      $ node/eks-rhl-1 labeled
      $ [root@edk-rhl-1 kubespray]# kubectl label nodes eks-rhl-2 cluster=sqream
      $ node/eks-rhl-2 labeled
      $ [root@edk-rhl-1 kubespray]# kubectl label nodes eks-rhl-3 cluster=sqream
      $ node/eks-rhl-3 labeled

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
   
Copying Your Kubernetes Configuration API File to the Master Cluster Nodes
-------------------------------------------------  
After adding a SQream label on your Kubernetes cluster nodes, you must copy your Kubernetes configuration API file to your Master cluster nodes.

When the Kubernetes cluster installation is complete, an API configuration file is automatically created in the **.kube** folder of the root user. This file enables the **kubectl** command access Kubernetes' internal API service. Following this step lets you run **kubectl** commands from any node in the cluster.


.. warning:: You must perform this on the management server only!

**To copy your Kubernetes configuration API file to your Master cluster nodes:**

1. Create the **.kube** folder in the **local user** directory:

   .. code-block:: postgres
   
      $ mkdir /home/<local user>/.kube

2. Copy the configuration file from the root user directory to the <local user> directory:

   .. code-block:: postgres
   
      $ sudo cp /root/.kube/config /home/<local user>/.kube

3. Change the file owner from **root user** to the <local user>:

   .. code-block:: postgres
   
      $  sudo chown <local user>.<local user> /home/<local user>/.kube/config

4. Create the **.kube** folder in the other nodes located in the <local user> directory:

   .. code-block:: postgres
   
      $ ssh <local user>@<node name> mkdir .kube

5. Copy the configuration file from the management node to the other nodes:

   .. code-block:: postgres
   
      $ scp /home/<local user>/.kube/config <local user>@<node name>:/home/<local user>/.kube/
	  
6. Under local user on each server you copied **.kube** to, run the following command:

   .. code-block:: postgres
   
      $ sudo usermod -aG docker $USER

This grants the local user the necessary permissions to run Docker commands.

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

Creating an env_file in Your Home Directory
-------------------------------------------------
After copying your Kubernetes configuration API file to your Master cluster nodes, you must create an **env_file** in your home directory, and must set the VIP address as a variable.

.. warning:: You must perform this on the management server only!



**To create an env_file for local users in the user's home directory:**

1. Set a variable that includes the VIP IP address:

   .. code-block:: postgres
   
      $ export VIP_IP=<VIP IP>
	  
.. note:: If you use Kerberos, replace the ``KRB5_SERVER`` value with the IP address of your Kerberos server.
   
2. Do one of the following:

   * For local users:

     .. code-block:: postgres
   
        $ mkdir /home/$USER/.sqream
   
3. Make the following replacements to the **kubespray.settings.sh** file, verifying that the ``KRB5_SERVER`` parameter is set to your server IP:


   .. code-block:: postgres  
   
        $ cat <<EOF > /home/$USER/.sqream/env_file
        SQREAM_K8S_VIP=$VIP_IP
        SQREAM_ADMIN_UI_PORT=8080
        SQREAM_DASHBOARD_DATA_COLLECTOR_PORT=8100
        SQREAM_DATABASE_NAME=master
        SQREAM_K8S_ADMIN_UI=sqream-admin-ui
        SQREAM_K8S_DASHBOARD_DATA_COLLECTOR=dashboard-data-collector
        SQREAM_K8S_METADATA=sqream-metadata
        SQREAM_K8S_NAMESPACE=sqream
        SQREAM_K8S_PICKER=sqream-picker
        SQREAM_K8S_PROMETHEUS=prometheus
        SQREAM_K8S_REGISTRY_PORT=6000
        SQREAM_METADATA_PORT=3105
        SQREAM_PICKER_PORT=3108
        SQREAM_PROMETHEUS_PORT=9090
        SQREAM_SPOOL_MEMORY_RATIO=0.25
        SQREAM_WORKER_0_PORT=5000
        KRB5CCNAME=FILE:/tmp/tgt
        KRB5_SERVER=kdc.sq.com:<server IP>1
        KRB5_CONFIG_DIR=${        $ SQREAM_MOUNT_DIR}/krb5
        KRB5_CONFIG_FILE=${KRB5_CONFIG_DIR}/krb5.conf
        HADOOP_CONFIG_DIR=${        $ SQREAM_MOUNT_DIR}/hadoop
        HADOOP_CORE_XML=${HADOOP_CONFIG_DIR}/core-site.xml
        HADOOP_HDFS_XML=${HADOOP_CONFIG_DIR}/hdfs-site.xml
        EOF  

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
		




Creating a Base Kubernetes Namespace
------------------------------------
After creating an env_file in the user's home directory, you must create a base Kubernetes namespace.

You can create a Kubernetes namespace by running the following command:

.. code-block:: postgres
   
   $ kubectl create namespace sqream-init    
   
The following is an example of the correct output:

.. code-block:: postgres
   
   $ namespace/sqream-init created
   
Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

   
Pushing the **env_file** File to the Kubernetes Configmap
--------------------------------------   
After creating a base Kubernetes namespace, you must push the **env_file** to the Kubernetes configmap. You must push the **env_file** file to the Kubernetes **configmap** in the **sqream-init** namespace.

This is done by running the following command:

.. code-block:: postgres
   
   $ kubectl create configmap sqream-init -n sqream-init --from-env-file=/home/$USER/.sqream/env_file

The following is an example of the correct output:

.. code-block:: postgres
   
   $ configmap/sqream-init created


Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     


Installing the NVIDIA Docker2 Toolkit
-------------------------------------
After pushing the **env_file** file to the Kubernetes configmap, you must install the NVIDIA Docker2 Toolkit. The **NVIDIA Docker2 Toolkit** lets users build and run GPU-accelerated Docker containers, and must be run only on GPU servers. The NVIDIA Docker2 Toolkit includes a container runtime library and utilities that automatically configure containers to leverage NVIDIA GPUs.


Installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on CentOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

3. Verify that the **nvidia-docker2** package has been installed correctly:

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

For more information on installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on CentOS, see `NVIDIA Docker Installation - CentOS distributions <https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#centos-distributions-1>`_
     
Installing the NVIDIA Docker2 Toolkit on an x86_64 Bit Processor on Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
    
Modifying the Docker Daemon JSON File for GPU and Compute Nodes
-------------------------------------
After installing the NVIDIA Docker2 toolkit, you must modify the Docker daemon JSON file for GPU and Compute nodes.

Modifying the Docker Daemon JSON File for GPU Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**To modify the Docker daemon JSON file for GPU nodes:**     
     
1. Enable GPU and set HTTP access to the local Kubernetes Docker registry.

.. note:: The Docker daemon JSON file must be modified on all GPU nodes.

.. note:: Contact your IT department for a virtual IP.

2. Replace the ``VIP address`` with your assigned VIP address.

::

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

6. Apply the changes and restart Docker:

   .. code-block:: postgres
   
      $ systemctl daemon-reload && systemctl restart docker
      
7. Exit the root user:
 
  .. code-block:: postgres
   
     $ exit
	 
Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

      
Modifying the Docker Daemon JSON File for Compute Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You must follow this procedure only if you have a Compute node.

**To modify the Docker daemon JSON file for Compute nodes:**

1. Switch to a root user:

   .. code-block:: postgres
   
      $  sudo -i

2. Set a variable that includes a VIP address.

.. note:: Contact your IT department for a virtual IP.

3. Replace the ``VIP address`` with your assigned VIP address.

   .. code-block:: postgres
   
      $ cat <<EOF > /etc/docker/daemon.json
      $ {
      $    "insecure-registries": ["$VIP_IP:6000"]
      $ }
      $ EOF 

4. Restart the services:

   .. code-block:: postgres
   
      $ systemctl daemon-reload && systemctl restart docker

5. Exit the root user:
 
 
  .. code-block:: postgres
   
     $ exit

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
   
Installing the Nvidia-device-plugin Daemonset
----------------------------------------------
After modifying the Docker daemon JSON file for GPU or Compute Nodes, you must installing the Nvidia-device-plugin daemonset. The Nvidia-device-plugin daemonset is only relevant to GPU nodes.

**To install the Nvidia-device-plugin daemonset:**

1. Set ``nvidia.com/gpu`` to ``true`` on all GPU nodes:

.. code-block:: postgres
   
   $ kubectl label nodes <GPU node name> nvidia.com/gpu=true
      
2. Replace the *<GPU node name>* with your GPU node name:
   
   For a complete list of GPU node names, run the ``kubectl get nodes`` command.

   The following is an example of the correct output:
   
   .. code-block:: postgres
   
      $ [root@eks-rhl-1 ~]# kubectl label nodes eks-rhl-1 nvidia.com/gpu=true
      $ node/eks-rhl-1 labeled
      $ [root@eks-rhl-1 ~]# kubectl label nodes eks-rhl-2 nvidia.com/gpu=true
      $ node/eks-rhl-2 labeled
      $ [root@eks-rhl-1 ~]# kubectl label nodes eks-rhl-3 nvidia.com/gpu=true
      $ node/eks-rhl-3 labeled  

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     
   
Creating an Nvidia Device Plugin
----------------------------------------------   
After installing the Nvidia-device-plugin daemonset, you must create an Nvidia-device-plugin. You can create an Nvidia-device-plugin by running the following command 

.. code-block:: postgres
   
   $  kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/1.0.0-beta6/nvidia-device-plugin.yml
   
If needed, you can check the status of the Nvidia-device-plugin-daemonset pod status:

.. code-block:: postgres
   
   $ kubectl get pods -n kube-system -o wide | grep nvidia-device-plugin

The following is an example of the correct output:   

.. code-block:: postgres
   
   $ NAME                                       READY   STATUS    RESTARTS   AGE
   $ nvidia-device-plugin-daemonset-fxfct       1/1     Running   0          6h1m
   $ nvidia-device-plugin-daemonset-jdvxs       1/1     Running   0          6h1m
   $ nvidia-device-plugin-daemonset-xpmsv       1/1     Running   0          6h1m

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

Checking GPU Resources Allocatable to GPU Nodes
-------------------------------------
After creating an Nvidia Device Plugin, you must check the GPU resources alloctable to the GPU nodes. Each GPU node has records, such as ``nvidia.com/gpu:     <#>``. The ``#`` indicates the number of allocatable, or available, GPUs in each node.

You can output a description of allocatable resources by running the following command:

.. code-block:: postgres
   
   $ kubectl describe node | grep -i -A 7 -B 2 allocatable: 

The following is an example of the correct output:

.. code-block:: postgres
   
   $ Allocatable:
   $  cpu:                3800m
   $  ephemeral-storage:  94999346224
   $  hugepages-1Gi:      0
   $  hugepages-2Mi:      0
   $  memory:             15605496Ki
   $  nvidia.com/gpu:     1
   $  pods:               110 

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

Preparing the WatchDog Monitor
------------------------------
SQream's deployment includes installing two watchdog services. These services monitor Kuberenetes management and the server's storage network.

You can enable the storage watchdogs by adding entries in the **/etc/hosts** file on each server:

.. code-block:: postgres
   
   $ <address 1> k8s-node1.storage
   $ <address 2> k8s-node2.storage
   $ <address 3> k8s-node3.storage

The following is an example of the correct syntax:

.. code-block:: postgres
   
   $ 10.0.0.1 k8s-node1.storage
   $ 10.0.0.2 k8s-node2.storage
   $ 10.0.0.3 k8s-node3.storage

Go back to :ref:`Installing Your Kubernetes Cluster<install_kubernetes_cluster>`     

.. _installing_sqream_software:   

Installing the SQream Software
=================================
Once you've prepared the SQream environment for launching it using Kubernetes, you can begin installing the SQream software.

The **Installing the SQream Software** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
   
.. _getting_sqream_package:

Getting the SQream Package
--------------------------------
The first step in installing the SQream software is getting the SQream package. Please contact the SQream Support team to get the **sqream_k8s-nnn-DBnnn-COnnn-SDnnn-<arch>.tar.gz** tarball file.

This file includes the following values:

* **sqream_k8s-<nnn>** - the SQream installer version.
* **DB<nnn>** - the SQreamDB version.
* **CO<nnn>** - the SQream console version.
* **SD<nnn>** - the SQream Acceleration Studio version.
* **arch** - the server architecture. 

You can extract the contents of the tarball by running the following command:

.. code-block:: postgres
   
   $ tar -xvf sqream_k8s-1.0.15-DB2020.1.0.2-SD0.7.3-x86_64.tar.gz
   $ cd sqream_k8s-1.0.15-DB2020.1.0.2-SD0.7.3-x86_64
   $ ls

Extracting the contents of the tarball file generates a new folder with the same name as the tarball file.

The following shows the output of the extracted file:

.. code-block:: postgres

   drwxrwxr-x. 2 sqream sqream    22 Jan 27 11:39 license
   lrwxrwxrwx. 1 sqream sqream    49 Jan 27 11:39 sqream -> .sqream/sqream-sql-v2020.3.1_stable.x86_64/sqream
   -rwxrwxr-x. 1 sqream sqream  9465 Jan 27 11:39 sqream-install
   -rwxrwxr-x. 1 sqream sqream 12444 Jan 27 11:39 sqream-start

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`

Setting Up and Configuring Hadoop
--------------------------------
After getting the SQream package, you can set up and configure Hadoop by configuring the **keytab** and **krb5.conf** files.

.. note:: You only need to configure the **keytab** and **krb5.conf** files if you use Hadoop with Kerberos authentication.


**To set up and configure Hadoop:**

1. Contact IT for the **keytab** and **krb5.conf** files.

::

2. Copy both files into the respective empty **.hadoop/** and **.krb5/** directories:

.. code-block:: postgres
   
   $ cp hdfs.keytab krb5.conf .krb5/
   $ cp core-site.xml hdfs-site.xml .hadoop/

The SQream installer automatically copies the above files during the installation process.

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`

Starting a Local Docker Image Registry
--------------------------------
After getting the SQream package, or (optionally) setting up and configuring Hadoop, you must start a local Docker image registry. Because Kubernetes is based on Docker, you must start the local Docker image registry on the host's shared folder. This allows all hosts to pull the SQream Docker images.

**To start a local Docker image registry:**

1. Create a Docker registry folder:

   .. code-block:: postgres
   
      $ mkdir <shared path>/docker-registry/
   
2. Set the ``docker_path`` for the Docker registry folder:

   .. code-block:: postgres
   
      $ export docker_path=<path>
   
3. Apply the **docker-registry** service to the cluster:

   .. code-block:: postgres
   
      $ cat .k8s/admin/docker_registry.yaml | envsubst | kubectl create -f -
   
   The following is an example of the correct output:

   .. code-block:: postgres
   
      namespace/sqream-docker-registry created
      configmap/sqream-docker-registry-config created
      deployment.apps/sqream-docker-registry created
      service/sqream-docker-registry created

4. Check the pod status of the **docker-registry** service:

   .. code-block:: postgres
   
      $ kubectl get pods -n sqream-docker-registry
   
The following is an example of the correct output:

   .. code-block:: postgres
   
       NAME                                      READY   STATUS    RESTARTS   AGE
      sqream-docker-registry-655889fc57-hmg7h   1/1     Running   0          6h40m

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`

Installing the Kubernetes Dashboard
--------------------------------
After starting a local Docker image registry, you must install the Kubernetes dashboard. The Kubernetes dashboard lets you see the Kubernetes cluster, nodes, services, and pod status.

**To install the Kubernetes dashboard:**

1. Apply the **k8s-dashboard** service to the cluster:

   .. code-block:: postgres
   
      $ kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
   
   The following is an example of the correct output:

   .. code-block:: postgres
   
      namespace/kubernetes-dashboard created
      serviceaccount/kubernetes-dashboard created
      service/kubernetes-dashboard created
      secret/kubernetes-dashboard-certs created
      secret/kubernetes-dashboard-csrf created
      secret/kubernetes-dashboard-key-holder created
      configmap/kubernetes-dashboard-settings created
      role.rbac.authorization.k8s.io/kubernetes-dashboard created
      clusterrole.rbac.authorization.k8s.io/kubernetes-dashboard created
      rolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
      clusterrolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
      deployment.apps/kubernetes-dashboard created
      service/dashboard-metrics-scraper created
      deployment.apps/dashboard-metrics-scraper created

2. Grant the user external access to the Kubernetes dashboard:

   .. code-block:: postgres
   
      $ cat .k8s/admin/kubernetes-dashboard-svc-metallb.yaml | envsubst | kubectl create -f -
   
   The following is an example of the correct output:

   .. code-block:: postgres
      
      service/kubernetes-dashboard-nodeport created
   
3. Create the ``cluster-admin-sa.yaml`` file:

   .. code-block:: postgres
   
      $ kubectl create -f .k8s/admin/cluster-admin-sa.yaml
   
   The following is an example of the correct output:

   .. code-block:: postgres
      
      clusterrolebinding.rbac.authorization.k8s.io/cluster-admin-sa-cluster-admin created

4. Check the pod status of the **K8s-dashboard** service:

   .. code-block:: postgres
   
      $ kubectl get pods -n kubernetes-dashboard
   
   The following is an example of the correct output:

   .. code-block:: postgres
   
      NAME                                         READY   STATUS    RESTARTS   AGE
      dashboard-metrics-scraper-6b4884c9d5-n8p57   1/1     Running   0          4m32s
      kubernetes-dashboard-7b544877d5-qc8b4        1/1     Running   0          4m32s

5. Obtain the **k8s-dashboard** access token:

   .. code-block:: postgres
   
      $ kubectl -n kube-system describe secrets cluster-admin-sa-token
   
   The following is an example of the correct output:
 
   .. code-block:: postgres
     
      Name:         cluster-admin-sa-token-rbl9p
      Namespace:    kube-system
      Labels:       <none>
      Annotations:  kubernetes.io/service-account.name: cluster-admin-sa
                    kubernetes.io/service-account.uid: 81866d6d-8ef3-4805-840d-58618235f68d

      Type:  kubernetes.io/service-account-token

      Data
      ====
      ca.crt:     1025 bytes
      namespace:  11 bytes
      token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IjRMV09qVzFabjhId09oamQzZGFFNmZBeEFzOHp3SlJOZWdtVm5lVTdtSW8ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJjbHVzdGVyLWFkbWluLXNhLXRva2VuLXJibDlwIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImNsdXN0ZXItYWRtaW4tc2EiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiI4MTg2NmQ2ZC04ZWYzLTQ4MDUtODQwZC01ODYxODIzNWY2OGQiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06Y2x1c3Rlci1hZG1pbi1zYSJ9.mNhp8JMr5y3hQ44QrvRDCMueyjSHSrmqZcoV00ZC7iBzNUqh3n-fB99CvC_GR15ys43jnfsz0tdsTy7VtSc9hm5ENBI-tQ_mwT1Zc7zJrEtgFiA0o_eyfYZOARdhdyFEJg84bzkIxJFPKkBWb4iPWU1Xb7RibuMCjNTarZMZbqzKYfQEcMZWJ5UmfUqp-HahZZR4BNbjSWybs7t6RWdcQZt6sO_rRCDrOeEJlqKKjx4-5jFZB8Du_0kKmnw2YJmmSCEOXrpQCyXIiZJpX08HyDDYfFp8IGzm61arB8HDA9dN_xoWvuz4Cj8klUtTzL9effJJPjHJlZXcEqQc9hE3jw

6. Navigate to ``https://<VIP address>:5999``.

::
   
7. Select the **Token** radio button, paste the token from the previous command output, and click **Sign in**.
  
The Kubernetes dashboard is displayed.

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`

Installing the SQream Prometheus Package
--------------------------------
After installing the Kubernetes dashboard, you must install the SQream Prometheus package. To properly monitor the host and GPU statistics the **exporter service** must be installed on each Kubernetes cluster node.

This section describes how to install the following:

* **node_exporter** - collects host data, such as CPU memory usage.
* **nvidia_exporter** - collects GPU utilization data. 


.. note:: The steps in this section must be done on **all** cluster nodes.

To install the **sqream-prometheus** package, you must do the following:

1. :ref:`Install the exporter service <install_exporter_service>`

::

2. :ref:`Check the exporter service <check_exporter_status>`

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`


.. _install_exporter_service:

Installing the Exporter Service
~~~~~~~~~~~~~~~~~~~~~~~~

**To install the exporter service:**

1. Create a user and group that will be used to run the exporter services: 

   .. code-block:: console

      $ sudo groupadd --system prometheus && sudo useradd -s /sbin/nologin --system -g prometheus prometheus

2. Extract the **sqream_exporters_prometheus.0.1.tar.gz** file: 

   .. code-block:: console

      $ cd .prometheus
      $ tar -xf sqream_exporters_prometheus.0.1.tar.gz

3. Copy the exporter software files to the **/usr/bin** directory:

   .. code-block:: console

      $ cd  sqream_exporters_prometheus.0.1
      $ sudo cp node_exporter/node_exporter /usr/bin/
      $ sudo cp nvidia_exporter/nvidia_exporter /usr/bin/

4. Copy the exporters service file to the **/etc/systemd/system/** directory:

   .. code-block:: console

      $ sudo cp services/node_exporter.service /etc/systemd/system/
      $ sudo cp services/nvidia_exporter.service /etc/systemd/system/

5. Set the permission and group of the service files:

   .. code-block:: console

      $ sudo chown prometheus:prometheus /usr/bin/node_exporter
      $ sudo chmod u+x /usr/bin/node_exporter
      $ sudo chown prometheus:prometheus /usr/bin/nvidia_exporter
      $ sudo chmod u+x /usr/bin/nvidia_exporter

6. Reload the services:

   .. code-block:: console

      $ sudo systemctl daemon-reload

7. Start both services and set them to start when the server is booted up:

   * Node_exporter:

     .. code-block:: console

        $ sudo systemctl start node_exporter && sudo systemctl enable node_exporter

   * Nvidia_exporter:

     .. code-block:: console

        $ sudo systemctl start nvidia_exporter && sudo systemctl enable nvidia_exporter
		

		
.. _check_exporter_status:

Checking the Exporter Status
~~~~~~~~~~~~~~~~~~~~~~~~
After installing the **exporter** service, you must check its status.

You can check the exporter status by running the following command:

.. code-block:: console

   $ sudo systemctl status node_exporter && sudo systemctl status nvidia_exporter

Go back to :ref:`Installing Your SQream Software<installing_sqream_software>`


.. _running_sqream_install_service:
   
Running the Sqream-install Service
================================
The **Running the Sqream-install Service** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Installing Your License
--------------------------------
After install the SQream Prometheus package, you must install your license.

**To install your license:**

1. Copy your license package to the sqream **/license** folder.

.. note:: You do not need to untar the license package after copying it to the **/license** folder because the installer script does it automatically.

The following flags are **mandatory** during your first run: 

.. code-block:: console

   $ sudo ./sqream-install -i -k -m <path to sqream cluster> 

.. note:: If you cannot run the script with **sudo**, verify that you have the right permission (**rwx** for the user) on the relevant directories (config, log, volume, and data-in directories).

Go back to :ref:`Running the SQream_install Service<running_sqream_install_service>`.

Changing Your Data Ingest Folder
--------------------------------
After installing your license, you must change your data ingest folder.

You can change your data ingest folder by running the following command:

.. code-block:: console

   $ sudo ./sqream-install -d /media/nfs/sqream/data_in   

Go back to :ref:`Running the SQream_install Service<running_sqream_install_service>`.
   
Checking Your System Settings
--------------------------------
After changing your data ingest folder, you must check your system settings.

The following command shows you all the variables that your SQream system is running with:

.. code-block:: console

   $ ./sqream-install -s

After optionally checking your system settings, you can use the **sqream-start** application to control your Kubernetes cluster.

Go back to :ref:`Running the SQream_install Service<running_sqream_install_service>`.
      
SQream Installation Command Reference
--------------------------------
If needed, you can use the **sqream-install** flag reference for any needed flags by typing:

.. code-block:: console

   $ ./sqream-install --help
   
The following shows the **sqream--install** flag descriptions:
   
.. list-table:: 
   :widths: 22 59 25
   :header-rows: 1
   
   * - Flag
     - Function
     - Note
   * - **-i**
     - Loads all the software from the hidden **.docker** folder.
     - Mandatory
   * - **-k**
     - Loads the license package from the **/license** directory.
     - Mandatory
   * - **-m**
     - Sets the relative path for all SQream folders under the shared filesystem available from all nodes (sqreamdb, config, logs and data_in). No other flags are required if you use this flag (such as c, v, l or d).
     - Mandatory
   * - **-c**
     - Sets the path where to write/read SQream configuration files from. The default is **/etc/sqream/**.
     - Optional
   * - **-v**
     - Shows the location of the SQream cluster. ``v`` creates a cluster if none exist, and mounts it if does.
     - Optional
   * - **-l**
     - Shows the location of the SQream system startup logs. The logs contain startup and Docker logs. The default is **/var/log/sqream/**.
     - Optional	 
   * - **-d**
     - Shows the folder containing data that you want to import into or copy from SQream.
     - Optional	 
   * - **-n** <Namespace>
     - Sets the Kubernetes namespace. The default is **sqream**.
     - Optional
   * - **-N** <Namespace>
     - Deletes a specific Kubernetes namespace and sets the factory default namespace (sqream).
     - Optional
   * - **-f**
     - Overwrite existing folders and all files located in mounted directories.
     - Optional
   * - **-r**
     - Resets the system configuration. This flag is run without any other variables.
     - Optional
   * - **-s**
     - Shows the system settings.
     - Optional
   * - **-e**
     - Sets the Kubernetes cluster's virtual IP address.
     - Optional
   * - **-h**
     - Help, shows all available flags.
     - Optional

Go back to :ref:`Running the SQream_install Service<running_sqream_install_service>`.
   
Controlling Your Kubernetes Cluster Using SQream Flags
--------------------------------
You can control your Kubernetes cluster using SQream flags.

The following command shows you the available Kubernetes cluster control options:

.. code-block:: console

   $ ./sqream-start -h

The following describes the **sqream-start** flags:

.. list-table::
   :widths: 22 59 25
   :header-rows: 1
   
   * - Flag
     - Function
     - Note
   * - **-s**
     - Starts the sqream services, starting metadata, server picker, and workers. The number of workers started is based on the number of available GPU’s.
     - Mandatory	 
   * - **-p**
     - Sets specific ports to the workers services. You must enter the starting port for the sqream-start application to allocate it based on the number of workers.
     - 
   * - **-j**
     - Uses an external .json configuration file. The file must be located in the **configuration** directory.
     - The workers must each be started individually.	 
   * - **-m**
     - Allocates worker spool memory.
     - The workers must each be started individually.	 
   * - **-a**
     - Starts the SQream Administration dashboard and specifies the listening port.
     - 	 
   * - **-d**
     - Deletes all running SQream services.
     - 	 
   * - **-h**
     - Shows all available flags.
     - Help

Go back to :ref:`Running the SQream_install Service<running_sqream_install_service>`.

.. _using_sqream_start_commands:
   
Using the sqream-start Commands
=======================
In addition to controlling your Kubernetes cluster using SQream flags, you can control it using **sqream-start** commands.

The **Using the sqream-start Commands** section describes the following:

.. contents:: 
   :local:
   :depth: 1

Starting Your SQream Services
------------------------
You can run the **sqream-start** command with the **-s** flag to start SQream services on all available GPU's:

.. code-block:: console

   $ sudo ./sqream-start -s

This command starts the SQream metadata, server picker, and sqream workers on all available GPU’s in the cluster.

The following is an example of the correct output:

.. code-block:: console

   ./sqream-start -s
   Initializing network watchdogs on 3 hosts...
   Network watchdogs are up and running

   Initializing 3 worker data collectors ...
   Worker data collectors are up and running

   Starting Prometheus ...
   Prometheus is available at 192.168.5.100:9090

   Starting SQream master ...
   SQream master is up and running

   Starting up 3 SQream workers ...
   All SQream workers are up and running, SQream-DB is available at 192.168.5.100:3108	 
   All SQream workers are up and running, SQream-DB is available at 192.168.5.100:3108	 


Go back to :ref:`Using the SQream-start Commands<using_sqream_start_commands>`.
	 
Starting Your SQream Services in Split Mode
------------------------
Starting SQream services in split mode refers to running multiple SQream workers on a single GPU. You can do this by running the **sqream-start** command with the **-s** and **-z** flags. In addition, you can define the amount of hosts to run the multiple workers on. In the example below, the command defines to run the multiple workers on three hosts.

**To start SQream services in split mode:**

1. Run the following command:

.. code-block:: console

   $ ./sqream-start -s -z 3

This command starts the SQream metadata, server picker, and sqream workers on a single GPU for three hosts:

The following is an example of the correct output:

.. code-block:: console

   Initializing network watchdogs on 3 hosts...
   Network watchdogs are up and running

   Initializing 3 worker data collectors ...
   Worker data collectors are up and running

   Starting Prometheus ...
   Prometheus is available at 192.168.5.101:9090

   Starting SQream master ...
   SQream master is up and running

   Starting up 9 SQream workers over <#> available GPUs ...
   All SQream workers are up and running, SQream-DB is available at 192.168.5.101:3108
   
2. Verify all pods are properly running in k8s cluster (**STATUS** column):

.. code-block:: console

   kubectl -n sqream get pods                                               

   NAME                                          READY   STATUS             RESTARTS   AGE
   prometheus-bcf877867-kxhld                    1/1     Running            0          106s
   sqream-metadata-fbcbc989f-6zlkx               1/1     Running            0          103s
   sqream-picker-64b8c57ff5-ndfr9                1/1     Running            2          102s
   sqream-split-workers-0-1-2-6bdbfbbb86-ml7kn   1/1     Running            0          57s
   sqream-split-workers-3-4-5-5cb49d49d7-596n4   1/1     Running            0          57s
   sqream-split-workers-6-7-8-6d598f4b68-2n9z5   1/1     Running            0          56s
   sqream-workers-start-xj75g                    1/1     Running            0          58s
   watchdog-network-management-6dnfh             1/1     Running            0          115s
   watchdog-network-management-tfd46             1/1     Running            0          115s
   watchdog-network-management-xct4d             1/1     Running            0          115s
   watchdog-network-storage-lr6v4                1/1     Running            0          116s
   watchdog-network-storage-s29h7                1/1     Running            0          116s
   watchdog-network-storage-sx9mw                1/1     Running            0          116s
   worker-data-collector-62rxs                   0/1     Init:0/1           0          54s
   worker-data-collector-n8jsv                   0/1     Init:0/1           0          55s
   worker-data-collector-zp8vf                   0/1     Init:0/1           0          54s	 

Go back to :ref:`Using the SQream-start Commands<using_sqream_start_commands>`.
		 
Starting the Sqream Studio UI
--------------------------------
You can run the following command the to start the SQream Studio UI (Editor and Dashboard):

.. code-block:: console

   $ ./sqream-start -a

The following is an example of the correct output:

.. code-block:: console

   $ ./sqream-start -a
   Please enter USERNAME:
   sqream
   Please enter PASSWORD:
   ******
   Please enter port value or press ENTER to keep 8080:

   Starting up SQream Admin UI...
   SQream admin ui is available at 192.168.5.100:8080

Go back to :ref:`Using the SQream-start Commands<using_sqream_start_commands>`.
	   
Stopping the SQream Services
--------------------------------
You can run the following command to stop all SQream services:

.. code-block:: console

   $ ./sqream-start -d

The following is an example of the correct output:

.. code-block:: console

   $ ./sqream-start -d
   $ Cleaning all SQream services in sqream namespace ...
   $ All SQream service removed from sqream namespace

Go back to :ref:`Using the SQream-start Commands<using_sqream_start_commands>`.
	   
Advanced sqream-start Commands
--------------------------------
Controlling Your SQream Spool Size
~~~~~~~~~~~~~~~~~~~~~~~~
If you do not specify the SQream spool size, the console automatically distributes the available RAM between all running workers.

You can define a specific spool size by running the following command:

.. code-block:: console

   $ ./sqream-start -s -m 4

Using a Custom .json File
~~~~~~~~~~~~~~~~~~~~~~~~
You have the option of using your own .json file for your own custom configurations. Your .json file must be placed within the path mounted in the installation. SQream recommends placing your .json file in the **configuration** folder.

The SQream console does not validate the integrity of external .json files.

You can use the following command (using the ``j`` flag) to set the full path of your .json file to the configuration file:

.. code-block:: console

   $ ./sqream-start -s -f <full path>.json

This command starts one worker with an external configuration file.

.. note:: The configuration file must be available in the shared configuration folder.


Checking the Status of the SQream Services
~~~~~~~~~~~~~~~~~~~~~~~~
You can show all running SQream services by running the following command:

.. code-block:: console

   $ kubectl get pods -n <namespace> -o wide

This command shows all running services in the cluster and which nodes they are running in.

Go back to :ref:`Using the SQream-start Commands<using_sqream_start_commands>`.
	
Upgrading Your SQream Version
================================
The **Upgrading Your SQream Version** section describes the following:

.. contents:: 
   :local:
   :depth: 1
   
Before Upgrading Your System
----------------------------
Before upgrading your system you must do the following:

1. Contact SQream support for a new SQream package tarball file.

::

2. Set a maintenance window.


.. note:: You must stop the system while upgrading it.


Upgrading Your System
----------------------------
After completing the steps in **Before Upgrading Your System** above, you can upgrade your system.

**To upgrade your system:**

1. Extract the contents of the tarball file that you received from SQream support. Make sure to extract the contents to the same directory as in :ref:`getting_sqream_package` and for the same user:

  .. code-block:: console

     $ tar -xvf sqream_installer-2.0.5-DB2019.2.1-CO1.6.3-ED3.0.0-x86_64/
     $ cd sqream_installer-2.0.5-DB2019.2.1-CO1.6.3-ED3.0.0-x86_64/ 
 
2. Start the upgrade process run the following command: 

  .. code-block:: console

     $ ./sqream-install -i
   
The upgrade process checks if the SQream services are running and will prompt you to stop them.

3. Do one of the following:

   * Stop the upgrade by writing ``No``.
   * Continue the upgrade by writing ``Yes``.

If you continue upgrading, all running SQream workers (master and editor) are stopped. When all services have been stopped, the new version is loaded. 


.. note:: SQream periodically upgrades its metadata structure. If an upgrade version includes an upgraded metadata service, an approval request message is displayed. This approval is required to finish the upgrade process. Because SQream supports only specific metadata versions, all SQream services must be upgraded at the same time.


4. When SQream has successfully upgraded, load the SQream console and restart your services.

For questions, contact SQream Support.  
