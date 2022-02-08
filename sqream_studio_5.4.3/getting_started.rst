.. _getting_started:

****************************
Getting Started with SQream Acceleration Studio 5.4.3
****************************
Setting Up and Starting Studio
----------------
Studio is included with all `dockerized installations of SQream DB <https://docs.sqream.com/en/v2020.3.1/guides/operations/setup/local_docker.html#installing-sqream-db-docker>`_. When starting Studio, it listens on the local machine on port 8080.

Logging In to Studio
---------------
**To log in to SQream Studio:**

1. Open a browser to the host on **port 8080**.

   For example, if your machine IP address is ``192.168.0.100``, insert the IP address into the browser as shown below:

   .. code-block:: console

      $ http://192.168.0.100:8080

2. Fill in your SQream DB login credentials. These are the same credentials used for :ref:`sqream sql<sqream_sql_cli_reference>` or JDBC.

   When you sign in, the License Warning is displayed.
   
Navigating Studio's Main Features
-------------
When you log in, you are automatically taken to the **Editor** screen. The Studio's main functions are displayed in the **Navigation** pane on the left side of the screen.

From here you can navigate between the main areas of the Studio:

.. list-table::
   :widths: 10 90
   :header-rows: 1   
   
   * - Element
     - Description
   * - :ref:`Dashboard<monitoring_workers_and_services_from_the_dashboard>`
     - Lets you monitor system health and manage queues and workers.
   * - :ref:`Editor<executing_statements_and_running_queries_from_the_editor>`
     - Lets you select databases, perform statement operations, and write and execute queries.   
   * - :ref:`Logs<viewing_logs>`
     - Lets you view usage logs.
   * - :ref:`Roles<creating_assigning_and_managing_roles_and_permissions>`
     - Lets you create users and manage user permissions.
   * - :ref:`Configuration<configuring_your_instance_of_sqream>`
     - Lets you configure your instance of SQream.

By clicking the user icon, you can also use it for logging out and viewing the following:

* User information
* Connection type
* SQream version
* SQream Studio version
* License expiration date
* License storage capacity
* Log out

.. _back_to_dashboard_5.4.3:

.. _studio_dashboard_5.4.3:
