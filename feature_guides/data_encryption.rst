.. _data_encryption:

***************
Data Encryption
***************

**Data Encryption** helps protect sensitive data at rest by concealing it from unauthorized users in the event of a breach. This is achieved by scrambling the content into an unreadable format based on encryption and decryption keys. Typically speaking, this data pertains to **PII (Personally Identifiable Information)**, which is sensitive information such as credit card numbers and other information related to an identifiable person.

Users encrypt their data on a column basis by specifying ``column_name`` in the encryption syntax.

The demand for confidentiality has steadily increased to protect the growing volumes of private data stored on computer systems and transmitted over the internet. To this end, regulatory bodies such as the **General Data Protection Regulation (GDPR)** have produced requirements to standardize and enforce compliance aimed at protecting customer data.

Encryption can be used for the following:

* Creating tables with up to three encrypted columns.

   ::
   
* Joining encrypted columns with other tables.

   ::
   
* Selecting data from an encrypted column.

.. warning:: The ``SELECT`` statement decrypts information by default. When executing ``CREATE TABLE AS SELECT`` or ``INSERT INTO TABLE AS SELECT``, encrypted information will appear as clear text in the newly created table.

For more information on the encryption syntax, see :ref:`data_encryption_syntax`.

For more information on GDPR compliance requirements, see the `GDPR checklist <https://gdpr.eu/checklist/>`_.
   
.. rubric:: In This Section:   

.. toctree::
   :maxdepth: 1
   :titlesonly:

   data_encryption_methods
   data_encryption_types
   data_encryption_syntax
   data_encryption_permissions