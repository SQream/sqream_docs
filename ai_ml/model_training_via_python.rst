.. _model_training_via_python:

Model Training via Python
-------------------------

AISQream's Model Training via Python modules extends its machine learning capabilities beyond the currently embedded Linear Regression and XGBoost algorithms. This new feature allows for the seamless integration and utilization of a broader range of Python-based ML algorithms directly within SQream's GPU-accelerated environment, significantly reducing development time for new models.

Syntax
^^^^^^

-- Algorithm registration

.. code:: sql

    REGISTER ALGORITHM 'algorithm_name'
    OPTIONS
      ( alg_path = 'path_to_alg_file'
      [, train_method := Text -- defaults to 'train'
      , predict_method := Text -- defaults to 'predict'
      ]);

-- Create and train model

.. code:: sql

    CREATE [OR REPLACE] MODEL [database.schema.]model_name
    OPTIONS(model_option_list)
    AS {query_statement};

``model_option_list``:

.. code:: sql

    MODEL_PATH := Text    -- path to save the model to
    MODEL_TYPE := Text    -- algorithm name as registered
    MODEL_PARAMS := Text  -- MODEL_PARAMS map of Strings

-- Inference

.. code:: sql

    SELECT model_predict(
        [database.schema.]model_name,
        feature_col1 [,feature_column2, ...])
    FROM {query_statement}; --either <table_name> or (select_query) in parentheses

-- Drop model

.. code:: sql

    DROP MODEL [database.schema.]model_name;

-- Drop Algorithm registration

.. code:: sql

    UNREGISTER ALGORITHM 'algorithm_name';

Usage notes
^^^^^^^^^^^

* The label column is the last column in the chunk’s input for training.
* Distinguish between ``alg_path`` in the ``REGISTER ALGORITHM`` command and ``model_path`` in the ``CREATE MODEL`` command: the former specifies the path to the Python script while the latter specifies the path to the model output.
* The python file referred to in ``alg_path`` should contain a function for training and a function for inference, both of which should accept the input data in ``cudf.DataFrame`` form, and a map of string parameters. The ``model_path`` parameter in the train function will contain the path the model should be saved to, and later extracted in the predict function in the form of ``train_result_path``.
* Once registered, algorithms are persistent until removed by ``UNREGISTER ALGORITHM`` command.
* Python version is compatible with SQream’s prerequisites 3.11
* Embedded algorithms can not be unregistered.
* ``train_method`` and ``predict_method`` indicate the function names in the Python file, default values are ``train`` and ``predict`` respectively.
* Parameters for Train will be passed by the user and parsed at runtime by the Python code.
