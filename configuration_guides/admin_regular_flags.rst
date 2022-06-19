.. _admin_regular_flags:

*************************
Regular Administration Flags
*************************
The **Regular Administration Flags** page describes **Regular** modification type flags, which can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command:

* `Setting Bin Size <https://docs.sqream.com/en/v2020.3.2/configuration_guides/bin_sizes.html>`_
* `Setting CUDA Memory <https://docs.sqream.com/en/v2020.3.2/configuration_guides/check_cuda_memory.html>`_
* `Limiting Runtime to Utility Functions <https://docs.sqream.com/en/v2020.3.2/configuration_guides/compiler_gets_only_ufs.html>`_
* `Enabling High Bin Control Granularity <https://docs.sqream.com/en/v2020.3.2/configuration_guides/copy_to_restrict_utf8.html>`_
* `Reducing CPU Hashtable Sizes <https://docs.sqream.com/en/v2020.3.2/configuration_guides/cpu_reduce_hashtable_size.html>`_
* `Setting Chunk Size for Copying from CPU to GPU <https://docs.sqream.com/en/v2020.3.2/configuration_guides/cuda_mem_cpy_max_size_bytes.html>`_
* `Indicating GPU Synchronicity <https://docs.sqream.com/en/v2020.3.2/configuration_guides/cuda_mem_cpy_synchronous.html>`_
* `Enabling Modification of R&D Flags <https://docs.sqream.com/en/v2020.3.2/configuration_guides/developer_mode.html>`_
* `Checking for Post-Production CUDA Errors <https://docs.sqream.com/en/v2020.3.2/configuration_guides/enable_device_debug_messages.html>`_
* `Enabling Modification of clientLogger_debug File <https://docs.sqream.com/en/v2020.3.2/configuration_guides/enable_log_debug.html>`_
* `Activating the NVidia Profiler Markers <https://docs.sqream.com/en/v2020.3.2/configuration_guides/enable_nv_prof_markers.html>`_
* `Appending String at End of Log Lines <https://docs.sqream.com/en/v2020.3.2/configuration_guides/end_log_message.html>`_
* `Monitoring and Printing Pinned Allocation Reports <https://docs.sqream.com/en/v2020.3.2/configuration_guides/gather_mem_stat.html>`_
* `Increasing Chunk Size to Reduce Query Speed <https://docs.sqream.com/en/v2020.3.2/configuration_guides/increase_chunk_size_before_reduce.html>`_
* `Adding Rechunker before Expensing Chunk Producer <https://docs.sqream.com/en/v2020.3.2/configuration_guides/increase_mem_factors.html>`_
* `Setting the Buffer Size <https://docs.sqream.com/en/v2020.3.2/configuration_guides/level_db_write_buffer_size.html>`_
* `Maximum Pinned Percentage of Total RAM <https://docs.sqream.com/en/v2020.3.2/configuration_guides/max_pinned_percentage_of_total_ram.html>`_
* `Setting Memory Used to Abort Server <https://docs.sqream.com/en/v2020.3.2/configuration_guides/memory_reset_trigger_mb.html>`_
* `Splitting Large Reads for Concurrent Execution <https://docs.sqream.com/en/v2020.3.2/configuration_guides/mt_read.html>`_
* `Setting Worker Amount to Handle Concurrent Reads <https://docs.sqream.com/en/v2020.3.2/configuration_guides/mt_read_workers.html>`_
* `Setting Implicit Casts in ORC Files <https://docs.sqream.com/en/v2020.3.2/configuration_guides/orc_implicit_casts.html>`_
* `Setting Timeout Limit for Locking Objects before Executing Statements <https://docs.sqream.com/en/v2020.3.2/configuration_guides/statement_lock_timeout.html>`_
* `Interpreting Decimal Literals as Double Instead of Numeric <https://docs.sqream.com/en/v2020.3.2/configuration_guides/use_legacy_decimal_literals.html>`_
* `Interpreting VARCHAR as TEXT <https://docs.sqream.com/en/v2020.3.2/configuration_guides/use_legacy_string_literals.html>`_