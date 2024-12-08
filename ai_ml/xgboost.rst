.. _xgboost:

*******
XGBoost
*******

XGBoost (Extreme Gradient Boosting) is a powerful supervised machine learning algorithm based on decision trees, designed for both regression and classification tasks. It uses an ensemble of weak learners (typically decision trees) to build a strong predictive model through a process called gradient boosting, where each tree corrects the errors of the previous ones.

XGBoost is known for its speed, scalability, and high performance, thanks to optimizations like parallel processing, tree pruning, and handling missing values efficiently. It’s commonly used in competitive machine learning and practical applications like recommendation systems, risk assessment, and anomaly detection.

Syntax
------

.. code-block:: postgres

	# Create and train model
	CREATE [OR REPLACE] MODEL [database.schema.]model_name
	OPTIONS(model_option_list)
	AS {query_statement}

	model_option_list:
		MODEL_TYPE = 'XGBOOST'
		[VERBOSITY] = { 0 | 1 | 2 | 3 } -- 0=silent, 1=warning, 2=info, 3=debug, default=0
		[BOOSTER] = { 'GBTREE' | 'GBLINEAR' | 'DART' }
		[,treeBoosterParams]
		[,dartParams]
		[,linearBoosterParams]
		  
	treeBoosterParams :== --applicable when BOOSTER = { 'GBTREE' | 'DART' }
	  [,ETA | LEARNING_RATE] : float [0, 1]
	  [,GAMMA | MIN_SPLIT_LOSS]
	  [...]
	  -- please view the parameters table under Booster Parameters section
	  
	dartParams :==
	  [,SAMPLE_TYPE] = { 'UNIFORM' | 'WEIGHTED' }
	  [...]
	  -- please view the parameters table under Additional parameters for Dart Booster section

	,linearBoosterParams :==
	  [UPDATER] = { 'SHOTGUN' | 'COORD_DESCENT' }
	  [...]
	  -- please view the parameters table under Additional parameters for Linear Booster section  

	# Inference
	SELECT model_predict(
		[database.schema.]model_name,
		feature_col1 [,feature_column2, ...])
	FROM {query_statement};

	# DROP
	DROP MODER [database.schema.]model_name;
	
	
Parameters
----------

The parameters are divided to Global parameters (embedded in the syntax), general parameters (available per booster) and learning task parameters.

The parameters will be defined in the following table:

 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | **Parameter Name**              | **Parameter Type**                       | **Description**                                                             | **Comments**                                                                                                  |
 +=================================+==========================================+=============================================================================+===============================================================================================================+
 | ``verbosity``                   | Global Configuration                     | * ``0`` = silent                                                            | Optional, default is ``0``                                                                                    |
 |                                 |                                          | * ``1`` = warning                                                           |                                                                                                               |
 |                                 |                                          | * ``2`` = debug                                                             |                                                                                                               |
 |                                 |                                          | * ``3`` = info                                                              |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``booster``                     | General Parameters                       | ``gbtree``, ``gblinear`` or ``dart``                                        | ``gbtree`` and ``dart`` use tree based models while ``gblinear`` uses linear functions. Default is ``gbtree`` |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``disable_default_eval_metric`` | General Parameters                       | ``boolean``                                                                 | ``FALSE`` by default                                                                                          |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``eta`` , ``learning_rate``     | Booster Parameters                       | Step size shrinkage used in update to prevent over-fitting. ``float`` [0,1] | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``0.3``                         |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``gamma`` , ``min_split_loss``  | Booster Parameters                       | Minimum loss reduction required to make a further partition on a leaf node  | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | of the tree. ``float`` [0,``MAX_FLOAT``]                                    | Optional, default = ``0``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``max_depth``                   | Booster Parameters                       | Maximum depth of a tree. ``int`` [0, ``MAX_INT``]                           | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``6``                           |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``min_child_weight``            | Booster Parameters                       | Minimum sum of instance weight (hessian) needed in a child.                 | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | ``int`` [0, ``MAX_INT``]                                                    | Optional, default = ``1``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``max_delta_step``              | Booster Parameters                       | Sub-sample ratio of the training instances.                                 | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | ``float`` [0,1]                                                             | Optional, default = ``0``, no constraint if the value is set to ``0``.                                        |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``subsample``                   | Booster Parameters                       | Maximum delta step we allow each leaf output to be.                         | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | ``int`` [0, ``MAX_INT``]                                                    | Optional, default = ``1``, ``0.5`` - randomly sample half of the training data prior to growing trees.        |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``sampling_method``             | Booster Parameters                       | ``uniform``, ``gradient_based``                                             | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``uniform``                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``colsample_bytree``            | Booster Parameters                       | Group of parameters for sub-sampling of columns.                            | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 | ``colsample_bylevel``           |                                          | All ``colsample_by*`` parameters have a range of [``0``,``1``] that         | Optional, default = ``1``                                                                                     |
 | ``colsample_bynode``            |                                          | specify the fraction of columns to be sub-sampled.                          |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``lambda``, ``reg_lambda``      | Booster Parameters                       | L1 regularization term on weights. Increasing this value will make model    | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | more conservative. ``float`` [0, ``MAX_FLOAT``]                             | Optional, default = ``1``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``alpha``, ``reg_alpha``        | Booster Parameters                       | L2 regularization term on weights. Increasing this value will make model    | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | more conservative. ``float`` [0, ``MAX_FLOAT``]                             | Optional, default = ``1``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``tree_method``                 | Booster Parameters                       | The tree construction algorithm used by XGBoost                             | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | Choices include: ``auto``, ``exact``, ``approx``, ``hist``                  | Optional, default = ``auto``                                                                                  |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``scale_pos_weight``            | Booster Parameters                       | Control the balance of positive and negative weights.                       | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``1``                           |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``refresh_leaf``                | Booster Parameters                       | This is a parameter of the ``refresh`` updater. ``1`` means tree leafs and  | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | nodes’ stats are updated. ``0`` means only node stats are updated.          | Optional, default = ``1``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``process_type``                | Booster Parameters                       | A type of boosting process to run - ``default``, ``update``                 | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          |                                                                             | * Default: The ``normal`` boosting process which creates new trees.                                           |
 |                                 |                                          |                                                                             | * ``update`` Starts from an existing model and only updates its trees.                                        |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``grow_policy``                 | Booster Parameters                       | * Controls a way new nodes are added to the tree.                           | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          | * Currently supported only if ``tree_method`` is set to hist or approx.     | Optional, default= ``depthwise``                                                                              |
 |                                 |                                          | * Choices: ``depthwise``, ``lossguide``                                     |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``max_leaves``                  | Booster Parameters                       | Maximum number of nodes to be added. Not used by exact tree method.         | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``0``                           |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``max_bin``                     | Booster Parameters                       | * Only used if ``tree_method`` is set to ``hist`` or ``approx``.            | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``256``                         |
 |                                 |                                          | * Maximum number of discrete bins to bucket continuous features.            |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``num_parallel_tree``           | Booster Parameters                       | Number of parallel trees constructed during each iteration.                 | Applicable when booster is set to ``gbtree`` or ``dart``. Optional, default = ``1``                           |
 |                                 |                                          | This option is used to support boosted random forest                        |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``interaction_constraints``     | Booster Parameters                       | Constraints for interaction representing permitted interactions.            | Applicable when booster is set to ``gbtree`` or ``dart``.                                                     |
 |                                 |                                          |                                                                             | Optional, should be set automatically unless specified otherwise                                              |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``sample_type``                 | Dart Booster Parameters                  | Type of sampling algorithm:                                                 | Optional, default = ``uniform``                                                                               |
 |                                 |                                          | * ``uniform``  - dropped trees are selected uniformly.                      |                                                                                                               |
 |                                 |                                          | * ``weighted`` - dropped trees are selected in proportion to weight.        |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``normalize_type``              | Dart Booster Parameters                  | Type of normalization algorithm - ``tree`` | ``forest``                     | Optional, default = ``tree``                                                                                  |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``rate_drop``                   | Dart Booster Parameters                  | Dropout rate ``float`` [0,1]                                                | Optional, default = ``0.0``                                                                                   |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``one_drop``                    | Dart Booster Parameters                  | When enabled, at least one tree is dropped ``int``{0, 1}                    | Optional, default = ``0``                                                                                     |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+	 
 | ``skip_drop``                   | Dart Booster Parameters                  | Probability of skipping the dropout procedure during a boosting iteration.  | Optional, default = ``0.0``                                                                                   |
 |                                 |                                          | ``float`` [0, 1]                                                            |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``lambda``, ``reg_lambda``      | Linear Booster Parameters                | L2 regularization term on weights. Increasing this value will make model    | Optional, default = ``0``                                                                                     |
 |                                 |                                          | more conservative. ``float`` [0, ``MAX_FLOAT``]                             |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``updater``                     | Linear Booster Parameters                | * ``shotgun`` Parallel coordinate descent algorithm.                        | Optional, default = ``shotgun``                                                                               |
 |                                 |                                          | * ``coord_descentOrdinary`` coordinate descent algorithm.                   |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``feature_selector``            | Linear Booster Parameters                | Feature selection and ordering method.                                      | Optional, default = ``cyclic``                                                                                |
 |                                 |                                          | ``cyclic`` | ``shuffle`` | ``random`` | ``greedy``                          |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``top_k``                       | Linear Booster Parameters                | The number of top features to select in ``greedy`` and ``thrifty`` feature  | Optional, default = ``0``                                                                                     |
 |                                 |                                          | selector.  ``0`` means using all the features.                              |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 | ``objective``                   | Learning Task Parameters                 | ``reg:squarederrorvv`` | ``reg:squaredlogerror`` | ``reg:logisti`` |        | Optional, default = ``reg:squarederror``                                                                      |
 |                                 |                                          | ``reg:pseudohubererror`` | ``reg:absoluteerror`` | ``reg:quantileerror``    |                                                                                                               |
 |                                 |                                          | ``binary:logistic`` | ``binary:logitraw`` | ``binary:hinge``                |                                                                                                               |
 |                                 |                                          | ``count:poisson`` | ``survival:cox`` | ``survival:aft`` | ``rank:ndcg``     |                                                                                                               |
 |                                 |                                          | ``rank:map`` | ``rank:pairwise`` | ``reg:gamma`` | ``reg:tweedie``          |                                                                                                               |
 +---------------------------------+------------------------------------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
 
 
Usage notes & Limitations
-------------------------
* Based on `DMLC XGBoost <https://xgboost.readthedocs.io/en/stable/parameter.html#global-configuration>`_.
* Read more regarding `Feature Interaction Constraints <https://xgboost.readthedocs.io/en/stable/tutorials/feature_interaction_constraint.html>`_.
* Training and inference can be read directly from a table or a query expression.
* A minimum of 2 columns should be provided for training (feature column and a label).
* The label column is the last column in the chunk’s input for training.
* Model will be saved under database.schema hierarchy, like any other SQream object.
* ``model_predict`` doesn’t work within sub-query.
* Input feature types are Nullable ``FLOAT``
* Single label is supported, label should appear last.
