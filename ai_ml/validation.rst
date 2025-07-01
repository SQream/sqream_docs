{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww37900\viewh17980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 .. _validation:\
\
\
Validation Functions\
====================\
\
Validation functions provide tools to evaluate the performance of trained machine learning models against test datasets.\
\
Supported metrics include:\
\
- MSE / RMSE (for Linear Regression)\
- Area Under Curve (AUC) for binary classification (XGBoost)\
\
How to Use Model Validation Functions\
-------------------------------------\
\
These functions are used in a `SELECT` query to evaluate model performance.\
\
MSE / RMSE (for Regression)\
---------------------------\
\
Calculates the Root Mean Square Error for Linear Regression models.\
\
.. code-block:: sql\
\
   SELECT validation_functions.rmse(model_name, features, labels)\
   FROM test_table;\
\
Parameters:\
\
- `model_name`: Name of trained Linear Regression model\
- `features`: Column(s) used for prediction (tuple)\
- `labels`: Column with the true numeric values\
\
Example:\
\
.. code-block:: sql\
\
   SELECT\
       validation_functions.rmse(\
           house_price_model,\
           (bedrooms, square_feet),\
           actual_price\
       )\
   FROM\
       housing_test_data;\
\
Area Under Curve (for XGBoost)\
------------------------------\
\
Calculates AUC score for binary classification models.\
\
.. code-block:: sql\
\
   SELECT validation_functions.area_under_curve(model_name, features, labels)\
   FROM test_table;\
\
Parameters:\
\
- `model_name`: Name of trained XGBoost model\
- `features`: Column(s) used for prediction\
- `labels`: Column with binary labels (0 or 1)\
\
Example:\
\
.. code-block:: sql\
\
   SELECT\
       validation_functions.area_under_curve(\
           customer_churn_model,\
           (account_age, monthly_spend),\
           has_churned\
       )\
   FROM\
       customer_test_data;\
\
Usage Notes\
-----------\
\
- These functions behave like `SUM()` or `AVG()`: they return a **single scalar value**.\
- Cannot be used with `GROUP BY`.\
- Feature and label columns **must be numeric**.\
- Rows with NULLs are **ignored**.\
- Must use the correct function:\
  - `rmse()` 
\f1 \uc0\u8594 
\f0  Linear Regression\
  - `area_under_curve()` 
\f1 \uc0\u8594 
\f0  XGBoost\
\
  Otherwise, an error will occur.\
}