.. _catalog_tables:

Catalog Tables
--------------

Catalog tables provide metadata about the machine learning models and Python modules created within AISQream, allowing users to query and understand the properties of these stored objects.

Catalog Table: ml_models
^^^^^^^^^^^^^^^^^^^^^^

Contains all ML models with general common information:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.ml_models);

.. code:: sql

    create table "master"."sqream_catalog"."ml_models" (
       "model_id" bigint not null check ('CS ""flat""'),
       "database" text(32) not null check ('CS ""flat""'),
       "schema" text(32) not null check ('CS ""flat""'),
       "name" text(32) not null check ('CS ""flat""'),
       "ml_alg" text(32) not null check ('CS ""flat""')
    );

--# ml_models

.. code:: sql

    SELECT * FROM sqream_catalog.ml_models;

.. code:: text

    10,master,public,m1,LINEAR_REG
    11,master,public,ml_xgb_catalog_test,XGBOOST
    8,master,s,m,LINEAR_REG
    9,master,public,m,PY_MODEL

Catalog table: ml_linear_reg
^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains all Linear Regression models, with more detailed information specifically for Linear Regression:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.ml_linear_reg);

.. code:: sql

    create table "master"."sqream_catalog"."ml_linear_reg" (
       "model_id" bigint not null check ('CS ""flat""'),
       "database" text(32) not null check ('CS ""flat""'),
       "schema" text(32) not null check ('CS ""flat""'),
       "name" text(32) not null check ('CS ""flat""'),
       "ml_alg" text(32) not null check ('CS ""flat""'),
       "initial_algorithm" text(32) not null check ('CS ""flat""'),
       "gd_optimizer" text(32) not null check ('CS ""flat""'),
       "coefficients" text(32) not null check ('CS ""flat""'),
       "is_standardized" bool not null check ('CS ""flat""'),
       "learning_rate" real not null check ('CS ""flat""'),
       "epoch_count" int not null check ('CS ""flat""'),
       "loss_function" text(32) not null check ('CS ""flat""'),
       "tolerance" real not null check ('CS ""flat""'),
       "time" text(32) not null check ('CS ""flat""')
    );

--# ml_linear_reg

.. code:: sql

    SELECT * FROM sqream_catalog.ml_linear_reg;

.. code:: text

    10,master,public,m1,LINEAR_REG,SVD,ADAM,{0.500000|0.500000},1,0.0000,1,MSE,0.0000,2025-02-06 15:10:55.150
    8,master,s,m,LINEAR_REG,SVD,ADAM,{0.500000|0.500000},1,0.0000,1,MSE,0.0000,2025-02-06 15:10:42.121

Catalog table: ml_xgboost
^^^^^^^^^^^^^^^^^^^^^^^

Contains all XGboost models, with more detailed information specifically for XGboost:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.ml_xgboost);

.. code:: sql

    create table "master"."sqream_catalog"."ml_xgboost" (
       "model_id" bigint not null check ('CS ""flat""'),
       "database" text not null check ('CS ""flat""'),
       "schema" text not null check ('CS ""flat""'),
       "name" text not null check ('CS ""flat""'),
       "ml_alg" text not null check ('CS ""flat""'),
       "verbosity" text not null check ('CS ""flat""'),
       "booster" text not null check ('CS ""flat""'),
       "disable_default_eval_metric" text not null check ('CS ""flat""'),
       "tree_booster_parameters_eta" text not null check ('CS ""flat""'),
       "tree_booster_parameters_gamma" text not null check ('CS ""flat""'),
       "tree_booster_parameters_max_depth" text not null check ('CS ""flat""'),
       "tree_booster_parameters_min_child_weight" text not null check ('CS ""flat""'),
       "tree_booster_parameters_max_delta_step" text not null check ('CS ""flat""'),
       "tree_booster_parameters_subsample" text not null check ('CS ""flat""'),
       "tree_booster_parameters_sampling_method" text not null check ('CS ""flat""'),
       "tree_booster_parameters_colsample_bytree" text not null check ('CS ""flat""'),
       "tree_booster_parameters_colsample_bylevel" text not null check ('CS ""flat""'),
       "tree_booster_parameters_colsample_bynode" text not null check ('CS ""flat""'),
       "tree_booster_parameters_lambda" text not null check ('CS ""flat""'),
       "tree_booster_parameters_reg_lambda" text not null check ('CS ""flat""'),
       "tree_booster_parameters_alpha" text not null check ('CS ""flat""'),
       "tree_booster_parameters_reg_alpha" text not null check ('CS ""flat""'),
       "tree_booster_parameters_tree_method" text not null check ('CS ""flat""'),
       "tree_booster_parameters_scale_pos_weight" text not null check ('CS ""flat""'),
       "tree_booster_parameters_process_type" text not null check ('CS ""flat""'),
       "tree_booster_parameters_grow_policy" text not null check ('CS ""flat""'),
       "tree_booster_parameters_max_leaves" text not null check ('CS ""flat""'),
       "tree_booster_parameters_max_bin" text not null check ('CS ""flat""'),
       "tree_booster_parameters_num_parallel_tree" text not null check ('CS ""flat""'),
       "dart_booster_params_sample_type" text not null check ('CS ""flat""'),
       "dart_booster_params_normalize_type" text not null check ('CS ""flat""'),
       "dart_booster_params_rate_drop" text not null check ('CS ""flat""'),
       "dart_booster_params_one_drop" text not null check ('CS ""flat""'),
       "dart_booster_params_skip_drop" text not null check ('CS ""flat""'),
       "linear_booster_params_updater" text not null check ('CS ""flat""'),
       "linear_booster_params_feature_selector" text not null check ('CS ""flat""'),
       "linear_booster_params_top_k" text not null check ('CS ""flat""'),
       "objective" text not null check ('CS ""flat""'),
       "base_score" text not null check ('CS ""flat""'),
       "eval_metric" text not null check ('CS ""flat""'),
       "cut_off_top_positions" text not null check ('CS ""flat""'),
       "seed" text not null check ('CS ""flat""'),
       "seed_per_iteration" text not null check ('CS ""flat""'),
       "tweedie_variance_power" text not null check ('CS ""flat""'),
       "huber_slope" text not null check ('CS ""flat""'),
       "quantile_alpha" text not null check ('CS ""flat""'),
       "aft_loss_distribution" text not null check ('CS ""flat""'),
       "lambdarank_pair_method" text not null check ('CS ""flat""'),
       "lambdarank_num_pair_per_sample" text not null check ('CS ""flat""'),
       "lambdarank_normalization" text not null check ('CS ""flat""'),
       "lambdarank_bias_norm" text not null check ('CS ""flat""'),
       "lambdarank_unbiased" text not null check ('CS ""flat""'),
       "ndcg_exp_gain" text not null check ('CS ""flat""'),
       "epoch_count" text not null check ('CS ""flat""')
    );

--# ml_xgboost

.. code:: sql

    SELECT * FROM sqream_catalog.ml_xgboost;

.. code:: text

    1,master,public,m2,XGBOOST,VERBOSITY_SILENT,BOOSTER_GBTREE,0,0.300000,0.000000,6,1,0,1.000000,SAMPLING_METHOD_UNIFORM,1.000000,1.000000,1.000000,0.000000,0.000000,0.000000,0.000000,TREE_METHOD_AUTO,1.000000,PROCESS_TYPE_DEFAULT,GROW_POLICY_DEPTHWISE,0,0,1,SAMPLE_TYPE_UNSPECIFIED,NORMALIZE_TYPE_UNSPECIFIED,0.000000,0,0.000000,UPDATER_UNSPECIFIED,FEATURE_SELECTOR_UNSPECIFIED,0,OBJECTIVE_BINARY_LOGISTIC,0.000000,EVAL_METRIC_UNSPECIFIED,"""""",0,0,0.000000,0.000000,,AFT_LOSS_DISTRIBUTION_UNSPECIFIED,LAMBDARANK_PAIR_METHOD_UNSPECIFIED,0,0,0.000000,0,0,100

Catalog table: py_modules
^^^^^^^^^^^^^^^^^^^^^^^

Contains all Python modules:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.py_modules);

.. code:: sql

    "module_id" bigint not null check ('CS ""flat""'),   "database_name" text(32) not null check ('CS ""flat""'),   "module_name" text(32) not null check ('CS ""flat""'),   "path" text(32) not null check ('CS ""flat""'),   "entry_points" text(32) not null check ('CS ""flat""')

--# ml_linear_reg

.. code:: sql

    SELECT * FROM sqream_catalog.py_modules;

.. code:: text

    22,master,pm,/home/sagib/py_udf.py,"{[name:func_name, args:[TEXT], ret_type:DATE, gpu:true]}"
    36,master,m1,/home/sagib/py_udf.py,"{[name:return_input2, args:[TEXT], ret_type:TEXT, gpu:false]}"

Catalog table: py_module_permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains all Python modules permissions:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.py_module_permissions);

.. code:: sql

    database_name" text(32) not null check ('CS ""flat""'),   "module_id" bigint not null check ('CS ""flat""'),   "role_id" bigint not null check ('CS ""flat""'),   "permission_type" int not null check ('CS ""flat""')

--# py_module_permissions

.. code:: sql

    SELECT * FROM sqream_catalog.py_module_permissions;

.. code:: text

    master,0,8,11000
    Master,0,8,11001

Catalog table: registered_algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contains all Python based AI models registered:

--# DDL

.. code:: sql

    SELECT get_ddl(sqream_catalog.registered_algorithms);

.. code:: sql

    "id" bigint not null check ('CS ""flat""'),
      "database_name" text(32) not null check ('CS ""flat""'),
      "alg_name" text(32) not null check ('CS ""flat""'),
      "alg_path" text(32) not null check ('CS ""flat""'),
      "train_method" text(32) not null check ('CS ""flat""'),
      "predict_method" text(32) not null check ('CS ""flat""')

--# registered_algorithms

.. code:: sql

    SELECT * FROM sqream_catalog.registered_algorithms;

.. code:: text

    6,master,logistic_regression,/tmp/sagib.py,train,predict
