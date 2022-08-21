.. _advancing_to_the_next_release_version:

***********************
How Do I Advance to the Next Release Version?
***********************
This page describes how to advancea branch to the next release notes version.

**To advance a documentation branch to the next release notes version:**
1. Create your new branch:


   1. From the GitHub remote platform, select a repository.

       ::

   2. From the branch menu, select the branch you want to base your new branch on.

       ::

   3. In the field displayed below the selected branch, type the name of the new branch.

      Remember that the branch naming convention is **vYYYY.##**. For example, the naming convention for the 2022.1.2 release notes branch is **v2022.1.2**.


   4. Press **Enter**.

      Your new branch is created and is 100% identical to the branch that it's based on.

2. Modify your new branch in all of the relevant ways:

   1. Create all new pages corresponding to new features.

      New features can refer to whatever the new release includes, such as new feature guide, operational guide, or configuration guide pages, etc. Some new features include new configuration flags, meaning that you have to document the new feature **and** create a page for the related new configuration flag. You can add new images, such as screenshots, if needed. For more information, see :ref:`updating_other_areas_of_the_documentation`.

   2. Modify the content of existing pages to reflect the new feature(s).

       ::

   3. Replace all absolute links to point to the new branch (except for on the actual release notes. See :ref:`flyout_menu_protocol`).

      For example, the item in the first bullet must be replaced with the item in the second:

      * ```Setting Total Device Memory Usage in SQream Instance <https://docs.sqream.com/en/v2022.1.1/configuration_guides/cuda_mem_quota.html>`_``

      * ```Setting Total Device Memory Usage in SQream Instance <https://docs.sqream.com/en/v2022.1.2/configuration_guides/cuda_mem_quota.html>`_``.

      Using the **ref** syntax avoids the need to replace absolute links (and each branch has many), but cannot be used in all cases. Because the **ref** syntax can only point to a page and not to a specific section on a page, if you want to link users to a certain section you must use an absolute link. Instead, you can use the **ref** syntax and instruct users to navigate to the correct section on the page. The **ref** syntax is **:ref:`<anchor_name>`**.

      There are certain specific cases in release notes documentation where you must use the *absolute link* instead of the **ref** syntax, as shown below:

      .. code-block::

         .. _admin_worker_flags:

            *************************
            Worker Administration Flags
            *************************
            The **Worker Administration Flags** page describes **Worker** modification type flags, which can be modified by administrators on a session and cluster basis using the ``ALTER SYSTEM SET`` command:

            * `Setting Total Device Memory Usage in SQream Instance <https://docs.sqream.com/en/v2022.1.1/configuration_guides/cuda_mem_quota.html>`_
            * `Enabling Manually Setting Reported IP <https://docs.sqream.com/en/v2022.1.1/configuration_guides/machine_ip.html>`_
            * `Setting Port Used for Metadata Server Connection <https://docs.sqream.com/en/v2022.1.1/configuration_guides/metadata_server_port.html>`_
            * `Assigning Local Network IP <https://docs.sqream.com/en/v2022.1.1/configuration_guides/use_config_ip.html>`_
            * `Enabling the Query Healer <https://docs.sqream.com/en/v2022.1.1/configuration_guides/is_healer_on.html>`_
            * `Configuring the Query Healer <https://docs.sqream.com/en/v2022.1.1/configuration_guides/healer_max_inactivity_hours.html>`_
            * `Adjusting Permitted Log-in Attempts <https://docs.sqream.com/en/v2022.1.1/configuration_guides/login_max_retries.html>`_

For more information, see :ref:`documenting_minor_releases`.