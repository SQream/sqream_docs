.. _show_version:

*****************
SHOW_VERSION
*****************

``SHOW_VERSION()`` is a function that returns the system version for SQream DB.

Permissions
=============

No special permissions are required.

Syntax
==========

.. code-block:: postgres

   show_version_statement ::=
       SELECT SHOW_VERSION()
       ;

Parameters
============

None

Notes
==========

To check the SQream DB version from the shell, run ``$ sqreamd --version``

Examples
===========

Getting the current SQream DB version
---------------------------------------


.. code-block:: psql

   t=> SELECT SHOW_VERSION();
   bytesread
   ---------
   v2019.3

