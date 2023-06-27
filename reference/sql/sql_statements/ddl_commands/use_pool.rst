.. _use_pool:

********
USE POOL
********

The ``USE [RESOURCE] POOL`` command lets you shift between pools within a session. 

Syntax
======

.. code-block::
	
	USE [RESOURCE] POOL <pool_name>

Parameters
==========

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``pool_name``
     - Specifies the name of a specific pool you wish to shift to within the current session	
     
Example
=======

.. code-block::

	USE POOL bi_pool;

Permission
==========

The ``USE POOL`` command requires **Comment** permission. 

.. topic:: Using the Editor

	You may also shift between pools within a session using the **Editor**. 
	
	In the left-hand side of the ribbon, select a pool from the **Pool** drop-down menu. 