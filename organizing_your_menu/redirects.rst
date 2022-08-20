.. _redirects:

***********************
Why Do I Need Redirects?
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

Making a **redirect** refers to automatically redirecting a link to another, whether the link is broken or not.

**To make a redirect:**

1. Navigate to `Read-the-Docs <https://readthedocs.com/dashboard/>`_.

   .. note:: If you can't sign in, speak with Slavi Khodorkovsky, who is the **IT manager**.

2. Click **sqream / sqream_docs**.

    ::

3. Click **Admin**.

    ::

4. Click **Redirects**.

    ::

5. Scroll to the bottom of the page, and from the **Redirect Type** select **Exact Redirect**.

    ::

6. Paste the broken and new URLs, as shown in the following example:

   * **From URL** :/en/v2021.2/guides/features/python_functions.htm

        ::

   * **To URL** :/en/v2021.2/feature_guides/python_functions.html

   I created the redirect above after deleting the **Guides** section and renaming the **Features** section **Feature Guides**.

   .. note:: The string you put in both fields must follow the above format or the redirect will not be created.

7. Repeat **Step 6** for all branches.

   .. tip:: Prepare your **From URL** and **To URL** fields in an Excel sheet.