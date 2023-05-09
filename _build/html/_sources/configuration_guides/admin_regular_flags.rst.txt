.. _admin_regular_flags:

*************************
Regular Administration Flags
*************************
The **Regular Administration Flags** page describes **Regular** modification type flags, which can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command: 

* :ref:`Setting Bin Size<bin_sizes>`
* :ref:`Setting CUDA Memory<check_cuda_memory>`
* :ref:`Limiting Runtime to Utility Functions<compiler_gets_only_ufs>`
* :ref:`Enabling High Bin Control Granularity<copy_to_restrict_utf8>`
* :ref:`Reducing CPU Hashtable Sizes<cpu_reduce_hashtable_size>`
* :ref:`Setting Chunk Size for Copying from CPU to GPU<cuda_mem_cpy_max_size_bytes>`
* :ref:`Indicating GPU Synchronicity<cuda_mem_cpy_synchronous>`
* :ref:`Setting the Graceful Server Shutdown<graceful_shutdown>`
* :ref:`Enabling Modification of R&D Flags<developer_mode>`
* :ref:`Checking for Post-Production CUDA Errors<enable_device_debug_messages>`
* :ref:`Enabling Modification of clientLogger_debug File<enable_log_debug>`
* :ref:`Activating the NVidia Profiler Markers<enable_nv_prof_markers>`
* :ref:`Appending String at End of Log Lines<end_log_message>`
* :ref:`Monitoring and Printing Pinned Allocation Reports<gather_mem_stat>`
* :ref:`Increasing Chunk Size to Reduce Query Speed<increase_chunk_size_before_reduce>`
* :ref:`Adding Rechunker before Expensing Chunk Producer<increase_mem_factors>`
* :ref:`Setting the Buffer Size<level_db_write_buffer_size>`
* :ref:`Setting Memory Used to Abort Server<memory_reset_trigger_mb>`
* :ref:`Splitting Large Reads for Concurrent Execution<mt_read>`
* :ref:`Setting Worker Amount to Handle Concurrent Reads<mt_read_workers>`
* :ref:`Setting Implicit Casts in ORC Files<orc_implicit_casts>`
* :ref:`Setting Timeout Limit for Locking Objects before Executing Statements<statement_lock_timeout>`
* :ref:`Interpreting Decimal Literals as Double Instead of Numeric<use_legacy_decimal_literals>`
* :ref:`Using Legacy String Literals<use_legacy_string_literals>`
* :ref:`Blocking New VARCHAR Objects<block_new_varchar_objects>`
