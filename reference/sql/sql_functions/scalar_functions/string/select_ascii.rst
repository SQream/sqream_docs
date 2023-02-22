.. _select_ascii:

********************
SELECT ASCII
********************
The **SELECT ASCII** function is used to return the ASCII code value of the leftmost character of a string.

Syntax
==========
The following shows the syntax for the SELECT ASCII function:

.. code-block:: postgres

   SELECT ASCII('');

Parameters
============
The following table shows the DECODE parameters:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - 
     - 
   * - 
     - 

Returns
=========

The SELECT ASCII function returns ``integer``.

Example
===========
.. code-block:: postgres

   SELECT ASCII('hello');

   
Permissions
=============

The role must have the ``SUPERUSER`` permissions.