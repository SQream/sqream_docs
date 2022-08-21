.. _flyout_menu_protocol:

*************************
The Flyout Menu Protocol
*************************
You can switch and view branches on the front-end from the fly-out menu, located at the bottom of the documentation page.

To avoid crowding the fly-out menu, our policy is to show only major release branches on it. Because users cannot access minor branches from the fly-out menu, they can be accessed from each version from their respective release notes branch page.

For example, the 2021.1 version shows all of its related minor versions:

* Release Notes 2021.2.1.24

   ::

* Release Notes 2021.2.1

   ::

* Release Notes 2021.2

If you were to navigate to the **Latest** branch and select 2021.2.1.24 above, you would be taken to the 2021.2.1.24 release notes page. At this point you would still be viewing the Latest branch. However, all of the links on this page direct you to the 2021.2.1.24 branch itself. Once you're viewing this branch, all links direct you to the pages within that branch. This method allows us to give users access to all branches without showing all of them on the fly-out menu.

.. note:: All links you make on each branch's release notes page must use the absolute link format. Using the ``::ref:`` format links only to pages on the branch you place it in. In this case, you need to link to a page on a *different* branch.
   