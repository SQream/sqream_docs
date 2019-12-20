.. _monitoring:

***********************
Monitoring
***********************

monitoring sqream:

monitoring alerts
watching processes

GPU temperature  
nvidia-smi  - Temp 
Temp > 85 
GPU usage 
nvidia-smi -  GPU-Util 
For Information only 
Nice to put on graph to track system usage 
Processes - sqreamd 
ps aux | grep sqreamd 
Alert if one or more sqreamd processes are down 
Process - metadata 
ps aux | grep metadata 
Alert if down 
Process – server picker 
ps aux | grep server_picker 
Alert if down 
Disk Space – Storage 
df -h 
Alert if storage usage > 75% 
Disk Space – Cluster 
du -sh /SQream/sqream_cluster/sqreamdb 
For Information only 
Nice to put on graph to track full DB growth 
Disk Space – leveldb 
du -sh 
/SQream/sqream_cluster/leveldb
For Information only 
Nice to put on graph to track system usage 
Disk Space – DB usage 
du -sh 
/SQream/sqream_cluster/sqreamdb/datab ases/ 
For Information only 
Nice to put on graph to track specific platform db growth 
Server Disk Space 
df -h 
Alert if disk usage > 75% 
Memory Consumption 
free –g 
Alert if Mem usage > 95% 


monitoring a running statement
select show_node_info(statement_id);
try to explain how to actually use it (if this is even possible)

monitoring the activity of the system


show_cluster_nodes

show_conf

backup_storage?

show_server_status()

stop_statement()


show_locks

how do you release locks

sqream_version

what else?

viewing the usage history - link to the logs



.. toctree::
   :maxdepth: 2
   :caption: In this section:
   :glob:

