.. _creating_the_release_notes_page:

********************************************************
Creating the Release Notes Page
********************************************************
Once you've completed the above sections, you can create your actual release notes page. It's a good practice to document the release notes page **after** updating and/or documenting all new and/or updated features, which makes it easier to accurately and briefly summarize them.

This section describes the following:

.. contents:: 
   :local:
   :depth: 1

Summarizing the Release Version
---------------------------
Creating the release notes page refers to creating the new release's "landing page", such as `Release Notes 2022.1.2 <https://docs.sqream.com/en/latest/releases/2022.1.2.html>`_. This landing page summarizes the contents of the new release and cross-references users to all related new and/or existing documentation. Make sure to use the **Release Notes Template** document when creating your release notes page.

.. note:: Make sure that all links to other areas of the documentation on the release notes page are absolute links and not relative links (``:ref:`` syntax).The one notable exception is the links on each minor release notes page. Because we **do not show** any minor branches on the fly-out menu, users have no way to access them. Therefore, every link on each respective release notes page must be an **absolute link** pointing to its respective branch. Clicking one of these absolute links takes the user to that specific branch, where all of its features are documented. Once in that branch, all ``:ref:`` links point to only to pages within that specific branch.

.. note:: The file being called by the ``toctree`` syntax must be located in the folder containing the **index** file calling it. Even if the page's anchor exists in the TOC tree, the page will not appear on the front-end if the file is not in the same folder as the **index** file. To the converse, if the file exists, but its anchor is not in the TOC tree, users will be able to search for it using the search bar, but will not see it anywhere on the menu.

For more information about, see :ref:`links_and_ref_syntax`.

When creating your release notes page, use the :download:`Release Notes Template <release_notes_template.txt>`.

Documenting the Resolved Issues
------------------------------
**Resolved issues** are outstanding bugs that the **Development** team has resolved before a release date. Each release notes version has its own internal page classifying all bugs as either **Public** or **Private**, defined in the **Documentation Scope** column. As each bug is resolved the person working on it changes its status to **Resolved**. The only bugs that you should include on the release notes pages are those that are *both* **Public** and **Resolved**. Bugs that are not resolved are typically rolled over to the next release.

When you document a release's known issues you must only document **external**, or **public** bugs. Public bugs are those that the **Product** and **Development** team have decided should be exposed to the public in our release notes.

.. warning:: Private bugs **cannot** be exposed to the public, either because they are irrelevant to our users, or worse, we **don't want them knowing about them**, such as if they are relevant only to a particular customer.

If you need any help determining the status of bugs, speak with **Ben Esh**.

For more information about your resolved issues, see `Known and resolved issues <https://sqream.atlassian.net/projects/SQ?orderField=RANK&selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page&status=released>`_.