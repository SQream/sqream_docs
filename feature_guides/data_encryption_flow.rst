.. _data_encryption_process:

***********************
Data Encryption Process
***********************
The **Data Encryption Process** page describes end-to-end encryption process, and describes the following:

.. contents::
   :local:
   :depth: 1

Encryption
----------------
The following describes the encryption process:

1. Users with the required encryption execution permission access the system (see Permissions & privileges  section)

User will choose the specific columns he would like to encrypt in the file in which he will upload (see constraints section), the syntax will encapsulates the hint which will trigger the encryption (see syntax section)

User will provide the location of the master key from which the encryption will be derived in the remote repository (whether KMS or IBM SKLM) see syntax section for the exact convention (this section will not be applied in the MVP scope)

User will trigger the copy command and the data will be transported upon TLS session (not yet data at rest encryption)

Once data arrived to Sqream database it will be encrypted and saved

For more information, see :ref:`data_encryption_permissions`.

Decryption
----------------



Encrypted Columns
----------------
Column/Table-level encryption - More granular approach, encrypt only what you really need to




Constraints
----------------
Describe these in one of the existing sections.

