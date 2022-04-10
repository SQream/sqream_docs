.. _key_evaluation_operational_modes:

**************************
Operational Modes
**************************
Key Evaluation can be used to do one of the following:

**Comment** - *Do users initiate one of these modes, or do they occur in the background on their own? The answer to this question determines whether key evaluation belongs in Feature Guides or Operational Guides.*

.. contents:: 
   :local:
   :depth: 1

View All Problematic Chunk Keys
----------
You can use the **View** mode to find all problematic keys in the database for all databases and/or tables.

The following shows the View command options:

.. code-block::
     
   $ select  keys_evaluate ('view');

.. code-block::
     
   $ select  keys_evaluate ('view', 'master');

.. code-block::
     
   $ select  keys_evaluate ('view', 'master', 'public.tbl');

Find and Clean Problematic Keys from Storage
----------
You can use the **Clean Storage** mode to find all problematic keys located in the Storage for all databases.

The following shows the Clean Storage command:

.. code-block::
     
   $ select  keys_evaluate ('clean_storage');

.. note:: This mode backs up the levelDB to the **backup** folder in the cluster before finding and cleaning problematic keys from your storage.
   
Find and Clean Problematic Keys from a Database
----------
You can use the **Clean Database** mode to find and clean all problematic keys located for a specific database and/or table.

The following shows the Clean Database command options:

.. code-block::
     
   $ select keys_evaluate ('clean_database','master');

.. code-block::
     
   $ select keys_evaluate ('clean_database','master', 'public.tbl');

.. note:: This mode backs up the levelDB to the **backup** folder in the cluster before finding and cleaning problematic keys from your database. 
   
Clean Specifically Defined Chunk Keys
----------
**Comment** - *Currently not supported. Remove until further notice?*

You can use the **Clean Chunk Key** mode to clean a specific problematic chunk key. **Comment** - *Note: data_diag vs keys_evaluate.*

The following shows the Clean Chunk Key command options:

.. code-block::
     
   $ select data_diag (12, '<path to missing file>');