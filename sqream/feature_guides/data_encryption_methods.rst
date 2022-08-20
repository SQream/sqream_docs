.. _data_encryption_methods:

***********************
Encryption Methods
***********************
Data exists in one of following states and determines the encryption method:

.. contents::
   :local:
   :depth: 1

Encrypting Data in Transit
----------------
**Data in transit** refers to data you use on a regular basis, usually stored on a database and accessed through applications or programs. This data is typically transferred between several physical or remote locations through email or uploading documents to the cloud. This type of data must therefore be protected while **in transit**. SQream encrypts data in transit using SSL when, for example, users insert data files from external repositories over a JDBC or ODBC connection.

For more information, see `Use TLS/SSL When Possible <https://docs.sqream.com/en/latest/operational_guides/security.html#use-tls-ssl-when-possible>`_.

Encrypting Data at Rest
----------------
**Data at rest** refers to data stored on your hard drive or on the cloud. Because this data can be potentially intercepted **physically**, it requires a form of encryption that protects your data wherever you store it. SQream faciliates encryption by letting you encrypt any columns located in your database that you want to keep private.