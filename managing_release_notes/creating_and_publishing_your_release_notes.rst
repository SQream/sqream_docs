.. _creating_and_publishing_your_release_notes:


********************************************************
Creating and Publishing Your Release Notes
********************************************************
This section describes the following best practices in the **correct order** for documenting your release notes:

.. contents:: 
   :local:
   :depth: 1

Creating a New Branch
===============
When it's time to release a new version of SQream, you must create a new branch where you will document all new features. This is done by creating a new branch based on the previous branch.

**To create a new branch:**

1. From `GitHub remote <https://github.com/SQream/sqream_docs>`_, from the branch menu, select the most current branch (such as **v2022.1.1**).

     ::

2. Type a name for the new branch.

   The naming convention for branches is **vXXXX.X**, such as **v2022.1.2**. The new branch has been created and is identical to the branch you based it on.

Activating the New Branch
=========
When you create a new branch is it automatically set to **Inactive**, which means that it **cannot be accessed on the front end**, even if set to **Private** and shared with others.

**To activate the new branch:**

1. From `Read-the-Docs <https://readthedocs.com/dashboard/>`_, click **Admin**.

   A list of branches is displayed.

2. Scroll to the **Inactive Branches** area at the bottom of the page and locate the row corresponding to your new branch

     ::

3. In the row corresponding to the new branch, click **Edit**.

     ::

4. Set the branch to the following:

   * **Active** - Lets you view the branch on the front end.

      ::

   * **Hidden** - Hides the branch from the fly-out menu.

      ::

   * **Private** - Lets you view the branch only from a custom private link.
 
5. Click **Save**.

   Your new branch is moved to the **Active Branch** area at the top of the page.

For more information about private branches, see :ref:`private_branches`.

Modifying the New Branch
===============
Once you've activated your new branch you can begin modifying it. Modifying a branch refers to the following:

* Creating all required new pages and/or updating existing ones as needed.

   ::

* Updating the **conf.py** file.

Note that documenting features may require updating several areas of the documentation. For example, the Query Healer feature introduced in release notes 2022.1.1 includes two new configuration flags. When you document a new feature make sure to clarify all related new and/or existing documentation.

.. tip:: On every new page, include a link to all related documentation. For example, the `Query Healer <https://docs.sqream.com/en/latest/feature_guides/query_healer.html>`_ page includes a link to its related configuration flags.

Every branch has its own unique **conf.py** file, which is located in each branch's main folder. When you create a new branch you must modify the release version in the **Project Information** section of the **conf.py** file, as shown below:

.. code-block::

   # -- Project information -----------------------------------------------------

   project = 'SQream DB'
   copyright = '2022 SQream'
   author = 'SQream Documentation'


   # The full version, including alpha/beta/rc tags
   release = '2022.1.1'

.. warning:: The branch defined in ``release = 'yyyy.x.x'`` in the **conf.py** file associates the content of each branch with its respective content. Make sure to set this to the correct branch, or the wrong branch will be displayed on the front end.

As you're working, make sure to generate and view your build file to verify that your page formatting is correct.

.. tip:: It is recommended to begin sending your documentation for review immediately after completing your first draft, ideally giving all involved developers and PRD authors enough time to review your documentation. Occasional delays in the development process, and the introduction of last-minute changes, sometimes require you to update documentation very close to the release date. Make sure to actively reach out to and communicate with the involved parties during the review cycle. Note that the `upcoming_releases <https://app.slack.com/client/T0ARL90PK/C03NZE9DKAA>`_ Slack channel is used daily to communicate regarding important release developments.

For more information, see :ref:`the_review_process`

Creating the Release Notes Page
=================
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

Setting Up Your Topic Menu
=====================
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

2. In GitHub, navigate to **releases/index.rst**.

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

2. Create an **index** file for the current release, such as **2020.3_index.rst**.

3. In that index file, include all existing release notes pages in the ``toctree``, as in the following example:

   .. code-block::

      .. toctree::
         :maxdepth: 1
         :glob:

         2020.3.2.1
         2020.3.2
         2020.3.1
         2020.3

2. In GitHub, navigate to **releases/index.rst**.

3. Replace **2020.3** with **2020.3_index** in the ``toctree``, as shown below:

   .. code-block::

      .. toctree::
         :maxdepth: 2
         :glob:
         :hidden:

         2020.3_index
         2020.2
         2020.1

Because we do not display minor releases in the fly-out menu, this method is used to give users access to all major and minor versions released during each year.

Running a Final Review
=============
Reviewing all documentation on your new branch is the final step before duplicating the modifications to the Master branch and publishing them. During this page you want to briefly run through all documentation you created and/or updated, and follow all links to make sure that they work and direct to the correct location.

During this phase, make sure that the following are correct:

 * TOC and toctree syntax

     ::

 * As described <in other document>, make sure that your release notes landing pages uses only absolute links, and not the :ref:: syntax.

     ::

 * All links work and direct to the correct locations

     ::

 * Grammar and punctuation

Because your branch is still set to Private at this point, you can actually publish it and begin viewing it on the front end using the Private link.

For more information, see Private Branches.

Duplicating All Changes to the Master Branch
===================
When the time has arrived to publish the new release, you must manually copy and paste all new documentation you created in the new branch to the Master branch. The reason for this is that the new and Master branches must be identical.

.. tip:: In the first phase when you create a new branch, you should based the new branch off of the previous branch and not off of **latest**. In the event you forget to modify the **conf.py** file in your new branch, the Master branch will still be set at the default landing page on our documentation.

The best practice is to save all new documentation for each branch locally in an easy-to-find location, and manually copy all new and/or updated existing content to the correct folders in the Master branch. This ensures that all modifications you made on your new branch are documented in the Master branch.

.. tip:: Because the Master branch is the default branch users see when accessing our front-end documentation, update the Master branch before publishing the new branch.

Publishing the New Branch
====================
After completing all of the above, you can publish the new branch on the release date by setting it to **Public**.

For a short video describing how to set your branch to public, see 
`Setting A Branch to Public <https://drive.google.com/file/d/1xLjDPXGGmYtk8IbQkHKc6vA6z5YOHi6U/view>`_.

**To set a private branch to Public:**

1. Navigate to `Read-the-Docs <https://readthedocs.com/dashboard/>`_.

   .. note:: If you can't sign in, speak with Slavi Khodorkovsky, who is the **IT manager**.

2. In the top horizontal menu, click **Versions**.
 
    ::

3. Click **Edit** corresponding to a private branch that you want to make public.

   The branch’s status (Private/Public) is displayed on the far right in each version row.

4. Set the branch to the following and click **Save**:

   * Active

      ::

   * Public

5. Validate that the branch is being built:

   1. In **Read-the-Docs**, click **Builds**.

       ::
   
   2. In the **Recent Builds** list, check that the status of the most recent item (the top row) says either **Triggered**, **Building**, or **Uploading**. When the build is complete, the status will say **Passed**.

6. Check the front-end to validate that the page is displayed.

   If the page is not displayed in the menu, check the following:

   * That the file exists.

      ::

   * That the correct file is included in the ``toctree`` in both **index** files.

      ::

   * That the file name and anchor are identical.

      ::

   * That the file extension is **.rst** and not **.txt**.