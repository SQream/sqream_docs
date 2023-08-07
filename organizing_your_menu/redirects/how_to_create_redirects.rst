.. _how_to_create_redirects:

***********************
How To Create Redirects
***********************

Redirects are used to automatically send users from one web page to another, typically when the original page has moved or been replaced by a new one. 

Redirect Reasons
================

.. list-table::
   :widths: 1 10 5
   :header-rows: 1
   
   * - Redirect Reason
     - Description
     - Example	
   * - Renamed Versions
     - All renamed versions, whether public or private, should be redirected. While uncommon, version names may change, requiring redirection of URLs from old versions to new ones. In certain cases, past SQreamDB versions with the letter **v** attached encountered 404 errors after the letter was removed. To handle this, use the ``$rest`` keyword to redirect from the old version and include the old version name, and redirect to the new version by including the new version name.
     - Redirect Type: Exact Redirect

       From URL: /en/v4.0/$rest

       To URL: /en/4.0/	 
   * - Archived Documentation Versions
     - Archived documentation versions, labeled as **Private**, do not appear in your Flyout menu. It's typical for outdated documentation to become obsolete and go offline. In such cases, URLs with archived versions should be redirected to URLs containing the ``latest`` version. Redirect from the archived version by incorporating its name and using the ``$rest`` keyword. To direct to the ``latest`` version, include ``latest`` in the URL.
     - Redirect Type: Exact Redirect

       From URL: /en/2021.1/$rest

       To URL: /en/latest/	 
   * - Path Changes
     - Redirects are necessary for both private and public paths that don't exist. Previously, SQreamDB documentation utilized the path ``/third_party_tools/``, which was later changed to ``/connecting_to_sqream/``. To address broken paths in a version, redirect by incorporating the version name and using the ``$rest`` keyword. Redirect to the same version with the updated path. Keep in mind that all private versions are directed to the latest version, thus this redirect applies universally.
     - **Public Version Example**

       Redirect Type: Exact Redirect

       From URL: /en/2021.2/third_party_tools/$rest

       To URL: /en/2021.2/connecting_to_sqream/

       **Private Version Example**
	   
       Redirect Type: Exact Redirect

       From URL: /en/latest/third_party_tools/$rest

       To URL: /en/latest/connecting_to_sqream/	 
   * - Deleted Page
     - Specific pages which were deleted must be redirected to a general documentation page.
     - Redirect Type: Page Redirect

       From URL: /installation_guides/docker_container.html

       To URL: /installation_guides/index.html 
   * - Path Changes and Deleted Page
     - The path ``/guides/operations/`` has been eliminated, and certain pages within it, like ``configuration`` and ``installing_sqream_with_binary``, have either been deleted or relocated to a new path. The redirection of this path should employ a ``#`` symbol.
     - Redirect Type: Exact Redirect

       From URL: /en/2021.2/guides/operations/$rest

       To URL: /en/2021.2/operational_guides/index.html#


Creating Redirects
==================

1. Navigate to `Read-the-Docs <https://readthedocs.com/dashboard/>`_ > **sqream_docs** > **Admin** > **Redirects**

    ::
	
2. Select **Add Redirect**.
   
   A **Redirects** page opens.

   .. image:: /_static/images/redirects.png
       

3. From the **Redirect Type** menu, select the redirect type you wish to create.



