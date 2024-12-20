.. _getting_started:

***********************************************
Getting Started with SQream Acceleration Studio
***********************************************

Setting Up and Starting Studio
------------------------------

When starting Studio, it listens on the local machine on port 8080.

Logging In to Studio
--------------------

1. Open a browser to the host on **port 8080**.

   For example, if your machine IP address is ``192.168.0.100``, insert the IP address into the browser as shown below:

   .. code-block:: console

      $ http://192.168.0.100:8080

2. Fill in your SQream DB login credentials. These are the same credentials used for :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

   When you sign in, the License Warning is displayed.
   
.. _monitoring_workers_and_services_from_the_dashboard:
   
Navigating Studio's Main Features
---------------------------------

When you log in, you are automatically taken to the **Editor** screen. The Studio's main functions are displayed in the **Navigation** pane on the left side of the screen.

From here you can navigate between the main areas of the Studio:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Editor<executing_statements_and_running_queries_from_the_editor>`
     - Lets you select databases, perform statement operations, and write and execute queries.   
   * - :ref:`Logs<viewing_logs>`
     - Lets you view usage logs.
   * - :ref:`Roles<creating_assigning_and_managing_roles_and_permissions>`
     - Lets you create users and manage user permissions.
   * - :ref:`Configuration<configuring_your_instance_of_sqream>`
     - Lets you configure your instance of SQream.

By clicking the user icon, you can view the following:

* User information
* Connection type
* SQream version
* SQream Studio version
* License expiration date
* License storage capacity
* :ref:`Activity report<view_activity_report>`     
* Log out

.. _view_activity_report:

View Activity Report
--------------------

The **View activity report** menu item enables you to monitor storage and resource usage, including GPUs, workers, and machines. You can select different time frames to view cluster activity and export the data as a PDF for use in financial records, briefings, or quarterly and yearly reports.