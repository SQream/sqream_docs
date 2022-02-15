.. _installing_dashboard_data_collector:



***********************
Installing the Dashboard Data Collector
***********************

Installing the Dashboard Data Collector
^^^^^^^^^^^^^^^
After accessing the Prometheus user interface, you can install the **Dashboard Data Collector**. You must install the Dashboard Data Collector to enable the Dashboard in Studio.

.. note:: Before installing the Dashboard Data collector, verify that Prometheus has been installed and configured for the cluster.

**To install the Dashboard Data Collector:**

1. Store the Data Collector Package obtained from `SQream Artifactory <http://artifactory.host-98.sq.l/artifactory/dashboard/data_collector/tarball>`_.

  ::

2. Extract and rename the package:

   .. code-block:: console
   
      $ tar -xvf dashboard-data-collector-0.5.2.tar.gz 
      $ mv package dashboard-data-collector
	  
3. Change your directory to the location of the package folder: 

   .. code-block:: console
   
      $ cd dashboard-data-collector

4. Set up the data collection by modifying the SQream and Data Collector IPs, ports, user name, and password according to the cluster:

   .. code-block:: console
   
      $ npm run setup -- \
      $ 	--host=127.0.0.1 \
      $ 	--port=3108 \
      $ 	--database=master \
      $ 	--is-cluster=true \
      $ 	--service=sqream \
      $ 	--dashboard-user=sqream \
      $ 	--dashboard-password=sqream \
      $ 	--prometheus-url=http://127.0.0.1:9090/api/v1/query

5. Debug the Data Collector:

   .. code-block:: console
   
      $ npm start

   A json file is generated in the log, as shown below:   

   .. code-block:: console
   
      $ {
      $   "machines": [
      $     {
      $       "machineId": "dd4af489615",
      $       "name": "Server 0",
      $       "location": "192.168.4.94",
      $       "totalMemory": 31.19140625,
      $       "gpus": [
      $         {
      $           "gpuId": "GPU-b17575ec-eeba-3e0e-99cd-963967e5ee3f",
      $           "machineId": "dd4af489615",
      $           "name": "GPU 0",
      $           "totalMemory": 3.9453125
      $         }
      $       ],
      $       "workers": [
      $         {
      $           "workerId": "sqream_01",
      $           "gpuId": "",
      $           "name": "sqream_01"
      $         }
      $       ],
      $       "storageWrite": 0,
      $       "storageRead": 0,
      $       "freeStorage": 0
      $     },
      $     {
      $       "machineId": "704ec607174",
      $       "name": "Server 1",
      $       "location": "192.168.4.95",
      $       "totalMemory": 31.19140625,
      $       "gpus": [
      $         {
      $           "gpuId": "GPU-8777c14f-7611-517a-e9c7-f42eeb21700b",
      $           "machineId": "704ec607174",
      $           "name": "GPU 0",
      $           "totalMemory": 3.9453125
      $         }
      $       ],
      $       "workers": [
      $         {
      $           "workerId": "sqream_02",
      $           "gpuId": "",
      $           "name": "sqream_02"
      $         }
      $       ],
      $       "storageWrite": 0,
      $       "storageRead": 0,
      $       "freeStorage": 0
      $     }
      $   ],
      $   "clusterStatus": true,
      $   "storageStatus": {
      $     "dataStorage": 49.9755859375,
      $     "totalDiskUsage": 52.49829018075231,
      $     "storageDetails": {
      $       "data": 0,
      $       "freeData": 23.7392578125,
      $       "tempData": 0,
      $       "deletedData": 0,
      $       "other": 26.236328125
      $     },
      $     "avgThroughput": {
      $       "read": 0,
      $       "write": 0
      $     },
      $     "location": "/"
      $   },
      $   "queues": [
      $     {
      $       "queueId": "sqream",
      $       "name": "sqream",
      $       "workerIds": [
      $         "sqream_01",
      $         "sqream_02"
      $       ]
      $     }
      $   ],
      $   "queries": [],
      $   "collected": true,
      $   "lastCollect": "2021-11-17T12:46:31.601Z"
      $ }
	  
.. note:: Verify that all machines and workers are correctly registered.


6. Press **CTRL + C** to stop ``npm start``.

  ::


7. Start the Data Collector with the ``pm2`` service:

   .. code-block:: console
   
      $ pm2 start ./index.js --name=dashboard-data-collector
	  
8. Add the following parameter to the SQream Studio setup defined in :ref:`Step 4<add_parameter_20201>` in **Installing Studio** below.

   .. code-block:: console
   
      --data-collector-url=http://127.0.0.1:8100/api/dashboard/data

Back to :ref:`Installing Studio on a Stand-Alone Server<install_studio_top>`
