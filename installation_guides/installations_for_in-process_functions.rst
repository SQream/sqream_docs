.. _installations_for_in-process_functions:

==================================================
Installations for In-Process Functions
==================================================

This document outlines the requirements and installation steps necessary to enable in-process functions (e.g., **Text to Array**, **Hex to Int**).

The following requirements must be configured on **each server**.

Python Requirements
-------------------

**Python Version:** 3.11.7

Python installation requirements are mentioned here: :ref:`pre-installation_configurations` on 'installing-recommended-tools' section.


Install CUDA Toolkit
--------------------

Installation steps may vary based on the operating system version and architecture. Please refer to the official NVIDIA documentation for specific packages.

* **Download Source:** `NVIDIA CUDA Toolkit Downloads <https://developer.nvidia.com/cuda-toolkit-archive>`_

Install CuPy Library
--------------------

In-process functions are Python-based and utilize the CuPy library. As these functions depend on the local Python installation, this library must be installed manually.

To install CuPy for Python 3.11:

* **Download Source:** `CuPy installation <https://docs.cupy.dev/en/stable/install.html#installing-cupy-from-pypi>`_
   
