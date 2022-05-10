.. _data_encryption_overview:

***********************
Overview
***********************
The demand for confidentiality has steadily increased to protect the growing volumes of private data stored on computer systems and transmitted over the internet. To this end, regulatory bodies such as the **General Data Protection Regulation (GDPR)** have produced requirements to standardize and enforce compliance aimed at protecting customer data. **Data Encryption** helps protect sensitive data by preventing unauthorized users from reading it in the event of a breach.

The method of encryption required depends on the type of data used, namely data in transit and data at rest. This is achieved by scrambling the content into an unreadable format based on encryption and decryption keys using the **AES-256** algorithm. This algorithm supports the largest bit size (256 bits) and is practically unbreakable based on brute force. 

Encryption can be used for the following:

* Encrypting existing data.

   ::
   
* Selecting data from an encrypted column.

   ::
   
* Creating tables with one or more encrypted columns.

   ::   
   
* Joining encrypted columns with other tables.
   
   ::   
   
* Deleting encrypted columns.

For more information on encryption methods, see :ref:`data_encryption_methods`. 

For more information on GDPR compliance requirements, see the `GDPR checklist <https://gdpr.eu/checklist/>`_.