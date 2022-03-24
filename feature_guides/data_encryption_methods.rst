.. _data_encryption_methods:

***********************
Encryption Methods
***********************
The **Encryption Methods** section describes the following:

.. contents::
   :local:
   :depth: 1

Encrypting Data in Transit
----------------
**In-transit data** refers to data files inserted from customer repositories using the COPY FROM command, and is transmitted to SQream over a TLS-encrypted channel using a JDBC or ODBC connection.

For more information, see the following:

* :ref:`copy_from`
* `JDBC <https://docs.sqream.com/en/latest/third_party_tools/client_drivers/jdbc/index.html>`_
* :ref:`odbc`

Encrypting Data at Rest
----------------
For **data at rest,** housed physically on computer data, you can encrypt one or more column as needed according to your specifications. Data at rest is encrypted before being written into files, and decrypted after being read from them. All existing unencrypted historical and data inserted into this column at a later time is encrypted for the specified column values. Data at rest is encrypted (**Comment** - *And decrypted?*) using the **AES-256** algorithm.

**Comment** - *Because the encryption keys are hidden from users, I didn't document them here. Please confirm that this is correct.*