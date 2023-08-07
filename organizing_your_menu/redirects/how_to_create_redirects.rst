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
     - All renamed versions must be redirected, whether public or private. All though it is uncommon, version names may change over time. When this happens, URLs containing the old version must be redirected to URLs containing the new version name. In the past, some SQreamDB versions had the letter **v** attached to them. At some point, the letter v was removed, creating 404s. Redirect from old version by including the old version name and using the ``$rest`` keyword. Redirect to the new version by including the new version name.
     - Redirect Type: Exact Redirect

       From URL: /en/v4.0/$rest

       To URL: /en/4.0/	 
   * - Archived Documentation Versions
     - Archived documentation versions are tagged as **Private** and may not be seen in your Flyout menu. It is very common for old documentation versions to become irrelevant and go offline. When this happens, URLs containing archived versions must be redirected to URLs containing ``latest`` version. Redirect from archived version by including the archived version name and using the ``$rest`` keyword. Redirect to the ``latest`` version by including ``latest``.
     - Redirect Type: Exact Redirect

       From URL: /en/2021.1/$rest

       To URL: /en/latest/	 
   * - Path Changes
     - Non-existing paths must be redirected, whether private or public. SQreamDB documentation used to have the following path: ``/third_party_tools/`` which was replaced by ``/connecting_to_sqream/``. Redirect from version containing broken path by including version name and using the ``$rest`` keyword. Redirect to the same version and include the new path. Remember that all private versions are redirected to the latest version so the following redirect affects all.
     - **Public Version Example**

       Redirect Type: Exact Redirect

       From URL: /en/2021.2/third_party_tools/$rest

       To URL: /en/2021.2/connecting_to_sqream/

       **Private Version Example**
	   
       Redirect Type: Exact Redirect

       From URL: /en/latest/third_party_tools/$rest

       To URL: /en/latest/connecting_to_sqream/	 
   * - Deleted Page
     - Redirecting a specific page which was deleted to a general documentation page.
     - Redirect Type: Page Redirect

       From URL: /installation_guides/docker_container.html

       To URL: /installation_guides/index.html 
   * - Path Changes and Deleted Page
     - ``/guides/operations/`` is a path which was removed. Some pages within this path, such as ``configuration`` and ``installing_sqream_with_binary`` were either deleted or relocated under a different path. The path must be redirected using a ``#``.
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



