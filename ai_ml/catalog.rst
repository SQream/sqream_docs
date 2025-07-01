{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _catalog:\
\
\
Catalog Tables\
==============\
\
AISQream includes system catalog tables that store metadata about ML models, Python modules, and registered algorithms. These tables are queryable using SQL and help users monitor and manage registered objects.\
\
Catalog Table: ml_models\
-------------------------\
\
Contains all ML models with general information.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.ml_models;\
\
.. list-table::\
   :widths: 20 20 20 20 20\
   :header-rows: 1\
\
   * - model_id\
     - database\
     - schema\
     - name\
     - ml_alg\
   * - 10\
     - master\
     - public\
     - m1\
     - LINEAR_REG\
   * - 11\
     - master\
     - public\
     - ml_xgb_catalog_test\
     - XGBOOST\
   * - 9\
     - master\
     - public\
     - m\
     - PY_MODEL\
\
Catalog Table: ml_linear_reg\
----------------------------\
\
Stores additional configuration for Linear Regression models.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.ml_linear_reg;\
\
Sample schema (simplified):\
\
- model_id\
- initial_algorithm\
- gd_optimizer\
- coefficients\
- learning_rate\
- loss_function\
- tolerance\
- epoch_count\
\
Catalog Table: ml_xgboost\
-------------------------\
\
Stores configuration for XGBoost models.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.ml_xgboost;\
\
Includes full list of booster parameters (eta, max_depth, sampling_method, etc.), evaluation metrics, and seed configuration.\
\
Catalog Table: py_modules\
--------------------------\
\
Lists all registered Python modules.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.py_modules;\
\
Fields include:\
\
- module_id\
- database_name\
- module_name\
- path\
- entry_points\
\
Catalog Table: py_module_permissions\
------------------------------------\
\
Tracks which roles have permissions to use modules.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.py_module_permissions;\
\
Fields:\
\
- database_name\
- module_id\
- role_id\
- permission_type\
\
Catalog Table: registered_algorithms\
------------------------------------\
\
Contains all registered Python-based ML algorithms.\
\
.. code-block:: sql\
\
   SELECT * FROM sqream_catalog.registered_algorithms;\
\
Fields:\
\
- id\
- database_name\
- alg_name\
- alg_path\
- train_method\
- predict_method\
}