.. _sqream_storage_cli_reference:

*************************
SqreamStorage
*************************

``SqreamStorage`` allows the creation of a new :ref:`storage cluster<storage_cluster>`.

This page serves as a reference for the options and parameters.

Running SqreamStorage
=======================

``SqreamStorage`` can be found in the ``bin`` directory of your SQream DB installation..

Command line arguments
==========================

``SqreamStorage`` supports the following command line arguments:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Argument
     - Shorthand
     - Description
   * - ``--create-cluster``
     - ``-C``
     - Creates a storage cluster at a specified path
   * - ``--cluster-root``
     - ``-r``
     - Specifies the cluster path. The path must **not** already exist.


Examples
=============

Create a new storage cluster
----------------------------------

Create a new cluster at ``/home/rhendricks/raviga_database``:

.. code-block:: console

   $ SqreamStorage --create-cluster --cluster-root /home/rhendricks/raviga_database
   Setting cluster version to: 26

This can also be written shorthand as ``SqreamStorage -C -r /home/rhendricks/raviga_database``.

This message confirms the creation of the cluster successfully.
