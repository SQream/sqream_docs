.. _data_encryption_methods:

***********************
Encryption Methods
***********************
As attackers increasingly discover innotative methods to compromise systems and intercept data, modern enterprises must employ effective data protection methods. To this end SQream uses the encryption methods described below to secure sensitive data both in transit and at rest:

.. contents::
   :local:
   :depth: 1
   
Encrypting Data in Transit
----------------
**Data in transit**, also known as data in motion or data in flight, is data en route between any source and destination, such as over the internet or through a private network. Data protection in transit refers to providing a secure TS connection for data transferred between networks or from local to cloud storage devices. Encrypting data in transit is necessary because data in transit is typically considered relatively vulnerable to interception. SQream encrypts data in transit using SSL when, for example, users insert data files from external repositories over a JDBC or ODBC connection. 

For more information, see :ref:`installing_nginx_proxy_over_secure_connection`.

Encrypting Data at Rest
----------------
**Data at rest** refers to data stored on your hard drive or on the cloud. Because this type of data can be potentially intercepted **physically**, it requires a form of encryption that protects your data wherever it's stored. SQream faciliates encryption by letting you encrypt a maximum of three columns located in your database that you want to keep private.