.. _describe_session_queries:

*****************
DESCRIBE SESSION QUERIES
*****************
The ``DESCRIBE SESSION QUERIES`` command outputs a list of queries per session, including queued queries.

Syntax
==========
The following is the correct syntax for the ``DESCRIBE SESSION QUERIES`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES  [SESSION ID <session-id>] 

Parameters
============
The following parameters can be used with the ``DESCRIBE SESSION QUERIES`` command:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - SESSION ID
     - Displays the session ID.
	 
Examples
==============
The following is an example of the ``DESCRIBE SESSIONS`` command:

.. code-block:: postgres

   DESCRIBE SESSION QUERIES SESSION ID  'b6173e04-6e2a-4266-bef0-6fc9b8ffc097';
   	 
Output
=============
Using the ``DESCRIBE SESSIONS`` command generates the following output:

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Description
     - Type
     - Example
   * - ``session_id``
     - Displays the session ID.
     - Integer
     - b6173e04-6e2a-4266-bef0-6fc9b8ffc097	 

Permissions
=============
**Comment** - *What are the permissions?*