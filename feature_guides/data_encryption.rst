.. _data_encryption:

***********************
Data Encryption
***********************
The **Data Encryption** page:

.. contents::
   :local:
   :depth: 1

Overview
==============
Encryption functionality is an increasing growing demands from customers and new projects prospects (see Customers Specific Requirements section for more information), the functionality manifests in all sorts of ways as seen in the below section (implementation option) and the reason for it to be very important to customers is due to market strive to comply to the GDPR compliance regulations as it shows in the GDPR Compliance section.

The encryption demand is growing around the world as it can be inserted to our sales pitch to promote vendors which security features is very important for them 

Column/Table-level encryption - More granular approach, encrypt only what you really need to

Syntax
==============
The following is the correct syntax for encrypting a new table:

.. code-block:: console
     
   CREATE TABLE client_name  (
        first_name TEXT(128),
        last_name TEXT(128),
        salary INT(6) ENCRYPT);
  
The following is the correct syntax for decrypting a new table:

.. code-block:: console

   SELECT * FROM TABLE;

The following is an example of encrypting a new table:

.. code-block:: console
     
   EXAMPLE

The following is an example of decryping a new table:

.. code-block:: console
     
   EXAMPLE

Encrypting Data in Transit
==============

Encrypting Data at Rest
==============

Data Types
==============

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







Security Encryption available in one column.
Is there a flag associated with this feature?
There already is a Security page. Are we overriding it?
Give the big picture in the Overview.
Show Inon the before/after example.
Minimum Viable Product MVP
Permissions section - external
Deadline: two weeks minimum