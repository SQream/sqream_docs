.. _releases:

*************
Release Notes
*************

:ref:`March 2024 <march_2024>`

* Introducing new **Dashboard** charts for monitoring and responding to system changes:

  * Worker Loads
  * Queued Statements
  * Jobs
  * Tasks 
  
* We've improved the ``DESCRIBE SESSION QUERIES`` command, allowing ``SUPERUSER`` roles to investigate multiple sessions.

* You now have the ability to grant temporary access to a BLUE support team member. This feature is beneficial for having our support team validate usage and perform checks on your specific environment. 

* We've improved the ``DESCRIBE COLUMNS`` command, allowing you to list information about ``VIEW`` columns.

:ref:`February 2024 <february_2024>`

* The ``DESCRIBE SESSION QUERIES`` command now provides the name of the resource pool used with each query execution.
* With a new filter, you can now choose to concentrate on either user-initiated or system-initiated operations when monitoring your daily workflows through the ``DESCRIBE SESSIONS`` and ``AUDITLOG`` commands.
* Use the new ``IsCastable`` function to safely check if a cast operation is supported for a given column and data type, providing an alternative within a ``CASE`` statement when an exception occurs.

:ref:`December 2023 <december_2023>`

* Now, through the UI, you can terminate executed jobs, especially useful in cases of delays or resource consumption. It's beneficial when a job awaits a resource held by another job or different cluster users, preventing issues during execution. 
* Users can seamlessly transfer existing jobs between clusters, crucial for data teams looking to expedite data movement tasks. 
* The integration of Python scripts into database operations enhances automation, allowing users to schedule and execute routine tasks efficiently, reducing manual effort and minimizing errors. Python's scripting flexibility enables agile development, fostering an iterative and responsive approach to database job creation.

:ref:`November 2023 <november_2023>`

* BLUE now leverages Apache Calcite for precise query interpretation, transforming queries efficiently with its algebraic representation and cost-based optimizer. 
* You can seamlessly share Jobs with specific team members, streamlining workflow and project expansion. 
* The new CLI table view feature enhances data querying in BLUE, offering improved readability and organization, along with visual representations for easier comprehension and navigation.

:ref:`October 2023 <october_2023>`

* You can now schedule jobs with greater precision, choosing hourly or minute-based execution for SQL workflows. 
* Regarding security, our recent penetration test successfully addressed all SOC2 Type 2 findings, strengthening our security measures. 
* We introduced character limits within ``JSON`` scripts for Job and task names and descriptions to enhance system security.

:ref:`September 2023 <september_2023>`

* Quickly check Worker availability with the Resource Availability Status, distinguish active clusters from suspended ones, and resize your BLUE cluster as needed for enhanced parallelism. 
* The ``AUDITLOG`` command now offers insights into essential client actions, including system events and resource management.

:ref:`July 2023 <july_2023>`

* Introducing the new ``DESCRIBE POOLS`` Command, listing existing resource pools and configurations, like pool name, allocation count, policies, and ID. 
* Boost efficiency with multi-statement execution, executing multiple SQL statements in one script. 
* Explore the new BLUE dashboard with **Job** action metrics, tracking job and task statuses for enhanced performance insights.
   
:ref:`June 2023 <june_2023>`

* Explore the capabilities of **Jobs**, a versatile SQL workflow management tool automating complex sequences of SQL scripts for seamless data preparation and insights delivery. 
* Optimize resource utilization with the **Resource Pool** panel, efficiently managing costs and enhancing cluster performance.

:ref:`May 2023 <may_2023>`

* Auth0's powerful capabilities empower BLUE to provide IDP authentication, multi-factor authentication, encryption, and anomaly detection, ensuring robust user data protection and access control. 
* Benefit from automatic suspension and resumption of your BLUE environment, efficiently managing resources during inactivity.
* BLUE is now available on the Google Cloud Platform (GCP) Marketplace, streamlining deployment for enhanced flexibility and scalability.
   


.. toctree::
   :maxdepth: 1
   :glob:
   :hidden:

   2024/march_2024
   2024/february_2024
   2023/december_2023
   2023/november_2023
   2023/october_2023
   2023/september_2023
   2023/july_2023
   2023/june_2023
   2023/may_2023