{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _python_training:\
\
\
Model Training via Python\
=========================\
\
AISQream's Model Training via Python modules extends its machine learning capabilities beyond the currently embedded Linear Regression and XGBoost algorithms.\
\
This feature allows integration and usage of a broader range of Python-based ML algorithms directly within SQream\'92s GPU-accelerated environment, reducing development time for new models.\
\
Syntax\
------\
\
.. code-block:: sql\
\
   -- Algorithm registration\
   REGISTER ALGORITHM 'algorithm_name'\
   OPTIONS (\
     alg_path = 'path_to_alg_file'\
     [, train_method := Text ]  -- defaults to 'train'\
     [, predict_method := Text ]  -- defaults to 'predict'\
   );\
\
.. code-block:: sql\
\
   -- Create and train model\
   CREATE [OR REPLACE] MODEL [database.schema.]model_name\
   OPTIONS (\
     MODEL_PATH := Text,        -- path to save model\
     MODEL_TYPE := Text,        -- registered algorithm name\
     MODEL_PARAMS := Text       -- stringified map of params\
   )\
   AS \{query_statement\};\
\
.. code-block:: sql\
\
   -- Inference\
   SELECT model_predict(\
     [database.schema.]model_name,\
     feature_col1 [, feature_col2, ...]\
   )\
   FROM \{query_statement\};\
\
.. code-block:: sql\
\
   -- Drop model\
   DROP MODEL [database.schema.]model_name;\
\
   -- Drop algorithm registration\
   UNREGISTER ALGORITHM 'algorithm_name';\
\
Usage Notes\
-----------\
\
- The label column must be the **last column** in the input.\
- `alg_path` refers to the Python file containing functions, while `model_path` is where trained models are saved.\
- Python script must contain:\
  - `train()` function: accepts `cudf.DataFrame` and parameters map, returns trained model and saves it to model_path.\
  - `predict()` function: loads model and returns predictions.\
\
- Python version: **3.11** (must match SQream's prerequisites).\
- Embedded algorithms (like XGBoost and Linear Regression) **cannot be unregistered**.\
- `train_method` and `predict_method` default to `"train"` and `"predict"` unless otherwise specified.\
\
Limitations\
-----------\
\
- Algorithms persist until explicitly unregistered.\
- Python code runs under default Linux privileges and should be treated carefully.\
- Currently supports only scalar (single-value) return types.\
- Supports **chunked batch processing only**.\
- Each Python module runs per-worker and must be aligned with system ports.\
- No support for nested Python calls or arrays (yet).\
}