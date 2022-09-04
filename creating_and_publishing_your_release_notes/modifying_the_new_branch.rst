.. _modifying_the_new_branch:

********************************************************
Modifying the New Branch
********************************************************
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

For more information, see the following:

* :ref:`the_review_process`

   ::

* :ref:`updating_other_areas_of_the_documentation`