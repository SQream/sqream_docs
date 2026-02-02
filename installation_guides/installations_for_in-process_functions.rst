.. _in_process_python_functions:

***************************
In-Process Python Functions
***************************

This section describes the required steps to enable and use **In-Process Python functions**
on a production SQreamDB machine.

.. contents::
   :local:
   :depth: 2

Overview
========

In order to use In-Process Python functions on a **production machine**
(**not** a development machine with ``sqream_prerequisites`` installed),
several system-level dependencies must be installed and configured manually.

Before proceeding, make sure you have completed all steps described in:
:ref:`pre-installation_configurations`

CUDA Installation
=================

This section verifies that CUDA is already installed on the system
(either via repository or NVIDIA runfile).

Checking CUDA Repository
------------------------

Verify that a CUDA repository is installed:

.. code-block:: console

   rpm -qa | grep cuda

If CUDA repository is installed, you should see output similar to:

.. code-block:: console

   cuda-repo-rhel8-12-3-local-12.3.2_545.23.08-1.x86_64

Handling Missing CUDA Repository
--------------------------------

If no CUDA repository is found (``cuda-repo`` does not appear in ``rpm -qa``):

1. Check repository files:

   .. code-block:: console

      ls -l /etc/yum.repos.d/ | grep cuda

2. If CUDA was installed manually (runfile install), the repository will not appear.

   Verify where CUDA is installed:

   .. code-block:: console

      which nvcc

3. If CUDA binaries are not in ``PATH``, check the default installation location:

   .. code-block:: console

      cd /usr/local
      ls -l | grep cuda

You should see output similar to:

.. code-block:: console

   cuda -> /usr/local/cuda-13.0/
   cuda-13.0/

CUDA Toolkit Installation
=========================

The CUDA Toolkit must match the installed CUDA driver version.

Installing CUDA Toolkit via DNF
-------------------------------

Install the CUDA toolkit that matches your driver version.

.. code-block:: console

   sudo dnf install cuda-toolkit-12-3

.. warning::

   If your CUDA driver version is different (for example **12.9**),
   you must install the **matching toolkit**:

   .. code-block:: console

      sudo dnf install cuda-toolkit-12-9

Removing Incorrect CUDA Toolkit
-------------------------------

If the installed CUDA toolkit version is **not 12.3.2**, it must be removed.

**Toolkit installed via DNF**

.. code-block:: console

   rpm -qa | grep cuda-toolkit

.. code-block:: console

   sudo dnf remove "cuda-toolkit*"

**Toolkit installed via runfile**

.. code-block:: console

   cd /usr/local
   sudo rm -rf /usr/local/cuda-13.0/
   sudo rm cuda

Installing CUDA Toolkit via Runfile
-----------------------------------

Install CUDA Toolkit **12.3.2** using the NVIDIA runfile
(even if the driver version is higher).

1. Download the runfile:

   .. code-block:: console

      wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_545.23.08_linux.run

2. Install the toolkit only:

   .. code-block:: console

      sudo sh cuda_12.3.2_545.23.08_linux.run \
        --silent \
        --toolkit \
        --no-man-page \
        --override

Configuring CUDA Toolkit for Python
-----------------------------------

Add CUDA library paths:

.. code-block:: console

   sudo tee /etc/ld.so.conf.d/cuda-12-3.conf > /dev/null << 'EOF'
   /usr/local/cuda-12.3/lib64
   /usr/local/cuda-12.3/targets/x86_64-linux/lib
   EOF

Reload the dynamic linker configuration:

.. code-block:: console

   sudo ldconfig

Python Setup
=============

Verifying Python Version
------------------------

Ensure **Python 3.11** is installed and set as the default Python version
(as required by the pre-installation configuration).

.. code-block:: console

   python3 --version

Expected output:

.. code-block:: console

   Python 3.11.7

CuPy Installation
=================

Installing CuPy
----------------

Install CuPy using ``pip``:

.. code-block:: console

   pip3 install cupy

Alternatively, install CuPy using one of the supported methods described in:
https://docs.cupy.dev/en/stable/install.html#installing-cupy-from-pypi

Verification
=============

After completing all steps:

* CUDA is installed and detected
* CUDA toolkit version matches **12.3.2**
* CUDA libraries are visible to the dynamic linker
* Python 3.11 is installed
* CuPy is installed successfully

The system is now ready to run **In-Process Python functions** within SQreamDB.

