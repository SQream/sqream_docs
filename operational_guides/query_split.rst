.. _query_split:

****************************
Query Split
****************************

The split query operation optimizes long-running queries by executing them in parallel on different GPUs, thereby reducing overall run time. It's crucial to note that not every query may benefit from this approach, as the splitting mechanism introduces some overhead runtime. Additionally, it's emphasized that splitting can only be performed in the UI, leveraging Meta-scripting, a feature currently exclusive to the UI environment.

The four stages of using the query split operation are:

* Creating an empty table that would hold the results of the query
* 

.. contents::
   :local:
   :depth: 1
   
Syntax
========

.. code-block:: sql

#Creating a table