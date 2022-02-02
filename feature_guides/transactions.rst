.. _transactions:

***********************
Transactions
***********************

SQream DB supports serializable transactions. This is also called 'ACID compliance'. 

The implementation of transactions means that commit, rollback and recovery are all extremely fast.

SQream DB has extremely fast bulk insert speed, with minimal slowdown when running concurrent inserts. There is no performance reason to break large inserts up into multiple transactions.

The phrase "supporting transactions" for a database system sometimes means having good performance for OLTP workloads, SQream DB's transaction system does not have high performance for high concurrency OLTP workloads.

SQream DB also supports :ref:`transactional DDL<ddl_commands_list>`.


