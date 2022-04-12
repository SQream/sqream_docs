.. _installing_sqream_on_the_cloud:

*************************
Installing SQream on the Cloud
*************************

.. image:: /_static/images/in_progress.png
  :width: 400

The **SQream on the Cloud** page describes the following:

.. contents::
   :local:
   :depth: 1


  
Raising a Machine
===============  
  
step 1:

1. access Jenkins: http://192.168.0.128/view.

#. Click Deployment tab.

#. Click AWS-CLoud-allocator.

#. Click Build with Parameters.

#. fill in the following details:

   #. From cloud_provider, select Amazon.

   #. action-create

   #. state-choose by customer  location

   #. imageList-ask DevOps which image to use, for now:

#. DiskSize-change 50 to 200

Note: projects-name of the POC in low case, no spaces, no underscores.

#. EIP - Assigns the user a fixed External IP.

#. Bucket  (if check- new bucket with a project name will be created)

#. instanceType-g4dn.8xlarge

4. click build

The build is displayed in the Build History seciton on the left.

Connecting to the Machine
===============

step 2:
connect with ssh to the machine in the report

example:


 


ssh -i sq_ohio.pem ec2-user@3.130.184.223
 ask DevOps to get the pem file for the key name in the report


sudo su - sqream
stop monit:


sudo systemctl stop monit
 


cd /etc/sqream
edit sqream1_config.json and set bucket name

 


vim sqream1_config.json
change these flags:


 "tablespaceURL": "s3://totalplaypoc/",
    "tempPath": "s3://totalplaypoc/",
create a new license :

http://jenkins.host-98.sq.l/view/License%20Jobs/job/SQream_License_Generator_New/

replace license.enc under /etc/SQream in the new license

Procedure
===============

step 3:
copy version from your Linux machine to AWS instance:


scp -i sq_ohio.pem sqream-db-v2021.1.2_poc_tp1.cpu-generic.pascal.cuda-9.1.el7.centos.x86_64.tar.gz ec2-user@3.130.184.223:~/
sudo mv sqream-db-v2021.1.2_poc_tp1.cpu-generic.pascal.cuda-9.1.el7.centos.x86_64.tar.gz /home/sqream/
su - sqream
sudo chown sqream:sqream sqream-db-v2021.1.2_poc_tp1.cpu-generic.pascal.cuda-9.1.el7.centos.x86_64.tar.gz 
ls -l //to check that doesnt exist in /home/sqream sqream folder
 

Upgrade SQream version:


mv sqream sqream-db-v2021.1.2_poc_tp1
tar -xf sqream-db-v2021.1.2_poc_tp1
sudo mv sqream-db-v2021.1.2_poc_tp1 /usr/local/
cd /usr/local/
sudo chown -R sqream:sqream /usr/local/sqream-db-v2021.1.2_poc_tp1
sudo rm sqream
sudo ln -s sqream-db-v2021.1.2_poc_tp1 sqream
cd sqream/bin/
sudo monit stop all
./upgrade_storage /home/sqream/sqream_storage/
sudo monit start all
sudo systemctl daemon-reload
sudo reboot
step 4:
Connect to SQream editor on http://3.130.184.223:8080/ (with machine IP from the report)

 

step 5:
Turn off the machine.

The cost of the machines is high so it is important to turn them off immediately after use.

Access Jenkins from the Cloud-allocator.

Your last build is displayed in the Under Permalinks section, you can see your last build.
Click on the most current Last build (located at the top of the list), as shown below



 

Click on Rebuild.

Verify that the cloud_provaider is Amazon.

Change the action to STOP.

Click Rebuild.

Note: You also can search for your name in the Build History field for the entire machines you have created. You can select a machine from this list.

You can also turn on machines by changing the action to START.

Troubleshooting
===============

.. contents::
   :local:
   :depth: 1


Build Fails
************
1. Click **Console Output**.



