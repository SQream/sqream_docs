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

.. list-table:: 
   :widths: auto
   :header-rows: 1
   
   * - Parameter Name
     - Parameter Type
     - Description
     - Comments
   * - ``verbosity``
     - Global Configuration
     - 
	 * ``0`` = silent
	 * ``1`` = warning
	 * ``2`` = debug
	 * ``3`` = info
     - Optional, default is 0



Usage notes & Limitations
-------------------------
* Based on `DMLC XGBoost <https://xgboost.readthedocs.io/en/stable/parameter.html#global-configuration>`_.
