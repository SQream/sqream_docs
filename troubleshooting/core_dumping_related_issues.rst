.. _core_dumping_related_issues:

***********************
Core Dumping Related Issues
***********************

The **Core Dumping Related Issues** page describes the troubleshooting procedure to be followed if all parameters have been configured correctly, but the cores have not been created.

**To troubleshoot core dumping:**

1. Reboot the server.

2. Verify that you have folder permissions:

   .. code-block:: console

      $ sudo chmod -R 777 /tmp/core_dumps   
   
3. Verify that the limits have been set correctly:

   .. code-block:: console

      $ ulimit -c

   If all parameters have been configured correctly, the correct output is:

   .. code-block:: console

      $ unlimited	

4. If all parameters have been configured correctly, but running **ulimit -c** outputs **0**, run the following:

   .. code-block:: console

      $ sudo vim /etc/profile

5. Search for line and tag it with the **hash** symbol:

   .. code-block:: console

      $ ulimit -S -c 0 > /dev/null 2>&1	 
	  

6. If the line is not found in **/etc/profile** directory, do the following:	  
	  
   a. Run the following command:

      .. code-block:: console

         $ sudo vim /etc/init.d/functions

   b. Search for the following:
   
      .. code-block:: console

         $ ulimit -S -c ${DAEMON_COREFILE_LIMIT:-0} >/dev/null 2>&1

   c. If the line is found, tag it with the **hash** symbol and reboot the server |icon-new_2022.1|.

   
  
  
.. |icon-new_2022.1| image:: /_static/images/new_2022.1.png
   :align: middle
   
  
  