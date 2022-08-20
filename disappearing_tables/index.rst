.. _disappearing_tables:

***********************
Why Do My Tables Keep Disappearing?
***********************
Overview
=======================
It appears that you've stumbled upon a most aggravating magic trick! You may spend a relatively considerable amount of effort making a table, only to find that it disappears from your page when you publish it. Don't pull your hairs out. Read this page instead.

The reason that you're table has disappeared is not quantum physics, but has one of the following perfectly natural explanations:

* Your defined number of column widths does not match the amount of columns in the table.

   ::

* Some portion of your table is misaligned.

Disappearing Table 1
=======================
Mismatching your column widths setting and actual column numbers causes your table to disappear, as shown below:

.. code-block:: console

  .. list-table::
     :widths: 50 50
     :header-rows: 1   
  
      * - Column 1
        - Column 2
        - Column 3
      * - Column 1, Row 1
        - Column 2, Row 1
        - Column 3, Row 1
      * - Column 3, Row 1
        - Column 3, Row 2
        - Column 3, Row 3

Note that only *two column widths* are described for the table above, although *three* are actually included in the table. So much trouble in the world.

Disappearing Table 2
=======================
Conversely, setting three column widths for two columns also causes your table to disappear, as shown below:

.. code-block:: console

   .. list-table::
      :widths: 50 50 50
      :header-rows: 1   
   
      * - Column 1
        - Column 2
      * - Column 1, Row 1
        - Column 2, Row 1
      * - Column 3, Row 1
        - Column 3, Row 2

The table width above is defined for three columns, while the table only has two. First world problems, indeed.

Example 1
=======================
The following table is misaligned as described above:

.. list-table::
   :widths: 50 50
   :header-rows: 1   
   
   * - Column 1
     - Column 2
     - Column 3
   * - Column 1, Row 1
     - Column 2, Row 1
     - Column 3, Row 1
   * - Column 3, Row 1
     - Column 3, Row 2
     - Column 3, Row 3

Do you see the table? No, you don't, because it's misaligned. Go ahead and check this file in the back-end, you'll see that the table syntax is there.

Example 2
=======================
As above, the following table doesn't appear because it's misaligned:

.. list-table::
   :widths: auto
   :header-rows: 1   
   
   * - Column 1
     - Column 2
     - Column 3
    * - Column 1, Row 1
     - Column 2, Row 1
     - Column 3, Row 1
   * - Column 3, Row 1
     - Column 3, Row 2
     - Column 3, Row 3

I promise you that the table syntax is really there! I'm trying to make things easier for you, I really am.