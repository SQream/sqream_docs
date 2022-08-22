.. _setting_a_branch_to_public:

***********************
Setting A Branch to Public
***********************
I’ve made and prepared the 2022.1.2 release branch and set it to **Private**. This allows us to view it without publishing it on the front-end. Because I’ve documented all the features and resolved issues, all you need to do to publish it is to set it to **Public**.

For a short video describing how to set your branch to public, see 
`Setting A Branch to Public <https://drive.google.com/file/d/1xLjDPXGGmYtk8IbQkHKc6vA6z5YOHi6U/view>`_.

**To set a private branch to Public:**

1. Navigate to `Read-the-Docs <https://readthedocs.com/dashboard/>`_.

   .. note:: If you can't sign in, speak with Slavi Khodorkovsky, who is the **IT manager**.

2. Do one of the following:

   * **If the branch is not active** - At the bottom of the page in the **Activate a version** section, click **Activate** corresponding to a branch that you want to make Active. Activating a branch displays it on the top half of the screen. The **2022.1.2** branch is Active.

        ::

   * **If the branch is already active** – Continue to **Step 3** below.

3. In the top horizontal menu, click **Versions**.
 
    ::

4. Click **Edit** corresponding to a private branch that you want to make public.

   The branch’s status (Private/Public) is displayed on the far right in each version row.

5. Set the branch to the following and click **Save**:

   • Active

      ::

   • Public

6. Validate that the branch is being built:

   1. In **Read-the-Docs**, click **Builds**.

       ::
   
   2. In the **Recent Builds** list, check that the status of the most recent item (the top row) says either **Triggered**, **Building**, or **Uploading**. When the build is complete, the status will say **Passed**.

7. Check the front-end to validate that the page is displayed.

   If the page is not displayed, check the page syntax of 