.. _transactions:

***********************
Transactions
***********************

serializable

commit, rollback and recovery are all extremely fast

not performance for high concurrency oltp workloads

extremely fast injest rate

no reason to break large inserts up into multiple transactions

"supporting transactions": means oltp performance sometimes

"acid": means serializable more or less, which we support

transactional ddl

