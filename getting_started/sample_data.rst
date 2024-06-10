.. _sample_data:

***********
Sample Data
***********



SQream Blue offers users access to two pre-configured databases; ``master`` and ``blue_sample_data``. The ``blue_sample_data`` database includes four schemas; 

* ``public``
* ``tpch_blue1``
* ``tpch_blue10``
* ``tpch_blue100``
* ``tpch_blue1000``. 

These schemas are differentiated by their allocated storage capacities, denoted by the numbers 1, 10, 100, and 1000, representing the size in terabytes (TB) of each schema. 

Each schema within the ``blue_sample_data`` database is equipped with six TPC-H benchmark foreign tables. These tables serve as essential components for performance evaluation, containing simulated data representative of real-world scenarios.



TPC-H schema ER Diagram
=======================

.. figure:: /_static/images/tpch_tables.png
   :scale: 70 %