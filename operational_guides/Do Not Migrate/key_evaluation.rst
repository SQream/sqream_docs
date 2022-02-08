.. _key_evaluation:

**************************
Key Evaluation
**************************
The **Key Evaluation** operation lets you evaluate problematic keys based on a number of parameters.

Take suitable action according to the nature of the problem.

Key Evaluation can be run using one of the following operational modes:

.. contents:: 
   :local:
   :depth: 1

View
----------
You can use the **View** mode to find all problematic keys in the database for all databases and/or tables.

The following shows the View command options:

.. code-block::
     
   $ select  keys_evaluate ('view');

.. code-block::
     
   $ select  keys_evaluate ('view', 'master');

.. code-block::
     
   $ select  keys_evaluate ('view', 'master', 'public.tbl');

Clean Storage
----------
You can use the **Clean Storage** mode to find all problematic keys located in the Storage for all databases.

The following shows the Clean Storage command:

.. code-block::
     
   $ select  keys_evaluate ('clean_storage');   
   
Clean Database
----------
You can use the **Clean Database** mode to find and clean all problematic keys located for a specific database and/or table.

The following shows the Clean Database command options:

.. code-block::
     
   $ select keys_evaluate ('clean_database','master');

.. code-block::
     
   $ select keys_evaluate ('clean_database','master', 'public.tbl');   
   
Clean Chunk Key
----------
You can use the **Clean Chunk Key** mode to clean a specific problematic chunk key.

The following shows the Clean Chunk Key command options:

.. code-block::
     
   $ select data_diag (12, '<path to missing file>');