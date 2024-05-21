:orphan:

.. _alter_table_store_statistics:

****************************
ALTER TABLE STORE STATISTICS
****************************



Syntax
======

.. code-block:: postgres

	ALTER TABLE STORE STATISTICS

Examples
========

.. code-block:: postgres

	ALTER TABLE "nba" DROP STATISTICS FOR COLUMNS "number";

Permissions
===========

The role must have the ``SUPERUSER`` permissions.

