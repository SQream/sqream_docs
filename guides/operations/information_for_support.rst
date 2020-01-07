.. _information_for_support:

*******************************************
Gathering information for SQream support
*******************************************

.. What do we want to look into a performance issue

.. what about other kinds of issues

.. what about bug reports

When you encounter a problem that you can't solve by yourself, `SQream Support <http://support.sqream.com/>`_ is here to help. 

Getting support and reporting bugs
=======================================

When contacting `SQream Support <http://support.sqream.com/>`_, we recommend reporting the following information:

* What is the problem encountered?
* What was the expected outcome?
* How can SQream reproduce the issue? 

If comfortable, attach as many of the following:

* Error messages or result outputs
* DDL and queries that reproduce the issue
* :ref:Log files<logging>`
* Screen captures if relevant

SQream support may have additional questions or requests, based on the information provided.

How SQream debugs issues
===================================

Reproduce
--------------

To debug most issues, we need to reproduce the problem. Some problems are repeatable, and can be repdroduced even without accessing the problematic database.

Reproducing an issue consists of understanding:

#. What was SQream DB doing at the time?
#. How is the SQream DB cluster configured?
#. How does the schema look?
#. What is the query or statement that exposed the problem?
#. Were there any external factors? (e.g. Network disconnection, hardware failure, etc.)

See the :ref:`reproducible_statement` section ahead for information about collecting a full reproducible example.

Logs
--------

The logs produced by SQream DB contain a lot of information that may be useful for debugging.

Look for :ref:`error messages in the log and the offending statements<tracing_errors>`. SQream's support staff are experienced in correlating logs to workloads, and finding possible problems.

See the :ref:`collecting_logs` section ahead for information about collecting a set of logs that can be analyzed by SQream support.


Fix
---------

Once the issue is reproduced, it can be fixed.

A fix can be issued as a hotfix to an existing version, or as part of a bigger major release.

Your SQream account manager will keep you up-to-date about the status of the problem reported.



.. _reproducible_statement:

Collecting a reproducible example of a problematic statement
===============================================================

SQream DB contains an SQL utility that can help SQream support reproduce a problem with a query or statement.

This utility compiles and executes a statement, and collects the relevant data in a small database which can be used to recreate and investigate the issue.

SQL Syntax
---------------

.. code-block:: postgres
   
   SELECT EXPORT_REPRODUCIBLE_SAMPLE(output_path, query_stmt [, ... ])
   ;
   
   output_path ::= 
      filepath
      

Parameters
---------------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
   * - ``output_path``
     - Path for the output archive. The output file will be a tarball.
   * - ``query_stmt [, ...]``
     - Statements to analyze.

Example
-----------

.. code-block:: postgres

   SELECT EXPORT_REPRODUCIBLE_SAMPLE('/home/rhendricks', 'SELECT * FROM t', $$SELECT "Name", "Team" FROM nba$$);

.. _collecting_logs:

Collecting logs and metadata database
=============================================

SQream DB comes bundled with a data collection utility and an SQL utility intended for collecting logs and additional information that can help SQream support drill down into possible issues.

See more information in the :ref:`Collect logs from your cluster<collecting_logs>` section of the logging guide.

Examples
-----------------

Write an archive to ``/home/rhendricks``, containing log files:

.. code-block:: postgres
   
   SELECT REPORT_COLLECTION('/home/rhendricks', 'log')
   ;

Write an archive to ``/home/rhendricks``, containing log files and metadata database:

.. code-block:: postgres
   
   SELECT REPORT_COLLECTION('/home/rhendricks', 'db_and_log')
   ;
   

Using the command line utility:

.. code-block:: console
   
   $ ./bin/report_collection /home/rhendricks/sqream_storage /home/rhendricks db_and_log
