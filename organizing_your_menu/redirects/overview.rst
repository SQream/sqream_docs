.. _overview:

***********************
Overview
***********************
When you rearrange your menu items, even in the slightest way, you break existing links. For example, moving the **installing_sqream** file from the **getting_started** index file to another menu item breaks the link that once led to that page.

Compare the following URLs:

* **Previous URL:** https://docs.sqream.com/en/v2021.2/guides/features/python_functions.html

   ::

* **New URL:** https://docs.sqream.com/en/v2021.2/feature_guides/python_functions.html

.. note:: The first bullet above is a redirect. Notice that clicking it takes longer to reach the destination page, which is identical to that of the second bullet.

.. tip:: Wrap URLs with the ``code`` syntax to break links, as shown in the bullets above.

If you move that file to the **Installation Guides** section, the previous URL is broken. Even though users can still find the new page using the menu or search bar, Google searches do not index broken links, causing a **404 error**. In addition, if any user has saved a URL in his bookmarks, trying to access it will as well show a 404 error.

.. tip:: Speak with Raz Kaplan-Aviv every month about running a system-wide diagnostic to generate a list of all broken links.