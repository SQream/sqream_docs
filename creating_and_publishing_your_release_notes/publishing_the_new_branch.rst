.. _publishing_the_new_branch:

********************************************************
Publishing the New Branch
********************************************************
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