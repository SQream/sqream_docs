.. _linear_regression:

***********************
In-DB Linear Regression
***********************

Linear regression is a fundamental component of the data science pipeline, used to model relationships between variables and make predictions based on observed data.

SQreamDB supports data preparation and standardization, data training, and inference using data stored in and outside SQreamDB, providing a comprehensive platform for conducting end-to-end data analysis and machine learning tasks.

.. contents:: 
   :local:
   :depth: 1

Before You Begin
================

* Python version

* SQreamDB :ref:`JDBC connector<java_jdbc>` version

* SQDB version

* Missing data is not supported 

Parameters
----------

.. list-table::
   :widths: auto
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description	 
   * - Tolerance
     - ``1e-4``
     - Tolerance determines when to stop training based on the improvement in model performance. If the improvement falls below the tolerance threshold, training stops early.
   * - Label Index
     - ``0``
     - Label index identifies the position of the target variable (dependent variable) within the dataset, crucial for training a linear regression model.	 
   * - Max Number of Epochs
     - ``1500``
     - Max number of epochs sets the limit on how many times the training algorithm iterates over the dataset during model training, helping control training duration and complexity.

Importing Python Libraries
==========================

.. code-block:: python

	df = session.table('customers')
	       .join('orders',on='customer_id')
	       .filter('active')
	       .to_pandas()

Data Preparation
================

Missing data is not supported. 

* All data, including labels and features, should be stored in the same table.

* Ensure that feature values (X) are within the same range. If not, consider normalizing or standardizing the features (X) separately for both training and testing datasets.
	 
.. _normalization:

Normalization (Standardization)
-------------------------------

Centering and scaling should be done independently on each feature by computing the relevant statistics on the samples in the training set.

We suggest standardizing features by removing the mean and scaling to unit variance. The standard score of a sample :math:`x` is calculated as :math:`z = x - \frac{u}{s}`, where:

* :math:`u` is the mean of the training samples

* :math:`s` is the standard deviation of the training samples

Training Data
=============

There is no need to export data out of SQreamDB for the training process.

.. code-block::

	def train(data):
	  model = sk.LinearRegression()
	  X,y = df #...
	  X_train, X_test, y_train, y_test = split_train_test(X,y)
	  model.fit(X_train,y_train)

	session.register('train_sp',train)
	model = session.execute('train_sp', source_table='customers')

Testing and Inference
=====================

.. code-block:: python

	session.import_model('model0',model)
	test_results = session.table('customers_test').predict('model0')
	# compare test results and test ground truth...
	prediction_results = session.sql('select *,predict(''model0'',*) from customers');

