.. _data_encryption:

***********************
Data Encryption
***********************

The **Data Encryption** page describes the following:

.. contents::
   :local:
   :depth: 1
   
   
Overview
==============
**Data Encryption** helps protect sensitive data by preventing unauthorized users from reading it in the event of a breach. This is achieved by scrambling the content into an unreadable format based on encryption and decryption keys.

The demand for confidentiality has steadily increased to protect the growing volumes of private data stored on computer systems and transmitted over the internet. To this end, regulatory bodies such as the **General Data Protection Regulation (GDPR)** have produced requirements to standardize and enforce compliance aimed at protecting customer data.

For more information on GDPR compliance requirements, see the `GDPR checklist <https://gdpr.eu/checklist/>`_.

Column/Table-level encryption - More granular approach, encrypt only what you really need to


   
Encryption Methods
==============
The **Encryption Methods** section describes the following:

.. contents::
   :local:
   :depth: 1

Encrypting Data in Transit
----------------
**In-transit data** refers to data files inserted from customer repositories using the COPY FROM command, and is transmitted to SQream over a TLS-encrypted channel using a JDBC or ODBC connection.

For more information, see the following:

* :ref:`copy_from`
* :ref:`jdbc`
* :ref:`odbc`

Encrypting Data at Rest
----------------

Data Types
==============

Syntax
==============
The following is the correct syntax for **encrypting** a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        first_name TEXT(128),
        last_name TEXT(128),
        salary INT(6) ENCRYPT);
		
The following is an example of encrypting a new table:

.. code-block:: console
     
   EXAMPLE
  
The following is the correct syntax for **decrypting** a new table:

.. code-block:: console

   SELECT * FROM TABLE;

The following is an example of decrypting a new table:

.. code-block:: console
     
   EXAMPLE

How Encryption Works
==============
The **How Encryption Works** page describes the following:

.. contents::
   :local:
   :depth: 1

Encryption
----------------



Decryption
----------------



Encrypted Columns
----------------



Constraints
----------------
Describe these in one of the existing sections.



Use Case Considerations
==============
Include the relevant content from this section in the correct places in this document.



Permissions
==============



Usage Notes
==============
Include the relevant content from this section in the correct places in this document.


