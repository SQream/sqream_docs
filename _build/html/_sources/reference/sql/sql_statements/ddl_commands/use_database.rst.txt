.. _use_database:

*****************
USE DATABASE
*****************
The ``USE DATABASE`` command lets you switch between databases on your existing connection and session. You can use this command instead of ``/c``, which closes your existing connection and opens a new one. In addition, **USE DATABASE** retains any ``SET`` commands that you've set, while ``/c`` restores the default values.

Syntax
==========
The following is the correct syntax for switching databases with the **USE DATABASE** command:

.. code-block:: postgres

   USE DATABASE <name>

Parameters
============
The following parameter can be used when switching databases with the **USE DATABASE** command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``name``
     - The name of the database.
     
Examples
===========
The following is an example of the **USE DATABASE** command:

.. code-block:: postgres

   USE DATABASE <public>

Permissions
=============
**Comment** - *What are the permissions?*