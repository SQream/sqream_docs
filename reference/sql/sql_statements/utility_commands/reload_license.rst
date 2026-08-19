:orphan:

.. _reload_license:

**************
RELOAD LICENSE
**************

``RELOAD_LICENSE`` reads the license file again while the system is running, so that a replaced or renewed license takes effect without restarting the workers.

Use it after replacing the license file on disk, such as when renewing an expired license or raising a capacity limit. The file is read from the path the worker was started with.

See also :ref:`get_license_info`.

Permissions
===========

The role must have the ``SUPERUSER`` permissions.

Syntax
======

.. code-block:: postgres

   reload_license_statement ::=
       SELECT RELOAD_LICENSE()
       ;

Parameters
==========

``RELOAD_LICENSE`` takes no parameters.

Returns
=======

``RELOAD_LICENSE`` returns no result set. The statement succeeds if the license file was read and accepted.

Notes
=====

* If the new license file is invalid, the statement fails with the license error and the previously loaded license remains in effect.

Examples
========

Reloading the license after replacing the license file:

.. code-block:: postgres

   SELECT RELOAD_LICENSE();
