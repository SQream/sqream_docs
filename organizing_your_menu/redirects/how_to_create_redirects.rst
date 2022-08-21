.. _how_to_create_redirects:

***********************
How To Create Redirects
***********************
Making a **redirect** refers to automatically redirecting a link to another, whether the link is broken or not.

**To make a redirect:**

1. Navigate to `Read-the-Docs <https://readthedocs.com/dashboard/>`_.

   .. note:: If you can't sign in, speak with Slavi Khodorkovsky, who is the **IT manager**.

   .. image:: /_static/images/redirects.png
       :align: right

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