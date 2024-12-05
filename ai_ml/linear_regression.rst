.. _linear_regression:

*****************
Linear Regression
*****************


Linear Regression is a supervised machine learning algorithm used to model the relationship between a dependent variable (target) and one or more independent variables (features). It predicts a continuous output by finding the best-fitting line (or hyperplane in multiple dimensions) that minimizes the difference between the actual and predicted values, typically using a method called least squares.

In simple terms, Linear Regression aims to answer: "How does the target variable change with respect to the features?" It’s widely used in predictive analytics, trend analysis, and data modeling.

Syntax
------

.. code-block:: postgres

	# Create and train model
	CREATE [OR REPLACE] MODEL [database.schema.]model_name
	OPTIONS(model_option_list)
	AS {query_statement}

	model_option_list:
		MODEL_TYPE = { 'LINEAR_REG' }
		[, INITIAL_ALGORITHM = { 'SVD' | 'EIGENDECOMPOSITION' | 'QR_DECOMPOSITION'} ]
		[, GD_OPTIMIZER = { 'SGD' | 'ADAM'} ]
		[, STANDARDIZATION = TRUE | FALSE ]
		[, LEARNING_RATE = FLOAT ]
		[, EPOCH_COUNT = INT ]
		[, TOLERANCE = FLOAT ]
		
	# Inference
	SELECT model_predict(
		[database.schema.]model_name,
		feature_col1 [,feature_column2, ...])
	FROM {query_statement};
	
	# DROP
	DROP MODER [database.schema.]model_name;
	
	
Parameters
----------

* ``MODEL_TYPE`` - Specify the algorithm, Mandatory.
* ``INITIAL_ALGORITHM`` - Algorithm to fit liner model, Optional default ``SVD``.
* ``GD_OPTIMIZER`` - The optimizer being used at the second part of the implementation (Gradient descent), Optional default ``ADAM``.
* ``STANDARDIZATION`` - If ``TRUE``, the features will be normalized by subtracting the mean and dividing by the column-wise standard deviation, Optional default ``FALSE``.
* ``LEARNING_RATE`` - Rate of speed where the gradient moves during gradient descent, Optional, default 0.01.
* ``EPOCH_COUNT`` - Defines the number of times the entire data set has to be worked through the learning algorithm, Optional.
* ``LOSS_FUNCTION`` - Quantify the distance between the real and predicted values of the target, Optional default ``MSE``.
* ``TOLERANCE`` - Minimal loss reduction needed to continue for another epoch 0.01.

Usage notes & Limitations
-------------------------
* Based on Nvidia `RAPIDS Linear Regression <https://docs.rapids.ai/api/cuml/stable/api/#linear-regression>`_.
* Training and inference can be read directly from a table or a query expression.
* A mimimum of 2 columns should be provided for training (feature column and a label).
* The label column is the last column in the chunk’s input for training.
* Model will be saved under database.schema hierarchy, like any other SQream object.
* ``model_predict`` doesn’t work within sub-query.
