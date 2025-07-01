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
^^^^^^

**Create and train model**

.. code:: sql

    CREATE [OR REPLACE] MODEL [database.schema.]model_name
    OPTIONS(model_option_list)
    AS {query_statement};

``model_option_list``:

.. code:: sql

    MODEL_TYPE = 'XGBOOST',

    MODEL_PATH = 'PATH/TO/MODEL/JSON/TO/CREATE/WITH_NAME_OF_MODEL_INCLUDED.json' -- must for xgboost

    [VERBOSITY] = {silent | info | warning | debug}

    [BOOSTER] = { 'GBTREE' | 'GBLINEAR' | 'DART' }

    [,treeBoosterParams]

    [,dartParams]

    [,linearBoosterParams]

``treeBoosterParams``: (applicable when BOOSTER = { 'GBTREE' | 'DART' }`)

.. code:: sql

    [,ETA | LEARNING_RATE] : float
    [,GAMMA | MIN_SPLIT_LOSS]
    [...]
    -- please view the parameters table under Booster Parameters section

``dartParams``:

.. code:: sql

    [,SAMPLE_TYPE] = { 'UNIFORM' | 'WEIGHTED' }
    [...]
    -- please view the parameters table under Additional parameters for Dart Booster section

``linearBoosterParams``:

.. code:: sql

    [UPDATER] = { 'SHOTGUN' | 'COORD_DESCENT' }
    [...]
    -- please view the parameters table under Additional parameters for Linear Booster section

**Inference**

.. code:: sql

    SELECT model_predict(
    [database.schema.]model_name,
    feature_col1 [,feature_column2, ...])
    FROM {query_statement};

**DROP**

.. code:: sql

    DROP MODEL [database.schema.]model_name;

Example:
^^^^^^^^

.. code:: sql

    CREATE MODEL mod
    OPTIONS
    ( model_type = 'xgboost'
    , path='/home/sqream/mod.json' --full path
    , max_depth = 10, eta = 0.3, max_bin=100
    , verbosity= 'SILENT', tree_method='APPROX'
    ) AS
    SELECT * from t_train;
Parameters
----------

XGBoost Parameters — XGBoost 2.1.3 documentation. The parameters can be divided into global parameters (appear in the syntax), general parameters (available per booster) and learning task parameters.


Global Configuration
""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - verbosity
     - "silent, info, warning, debug"
     - "Optional, default is silent"

General Parameters
""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - booster
     - "gbtree, gblinear or dart"
     - "gbtree and dart use tree based models while gblinear uses linear functions. Default is gbtree."
   * - disable_default_eval_metric
     - boolean
     - "false by default."

Booster Parameters (applicable when booster is set to gbtree or dart)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - "eta, learning_rate"
     - "float [0, 1]"
     - "Step size shrinkage used in update to prevent overfitting. Optional, default = 0.3."
   * - "gamma, min_split_loss"
     - "float [0, MAX_FLOAT]"
     - "Minimum loss reduction required to make a further partition on a leaf node of the tree. Optional, default = 0."
   * - max_depth
     - "int [0, MAX_INT]"
     - "Maximum depth of a tree. Optional, default = 6."
   * - min_child_weight
     - "int [0, MAX_INT]"
     - "Minimum sum of instance weight (hessian) needed in a child. Optional, default = 1."
   * - max_delta_step
     - "int [0, MAX_INT]"
     - "Maximum delta step we allow each leaf output to be. Optional, default = 0. If the value is set to 0, it means there is no constraint."
   * - subsample
     - "float (0,1]"
     - "Subsample ratio of the training instances. Optional, default = 1. Setting it to 0.5 means that XGBoost would randomly sample half of the training data prior to growing trees."
   * - sampling_method
     - "uniform, gradient_based"
     - "Optional, default= uniform."
   * - colsample_bytree
     - "float (0, 1]"
     - "This is a family of parameters for subsampling of columns. All colsample_by* parameters have a range of (0, 1] specify the fraction of columns to be subsampled. Optional, default = 1."
   * - colsample_bylevel
     - "float (0, 1]"
     -
   * - colsample_bynode
     - "float (0, 1]"
     -
   * - "lambda, reg_lambda"
     - "float [0, MAX_FLOAT]"
     - "L1 regularization term on weights. Increasing this value will make the model more conservative. Optional, default = 1."
   * - "alpha, reg_alpha"
     - "float [0, MAX_FLOAT]"
     - "L2 regularization term on weights. Increasing this value will make the model more conservative. Optional, default = 1."
   * - tree_method
     - "auto, exact, approx, hist"
     - "The tree construction algorithm used in XGBoost. See description in the reference paper and Tree Methods. Optional, default = auto."
   * - scale_pos_weight
     - float
     - "Control the balance of positive and negative weights. Optional, default = 1."
   * - refresh_leaf
     - boolean
     - "This is a parameter of the refresh updater. When this flag is True, tree leafs as well as tree nodes’ stats are updated. When it is False, only node stats are updated. Optional, default = True."
   * - process_type
     - "default, update"
     - "A type of boosting process to run. Optional, default = default. default: The normal boosting process which creates new trees. update: Starts from an existing model and only updates its trees."
   * - grow_policy
     - "depthwise, lossguide"
     - "Controls a way new nodes are added to the tree. Currently supported only if tree_method is set to hist or approx. Optional, default= depthwise."
   * - max_leaves
     - int
     - "Maximum number of nodes to be added. Not used by exact tree method. Optional, default = 0."
   * - max_bin
     - int
     - "Only used if tree_method is set to hist or approx. Maximum number of discrete bins to bucket continuous features. Optional, default = 256."
   * - num_parallel_tree
     - int
     - "Number of parallel trees constructed during each iteration. This option is used to support boosted random forest. Optional, default = 1."

Additional parameters for Dart Booster
""""""""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - sample_type
     - "uniform, weighted"
     - "Type of sampling algorithm. uniform: dropped trees are selected uniformly. weighted: dropped trees are selected in proportion to weight. Optional, default = uniform."
   * - normalize_type
     - "tree, forest"
     - "Type of normalization algorithm. Optional, default = tree."
   * - rate_drop
     - float
     - "Dropout rate. Optional, default = 0.0."
   * - one_drop
     - bool
     - "When this flag is enabled, at least one tree is always dropped during the dropout. Optional, default = false."
   * - skip_drop
     - float
     - "Probability of skipping the dropout procedure during a boosting iteration. Optional, default = 0.0."

Parameters for Linear Booster
"""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - "lambda, reg_lambda"
     - "float [0, MAX_FLOAT]"
     - "L2 regularization term on weights. Increasing this value will make the model more conservative. Optional, default = 0."
   * - "alpha, reg_alpha"
     - "float [0, MAX_FLOAT]"
     - "L1 regularization term on weights. Increasing this value will make the model more conservative. Optional, default = 0."
   * - updater
     - "shotgun, coord_descent"
     - "Optional, default= shotgun."
   * - feature_selector
     - "cyclic, shuffle, random, greedy"
     - "Feature selection and ordering method. Optional, default = cyclic."
   * - top_k
     - int
     - "The number of top features to select in greedy and thrifty feature selector. The value of 0 means using all the features. Optional, default = 0."

Learning Task Parameters
""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - objective
     - "reg_squarederror, reg_squaredlogerror, reg_logistic, reg_pseudohubererror, reg_absoluteerror, reg_quantileerror, binary_logistic, binary_logitraw, binary_hinge, count_poisson, survival_cox, survival_aft, rank_ndcg, rank_map, rank_pairwise, reg_gamma, reg_tweedie"
     - "Optional, default = reg_squarederror."
   * - base_score
     - float
     - "The initial prediction score of all instances, global bias. If base_margin is supplied, base_score will not be added. Default is not passing any params."
   * - eval_metric
     - "reg_squarederror, reg_squaredlogerror, reg_logistic, reg_pseudohubererror, reg_absoluteerror, reg_quantileerror, binary_logistic, binary_logitraw, binary_hinge, count_poisson, survival_cox, survival_aft, rank_ndcg, rank_map, rank_pairwise, reg_gamma, reg_tweedie, rmse (root mean square error)"
     - "Optional, default according to objective: rmsle default metric of reg_squaredlogerror, mphe default metric of reg_pseudohubererror objective."
   * - seed
     -
     - "Random number seed. Optional, default = 0."
   * - seed_per_iteration
     - boolean
     - "Seed PRNG deterministically via iterator number. Optional, default = false."

Parameters for Tweedie Regression
"""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - tweedie_variance_power
     - "float (1,2)"
     - "Parameter that controls the variance of the Tweedie distribution range. Optional, default=1.5."

Parameter for using Pseudo-Huber
""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - huber_slope
     - float
     - "A parameter used for Pseudo-Huber loss to define the δ term. Optional, default = 1.0."

Parameter for using Quantile Loss
"""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - quantile_alpha
     - "float [0, 1]"
     - "A scalar or a list of targeted quantiles. Optional, default = 0.5."

Parameter for using AFT Survival Loss survival: AFT and Negative Log Likelihood of AFT metric
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - aft_loss_distribution
     - "normal, logistic or extreme"
     - Optional

Parameters for learning to rank
"""""""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - lambdarank_pair_method
     - "mean, topk"
     - "Optional, default = topk."
   * - lambdarank_num_pair_per_sample
     - "int [1, MAX_INT]"
     - "It specifies the number of pairs sampled for each document when pair method is mean. Optional."
   * - lambdarank_normalization
     -
     - "Specify whether we need to debias input click data. Optional, default = true."
   * - lambdarank_bias_norm
     - float
     - "Lp normalization for position debiasing, default is L2. Only relevant when lambdarank_unbiased is set to true. Optional, default = 2.0."
   * - ndcg_exp_gain
     -
     - "Whether we should use the exponential gain function for NDCG. Optional, default = true."

Command Line Parameters
"""""""""""""""""""""""

.. list-table::
   :header-rows: 1

   * - Parameter Name
     - Values
     - Comments
   * - epoch_count
     - int
     - "The number of rounds for boosting. Optional, default 10."

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

