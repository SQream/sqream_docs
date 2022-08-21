.. _private_branches:

***********************
What Are Private Branches?
***********************
Private branches are branches that you want to make accesible to people at SQream without publishing them. You can set branches to private in Read-the-Docs.

**To set a branch to private:**

1. Log in to Read-the-Docs.

   If you cannot log in to Read-the-Docs, speak with Slavi.

2. At the bottom of the page in the **Activate a version** section, click **Activate** corresponding to a branch that you want to share.

   When you create a new branch, it is automatically inactive.

3. In the top horizontal menu, click **Versions**.

    ::

4. Click **Edit** corresponding to a private branch that you want to share.

   The branch's status (Private/Public) is displayed on the far right in each version row.

5. Set the branch to the following and click **Save**:

   * Active
   * Hidden
   * Private

6. In the top horizontal menu, click **Admin**.

    ::

7. In the left vertical menu, click **Sharing**.

    ::

8. Click **New Share**.

    ::

9. From the **Access type** dropdown menu, select **Secret link**.

    ::

10. In the **Expires** field, set an expiration date for the secret link.

     ::

11. (Optional) In the **Description** field write a description to indicate the purpose of the private branch you're sharing.

     ::

12. Clear **Grant access to all versions for this project or select individual versions**.

     ::

13. From the **Versions** panel, select a private branch you want to share.

    A private link is generated for the private branch you selected to share in the **Sharing** section. You can provide this link to anybody at SQream to let them view a branch before publishing it. The link directs users to SQream's home documentation page corresponding to this private branch. You can direct users to a specific page by appending the link with your desired path as follows:

   .. code-block:: console

      https://docs.sqream.com/_/sharing/Af30ZOGNth4lmS47HKL6hc2UWN9pbAoA?next=/en/v2022.1.1/getting_started/index.html

   .. note:: Private branches are visible on the flyout menu only by clicking on a private link. Users viewing the front-end from a public branch cannot see any private branches.