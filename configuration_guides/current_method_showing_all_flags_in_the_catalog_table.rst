.. _current_method_showing_all_flags_in_the_catalog_table:

**************************
Showing All Flags in the Catalog Table
**************************
SQream uses the **sqream_catalog.parameters** catalog table for showing all flags, providing the scope (default, cluster and session), description, default value and actual value.

The following is the correct syntax for a catalog table query:

.. code-block:: console
   
   SELECT * FROM sqream_catalog.settings

The following is an example of a catalog table query:

.. code-block:: console
   
   externalTableBlobEstimate, 100, 100, default,
   varcharEncoding, ascii, ascii, default, Changes the expected encoding for Varchar columns
   useCrcForTextJoinKeys, true, true, default,
   hiveStyleImplicitStringCasts, false, false, default,