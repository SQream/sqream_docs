.. _setting_up_your_topic_menu:

********************************************************
Setting Up Your Topic Menu
********************************************************
This section describes the following:

.. contents:: 
   :local:
   :depth: 1

Overview
----------------
Now that you've documented all of your new features and resolved issues, you need to add your release notes page to the topic menu. This is done slightly differently depending on whether you're documenting a major or minor release.

For example, when only a major release exists, such as `Release Notes 2020.2 <https://docs.sqream.com/en/latest/releases/2020.2.html>`_, the menu displays a link directly to the release notes landing page. However, when minor releases exist, the menu displays a link to a page that includes a link to all major and minor releases, such as for `Release Notes 2022.1 <https://docs.sqream.com/en/latest/releases/2022.1_index.html>`_.

Adding a Major Branch to the Menu
-------------------
This section desribes how to add a major branch to your menu.

**To add a major branch to your menu:**

1. Create the new release notes page.

    ::

2. In GitHub, navigate to **releases/index.rst**.

    ::

3. Add the anchor of the new release notes page to the ``toctree``, such as for **2020.3** below:

   .. code-block::

      .. toctree::
         :maxdepth: 2
         :glob:
         :hidden:

         2020.3
         2020.2
         2020.1

Adding a Minor Branch to the Menu
-------------------
This section desribes how to add a minor branch to your menu.

**To add a minor branch to your menu:**

1. Create the new release notes page.

    ::

2. Create an **index** file for the current release, such as **2020.3_index.rst**.

    ::

3. In that index file, include all existing release notes pages in the ``toctree``, as in the following example:

   .. code-block::

      .. toctree::
         :maxdepth: 1
         :glob:

         2020.3.2.1
         2020.3.2
         2020.3.1
         2020.3

4. In GitHub, navigate to **releases/index.rst**.

    ::

5. Replace **2020.3** with **2020.3_index** in the ``toctree``, as shown below:

   .. code-block::

      .. toctree::
         :maxdepth: 2
         :glob:
         :hidden:

         2020.3_index
         2020.2
         2020.1

Because we do not display minor releases in the fly-out menu, this method is used to give users access to all major and minor versions released during each year.