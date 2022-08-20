.. _index_files:

***********************
Index File Structure
***********************
This page teaches you how to build an **index file** and includes the following information:

.. contents:: 
   :local:
   :depth: 1

Overview
=======================
An index page includes the following syntactical elements:

* **Folder** - While the folder is not a syntactical element, the name of a folder must be identical to the index file's anchor name. For example, the **Feature Guides** folder name is **feature_guides**, which is identical to the index file's anchor - **feature_guides**. If these two are not identical, your page will not be displayed on the topic menu.

  .. warning:: If your **folder name** and **file anchor name** are not identical, your page will not be displayed on the topic menu.

* **Anchor** - An anchor is a page's unique identifier, and every page must have one. The anchor is used for nesting the page in menus and for creating cross references to it. Without an anchor, your page will not appear in menus, and you will not be able to create cross references to it. The index file name **must be** ``index`` to designate the file as an index file. The file name does *not need to be* identical to the anchor name. For example, the name of the file titled **Anatomy of a File** is **index**.

   ::

* **Page title** - The page title determines the text displayed as the name of the topic menu item. The page title does *not need to be* identical to the anchor name or the file name.

   ::

* **TOC tree** - The TOC tree uses page anchor names to determine which pages will be nested in a menu item. In addition, including a TOC tree displays the menu items as a linked bulleted list where your place it on your page.

The following is an example of the TOC tree syntax:

.. code-block:: console

   .. toctree::
      :maxdepth: 1
      :caption: Getting Started
      :glob:

      overview/index
      doc_set/index
      main_tasks/index
      platforms/index

.. warning:: If your menu item corresponds to a level 1 heading (i.e., a folder), you must include ``/index`` after the anchor name for it to be displayed in the menu. You **do not** need to include ``/index`` after an anchor name corresponding to a page.

Example
=======================
The following is the index file structure template:

.. code-block:: console

   .. _<anchor_name>:

   ***********************
   <Page Title>
   ***********************
   <Description> 

   This section describes the following features: 

   .. toctree::
      :maxdepth: 1
      :titlesonly:

      <Anchor of nested page 1>
      <Anchor of nested page 2>

The following is an example of the index file structure template using the Feature Guides index file:

.. code-block:: console

   .. _feature_guides:

   ***********************
   Feature Guides
   ***********************
   The **Feature Guides** section describes background processes that SQream uses to manage several areas of operation, such as data ingestion, load balancing, and access control. 

   This section describes the following features: 

   .. toctree::
      :maxdepth: 1
      :titlesonly:

      data_encryption
      compression
      python_functions
      workload_manager
      transactions
      concurrency_and_locks
      concurrency_and_scaling_in_sqream





