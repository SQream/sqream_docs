.. _creating_or_cloning_a_storage_cluster:

****************************************
Creating or Cloning Storage Clusters
****************************************
When SQream DB is installed, it comes with a default storage cluster. This guide will help if you need a fresh storage cluster or a separate copy of an existing storage cluster.

Creating a New Storage Cluster
=====================================

SQream DB comes with a CLI tool, :ref:`sqream_storage_cli_reference`. This tool can be used to create a new empty storage cluster.

In this example, we will create a new cluster at ``/home/rhendricks/raviga_database``:

.. code-block:: console

   $ SqreamStorage --create-cluster --cluster-root /home/rhendricks/raviga_database
   Setting cluster version to: 26

This can also be written shorthand as ``SqreamStorage -C -r /home/rhendricks/raviga_database``.

This ``Setting cluster version...`` message confirms the creation of the cluster successfully.

Telling SQream DB to Use a Storage Cluster
===============================================

Permanently Setting the Storage Cluster Setting
-------------------------------------------------------

To permanently set the new cluster location, change the ``"cluster"`` path listed in the configuration file.

For example:

.. code-block:: json
   :emphasize-lines: 11

   {
       "compileFlags": {
       },
       "runtimeFlags": {
       },
       "runtimeGlobalFlags": {
       },
       "server": {
           "gpu": 0,
           "port": 5000,
           "cluster": "/home/sqream/my_old_cluster",
           "licensePath": "/home/sqream/.sqream/license.enc"
       }
   }

should be changed to

.. code-block:: json
   :emphasize-lines: 11

   {
       "compileFlags": {
       },
       "runtimeFlags": {
       },
       "runtimeGlobalFlags": {
       },
       "server": {
           "gpu": 0,
           "port": 5000,
           "cluster": "/home/rhendricks/raviga_database",
           "licensePath": "/home/sqream/.sqream/license.enc"
       }
   }

Now, the cluster should be restarted for the changes to take effect.

Starting a Temporary SQream DB worker with a Storage Cluster
-------------------------------------------------------------

Starting a SQream DB worker with a custom cluster path can be done in two ways:

Using a Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to the technique above, create a configuration file with the correct cluster path. Then, start ``sqreamd`` using the ``-config`` flag:

.. code-block:: console

   $ sqreamd -config config_file.json
   
Note that using a configuration file is the recommended method.

Using the Command Line Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use sqreamd's command line parameters to override the default storage cluster path:

.. code-block:: console

   $ sqreamd /home/rhendricks/raviga_database 0 5000 /home/sqream/.sqream/license.enc

.. note:: sqreamd's command line parameters' order is ``sqreamd <cluster path> <GPU ordinal> <TCP listen port (unsecured)> <License path>``

Copying an Existing Storage Cluster
=====================================

Copying an existing storage cluster to another path may be useful for testing or troubleshooting purposes.

#. Identify the location of the active storage cluster. This path can be found in the configuration file, under the ``"cluster"`` parameter.

#. Shut down the SQream DB cluster. This prevents very large storage directories from being modified during the copy process.

#. (optional) Create a tarball of the storage cluster, with ``tar -zcvf sqream_cluster_`date +"%Y-%m-%d-%H-%M"`.tgz <cluster path>``. This will create a tarball with the current date and time as part of the filename.

#. Copy the storage cluster directory (or tarball) with ``cp`` to another location on the local filesystem, or use ``rsync`` to copy to a remote server.

#. After the copy is completed, start the SQream DB cluster to continue using SQream DB.
