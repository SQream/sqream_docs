.. _configuring_sqream:

****************
Configuring BLUE
****************

Session-based configurations are not persistent and are deleted when your session ends. This method enables you to modify all required configurations while avoiding conflicts between flag attributes modified on different devices at different points in time.

The ``SET <flag_name>`` command is used to modify flag attributes. Any modifications you make with this command, apply only to your open session, and are not saved when it ends.

For example, when the query below has completed being executed, the values configured will be restored to its previous setting: 

.. code-block:: none
   
   set spoolMemoryGB=700;
   select * from table a where date='2021-11-11'
