.. _transactions:

***********************
Transactions
***********************

SQream DB supports serializable transactions. This is also called 'ACID'.

The implementation of transactions means that commit, rollback and recovery are all extremely fast.

SQreamDB extremely fast bulk insert speed, with minimal slowdown when running concurrent inserts. There is no performance reason to break large inserts up into multiple transactions.

Supporting transactions for a database system sometimes means having good performance for OLTP workloads, SQreamDB' transaction system does not have high performance for high concurrency OLTP workloads.

SQream DB also supports transactional DDL.


