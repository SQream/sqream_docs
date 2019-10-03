.. _sql_feature_support:

####################
SQL Feature Support
####################

Even though SQL is standardized in various ANSI documents, no DBMS implements the entire standard.
Some features have no implementation at all.

To understand which SQL features SQream DB supports, use the tables below.

***********
Data types
***********

.. list-table:: Values
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - ``tinyint``
     - ✓
     - Unsigned 1 byte integer (0 - 255)
   * - ``smallint``
     - ✓
     - 2 byte integer (-32,768 - 32,767)
   * - ``int``
     - ✓
     - 4 byte integer (-2,147,483,648 - 2,147,483,647)
   * - ``bigint``
     - ✓
     - 8 byte integer (-9,223,372,036,854,775,808 - 9,223,372,036,854,775,807)
   * - ``real``
     - ✓
     - 4 byte floating point
   * - ``double``, ``float``
     - ✓
     - 8 byte floating point
   * - ``decimal``, ``numeric``
     - Planned
     - Use ``double`` instead
   * - ``varchar``
     - ✓
     - Variable length string - ASCII only
   * - ``nvarchar``
     - ✓
     - Variable length string - UTF-8 encoded
   * - ``text``
     - Planned
     - Use ``varchar``, ``nvarchar``
   * - ``date``
     - ✓
     - Date
   * - ``datetime``, ``timestamp``
     - ✓
     - Date and time
   * - ``null``
     - ✓
     - Null value

***********
Contraints
***********

.. list-table:: Contraints
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

*************
Transactions
*************

.. list-table:: Transactions
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

*************
Indexes
*************

.. list-table:: Indexes
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

***************
Schema changes
***************

.. list-table:: Schema changes
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

*************
Statements
*************

.. list-table:: Statements
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

*************
Clauses
*************

.. list-table:: Clauses
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

******************
Table expressions
******************

.. list-table:: Table expressions
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

******************
Scalar expressions
******************

.. list-table:: Scalar expressions
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

******************
Permissions
******************

.. list-table:: Permissions
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * -
     -
     -

********************
Extra functionality
********************

.. list-table:: Extra functionality
   :widths: 30 5 65
   :header-rows: 1
   
   * - Item
     - Supported
     - Further information
   * - Information schema
     -
     -
   * - Views
     -
     -
   * - Window functions
     -
     -
   * - CTEs
     -
     -
   * - Saved queries
     -
     -
   * - Sequences
     -
     -