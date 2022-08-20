.. _tables:

***********************
Building Tables
***********************
There are two methods for building tables:

.. contents:: 
   :local:
   :depth: 1

Using Syntax to Manually Building a Table
======================
The following is the syntax for building tables:

.. code-block:: console

   .. list-table::
      :widths: 50 50
      :header-rows: 1   
   
      * - Column 1
        - Column 2
      * - Column 1, Row 1
        - Column 2, Row 1
      * - Column 1, Row 2
        - Column 2, Row 2
      * - Column 1, Row 3
        - Column 2, Row 3

The table for the above syntax looks like this:

.. list-table::
   :widths: 50 50
   :header-rows: 1   
   
   * - Column 1
     - Column 2
   * - Column 1, Row 1
     - Column 2, Row 1
   * - Column 1, Row 2
     - Column 2, Row 2
   * - Column 1, Row 3
     - Column 2, Row 3

.. warning:: Misaligning any rows or columns, or defining the wrong amount of column ``:widths:`` causes incorrect formatting and can cause your table to disappear.

             In addition, unless required, setting your ``:widths:`` to ``auto`` is recommended. This automatically sets your table (and column) width based on its contents.

Converting an Excel Table to .rst Format
======================
Converting an Excel table to .rst format is especially useful for complex tables, such as the one below:

+------------------+------------------+------------------+
| **Parameter 1**  | **Parameter 2**  | **Parameter 3**  |
+==================+==================+==================+
| Component 1                                            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+
| Component 2                                            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+
| Value            | Value            | Value            |
+------------------+------------------+------------------+

**How to convert an Excel table to .rst format:**

1. Make your table in Excel.

    ::

2. Go to the `Table Convert <https://tableconvert.com/excel-to-restructuredtext>`_ website.

    ::

3. Highlight, copy, and paste your table into the dark blue text field at the top of the page.

    ::

4. In the **Table Editor** section, click **Clear All**.

    ::

5. In the **Table Generator** section, scroll the bar to the right and select **reStructuredText**.

    ::

6. Select **Force separate lines**.

    ::

7. Copy and paste the generated table syntax into your page.

.. warning:: Misaligning any rows or columns can cause your table to disappear. The example below shows a misformatted table:

.. code-block:: console

   +------------------+------------------+---+
   | **Parameter 1**  | **Parameter 2**  | **Parameter 3**  |
   +==================+==================+==================+
   | Component 1                                            |
   +------------------+------------------+------------------+
   | Value            | Value            | Value            |
   +------------------+------------------+------------------+
   | Value            | Value            | Value            |
   +------------------+------------------+------------------+
   | Value            | Value            | Value            |
   +------------------+------------------+------------------+