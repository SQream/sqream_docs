.. _duplicating_all_changes_to_the_master_branch:

********************************************************
Duplicating All Changes to the Master Branch
********************************************************
When the time has arrived to publish the new release, you must manually copy and paste all new documentation you created in the new branch to the Master branch. The reason for this is that the new and Master branches must be identical.

.. tip:: In the first phase when you create a new branch, you should based the new branch off of the previous branch and not off of **latest**. In the event you forget to modify the **conf.py** file in your new branch, the Master branch will still be set at the default landing page on our documentation.

The best practice is to save all new documentation for each branch locally in an easy-to-find location, and manually copy all new and/or updated existing content to the correct folders in the Master branch. This ensures that all modifications you made on your new branch are documented in the Master branch.

.. tip:: Because the Master branch is the default branch users see when accessing our front-end documentation, update the Master branch before publishing the new branch.