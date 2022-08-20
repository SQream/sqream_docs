.. _understanding_the_url:

***********************
What Does a Page's URL Show?
***********************
A page's URL contains some valuable information, and can be used to get information about your file without checking it's location on the back-end.

Published Branch Pages
======================
The following is an example of a URL of a page on a published branch:

.. code-block:: console

   https://docs.sqream.com/en/latest/feature_guides/query_healer.html

This portion of the URL is common to every page:

.. code-block:: console

   https://docs.sqream.com/en/

The string ``latest`` refers to the branch. "Latest" refers to the "Master" branch, ``feature_guides`` to the folder name containing files, and ``query_healer`` to both the file's name and unique anchor (which must be identical).

The URL of a file nested in several sub-folders looks like this:

.. code-block:: console

   https://docs.sqream.com/en/v2022.1/reference/sql/index.html

Build File Pages
======================
The following is the URL of build file, such as the build file for the 2022.1.2 release notes:

.. code-block:: console

   file:///C:/Users/Yaniv/sqream_docs/_build/html/releases/2022.1.2.html

This portion indicates the file's location:

.. code-block:: console

   file:///C:/Users/Yaniv/sqream_docs/

The string ``build/html`` indicates that this is a build file. The string ``releases`` indicates the file location, and ``2022.1.2`` is the name and anchor of the file.

.. note:: Because build files are located locally on your machine, URLs to build files can only be seen on your machine.