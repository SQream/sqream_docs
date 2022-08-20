.. _links_and_ref_syntax:

***********************
Creating Links
***********************
This page describes the different types of links you can create:

.. contents:: 
   :local:
   :depth: 1

Using the :ref: Syntax
=======================
You can use the ``:ref:`` syntax to create a link directly to a page by referring to its anchor, as shown below:

.. code-block:: console

   :ref:`links_and_ref_syntax`

This is very useful because it is native to the branch where you place it, meaning that it is restricted to referring to pages on the branch you're on. This is ideal for advancing releases because it saves you from having to manually updating absolute links. The branch string on any absolute links in your documentation (except for notable exceptions) must be advanced to the next release notes branch.

For more information about notable exceptions, see :ref:`documenting_minor_releases`.

Using an Absolute Link
========================
You need to use absolute links for the notable exceptions described above.

The following is the syntax for creating an absolute link:

.. code-block:: console

   `Link text <link URL>`_

Creating a Custom Anchor
========================
A **custom anchor** is a hyperlink that takes you to another section on the page you're already on. The ideal place to use these is on a table of contents list on your page. Unless you want to customize the text that appears as the link, using the ``.. contents::`` syntax is recommended (and is less work). For example, you may the hyperlink to be in lower caps, while headings are capitalized.

**To create a custom anchor:**

1. Insert the anchor on the location of the page that you want the hyperlink to lead to.

   The following is the anchor text syntax:

   .. code-block:: console

      .. _<anchor_text>:

2. Create your custom hyperlink inline:

   The following is the custom hyperlink syntax:

   .. code-block:: console

      :ref:`link to a different section<cross-references to a location in the same document>`.

The following is an example of an anchor and custom hyperlink:

.. code-block:: console

   Managing Workers from the Workers Panel
   ------------
   From the **Workers** panel you can do the following:

   * :ref:`View workers <view_workers_>`
   * :ref:`Add a worker to a service<add_worker_to_service_>`
   * :ref:`View a worker's active query information<view_worker_query_information_>`
   * :ref:`View a worker's execution plan<view_worker_execution_plan_>`

   .. _view_workers_:

   Viewing Workers
   ^^^^^^^^
   The **Worker** panel shows each worker (``sqreamd``) running in the cluster. Each worker has a status bar that represents the status over time. The status bar is divided into 20 equal segments, showing the most dominant activity in that segment.

.. note:: The example above was taken from the `Monitoring Workers and Services from the Dashboard <https://docs.sqream.com/en/latest/sqream_studio_5.4.7/monitoring_workers_and_services_from_the_dashboard.html>`_ page.

.. tip:: You can use links in tables. For an example, see `Viewing Logs <https://docs.sqream.com/en/latest/sqream_studio_5.4.7/viewing_logs.html>`_. You can also use custom anchors between pages.

Creating a Link to a Heading on a Page
=========================
You can use the following syntax to create a link to a heading on a page:

.. code-block:: console

   `Connection string <https://docs.sqream.com/en/latest/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string>`_

Note the ``index.html#connection-string`` segment of the URL above. The ``#`` sign indicates that the segment after it is a name of a heading on a page.

To test this link, see `Connection string <https://docs.sqream.com/en/latest/connecting_to_sqream/client_drivers/jdbc/index.html#connection-string>`_.