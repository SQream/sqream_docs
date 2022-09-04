.. _adding_individual_files:

***********************
How to Add Individual Files
***********************
This section describes how to add individual files.

**To add individual files:**

1. Click **Add file**.

    ::

2. Click **Create new file**.

    ::

.. image:: /_static/images/individual.png
    :align: right 

3. In the **name your file** field, name your file using the following syntax:

   .. code-block:: console

      <anchor_name>.rst

   .. note::  You must include ``.rst`` for the file to be created correctly. You can determine that you have omitted the file format ``.rst`` if the **Preview** function does not work.

4. Paste and modify the following syntax into the **Edit new file** region:

   .. code-block:: console

      ***********************
      <Page Title>
      ***********************
      <Page content>

5. In the **Commit changes** region, type a mandatory and/or optional commit description.

    ::

6. Click **Commit new file**. 

.. note::  Verify that **Commit directly to the <branch name> branch** is selected. This option is selected by default.

When your file is created, the anchor name is displayed at the top of the page, as follows:

.. code-block:: console

   .. _<anchor_name>:

   ***********************
   <Page Title>
   ***********************
   <Page content>