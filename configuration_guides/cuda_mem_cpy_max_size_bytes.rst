.. _cuda_mem_cpy_max_size_bytes:

*************************
Setting Chunk Size for Copying from CPU to GPU
*************************
The ``cudaMemcpyMaxSizeBytes`` flag sets the chunk size for copying from CPU to GPU. If this value is set to ``0``, do not divide.

The following describes the ``cudaMemcpyMaxSizeBytes`` flag:

* **Data type** - uint
* **Default value** - ``0``
* **Allowed values** - 0-4000000000