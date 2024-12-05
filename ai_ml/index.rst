.. _ai_ml:

*****
AI/ML
*****

SQream has integrated `NVIDIA RAPIDS cuML <https://developer.nvidia.com/rapids>`_ and other popular ML open-source projects, such as the `DMLC XGBoost library <https://xgboost.readthedocs.io/en/stable/>`_. This integration
enhances performance, scalability, and efficiency, enabling you to seamlessly train various ML models in ``Python`` or ``SQL`` directly within the SQream Blue. Additionally, SQream's integration with ``cuDF``, through the `Ibis open-source project <https://ibis-project.org/>`_, streamlines data pre-processing tasks.
By combining the power of SQream's in-database processing and RAPIDS' GPU-accelerated ML libraries, data scientists can use familiar Python tools to train models on production-sized datasets, eliminating the need for data sampling or complex engineering efforts.
Besides the inherent benefits of RAPIDS’ libraries, SQream Blue users will be multi-purposing their existing GPUs for both data analytics and ML, building models that rely on bigger datasets and have fewer RAM limitations.

Supported Algorithms 
====================

* :ref:`linear_regression`
* :ref:`xgboost`

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :hidden:

   linear_regression
   xgboost

   
   
   