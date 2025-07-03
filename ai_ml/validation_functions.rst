.. _validation_functions:

Validation Functions
--------------------

Validation functions provide tools to evaluate the performance of trained machine learning models against test datasets, offering metrics like Mean Square Error (MSE), Root Mean Square Error (RMSE) and Area Under the Curve (AUC).

How to Use Model Validation Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use these functions in a SELECT statement to evaluate a model's performance against a test dataset.

MSE / RMSE (for Regression)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates the Root Mean Square Error for Linear Regression models.

Syntax
^^^^^^

.. code:: sql

    SELECT validation_functions.rmse(model_name, features, label) FROM test_table;

Parameters
^^^^^^^^^^

* ``'model_name'``: The name of your trained Linear Regression model.
* ``features``: The column(s) the model uses for prediction.
* ``labels``: The column with the true numeric values.

Example:
^^^^^^^^

.. code:: sql

    SELECT
        validation_functions.rmse(
            house_price_model,
            (bedrooms, square_feet),
            actual_price
        )
    FROM
        housing_test_data;

Area under curve (for XGBoost)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calculates the Area Under the Curve (AUC) for XGBoost binary classification models.

Syntax
^^^^^^

.. code:: sql

    SELECT validation_functions.area_under_curve(model_name, features, labels)
    FROM test_table;

Parameters
^^^^^^^^^^

* ``'model_name'``: The name of your trained XGBoost model.
* ``features``: The column(s) the model uses for prediction.
* ``labels``: The column with the true binary labels (0 or 1).

Example:
^^^^^^^^

.. code:: sql

    SELECT
        validation_functions.area_under_curve(
            customer_churn_model,
            account_age, monthly_spend,
            has_churned
        )
    FROM customer_test_data;

Usage notes
^^^^^^^^^^^

* These functions, like ``SUM()`` or ``AVG()``, return a single value for the entire dataset and cannot be used with a ``GROUP BY`` clause.
* Feature and label columns must be numeric; rows containing ``NULL`` values will be ignored.
* When selecting a model type, use ``rmse`` for Linear Regression and ``area_under_curve`` for XGBoost.
* Using the incorrect function for a model type will result in an error.
