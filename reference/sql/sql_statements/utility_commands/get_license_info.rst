.. _get_license_info:

********************
GET_LICENSE_INFO
********************
``GET_LICENSE_INFO`` displays information related to data size limitations, expiration date, and type of license currently used by the SQream cluster.
   
Permissions
=============
No special permissions are required.

Syntax
==========
The following is the correct syntax for running the ``GET LICENSE INFO`` statement:

.. code-block:: postgres
  
   get_license_info_statement ::=
    SELECT GET_LICENSE_INFO()
    ;

Returns
==========
The following table shows the ``GET_LICENSE_INFO`` license information in the order that it is returned:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Example
   * - ``compressed_cluster_size``
     - Shows the compressed size (GB) of the cluster.
     - 10
   * - ``uncompressed_cluster_size``
     - Shows the uncompressed size (GB) of the cluster.
     - 10
   * - ``compress_type``
     - Shows the compression type (``compressed``, ``uncompressed``).
     - compressed
   * - ``cluster_size_limit``
     - Shows the cluster size limit (GB) of the current license.
     - 20
   * - ``expiration_date``
     - Shows the expiration date of the current license.
     - 2024-03-18
   * - ``is_date_expired``
     - Shows whether the date has expired or not (``0`` - **No**, ``1`` - **Yes**).
     - 0
   * - ``is_size_exceeded``
     - Shows whether the cluster size has exceeded the license size limit or not (``0`` - **No**, ``1`` - **Yes**).
     - 0
   * - ``cluster_size_left``
     - Shows the remaining available cluster size (GB) in the license.
     - 10
	 
Example
===========
The following is an example of the returned license information described in the **Returns** section above:
  
.. code-block:: psql
     
   10,100,compressed,20,2045-03-18,0,0,10

Parameters
============
The ``GET_LICENSE_INFO`` command has no parameters.

Notes
=========
If the license expires or exceeds quotas, contact a SQream representative to extend the license.
