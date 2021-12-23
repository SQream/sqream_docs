.. _show_version:

*****************
SHOW_VERSION
*****************
The ``SHOW_VERSION()`` function returns the SQream system version.

The **SHOW_VERSION** page describes the following:

.. contents:: 
   :local:
   :depth: 1

Syntax
==========
The following is the correct syntax for the **SHOW_VERSION** function:

.. code-block:: postgres

   show_version_statement ::=
       SELECT SHOW_VERSION()
       ;

Parameters
============
The **SHOW_VERSION** function has no parameters.

Notes
==========
To check the SQream version from the shell, run ``$ sqreamd --version``.

Example
===========
The Examples section shows how to get the current SQream version:

.. code-block:: psql

   t=> SELECT SHOW_VERSION();
   bytesread
   ---------
   v2019.3

Permissions
=============
The **SHOW_VERSION** function requires no special permissions.
