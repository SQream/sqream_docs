.. _embedded_ml_models:

******************
Embedded ML Models
******************

SQream offers support for embedded and Python-based ML models.

AISQream empowers users to build and train machine learning models, including Linear Regression and XGBoost, directly within the database using SQL.


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

**Booster Parameters (applicable when booster is set to gbtree or dart)**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Description
   * - eta, learning_rate
     - float [0, 1]
     - Step size shrinkage used in update to prevent overfitting. Optional, default = 0.3
   * - gamma, min_split_loss
     - float [0, MAX_FLOAT]
     - Minimum loss reduction required to make a further partition on a leaf node of the tree. Optional, default = 0
   * - max_depth
     - int
     - Maximum tree depth. Default = 6
   * - min_child_weight
     - int
     - Minimum sum of instance weight in a child. Default = 1
   * - max_delta_step
     - int
     - Maximum delta step. Default = 0
   * - subsample
     - float (0,1]
     - Row sampling rate. Default = 1
   * - sampling_method
     - uniform, gradient_based
     - Sampling strategy. Default = uniform
   * - colsample_bytree / bylevel / bynode
     - float (0,1]
     - Feature sampling. Default = 1
   * - lambda, reg_lambda
     - float
     - L2 regularization. Default = 1
   * - alpha, reg_alpha
     - float
     - L1 regularization. Default = 1
   * - tree_method
     - auto, exact, approx, hist
     - Algorithm for growing trees. Default = auto
   * - scale_pos_weight
     - float
     - Control for imbalanced data. Default = 1
   * - refresh_leaf
     - boolean
     - Whether to refresh leaf value after training. Default = True
   * - process_type
     - default, update
     - Type of boosting process. Default = default
   * - grow_policy
     - depthwise, lossguide
     - Tree growth policy. Default = depthwise
   * - max_leaves
     - int
     - Maximum number of leaves. Default = 0
   * - max_bin
     - int
     - Number of bins for histogram. Default = 256
   * - num_parallel_tree
     - int
     - Number of parallel trees. Default = 1


**Additional parameters for Dart Booster**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Description
   * - sample_type
     - uniform, weighted
     - Sampling method for trees to drop. Default = uniform
   * - normalize_type
     - tree, forest
     - Normalization method. Default = tree
   * - rate_drop
     - float
     - Dropout rate for trees. Default = 0
   * - skip_drop
     - float
     - Probability of skipping dropout. Default = 0


**Parameters for Linear Booster**

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Parameter Name
     - Values
     - Description
   * - updater
     - shotgun, coord_descent
     - Optimization algorithm. Default = shotgun
   * - feature_selector
     - cyclic, shuffle, greedy, thrifty
     - Feature selection strategy. Default = cyclic


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

- Based on DMLC’s XGBoost.
- Training and inference can read directly from a table or query.
- At least 2 columns needed (features + label).
- Label must be last column.
- `model_predict` not allowed inside subqueries.
- Only one label column supported.
- Input features must be `Nullable Float`.
- Model is stored under `database.schema`.
- Export still under development.
- Max recommended: 8K features.

