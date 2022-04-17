.. _data_encryption_permissions:

***********************
Permissions
***********************
The **Permissions** page tells you how to create a table with encrypted columns as a superuser.

Users with the appropriate encryption permission privilege's can encrypt and decrypt data. In addition, only superusers granted permission can view encrypted tables in the **sqream_catalog**.

You can create a table with encrypted columns as a superuser as follows:

.. code-block:: console
     
   $ create or replace table t_enc(c1 int encrypt);
   
For more information about the SQream catalog, see the :ref:`catalog_reference`.