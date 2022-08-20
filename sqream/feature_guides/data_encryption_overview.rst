.. _data_encryption_overview:

***********************
Overview
***********************
**Data Encryption** helps protect sensitive data at rest by concealing it from unauthorized users in the event of a breach. This is achieved by scrambling the content into an unreadable format based on encryption and decryption keys. Typically speaking, this data pertains to **PII (Personally Identifiable Information)**, which is sensitive information such as credit card numbers and other information related to an identifiable person.

Users encrypt their data on a column basis by specifying ``column_name`` in the encryption syntax.

The demand for confidentiality has steadily increased to protect the growing volumes of private data stored on computer systems and transmitted over the internet. To this end, regulatory bodies such as the **General Data Protection Regulation (GDPR)** have produced requirements to standardize and enforce compliance aimed at protecting customer data.

Encryption can be used for the following:

* Creating tables up to three encrypted columns.

   ::
   
* Joining encrypted columns with other tables.

   ::
   
* Selecting data from an encrypted column.

For more information on the encryption syntax, see :ref:`data_encryption_syntax`.

For more information on GDPR compliance requirements, see the `GDPR checklist <https://gdpr.eu/checklist/>`_.