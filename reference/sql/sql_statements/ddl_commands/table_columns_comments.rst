.. _table_columns_comments:

*****************************************************
Adding Table and Column-Level Comments in Scailium
*****************************************************

Table and column-level comments in Scailium are used to document the meaning, usage, and constraints of each field in a table. Proper documentation improves query readability, reduces onboarding time, and minimizes misinterpretation of data.

Purpose
=======

Table and column comments should:

* Describe the business meaning of the table or column.
* Clarify units, formats, or encoding.
* Highlight special logic (e.g., derived fields, flags).
* Document allowed values where applicable.

When to Add Comments
====================

Add or update table or column comments when:

* Creating a new table.
* Adding new columns to an existing table.
* Refactoring or renaming columns or tables.
* Business logic of a column or table changes.

Syntax
======

Creating a Table with Comments
------------------------------

.. code-block:: postgres

   CREATE TABLE my_table (
     my_column1 INT COMMENT 'This is a column comment',
     my_column2 TEXT
   ) COMMENT = 'This is a table comment';

Modifying Comments
------------------

.. code-block:: postgres

   -- Update Table comment
   ALTER TABLE my_table COMMENT = 'This is an updated table comment.';

   -- Remove Table comment
   ALTER TABLE my_table COMMENT = '';

   -- Update Column comment
   ALTER TABLE my_table ALTER COLUMN my_column1 COMMENT = 'This is an updated column comment.';

   -- Remove Column comment
   ALTER TABLE my_table ALTER COLUMN my_column1 COMMENT = '';

Usage Example
=============

Table: ``customer_transactions``

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Column Name
     - Data Type
     - Comment
   * - transaction_id
     - BIGINT
     - Unique identifier for each transaction
   * - customer_id
     - BIGINT
     - ID of the customer performing the transaction
   * - amount
     - DOUBLE
     - Transaction amount in local currency
   * - currency_code
     - TEXT
     - ISO currency code (e.g., USD, EUR, ILS)
   * - is_fraud
     - BOOLEAN
     - Indicates whether the transaction was flagged as fraud
   * - created_at
     - TIMESTAMP
     - Timestamp when the transaction was created

Permissions
===========

* A user with **DDL (Data Definition Language)** permissions, specifically the ability to **CREATE** or **ALTER** a table or column, automatically has the permission to add, modify, or drop comments on that object.
* Only the object owner or a superuser can change the comment.
* All users with at least ``SELECT`` permission on a table can view its comments.

Viewing Comments
================

You can view comments by querying the system catalog:

.. code-block:: psql

   -- View table comments
   SELECT table_name, comment
   FROM sqream_catalog.tables
   WHERE table_name = 'customers';

   -- View column comments
   SELECT column_name, comment
   FROM sqream_catalog.columns
   WHERE table_name = 'customers' AND column_name = 'customer_id';