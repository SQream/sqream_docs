.. _creating_new_files:

***********************
How to Create New Files
***********************
Every page on the front-end corresponds to an **.rst** file on the back-end.

There are two ways to create files. The best way to create a file is to copy an existing one and modify it according to your needs. Every content file requires the following syntactical components:

* An **anchor** to uniquely identify the file. The anchor for this page is ``creating_documenation``.

* A **title**, which determines the title of the page that appears in the menu. The title of this page is **How Do I Create Documentation?**.

Note that the anchor appears in the page URL, as shown below for this page:

.. code-block:: console

   file:///C:/Users/Yaniv/technical_documentation_handover/technical_documentation_handover/_build/html/creating_documentation/index.html

The URL above belongs to an unpublished branch and is different than URLs belonging to published branches. The following is an example of a standard URL belonging to a published branch:

.. code-block:: console

   https://docs.sqream.com/en/latest/feature_guides/index.html

The following is the syntax of the file corresponding to **this** page:

.. code-block:: console

   .. _creating_documentation:

   ***********************
   How Do I Create Documentation?
   ***********************
   Every page on the front-end corresponds to an **.rst** file on the back-end.

The other way to create a file is open a new .txt file from scratch and write it manually or by copying and pasting text into it.
