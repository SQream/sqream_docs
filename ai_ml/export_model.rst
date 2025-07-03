.. _export_model:

Export Model
------------

The Export Model functionality allows users to save trained machine learning models (Currently supported for Linear Regression and XGBoost only) to external files in specified formats like JSON or Pickle.

Syntax
^^^^^^

.. code:: sql

    EXPORT MODEL [[<database name>.]<schema name>.]<model_name> TO <path>
    OPTIONS(output_type = {JSON | PICKLE});

Parameters
^^^^^^^^^^

* **Output type:**
    * Linear Regression model - JSON & PICKLE
    * XGBoost model - JSON only

Example
^^^^^^^

.. code:: sql

    CREATE OR REPLACE MODEL my_lr_model
    OPTIONS ( model_type = 'Linear_reg' , learning_rate = 0.01 )
    AS SELECT * FROM t;

    EXPORT MODEL my_lr_model to '/tmp/b.pkl'
    OPTIONS(output_type = PICKLE);