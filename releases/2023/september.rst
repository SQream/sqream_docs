.. _september_2023:

**************************
September 2023
**************************

SQream is introducing a new version release system that follows the more commonly used Major.Minor.Patch versioning schema. The newly released **4.0 version** is a minor version upgrade and does not require considerable preparation.

The 4.3 release notes were released on xx/xx/xxxx and describe the following:

.. contents:: 
   :local:
   :depth: 1      

New Features
------------

 
 
Newly Released Connector Drivers
--------------------------------


 
SQream Studio Updates and Improvements
--------------------------------------

SQream Studio v5.5.4 has been released. 

	::

Known Issues
------------

* :ref:`Percentile<percentile_disc>` is not supported for :ref:`Window Functions<window_functions>`.

* Performance degradation when using ``VARCHAR`` partition key in a :ref:`Window Functions<window_functions>` expression



Resolved Issues
-----------------------------

+------------------------+------------------------------------------------------------------------------------------+
|  **SQ No.**            | **Description**                                                                          |
+========================+==========================================================================================+
| SQ-11108               | Slow ``COPY FROM`` statements using ORC files                                            |
+------------------------+------------------------------------------------------------------------------------------+  


Naming Changes
--------------
No naming changes


Deprecated Features
-------------------

► ``INT96``

Due to Parquet's lack of support of the ``INT96`` data type, SQream has decided to deprecate this data type.


► Square Brackets ``[]``

The ``[]``, which are frequently used to delimit :ref:`identifiers<keywords_and_identifiers>` such as column names, table names, and other database objects, will soon be deprecated to facilitate the use of the ``ARRAY`` data type.

* Support in ``[]`` for delimiting database object identifiers ends on June 1st, 2023.
* To delimit database object identifiers, you will be able to use double quotes ``""``.


► ``VARCHAR``

The ``VARCHAR`` data type is deprecated to improve the core functionalities of the platform and to align with the constantly evolving ecosystem requirements.

* Support in the ``VARCHAR`` data type ends at September 30th, 2023.
* ``VARCHAR`` is no longer supported for new customers, effective from Version 2022.1.3.  
* The ``TEXT`` data type is replacing the ``VARCHAR`` and ``NVARCHAR`` data types.


End of Support
---------------
No End of Support changes were made.

  
