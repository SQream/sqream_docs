.. _identifying_configuration_issues:

***********************
Identifying Configuration Issues
***********************

The **Troubleshooting Common Issues** page describes how to troubleshoot the following common issues:

.. toctree::
   :maxdepth: 2
   :glob:
   :titlesonly:


Starting a SQream DB temporarily (not as part of a cluster, with default settings) can be helpful in identifying configuration issues.

Example:

.. code-block:: console

   $ sqreamd /home/rhendricks/raviga_database 0 5000 /home/sqream/.sqream/license.enc

.. tip:: 
   
   * Using ``nohup`` and ``&`` sends SQream DB to run in the background.
   
   * 
      It is safe to stop SQream DB at any time using ``kill``. No partial data or data corruption should occur when using this method to stop the process.
      
      .. code-block:: console
      
         $ kill -9 $SQREAM_PID