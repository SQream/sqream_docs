.. _sample_data:

***********
Sample Data
***********

SQream Blue offers users access to two pre-configured databases; ``master`` and ``blue_sample_data``. The ``blue_sample_data`` database includes four schemas with `TPC-H <https://www.tpc.org/tpch/>`_ and `TPCxBB <https://www.tpc.org/tpcx-bb>`_ sample data sets; 

* ``public``
* ``tpch_blue1``
* ``tpch_blue10``
* ``tpch_blue100``
* ``tpch_blue1000``
* ``tpcxbb_1tb``
* ``tpcxbb_30tb``. 

Schemas are differentiated by their allocated storage capacities:

* ``TPC-H``  denoted by the numbers 1, 10, 100, and 1000, representing the size in gigabytes (GB) of each schema. 
* ``TPCxBB`` denoted by the numbers 1, 30 representing the size in terabytes (TB) of each schema.

TPC-H schema ER Diagram
=======================

.. figure:: /_static/images/tpch_tables.png
   :scale: 60 %
   
Sample TPC-H Queries
====================

Here, you can find two TPC-H queries designed to answer two business questions. For all TPC-H queries, click `here <https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf>`_.

Minimum Cost Supplier Query 
---------------------------

This query finds which supplier should be selected to place an order for a given part in a given region. 

Business Question 
^^^^^^^^^^^^^^^^^

The Minimum Cost Supplier Query finds, in a given region, for each part of a certain type and size, the supplier who can supply it at minimum cost. If several suppliers in that region offer the desired part type and size at the same (minimum) cost, the query lists the parts from suppliers with the 100 highest account balances. For each supplier, the query lists the supplier's account balance, name and nation; the part's number and manufacturer; the supplier's address, phone number and comment information. 

Functional Query Definition 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the first 100 selected rows 

.. code-block:: postgres

	SELECT
	  s_acctbal,
	  s_name,
	  n_name,
	  p_partkey,
	  p_mfgr,
	  s_address,
	  s_phone,
	  s_comment
	FROM
	  part,
	  supplier,
	  partsupp,
	  nation,
	  region
	WHERE
	  p_partkey = ps_partkey
	  AND s_suppkey = ps_suppkey
	  AND p_size = [SIZE]
	  AND p_type like '%[TYPE]'
	  AND s_nationkey = n_nationkey
	  AND n_regionkey = r_regionkey
	  AND r_name = '[REGION]'
	  AND ps_supplycost = (
	    SELECT
	      MIN(ps_supplycost)
	    FROM
	      partsupp, supplier,
	      nation, region
	    WHERE
	      p_partkey = ps_partkey 
	      AND s_suppkey = ps_suppkey 
	      AND s_nationkey = n_nationkey 
	      AND n_regionkey = r_regionkey 
	      AND r_name = '[REGION]' 
	  )
	ORDER BY
	  s_acctbal desc,
	  n_name,
	  s_name,
	  p_partkey;
	  
Shipping Priority Query
-----------------------

This query retrieves the 10 unshipped orders with the highest value. 

Business Question 
^^^^^^^^^^^^^^^^^

The Shipping Priority Query retrieves the shipping priority and potential revenue, defined as the sum of l_extendedprice * (1-l_discount), of the orders having the largest revenue among those that had not been shipped as of a given date. Orders are listed in decreasing order of revenue. If more than 10 unshipped orders exist, only the 10 orders with the largest revenue are listed. 

Functional Query Definition 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the first 10 selected rows 

.. code-block:: postgres

	SELECT
	  l_orderkey,
	  sum(l_extendedprice * (1 - l_discount)) as revenue,
	  o_orderdate,
	  o_shippriority
	FROM
	  customer,
	  orders,
	  lineitem
	WHERE
	  c_mktsegment = '[SEGMENT]'
	  AND c_custkey = o_custkey
	  AND l_orderkey = o_orderkey
	  AND o_orderdate < date '[DATE]'
	  AND l_shipdate > date '[DATE]'
	GROUP BY
	  l_orderkey,
	  o_orderdate,
	  o_shippriority
	ORDER BY
	  revenue desc,
	  o_orderdate;
