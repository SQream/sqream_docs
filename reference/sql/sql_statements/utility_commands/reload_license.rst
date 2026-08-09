:orphan:

.. _reload_license:

********************
RELOAD_LICENSE
********************

``RELOAD_LICENSE`` loads a new license file while the system is up and running. It saves having to restart the workers for refreshing license information.

Syntax
==========

The following is the correct syntax when loading the license file:

.. code-block:: postgres

  SELECT RELOAD_LICENSE()()

Parameters
============

The Parameters section is not relevant for the ``RELOAD_LICENSE`` statement.

Returns
=========

There is no returned output.

Permissions
=============

The role must have the ``SUPERUSER`` permissions.
