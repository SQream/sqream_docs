.. _configuring_sqream:

**************************
Configuring SQream
**************************
The **Configuring SQream** page describes SQream’s method for configuring your instance of SQream and includes the following topics:

.. contents:: 
   :local:
   :depth: 1

	 
Session-Based Configuration
==============================
.. contents:: 
   :local:
   :depth: 1
   
Session-based configurations are not persistent and are deleted when your session ends. This method enables you to modify all required configurations while avoiding conflicts between flag attributes modified on different devices at different points in time.

The **SET flag_name** command is used to modify flag attributes. Any modifications you make with the **SET flag_name** command apply only to your open session, and are not saved when it ends

For example, when the query below has completed executing, the values configured will be restored to its previous setting: 

.. code-block:: console
   
   set spoolMemoryGB=700;
   select * from table a where date='2021-11-11'
