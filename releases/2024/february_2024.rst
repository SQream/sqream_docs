.. _february_2024:

******************
February 2024
******************

``DESCRIBE SESSION QUERIES`` New Output Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The ``DESCRIBE SESSION QUERIES`` command provides an output listing running and queued queries per session, including details such as the executing role, execution time, duration, and client information. A new parameter, ``pool_name``, has been introduced to indicate the resource pool used for executing the monitored queries.


See :ref:`DESCRIBE SESSIONS<describe_sessions>`


New Filtering for ``DESCRIBE SESSIONS`` and ``AUDITLOG``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new ``INITIATED BY`` filter, which facilitates access to information about the source triggering the queries proves particularly useful for examining queries initiated either by users or by the system exclusively.

See :ref:`DESCRIBE SESSIONS<describe_sessions>` and :ref:`AUDIT LOG<audit_log>`

