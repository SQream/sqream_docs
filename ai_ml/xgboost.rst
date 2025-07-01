{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _xgboost:\
\
\
XGBoost\
=======\
\
AISQream empowers users to train and use XGBoost models directly within the database using SQL.\
\
Syntax\
------\
\
.. code-block:: sql\
\
   --# Create and train model\
   CREATE [OR REPLACE] MODEL [database.schema.]model_name\
   OPTIONS(model_option_list)\
   AS \{query_statement\};\
\
.. code-block:: text\
\
   model_option_list:\
     MODEL_TYPE = 'XGBOOST',\
     MODEL_PATH = 'PATH/TO/MODEL/JSON/TO/CREATE/WITH_NAME_OF_MODEL_INCLUDED.json'  -- must for xgboost\
     [VERBOSITY] = \{silent | info | warning | debug\}\
     [BOOSTER] = \{ 'GBTREE' | 'GBLINEAR' | 'DART' \}\
     [, treeBoosterParams]\
     [, dartParams]\
     [, linearBoosterParams]\
\
--# Inference\
\
.. code-block:: sql\
\
   SELECT model_predict(\
       [database.schema.]model_name,\
       feature_col1 [,feature_column2, ...])\
   FROM \{query_statement\};\
\
--# DROP\
\
.. code-block:: sql\
\
   DROP MODEL [database.schema.]model_name;\
\
Example\
-------\
\
.. code-block:: sql\
\
   CREATE MODEL mod\
   OPTIONS\
   (\
       model_type = 'xgboost',\
       path = '/home/sqream/mod.json', -- full path\
       max_depth = 10,\
       eta = 0.3,\
       max_bin = 100,\
       verbosity = 'SILENT',\
       tree_method = 'APPROX'\
   ) AS\
   SELECT * FROM t_train;\
\
Parameters\
----------\
\
**Global Configuration**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - Parameter Name\
     - Values\
     - Comments\
   * - verbosity\
     - silent, info, warning, debug\
     - Optional, default is silent\
\
**General Parameters**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - Parameter Name\
     - Values\
     - Comments\
   * - booster\
     - gbtree, gblinear, dart\
     - Default is gbtree\
   * - disable_default_eval_metric\
     - boolean\
     - false by default\
\
**Tree Booster Parameters (for gbtree or dart)**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - Parameter Name\
     - Values\
     - Comments\
   * - eta, learning_rate\
     - float [0, 1]\
     - Step size shrinkage, default = 0.3\
   * - gamma, min_split_loss\
     - float\
     - Minimum loss reduction required to make partition, default = 0\
   * - max_depth\
     - int\
     - Default = 6\
   * - min_child_weight\
     - int\
     - Default = 1\
   * - max_delta_step\
     - int\
     - Default = 0\
   * - subsample\
     - float (0,1]\
     - Default = 1\
   * - sampling_method\
     - uniform, gradient_based\
     - Default = uniform\
   * - colsample_bytree / bylevel / bynode\
     - float (0, 1]\
     - Default = 1\
   * - lambda, reg_lambda\
     - float\
     - L2 regularization, default = 1\
   * - alpha, reg_alpha\
     - float\
     - L1 regularization, default = 1\
   * - tree_method\
     - auto, exact, approx, hist\
     - Default = auto\
   * - scale_pos_weight\
     - float\
     - Default = 1\
   * - refresh_leaf\
     - boolean\
     - Default = True\
   * - process_type\
     - default, update\
     - Default = default\
   * - grow_policy\
     - depthwise, lossguide\
     - Default = depthwise\
   * - max_leaves\
     - int\
     - Default = 0\
   * - max_bin\
     - int\
     - Default = 256\
   * - num_parallel_tree\
     - int\
     - Default = 1\
\
**Dart Booster Parameters**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - sample_type\
     - uniform, weighted\
     - Default = uniform\
   * - normalize_type\
     - tree, forest\
     - Default = tree\
   * - rate_drop\
     - float\
     - Default = 0.0\
   * - one_drop\
     - bool\
     - Default = false\
   * - skip_drop\
     - float\
     - Default = 0.0\
\
**Linear Booster Parameters**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - lambda, reg_lambda\
     - float\
     - Default = 0\
   * - alpha, reg_alpha\
     - float\
     - Default = 0\
   * - updater\
     - shotgun, coord_descent\
     - Default = shotgun\
   * - feature_selector\
     - cyclic, shuffle, random, greedy\
     - Default = cyclic\
   * - top_k\
     - int\
     - Default = 0 (all features)\
\
**Learning Task Parameters**\
\
.. list-table::\
   :widths: 30 30 40\
   :header-rows: 1\
\
   * - objective\
     - e.g. reg_squarederror, binary_logistic, etc.\
     - Default: reg_squarederror\
   * - base_score\
     - float\
     - Initial prediction score\
   * - eval_metric\
     - e.g. rmse, logloss, etc.\
     - Varies by objective\
   * - seed\
     - int\
     - Default = 0\
   * - seed_per_iteration\
     - boolean\
     - Default = false\
\
Usage Notes & Limitations\
--------------------------\
\
- Based on DMLC\'92s XGBoost\
- Training and inference can use tables or query expressions\
- At least 2 columns needed (feature + label)\
- Label column must be last\
- Model is saved under `database.schema`\
- `model_predict` doesn\'92t work in sub-queries\
- Only one label supported\
- Input features must be `Nullable Float`\
- Max 8K features recommended\
}