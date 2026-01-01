.. _installations_for_in-process_functions

==================================================
Installations for In-Process Functions
==================================================

This document outlines the requirements and installation steps necessary to enable in-process functions (e.g., **Text to Array**, **Hex to Int**).

The following requirements must be configured on **each server**.

Python Requirements
-------------------

**Minimal Python Version:** 3.11.7 and above.

1. Verify that the ``python3`` executable points to the correct version:

   .. code-block:: console

      python3 --version

2. If ``python3`` does not point to a version that meets the minimal requirements, update the Python version alternatives.

   * Check the current configuration:

     .. code-block:: console

        sudo update-alternatives --config python3

   * Change the version (replace ``X`` with your installed sub-version):

     .. code-block:: console

        sudo update-alternatives --set python3 /usr/bin/python3.X

.. warning::
   **Restart Required:** If the default Python version was changed, you must restart Sqream workers for the update to take effect.

Install CUDA Toolkit
--------------------

Installation steps may vary based on the operating system version and architecture. Please refer to the official NVIDIA documentation for specific packages.

* **Download Source:** `NVIDIA CUDA Toolkit 12.1 Downloads <https://developer.nvidia.com/cuda-12-1-0-download-archive>`_

Install CuPy Library
--------------------

In-process functions are Python-based and utilize the CuPy library. As these functions depend on the local Python installation, this library must be installed manually.

To install CuPy for Python 3.11:

* **Download Source:** `CuPy installation <https://docs.cupy.dev/en/stable/install.html#installing-cupy-from-pypi>`_
   
