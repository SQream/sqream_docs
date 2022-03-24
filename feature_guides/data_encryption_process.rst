.. _data_encryption_process:

***********************
Data Encryption Process
***********************
The **Data Encryption Process** page describes end-to-end encryption process, and describes the following:

.. contents::
   :local:
   :depth: 1

The Encryption Process
----------------
The following describes the encryption process:

1. A user with the required encryption execution permission accesses the system.

    ::
	
#. In the file to be uploaded, the user selects columns to encrypt. The syntax will (**Comment** - *"should" instead of "will"?)* includes the hint that triggers the encryption (see syntax section).

    ::

#. The user provides the location of the master key for deriving (**Comment** - *...generating/activating?*) the encryption in the remote repository. This applies to both **KMS** and **IBM SKLM**.

    ::
	
   **Comment** - *The source doc says, "this section will not be applied in the MVP scope." Should it stay in this doc?*

    ::

#. The user trigger (**Comment** - *"runs"?*) the COPY command to transport the data upon TLS session (not yet data at rest encryption) (**Comment** - *"Upon TLS session = when the TLS session is activated?"*

    ::
	
#. When the data is successfully inserted into the SQream database, it is encrypted and saved.

For more information, see the following:

* More information on permissions, see :ref:`data_encryption_permissions`.

   ::
   
* More information on which columns to encrypt, see the :ref:`Constraints<constraints>` section below.

   ::
 
* More information on triggering the encryption, and the master key location syntax, see :ref:`data_encryption_syntax`.

The Decryption Process
----------------
The following describes the encryption process:

1. A user with the required encryption execution permission accesses the system.

    ::
	
#. The user indicates the decryption. **Comment** - *"Indicates" = "triggers"?*)

    ::
	
#. The user can view the data derived from a table holding the encrypted data by decrypting the data by providing the location of the master key and selecting the required fields.

    :
	
   **Comment** - the source doc said, "this section will not be applied in the MVP scope." Should it stay in this doc?*

Once the specific statement ends- the user will be able to see the data in a human readable convention (plain text)

For more information, see the following:

* More information on triggering the decryption, see :ref:`data_encryption_syntax`.




Encrypted Columns
----------------
Column/Table-level encryption - More granular approach, encrypt only what you really need to



.. _constraints:

Constraints
----------------
Describe these in one of the existing sections.

