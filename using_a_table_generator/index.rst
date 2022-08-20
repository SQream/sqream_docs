.. _using_a_table_generator:

***********************
How Do I Make Tables Easily?
***********************
Converting an Excel table to .rst format is especially useful for complex tables, such as the one below:

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

For more information, see :ref:`tables`.