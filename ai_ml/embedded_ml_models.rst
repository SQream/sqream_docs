.. _embedded_ml_models:

******************
Embedded ML Models
******************

Linear Regression
=================

AISQream empowers users to build and train machine learning models, including Linear Regression, directly within the database using SQL.

Syntax
------

.. code-block:: sql

   --# Create and train model
   CREATE [OR REPLACE] MODEL [database.schema.]model_name
   OPTIONS(model_option_list)
   AS {query_statement};

.. code-block:: text

   model_option_list:
     MODEL_TYPE = { 'LINEAR_REG' | 'XGBOOST' }
   , MODEL_PATH = 'PATH/TO/MODEL/JSON/TO/CREATE/WITH_NAME_OF_MODEL_INCLUDED.json'
   [, INITIAL_ALGORITHM = { 'SVD' | 'EIGENDECOMPOSITION' | 'QR_DECOMPOSITION' } ]
   [, GD_OPTIMIZER = { 'SGD' | 'ADAM' } ]
   [, STANDARDIZATION = TRUE | FALSE ]
   [, LEARNING_RATE = FLOAT ]
   [, EPOCH_COUNT = INT ]
   [, LOSS_FUNCTION = { 'Mse', 'L1', 'SmoothL1', 'Huber' } ]
   [, TOLERANCE = FLOAT ]

.. code-block:: sql

   --# Inference
   SELECT model_predict(
       [database.schema.]model_name,
       feature_col1 [,feature_column2, ...])
   FROM {query_statement};

   --# DROP
   DROP MODEL [database.schema.]model_name;

Parameters
----------

.. list-table:: Linear Regression Parameters
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter Name
     - Description
     - Default Value
   * - MODEL_TYPE
     - Specify the algorithm.
     - Mandatory
   * - MODEL_PATH
     - Specify the path to save the model to.
     - Mandatory
   * - INITIAL_ALGORITHM
     - Algorithm to fit linear model.
     - SVD
   * - GD_OPTIMIZER
     - Optimizer used in second phase (gradient descent).
     - ADAM
   * - STANDARDIZATION
     - Normalize features (mean = 0, std = 1).
     - FALSE
   * - LEARNING_RATE
     - Gradient descent step size.
     - 0.01
   * - EPOCH_COUNT
     - Number of full passes over data.
     - Optional
   * - LOSS_FUNCTION
     - Distance between real and predicted values.
     - Mse
   * - TOLERANCE
     - Minimal loss reduction needed to continue training.
     - 0.01

Usage Notes & Limitations
--------------------------

- Based on Nvidia RAPIDS Linear Regression.
- Training and inference support direct use of table or query expression.
- At least 2 columns must be provided for training (feature column and a label).
- The label column must be the last column in the input.
- The model is saved in `database.schema` like any other SQream object.
- `model_predict` does not work within sub-queries.
- Model export functionality is still under development.
- Recommended limit: up to 8000 features in this version.


XGBoost
=======

AISQream empowers users to train and use XGBoost models directly within the database using SQL.

Syntax
------

.. code-block:: sql

   --# Create and train model
   CREATE [OR REPLACE] MODEL [database.schema.]model_name
   OPTIONS(model_option_list)
   AS {query_statement};

.. code-block:: text

   model_option_list:
     MODEL_TYPE = 'XGBOOST',
     MODEL_PATH = 'PATH/TO/MODEL/JSON/TO/CREATE/WITH_NAME_OF_MODEL_INCLUDED.json'  -- must for xgboost
     [VERBOSITY] = {silent | info | warning | debug}
     [BOOSTER] = { 'GBTREE' | 'GBLINEAR' | 'DART' }
     [, treeBoosterParams]
     [, dartParams]
     [, linearBoosterParams]

--# Inference

.. code-block:: sql

   SELECT model_predict(
       [database.schema.]model_name,
       feature_col1 [,feature_column2, ...])
   FROM {query_statement};

--# DROP

.. code-block:: sql

   DROP MODEL [database.schema.]model_name;

Example
-------

.. code-block:: sql

   CREATE MODEL mod
   OPTIONS
   (
       model_type = 'xgboost',
       path = '/home/sqream/mod.json', -- full path
       max_depth = 10,
       eta = 0.3,
       max_bin = 100,
       verbosity = 'SILENT',
       tree_method = 'APPROX'
   ) AS
   SELECT * FROM t_train;

Parameters
----------

**Global Configuration**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - verbosity
     - silent, info, warning, debug
     - Optional, default is silent

**General Parameters**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - booster
     - gbtree, gblinear, dart
     - Default is gbtree
   * - disable_default_eval_metric
     - boolean
     - false by default

**Tree Booster Parameters (for gbtree or dart)**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - eta, learning_rate
     - float [0, 1]
     - Step size shrinkage, default = 0.3
   * - gamma, min_split_loss
     - float
     - Minimum loss reduction required to make partition, default = 0
   * - max_depth
     - int
     - Default = 6
   * - min_child_weight
     - int
     - Default = 1
   * - max_delta_step
     - int
     - Default = 0
   * - subsample
     - float (0,1]
     - Default = 1
   * - sampling_method
     - uniform, gradient_based
     - Default = uniform
   * - colsample_bytree / bylevel / bynode
     - float (0, 1]
     - Default = 1
   * - lambda, reg_lambda
     - float
     - L2 regularization, default = 1
   * - alpha, reg_alpha
     - float
     - L1 regularization, default = 1
   * - tree_method
     - auto, exact, approx, hist
     - Default = auto
   * - scale_pos_weight
     - float
     - Default = 1
   * - refresh_leaf
     - boolean
     - Default = True
   * - process_type
     - default, update
     - Default = default
   * - grow_policy
     - depthwise, lossguide
     - Default = depthwise
   * - max_leaves
     - int
     - Default = 0
   * - max_bin
     - int
     - Default = 256
   * - num_parallel_tree
     - int
     - Default = 1

**Dart Booster Parameters**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - sample_type
     - uniform, weighted
     - Default = uniform
   * - normalize_type
     - tree, forest
     - Default = tree
   * - rate_drop
     - float
     - Default = 0.0
   * - one_drop
     - bool
     - Default = false
   * - skip_drop
     - float
     - Default = 0.0

**Linear Booster Parameters**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - lambda, reg_lambda
     - float
     - Default = 0
   * - alpha, reg_alpha
     - float
     - Default = 0
   * - updater
     - shotgun, coord_descent
     - Default = shotgun
   * - feature_selector
     - cyclic, shuffle, random, greedy
     - Default = cyclic
   * - top_k
     - int
     - Default = 0 (all features)

**Learning Task Parameters**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - objective
     - e.g. reg_squarederror, binary_logistic, etc.
     - Default: reg_squarederror
   * - base_score
     - float
     - Initial prediction score
   * - eval_metric
     - e.g. rmse, logloss, etc.
     - Varies by objective
   * - seed
     - int
     - Default = 0
   * - seed_per_iteration
     - boolean
     - Default = false

Usage Notes & Limitations
--------------------------

- Based on DMLC’s XGBoost
- Training and inference can use tables or query expressions
- At least 2 columns needed (feature + label)
- Label column must be last
- Model is saved under `database.schema`
- `model_predict` doesn’t work in sub-queries
- Only one label supported
- Input features must be `Nullable Float`
- Max 8K features recommended

