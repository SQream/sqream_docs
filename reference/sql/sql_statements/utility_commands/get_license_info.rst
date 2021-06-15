.. _get_license_info:

********************
GET_LICENSE_INFO
********************

SQream displays information related to data size limitations, expiration date, type of license shown by the new UF.

When invoked, ``get_license_info()`` returns the license information in the following order:

1. Compressed data size (GB)
2. Uncompressed data size (GB)
3. Compression type
4. Data size limit (GB)
5. Expiration date
6. ``is date expired(0/1)`` - ``0`` is **no**, and ``1`` is **yes**
7. ``is size exceeded(0/1)`` - ``0`` is **no**, and ``1`` is **yes**
8. ``data_size_left`` (GB)

The following is an example of the above licensing information:
  
.. code-block:: none
     
   10,100,compressed,20,2045-03-18,0,0,10
