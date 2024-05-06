:orphan:

.. _use_database:

************
USE DATABASE
************

The ``USE DATABASE`` command lets you shift between databases within an existing session.

Syntax
======

.. code-block:: postgres

   USE DATABASE <name>

Parameters
==========

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``name``
     - The name of the database.
     
Examples
========

.. code-block:: postgres

   USE DATABASE master;

Permissions
===========

The ``USE DATABASE`` command requires **Comment** permission. 