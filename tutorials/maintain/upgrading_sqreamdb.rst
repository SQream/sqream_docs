.. _upgrading_sqream_db:

***********************
Upgrading SQream DB
***********************

See :ref:`Release Notes <releases>` to learn about what's new in the latest release of SQream DB.

SQream DB can usually be upgraded one at a time, without interrupting the overall cluster availability. However, we we recommend the upgrade be performed across all nodes, to reduce the risk of problems.

.. contents:: In this topic:
   :local:

Check the upgrade path
========================
When upgrading from a previous version of SQream DB, it is recommended that you don't skip major releases. You can however skip patch and minor releases.

Prepare to upgrade
=====================

#. Copy the new SQream DB package to all servers

#. Refer to the *Operations* section of the release notes. Metadata upgrades are sensitive operations, and are best performed in isolation. If there are metadata upgrades required, we recommend that the entire SQream DB cluster be shut down to ensure a safe upgrade. 

#. Check any active statements across the cluster. If the cluster needs to be shut down, you may want to alert your users.

Perform the upgrade on each node
=================================

.. TODO: Give instructions. What happens with Docker vs. RPM vs. whatever?

Perform the upgrade on the master node
========================================

.. TODO: Give instructions


Troubleshooting
================

.. TODO: elaborate on some troubleshooting paths

After upgrading, a SQream DB cluster can't be downgraded.
If you experience any issues during the upgrade we recommend that you reach out to `SQream Support <http://support.sqream.com/>`_. or contact your SQream account manager for help.


.. rubric:: What's next?

.. TODO: Links for what's next after an upgrade.
