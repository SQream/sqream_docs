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
**Data in transit** refers to data you use on a regular basis, usually stored on a database and accessed through applications or programs. This type of data is typically transferred between several physical or remote locations through email or uploading documents to the cloud. This type of data must therefore be protected while **in transit**. SQream encrypts data in transit using SSL when, for example, users insert data files from external repositories over a JDBC or ODBC connection.

For more information, see :ref:`installing_nginx_proxy_over_secure_connection`.

Encrypting Data at Rest
----------------
**Data at rest** refers to data stored on your hard drive or on the cloud. Because this type of data can be potentially intercepted **physically**, it requires a form of encryption that protects your data wherever it's stored. SQream faciliates encryption by letting you encrypt any columns located in your database that you want to keep private.

For more information about the syntax used for decrypting your data, see :ref:`data_encryption_syntax`.