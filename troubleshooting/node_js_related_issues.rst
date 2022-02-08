.. _node_js_related_issues:

***********************
Node.js Related Issues
***********************
The **Node.js Related Issues** page describes how to resolve the following common issues:

.. toctree::
   :maxdepth: 2
   :glob:
   :titlesonly:

Preventing Heap Out of Memory Errors
--------------------------------------------

Some workloads may cause Node.JS to fail with the error:

.. code-block:: none

   FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory

To prevent this error, modify the heap size configuration by setting the ``--max-old-space-size`` run flag.

For example, set the space size to 2GB:

.. code-block:: console
   
   $ node --max-old-space-size=2048 my-application.js

Providing Support for BIGINT Data Type
------------------------

The Node.JS connector supports fetching ``BIGINT`` values from SQream DB. However, some applications may encounter an error when trying to serialize those values.

The error that appears is:
.. code-block:: none
   
   TypeError: Do not know how to serialize a BigInt

This is because JSON specification do not support BIGINT values, even when supported by Javascript engines.

To resolve this issue, objects with BIGINT values should be converted to string before serializing, and converted back after deserializing.

For example:

.. code-block:: javascript

   const rows = [{test: 1n}]
   const json = JSON.stringify(rows, , (key, value) =>
     typeof value === 'bigint'
         ? value.toString()
         : value // return everything else unchanged
   ));
   console.log(json); // [{"test": "1"}]