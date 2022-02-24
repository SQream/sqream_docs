.. _sqream_storage_cli_reference:

*************************
SqreamStorage
*************************
You can use the **SqreamStorage** program to create a new :ref:`storage cluster<storage_cluster>`.

The **SqreamStorage** page serves as a reference for the options and parameters.

Running SqreamStorage
=======================
The **SqreamStorage** program is located in the **bin** directory of your SQream installation..

Command Line Arguments
==========================
The **SqreamStorage** program supports the following command line arguments:

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

Example
=============
The **Examples** section describes how to create a new storage cluster at ``/home/rhendricks/raviga_database``:

.. code-block:: console

   $ SqreamStorage --create-cluster --cluster-root /home/rhendricks/raviga_database
   Setting cluster version to: 26

Alternatively, you can write this in shorthand as ``SqreamStorage -C -r /home/rhendricks/raviga_database``. A message is displayed confirming that your cluster has been created.