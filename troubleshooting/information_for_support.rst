.. _information_for_support:

**************************************
Gathering Information for BLUE Support
**************************************

.. What do we want to look into a performance issue

.. what about other kinds of issues

.. what about bug reports

Contact BLUE support at `blue_support@sqreamtech.com <blue_support@sqreamtech.com>`_ for any question.

Getting Support and Reporting Bugs
==================================

When contacting `BLUE Support <https://sqream.atlassian.net/servicedesk/>`_, we recommend reporting the following information:

* What is the problem encountered?
* What was the expected outcome?
* How can BLUE reproduce the issue? 

When possible, please attach as many of the following:

* Error messages or result outputs
* DDL and queries that reproduce the issue
* :ref:`Log files<logging>`
* Screen captures if relevant
* :ref:`Execution plan output<retrieving_execution_plan_output_using_studio>`

How BLUE Debugs Issues
======================

Reproduce
---------

If we are able to easily reproduce your issue in our testing lab, this greatly improves the speed at which we can fix it.

Reproducing an issue consists of understanding:

#. What was BLUE doing at the time?
#. How is the BLUE cluster configured?
#. How does the schema look?
#. What is the query or statement that exposed the problem?
#. Were there any external factors? (e.g. Network disconnection, hardware failure, etc.)

See the :ref:`reproducible_statement` section ahead for information about collecting a full reproducible example.


Fix
---

Once we have a fix, this can be issued as a hotfix to an existing version, or as part of a bigger major release.

Your BLUE account manager will keep you up-to-date about the status of the issue.

.. _reproducible_statement:

Collecting a Reproducible Example of a Problematic Statement
============================================================

BLUE contains an SQL utility that can help SQream support reproduce a problem with a query or statement.

This utility compiles and executes a statement, and collects the relevant data in a small database which can be used to recreate and investigate the issue.

SQL Syntax
----------

.. code-block:: postgres
   
   SELECT EXPORT_REPRODUCIBLE_SAMPLE(output_path, query_stmt [, ... ])
   ;
   
   output_path ::= 
      filepath
      

Parameters
----------

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
-------

.. code-block:: postgres

   SELECT EXPORT_REPRODUCIBLE_SAMPLE('/home/rhendricks', 'SELECT * FROM t', $$SELECT "Name", "Team" FROM nba$$);

.. _collecting_logs:
