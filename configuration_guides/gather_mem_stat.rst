.. _gather_mem_stat:

*************************
Monitoring and Printing Pinned Allocation Reports
*************************
The ``gatherMemStat`` flag monitors all pinned allocations and all **memcopies** to and from a device, and prints a report of pinned allocations that were not **memcopied** to and from the device using the **dump_pinned_misses** utility function.

The following describes the ``gatherMemStat`` flag:

* **Data type** - boolean
* **Default value** - ``FALSE``