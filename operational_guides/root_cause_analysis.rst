.. _root_cause_analysis:

*******************
Root Cause Analysis
*******************

The Root Cause Analysis (RCA) service enhances observability, enabling shorter investigation times and facilitating both high-level and detailed drill-downs.

.. contents::
   :local:
   :depth: 1

Before You Begin
================

It is essential that you have the following configured:

* Log files must be saved as ``JSON`` files  

Usage Notes
===========

By default, logs are saved as ``CSV`` files. To configure your log files to be saved as ``JSON`` instead, use the ``logFormat`` flag in your :ref:`legacy config file<current_method_flag_types>`. If your current logs are in ``CSV`` format and you require RCA, it's advisable to configure your logs to be saved in both ``CSV`` and ``JSON`` formats as outlined above.

Utility Functions
=================

The RCA executes the :ref:`export_open_snapshots` and :ref:`get_open_snapshots` utility functions. 