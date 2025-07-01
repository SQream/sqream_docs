{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _linear_regression:\
\
\
Linear Regression\
=================\
\
AISQream empowers users to build and train machine learning models, including Linear Regression, directly within the database using SQL.\
\
Syntax\
------\
\
.. code-block:: sql\
\
   --# Create and train model\
   CREATE [OR REPLACE] MODEL [database.schema.]model_name\
   OPTIONS(model_option_list)\
   AS \{query_statement\};\
\
.. code-block:: text\
\
   model_option_list:\
     MODEL_TYPE = \{ 'LINEAR_REG' | 'XGBOOST' \}\
   , MODEL_PATH = 'PATH/TO/MODEL/JSON/TO/CREATE/WITH_NAME_OF_MODEL_INCLUDED.json'\
   [, INITIAL_ALGORITHM = \{ 'SVD' | 'EIGENDECOMPOSITION' | 'QR_DECOMPOSITION' \} ]\
   [, GD_OPTIMIZER = \{ 'SGD' | 'ADAM' \} ]\
   [, STANDARDIZATION = TRUE | FALSE ]\
   [, LEARNING_RATE = FLOAT ]\
   [, EPOCH_COUNT = INT ]\
   [, LOSS_FUNCTION = \{ 'Mse', 'L1', 'SmoothL1', 'Huber' \} ]\
   [, TOLERANCE = FLOAT ]\
\
.. code-block:: sql\
\
   --# Inference\
   SELECT model_predict(\
       [database.schema.]model_name,\
       feature_col1 [,feature_column2, ...])\
   FROM \{query_statement\};\
\
   --# DROP\
   DROP MODEL [database.schema.]model_name;\
\
Parameters\
----------\
\
.. list-table:: Linear Regression Parameters\
   :widths: 25 25 50\
   :header-rows: 1\
\
   * - Parameter Name\
     - Description\
     - Default Value\
   * - MODEL_TYPE\
     - Specify the algorithm.\
     - Mandatory\
   * - MODEL_PATH\
     - Specify the path to save the model to.\
     - Mandatory\
   * - INITIAL_ALGORITHM\
     - Algorithm to fit linear model.\
     - SVD\
   * - GD_OPTIMIZER\
     - Optimizer used in second phase (gradient descent).\
     - ADAM\
   * - STANDARDIZATION\
     - Normalize features (mean = 0, std = 1).\
     - FALSE\
   * - LEARNING_RATE\
     - Gradient descent step size.\
     - 0.01\
   * - EPOCH_COUNT\
     - Number of full passes over data.\
     - Optional\
   * - LOSS_FUNCTION\
     - Distance between real and predicted values.\
     - Mse\
   * - TOLERANCE\
     - Minimal loss reduction needed to continue training.\
     - 0.01\
\
Usage Notes & Limitations\
--------------------------\
\
- Based on Nvidia RAPIDS Linear Regression.\
- Training and inference support direct use of table or query expression.\
- At least 2 columns must be provided for training (feature column and a label).\
- The label column must be the last column in the input.\
- The model is saved in `database.schema` like any other SQream object.\
- `model_predict` does not work within sub-queries.\
- Model export functionality is still under development.\
- Recommended limit: up to 8000 features in this version.\
}